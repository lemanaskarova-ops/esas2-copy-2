import urllib.request
import re
import ssl
import json
import os
from html import unescape
from concurrent.futures import ThreadPoolExecutor

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ids = ['8', '21', '18', '10', '5', '2', '13', '16', '3554', '27', '7', '24', '26', '28', '3422', '14', '19', '3', '17', '25', '11', '15', '30', '6', '3569', '9', '29', '20', '31', '4', '23', '22', '32', '12']

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return unescape(cleantext.strip())

def fetch_details(news_id):
    url = f'https://rabitakolleci.edu.az/news/{news_id}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
        title = clean_html(title_match.group(1)) if title_match else "Xəbər"
        
        # Date
        date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', html)
        date_str = date_match.group(1) if date_match else "2024"
        
        # Description
        desc_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', html, re.DOTALL)
        desc = ""
        if desc_match:
            desc = clean_html(desc_match.group(1))
            desc = " ".join(desc.split())
            if len(desc) > 200: desc = desc[:197] + "..."
        
        # Image
        img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', html)
        img_url = img_match.group(1) if img_match else ""
        
        return {
            'id': news_id,
            'title': title,
            'desc': desc,
            'date': date_str,
            'img': img_url,
            'url': url
        }
    except:
        return None

print("Fetching details for all news...")
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_details, ids))

results = [r for r in results if r]
print(f"Successfully fetched {len(results)} items.")

# Download images
for i, r in enumerate(results):
    if r['img']:
        ext = r['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = 'jpg'
        local_name = f"news_auto_{r['id']}.{ext}"
        try:
            req = urllib.request.Request(r['img'], headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, context=ctx).read()
            with open(local_name, 'wb') as f:
                f.write(data)
            r['local_img'] = local_name
        except:
            r['local_img'] = "news1.webp"
    else:
        r['local_img'] = "news1.webp"

with open('news_final.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
