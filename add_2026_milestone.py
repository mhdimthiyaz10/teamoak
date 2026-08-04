import os
import json

base_dir = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
about_file = os.path.join(base_dir, "about.html")
en_file = os.path.join(base_dir, "en.json")
ar_file = os.path.join(base_dir, "ar.json")

# 1. Update about.html
with open(about_file, 'r', encoding='utf-8') as f:
    content = f.read()

target_2024 = """<!-- 2024 -->
<div class="tl-item left fu d3">
<div class="tl-left">
<span class="tl-tag" data-i18n="about_new_horizons_innovation">New Horizons &amp; Innovation</span>
<h3 class="tl-heading" data-i18n="about_pushing_into_new_markets">Pushing Into New Markets</h3>
<ul class="tl-ventures">
<li data-i18n="about_bubble_bubble_tea_drinksuk_entered"><strong>Bubble Bubble Tea Drinks</strong><span class="loc">UK</span> — Entered the UK market, introducing a refreshing new brand of bubble tea drinks.</li>
<li data-i18n="about_team_oak_general_tradingsaudi_arabia"><strong>Team Oak General Trading</strong><span class="loc">Saudi Arabia</span> — Initiated as a building material trading company, expanding our trading operations and product offerings.</li>
</ul>
</div>
<div class="tl-dot">
<div class="tl-circle"><svg viewbox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"></path></svg></div>
<div class="tl-year">2024</div>
</div>
<div class="tl-right"></div>
</div>"""

milestone_2026 = """
<!-- 2026 -->
<div class="tl-item right fu d4">
<div class="tl-left"></div>
<div class="tl-dot">
<div class="tl-circle"><svg viewbox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"></path></svg></div>
<div class="tl-year">2026</div>
</div>
<div class="tl-right">
<span class="tl-tag" data-i18n="about_strategic_expansion_2026">Strategic Expansion</span>
<h3 class="tl-heading" data-i18n="about_broadening_our_portfolio">Broadening Our Portfolio</h3>
<ul class="tl-ventures">
<li data-i18n="about_makin_spare_parts_milestone"><strong>Makin Spare parts Trading Company</strong><span class="loc">UAE</span> — Established to provide high-quality automotive and machinery spare parts.</li>
<li data-i18n="about_cafein_milestone"><strong>Cafein</strong><span class="loc">UAE</span> — Launched a quick-service brand focused on healthy, fresh, and energizing options.</li>
<li data-i18n="about_logistics_milestone"><strong>Team Oak Logistics Services</strong><span class="loc">UAE</span> — Initiated to deliver seamless, comprehensive supply chain solutions.</li>
<li data-i18n="about_sugar_packing_milestone"><strong>Sugar Packing Unit</strong><span class="loc">UAE</span> — Started our state-of-the-art industrial sugar packing facility.</li>
</ul>
</div>
</div>"""

if "<!-- 2026 -->" not in content:
    if target_2024 in content:
        content = content.replace(target_2024, target_2024 + "\n" + milestone_2026)
        with open(about_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Updated about.html with 2026 milestone.")
    else:
        print("Could not find 2024 milestone target in about.html.")
else:
    print("2026 milestone already exists in about.html.")

# 2. Update JSON files
def update_json(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for k, v in translations.items():
        if k not in data:
            data[k] = v
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"No new keys added to {os.path.basename(filepath)}.")

en_translations = {
    "about_strategic_expansion_2026": "Strategic Expansion",
    "about_broadening_our_portfolio": "Broadening Our Portfolio",
    "about_makin_spare_parts_milestone": "<strong>Makin Spare parts Trading Company</strong><span class=\"loc\">UAE</span> — Established to provide high-quality automotive and machinery spare parts.",
    "about_cafein_milestone": "<strong>Cafein</strong><span class=\"loc\">UAE</span> — Launched a quick-service brand focused on healthy, fresh, and energizing options.",
    "about_logistics_milestone": "<strong>Team Oak Logistics Services</strong><span class=\"loc\">UAE</span> — Initiated to deliver seamless, comprehensive supply chain solutions.",
    "about_sugar_packing_milestone": "<strong>Sugar Packing Unit</strong><span class=\"loc\">UAE</span> — Started our state-of-the-art industrial sugar packing facility."
}

ar_translations = {
    "about_strategic_expansion_2026": "توسع استراتيجي",
    "about_broadening_our_portfolio": "توسيع محفظتنا",
    "about_makin_spare_parts_milestone": "<strong>شركة مكين لتجارة قطع الغيار</strong><span class=\"loc\">الإمارات</span> — تأسست لتوفير قطع غيار سيارات وآلات عالية الجودة.",
    "about_cafein_milestone": "<strong>كافين</strong><span class=\"loc\">الإمارات</span> — إطلاق علامة تجارية للخدمة السريعة تركز على الخيارات الصحية والطازجة والمنشطة.",
    "about_logistics_milestone": "<strong>خدمات تيم أوك اللوجستية</strong><span class=\"loc\">الإمارات</span> — بدأت لتقديم حلول سلسلة التوريد الشاملة والسلسة.",
    "about_sugar_packing_milestone": "<strong>وحدة تعبئة السكر</strong><span class=\"loc\">الإمارات</span> — بدأنا تشغيل منشأة تعبئة السكر الصناعية المتطورة لدينا."
}

update_json(en_file, en_translations)
update_json(ar_file, ar_translations)
