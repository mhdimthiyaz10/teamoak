import urllib.request
import urllib.parse
import re

url = 'https://www.google.com/maps/search/Best+Vibes+General+Contracting+LLC+Abu+Dhabi'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Look for the pb string in the HTML
    match = re.search(r'\"(https://www.google.com/maps/embed\?pb=[^\"]+)\"', html)
    if match:
        print('FOUND:', match.group(1))
    else:
        print('No pb found in the search results.')
        
    # Let's try to extract the cid or place id
    match2 = re.search(r'0x[0-9a-f]+:0x[0-9a-f]+', html)
    if match2:
        print('FOUND ID:', match2.group(0))
except Exception as e:
    print('Error:', e)
