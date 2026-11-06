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

ids = ['3569', '3554', '3464', '3422', '3294', '2819', '2676', '2659', '2589', '2581', '2566', '2540', '2532', '2522', '2483', '2441', '2419', '2391', '2365', '2318']

def clean(t):
    t = re.sub(r'<[^>]+>', ' ', t)
    t = unescape(t)
    t = " ".join(t.split())
    return t.strip()

def fetch(news_id):
    url = f'https://rabitakolleci.edu.az/news/{news_id}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        # Title
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
        title = clean(title_match.group(1)) if title_match else "Xəbər"
        title = title.replace(" – Bakı Dövlət Rabitə və Nəqliyyat Kolleci", "")
        
        # Date
        date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', html)
        date = date_match.group(1) if date_match else "2024"
        
        # Description
        content_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', html, re.DOTALL)
        desc = ""
        if content_match:
            desc = clean(content_match.group(1))
            if len(desc) > 200: desc = desc[:197] + "..."
        
        # Image
        img_matches = re.findall(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', html)
        img_url = ""
        for m in img_matches:
            if 'logo' not in m.lower() and 'icon' not in m.lower() and 'Emblem' not in m:
                img_url = m
                break
        
        return {
            'id': news_id,
            'title': title,
            'desc': desc,
            'date': date,
            'img': img_url,
            'url': url
        }
    except:
        return None

with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch, ids))

results = [r for r in results if r]

for r in results:
    if r['img']:
        ext = r['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = 'jpg'
        local = f"news_real_{r['id']}.{ext}"
        try:
            req = urllib.request.Request(r['img'], headers={'User-Agent': 'Mozilla/5.0'})
            with open(local, 'wb') as f:
                f.write(urllib.request.urlopen(req, context=ctx).read())
            r['local_img'] = local
        except:
            r['local_img'] = "news1.webp"
    else:
        r['local_img'] = "news1.webp"

with open('news_top_20.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
