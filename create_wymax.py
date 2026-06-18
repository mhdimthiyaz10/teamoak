import os

directory = r"c:\Users\Mohammed Imthiyaz\Documents\oak tm"
source_file = os.path.join(directory, "bubbl.html")
target_file = os.path.join(directory, "wymax-media.html")

with open(source_file, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "<title>Bubbl</title>": "<title>WYMAX MEDIA</title>",
    '<span class="page-eyebrow fu">Art of Bubble Tea</span>': '<span class="page-eyebrow fu">Media & Digital Solutions</span>',
    '<h1 class="fu d1">Bubbl<br><em>London</em></h1>': '<h1 class="fu d1">WYMAX<br><em>MEDIA</em></h1>',
    '<h2 class="fu">A Flavor Adventure Like No Other</h2>': '<h2 class="fu">Creative Media Services</h2>',
    'Located in the vibrant heart of London, BUBBL is where the art of bubble tea reaches new heights. Step into our chic, modern store and embark on a flavor adventure like no other. We\'re dedicated to serving up the freshest and most exciting bubble tea creations, crafted with the finest ingredients and a splash of creativity.': 'WYMAX MEDIA is a modern media and digital solutions agency dedicated to elevating your brand through creative storytelling, strategic marketing, and innovative digital design. We partner with businesses to create impactful narratives that resonate with their target audience.',
    'At BUBBL, our menu offers a tantalizing array of options, from classic milk teas and refreshing fruit blends to inventive specialty drinks that push the boundaries of flavor. Choose from a variety of premium teas, perfectly cooked tapioca pearls, and an assortment of unique toppings to make your drink truly your own. Our inviting space is designed for relaxation and enjoyment, whether you\'re stopping by for a quick treat or spending time with friends.': 'Our comprehensive suite of services includes brand identity development, digital marketing, content creation, and web design. By combining artistic vision with data-driven strategies, WYMAX MEDIA ensures that your brand not only stands out in a crowded marketplace but also achieves meaningful engagement and sustained growth.',
    'With a focus on quality, innovation, and a welcoming atmosphere, BUBBL isn\'t just a place to get your bubble tea fix – it\'s a destination where every visit is an experience.': 'With a focus on quality, innovation, and measurable results, WYMAX MEDIA is your trusted partner for navigating the digital landscape and building a brand presence that truly matters.'
}

for old_text, new_text in replacements.items():
    content = content.replace(old_text, new_text)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully created wymax-media.html")
