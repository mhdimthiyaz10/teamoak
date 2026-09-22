/* ============================================================
   MagicRings — Vanilla JS / Three.js port
   Implements the WebGL shader rings effect as a background
   ============================================================ */

const MagicRings = (() => {

  const vertexShader = `
    void main() {
      gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
  `;

  const fragmentShader = `
    precision highp float;

    uniform float uTime, uAttenuation, uLineThickness;
    uniform float uBaseRadius, uRadiusStep, uScaleRate;
    uniform float uOpacity, uNoiseAmount, uRotation, uRingGap;
    uniform float uFadeIn, uFadeOut;
    uniform float uMouseInfluence, uHoverAmount, uHoverScale, uParallax, uBurst;
    uniform vec2 uResolution, uMouse;
    uniform vec3 uColor, uColorTwo;
    uniform int uRingCount;

    const float HP = 1.5707963;
    const float CYCLE = 3.45;

    float fade(float t) {
      return t < uFadeIn ? smoothstep(0.0, uFadeIn, t) : 1.0 - smoothstep(uFadeOut, CYCLE - 0.2, t);
    }

    float ring(vec2 p, float ri, float cut, float t0, float px) {
      float t = mod(uTime + t0, CYCLE);
      float r = ri + t / CYCLE * uScaleRate;
      float d = abs(length(p) - r);
      float a = atan(abs(p.y), abs(p.x)) / HP;
      float th = max(1.0 - a, 0.5) * px * uLineThickness;
      float h = (1.0 - smoothstep(th, th * 1.5, d)) + 1.0;
      d += pow(cut * a, 3.0) * r;
      return h * exp(-uAttenuation * d) * fade(t);
    }

    void main() {
      float px = 1.0 / min(uResolution.x, uResolution.y);
      vec2 p = (gl_FragCoord.xy - 0.5 * uResolution.xy) * px;
      float cr = cos(uRotation), sr = sin(uRotation);
      p = mat2(cr, -sr, sr, cr) * p;
      p -= uMouse * uMouseInfluence;
      float sc = mix(1.0, uHoverScale, uHoverAmount) + uBurst * 0.3;
      p /= sc;
      vec3 c = vec3(0.0);
      float rcf = max(float(uRingCount) - 1.0, 1.0);
      for (int i = 0; i < 10; i++) {
        if (i >= uRingCount) break;
        float fi = float(i);
        vec2 pr = p - fi * uParallax * uMouse;
        vec3 rc = mix(uColor, uColorTwo, fi / rcf);
        c = mix(c, rc, vec3(ring(pr, uBaseRadius + fi * uRadiusStep, pow(uRingGap, fi), i == 0 ? 0.0 : 2.95 * fi, px)));
      }
      c *= 1.0 + uBurst * 2.0;
      float n = fract(sin(dot(gl_FragCoord.xy + uTime * 100.0, vec2(12.9898, 78.233))) * 43758.5453);
      c += (n - 0.5) * uNoiseAmount;
      gl_FragColor = vec4(c, max(c.r, max(c.g, c.b)) * uOpacity);
    }
  `;

  function init(mountElement, options = {}) {
    const cfg = {
      color:          '#ffffff',
      colorTwo:       '#888888',
      speed:          0.9,
      ringCount:      6,
      attenuation:    11,
      lineThickness:  2.2,
      baseRadius:     0.28,
      radiusStep:     0.09,
      scaleRate:      0.09,
      opacity:        0.75,
      noiseAmount:    0.05,
      rotation:       10,
      ringGap:        1.45,
      fadeIn:         0.65,
      fadeOut:        0.55,
      followMouse:    true,
      mouseInfluence: 0.1,
      hoverScale:     1.1,
      parallax:       0.03,
      clickBurst:     true,
      ...options
    };

    let renderer;
    try {
      renderer = new THREE.WebGLRenderer({ alpha: true, antialias: true });
    } catch (e) {
      console.warn('MagicRings: WebGL not available', e);
      return null;
    }

    renderer.setClearColor(0x000000, 0);
    renderer.domElement.style.position = 'absolute';
    renderer.domElement.style.inset = '0';
    renderer.domElement.style.width = '100%';
    renderer.domElement.style.height = '100%';
    mountElement.appendChild(renderer.domElement);

    const scene  = new THREE.Scene();
    const camera = new THREE.OrthographicCamera(-0.5, 0.5, 0.5, -0.5, 0.1, 10);
    camera.position.z = 1;

    const uniforms = {
      uTime:          { value: 0 },
      uAttenuation:   { value: cfg.attenuation },
      uResolution:    { value: new THREE.Vector2() },
      uColor:         { value: new THREE.Color(cfg.color) },
      uColorTwo:      { value: new THREE.Color(cfg.colorTwo) },
      uLineThickness: { value: cfg.lineThickness },
      uBaseRadius:    { value: cfg.baseRadius },
      uRadiusStep:    { value: cfg.radiusStep },
      uScaleRate:     { value: cfg.scaleRate },
      uRingCount:     { value: cfg.ringCount },
      uOpacity:       { value: cfg.opacity },
      uNoiseAmount:   { value: cfg.noiseAmount },
      uRotation:      { value: (cfg.rotation * Math.PI) / 180 },
      uRingGap:       { value: cfg.ringGap },
      uFadeIn:        { value: cfg.fadeIn },
      uFadeOut:       { value: cfg.fadeOut },
      uMouse:         { value: new THREE.Vector2() },
      uMouseInfluence:{ value: cfg.followMouse ? cfg.mouseInfluence : 0 },
      uHoverAmount:   { value: 0 },
      uHoverScale:    { value: cfg.hoverScale },
      uParallax:      { value: cfg.parallax },
      uBurst:         { value: 0 },
    };

    const material = new THREE.ShaderMaterial({
      vertexShader,
      fragmentShader,
      uniforms,
      transparent: true
    });

    scene.add(new THREE.Mesh(new THREE.PlaneGeometry(1, 1), material));

    /* ---- resize ---- */
    const resize = () => {
      const w   = mountElement.clientWidth;
      const h   = mountElement.clientHeight;
      const dpr = Math.min(window.devicePixelRatio, 2);
      renderer.setSize(w, h);
      renderer.setPixelRatio(dpr);
      uniforms.uResolution.value.set(w * dpr, h * dpr);
    };
    resize();
    window.addEventListener('resize', resize);
    const ro = new ResizeObserver(resize);
    ro.observe(mountElement);

    /* ---- mouse ---- */
    const mouse       = [0, 0];
    const smoothMouse = [0, 0];
    let hoverAmount   = 0;
    let isHovered     = false;
    let burst         = 0;

    mountElement.addEventListener('mousemove', e => {
      const r  = mountElement.getBoundingClientRect();
      mouse[0] = (e.clientX - r.left) / r.width  - 0.5;
      mouse[1] = -((e.clientY - r.top)  / r.height - 0.5);
    });
    mountElement.addEventListener('mouseenter', () => { isHovered = true; });
    mountElement.addEventListener('mouseleave', () => {
      isHovered = false;
      mouse[0] = mouse[1] = 0;
    });
    mountElement.addEventListener('click', () => { burst = 1; });

    /* ---- render loop ---- */
    let frameId;
    const animate = t => {
      frameId = requestAnimationFrame(animate);
      smoothMouse[0] += (mouse[0] - smoothMouse[0]) * 0.08;
      smoothMouse[1] += (mouse[1] - smoothMouse[1]) * 0.08;
      hoverAmount    += ((isHovered ? 1 : 0) - hoverAmount) * 0.08;
      burst          *= 0.95;
      if (burst < 0.001) burst = 0;

      uniforms.uTime.value        = t * 0.001 * cfg.speed;
      uniforms.uMouse.value.set(smoothMouse[0], smoothMouse[1]);
      uniforms.uHoverAmount.value = hoverAmount;
      uniforms.uBurst.value       = cfg.clickBurst ? burst : 0;

      renderer.render(scene, camera);
    };
    frameId = requestAnimationFrame(animate);

    /* returns cleanup fn */
    return () => {
      cancelAnimationFrame(frameId);
      window.removeEventListener('resize', resize);
      ro.disconnect();
      if (mountElement.contains(renderer.domElement))
        mountElement.removeChild(renderer.domElement);
      renderer.dispose();
      material.dispose();
    };
  }

  return { init };
})();

/* ---- Auto-initialise on the What We Do background ---- */
document.addEventListener('DOMContentLoaded', () => {
  const bg = document.getElementById('magic-rings-bg');
  if (!bg) return;

  const tryInit = () => {
    if (typeof THREE !== 'undefined') {
      MagicRings.init(bg);
    } else {
      setTimeout(tryInit, 100);
    }
  };
  tryInit();
});
