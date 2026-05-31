import os
import glob

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

injection_code = """
<!-- MOBILE NAV FIX -->
<style>
/* Global Mobile Navigation Fix */
.mobile-menu-btn {
    display: none;
    flex-direction: column;
    justify-content: space-between;
    width: 28px;
    height: 20px;
    cursor: pointer;
    z-index: 1000;
}
.mobile-menu-btn span {
    display: block;
    height: 2px;
    width: 100%;
    background-color: #fff;
    border-radius: 2px;
    transition: all 0.3s ease;
}

@media (max-width: 768px) {
    .mobile-menu-btn { display: flex; }
    
    .nav-links, .hero-nav-links {
        display: flex !important;
        flex-direction: column;
        position: fixed;
        top: 0;
        right: -100%;
        width: 280px;
        height: 100vh;
        background: rgba(10, 10, 10, 0.98);
        padding: 6rem 2rem 2rem;
        transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        align-items: flex-start;
        gap: 1.5rem !important;
        border-left: 1px solid rgba(255,255,255,0.05);
        z-index: 900;
        overflow-y: auto;
    }
    
    .nav.mobile-active .nav-links,
    .hero-navbar.mobile-active .hero-nav-links {
        right: 0 !important;
    }
    
    .mobile-menu-btn.active span:nth-child(1) { transform: translateY(9px) rotate(45deg); }
    .mobile-menu-btn.active span:nth-child(2) { opacity: 0; }
    .mobile-menu-btn.active span:nth-child(3) { transform: translateY(-9px) rotate(-45deg); }
    
    /* Make dropdowns relative for mobile */
    .nav-links li.has-arrow .dropdown,
    .hero-nav-links li.has-arrow .dropdown {
        position: relative !important;
        top: 0 !important; left: 0 !important;
        transform: none !important;
        width: 100% !important;
        min-width: 100% !important;
        box-shadow: none !important;
        padding: 0 0 0 1rem !important;
        background: transparent !important;
        margin-top: 10px !important;
        display: none !important;
    }
    .nav-links li.has-arrow.open .dropdown,
    .hero-nav-links li.has-arrow.open .dropdown {
        display: block !important;
        opacity: 1 !important;
        pointer-events: all !important;
    }
    
    .nav-links li.has-arrow .dropdown > li > a,
    .hero-nav-links li.has-arrow .dropdown > li > a {
        color: #fff !important;
        padding: 0.8rem 0 !important;
    }
    
    /* Flyouts */
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout {
        position: relative !important;
        top: 0 !important; left: 0 !important;
        transform: none !important;
        width: 100% !important;
        min-width: 100% !important;
        box-shadow: none !important;
        background: rgba(255,255,255,0.05) !important;
        padding: 0.5rem !important;
        margin-top: 5px !important;
        display: none !important;
    }
    .nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout,
    .hero-nav-links li.has-arrow .dropdown > li.has-flyout.open .flyout {
        display: block !important;
        opacity: 1 !important;
        pointer-events: all !important;
        transform: none !important;
    }
    
    .nav-links li.has-arrow .dropdown li.has-flyout .flyout li a,
    .hero-nav-links li.has-arrow .dropdown li.has-flyout .flyout li a {
        color: #ccc !important;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    var navContainer = document.querySelector('.hero-nav-container, .nav');
    if (navContainer && !document.querySelector('.mobile-menu-btn')) {
        var btn = document.createElement('div');
        btn.className = 'mobile-menu-btn';
        btn.innerHTML = '<span></span><span></span><span></span>';
        navContainer.appendChild(btn);
        
        btn.addEventListener('click', function() {
            this.classList.toggle('active');
            var navbar = document.querySelector('.hero-navbar, .nav');
            if(navbar) navbar.classList.toggle('mobile-active');
        });
    }
});
</script>
<!-- END MOBILE NAV FIX -->
"""

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if '<!-- MOBILE NAV FIX -->' not in content:
        # inject right before </body>
        new_content = content.replace('</body>', injection_code + '\n</body>')
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {os.path.basename(filepath)}")
