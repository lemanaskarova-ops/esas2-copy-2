import urllib.request
import re
import ssl
import json
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean(t):
    return unescape(re.sub(r'<[^>]+>', '', t)).strip()

def get_page(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    except:
        return ""

news_items = []
for p in range(1, 4):
    url = f'https://rabitakolleci.edu.az/news/' if p == 1 else f'https://rabitakolleci.edu.az/news/page/{p}/'
    print(f"Fetching {url}")
    html = get_page(url)
    if not html: break
    
    # Each article usually looks like <article ...> ... </article>
    articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    for art in articles:
        link_match = re.search(r'href=[\"\'](https://rabitakolleci.edu.az/news/(\d+))[\"\']', art)
        if not link_match: continue
        news_url = link_match.group(1)
        news_id = link_match.group(2)
        
        if news_id in [x['id'] for x in news_items]: continue
        
        title_match = re.search(r'<h[23][^>]*><a[^>]*>(.*?)</a>', art)
        title = clean(title_match.group(1)) if title_match else "Xəbər"
        
        img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', art)
        img_url = img_match.group(1) if img_match else ""
        
        desc_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', art, re.DOTALL)
        if not desc_match: desc_match = re.search(r'<p>(.*?)</p>', art, re.DOTALL)
        desc = clean(desc_match.group(1)) if desc_match else ""
        desc = " ".join(desc.split())
        if len(desc) > 150: desc = desc[:147] + "..."
        
        date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', art)
        date = date_match.group(1) if date_match else "2024"
        
        news_items.append({
            'id': news_id,
            'title': title,
            'desc': desc,
            'img': img_url,
            'url': news_url,
            'date': date
        })

print(f"Found {len(news_items)} items.")

for i, item in enumerate(news_items):
    if item['img']:
        ext = item['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = 'jpg'
        local = f"news_real_{item['id']}.{ext}"
        try:
            req = urllib.request.Request(item['img'], headers={'User-Agent': 'Mozilla/5.0'})
            with open(local, 'wb') as f:
                f.write(urllib.request.urlopen(req, context=ctx).read())
            item['local_img'] = local
        except:
            item['local_img'] = "news1.webp"
    else:
        item['local_img'] = "news1.webp"

with open('news_20_final.json', 'w', encoding='utf-8') as f:
    json.dump(news_items, f, ensure_ascii=False, indent=2)
