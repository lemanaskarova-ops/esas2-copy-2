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

# These were found by the previous step
all_ids = ['3569', '3554', '3422', '3398', '3391', '3386', '3376', '3363', '3351', '3341', '3322', '3291', '3284', '3272', '3266', '3257', '3248', '3240', '3228', '3216', '3203', '3196', '3189', '3174', '3156']

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    cleantext = cleantext.replace('\n', ' ').replace('\r', ' ').strip()
    return unescape(cleantext)

def fetch_details(news_id):
    url = f'https://rabitakolleci.edu.az/news/{news_id}'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html)
        if not title_match: title_match = re.search(r'<title>(.*?)</title>', html)
        title = clean_html(title_match.group(1)) if title_match else "Xəbər"
        if " – Bakı Dövlət Rabitə və Nəqliyyat Kolleci" in title:
            title = title.replace(" – Bakı Dövlət Rabitə və Nəqliyyat Kolleci", "")
            
        # Date
        date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', html)
        date_str = date_match.group(1) if date_match else "2024"
        
        # Description
        desc_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', html, re.DOTALL)
        desc = ""
        if desc_match:
            desc = clean_html(desc_match.group(1))
            desc = " ".join(desc.split())
            if len(desc) > 180: desc = desc[:177] + "..."
        
        # Image
        # Find images that are not logos or icons
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
            'date': date_str,
            'img': img_url,
            'url': url
        }
    except:
        return None

print("Fetching details for top 25 news...")
with ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_details, all_ids))

results = [r for r in results if r]
print(f"Successfully fetched {len(results)} items.")

# Download images
for i, r in enumerate(results):
    if r['img']:
        ext = r['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4 or len(ext) < 2: ext = 'jpg'
        local_name = f"news_real_{r['id']}.{ext}"
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

with open('news_final_25.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
