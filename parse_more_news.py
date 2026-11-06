import urllib.request
import re
import ssl
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return unescape(cleantext.strip())

url = 'https://rabitakolleci.edu.az/news'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')

blocks = html.split('<article')
results = []
for b in blocks[1:]:
    link_match = re.search(r'href=[\"\'](https://rabitakolleci.edu.az/news/\d+)[\"\']', b)
    if not link_match: continue
    link = link_match.group(1)
    
    img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', b)
    img_url = img_match.group(1) if img_match else None
    
    title_match = re.search(r'<h[23][^>]*><a[^>]*>(.*?)</a>', b)
    if not title_match:
        title_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', b)
    title = clean_html(title_match.group(1)) if title_match else 'Title not found'
    
    desc_match = re.search(r'<p>(.*?)</p>', b)
    desc = clean_html(desc_match.group(1)) if desc_match else ''
    
    results.append({'url': link, 'img': img_url, 'title': title, 'desc': desc})

print(results)
