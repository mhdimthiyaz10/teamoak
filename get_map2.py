import urllib.request
import urllib.parse
import re
import json

url = 'https://nominatim.openstreetmap.org/search?q=Best+Vibes+General+Contracting+Abu+Dhabi&format=json'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    response = urllib.request.urlopen(req).read().decode('utf-8')
    print('OSM:', response)
except Exception as e:
    pass

url2 = 'https://www.google.com/maps/search/Best+Vibes+General+Contracting+LLC+Abu+Dhabi'
req2 = urllib.request.Request(url2, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req2).read().decode('utf-8')
    match = re.search(r'\"(https://www.google.com/maps/embed\?pb=[^\"]+)\"', html)
    if match:
        print('FOUND EM:', match.group(1))
    
    # Let's just find any place url
    urls = re.findall(r'https://www\.google\.com/maps/place/[^\"]+', html)
    for u in urls[:5]:
        print('URL:', u)
except Exception as e:
    print('Err:', e)
