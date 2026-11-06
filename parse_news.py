import urllib.request
import re
import json
import ssl
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    'https://rabitakolleci.edu.az/news/3569',
    'https://rabitakolleci.edu.az/news/3554',
    'https://rabitakolleci.edu.az/news/3422',
    'https://rabitakolleci.edu.az/news/32',
    'https://rabitakolleci.edu.az/news/31',
    'https://rabitakolleci.edu.az/news/30'
]

results = []

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return unescape(cleantext.strip())

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        title_match = re.search(r'<h[12].*?>(.*?)</h[12]>', html, re.IGNORECASE | re.DOTALL)
        title = clean_html(title_match.group(1)) if title_match else 'Xəbər'
        
        img_match = re.search(r'<div[^>]*class="col-lg-8"[^>]*>.*?<img[^>]*src="(.*?)"', html, re.IGNORECASE | re.DOTALL)
        if not img_match:
            img_match = re.search(r'<div[^>]*class="col-lg-12"[^>]*>.*?<img[^>]*src="(.*?)"', html, re.IGNORECASE | re.DOTALL)
        img_url = img_match.group(1) if img_match else ""
        if img_url and not img_url.startswith('http'):
            img_url = 'https://rabitakolleci.edu.az' + img_url
            
        p_matches = re.findall(r'<p.*?>(.*?)</p>', html, re.IGNORECASE | re.DOTALL)
        desc = ""
        for p in p_matches:
            text = clean_html(p)
            if len(text) > 40:
                desc = text
                break
                
        results.append({
            'url': url,
            'title': title,
            'desc': desc,
            'image': img_url
        })
    except Exception as e:
        results.append({'url': url, 'error': str(e)})

with open('news_data.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved to news_data.json")
