import urllib.request
import re
import ssl
import json
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean(t):
    if not t: return ""
    t = re.sub(r'<[^>]+>', ' ', t)
    t = unescape(t)
    return " ".join(t.split()).strip()

def get_news(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        # Match each article block
        articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
        results = []
        for art in articles:
            link_match = re.search(r'href=[\"\'](https://rabitakolleci.edu.az/news/(\d+))[\"\']', art)
            if not link_match: continue
            url = link_match.group(1)
            news_id = link_match.group(2)
            
            # Title - often in h2 or h3 with class entry-title
            title_match = re.search(r'class=[\"\']entry-title[\"\'][^>]*>.*?<a[^>]*>(.*?)</a>', art, re.DOTALL)
            if not title_match:
                title_match = re.search(r'<h[23][^>]*>.*?<a[^>]*>(.*?)</a>', art, re.DOTALL)
            title = clean(title_match.group(1)) if title_match else "Xəbər"
            
            # Image
            img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', art)
            img_url = img_match.group(1) if img_match else ""
            
            # Description
            desc_match = re.search(r'class=[\"\']entry-content[\"\'][^>]*>(.*?)</div>', art, re.DOTALL)
            if not desc_match:
                desc_match = re.search(r'<p>(.*?)</p>', art, re.DOTALL)
            desc = clean(desc_match.group(1)) if desc_match else ""
            if len(desc) > 150: desc = desc[:147] + "..."
            
            # Date
            date_match = re.search(r'class=[\"\']ast-date-published[\"\'][^>]*>(.*?)</span>', art, re.DOTALL)
            date = clean(date_match.group(1)) if date_match else "2024"
            
            results.append({
                'id': news_id,
                'title': title,
                'desc': desc,
                'date': date,
                'img': img_url,
                'url': url
            })
        return results
    except Exception as e:
        print(f"Error {url}: {e}")
        return []

all_news = []
for p in range(1, 10):
    url = f'https://rabitakolleci.edu.az/news/category/umumi_xeberler/page/{p}/'
    print(f"Scraping {url}")
    items = get_news(url)
    if not items: break
    for it in items:
        if it['id'] not in [x['id'] for x in all_news]:
            all_news.append(it)
    if len(all_news) >= 25: break

print(f"Total found: {len(all_news)}")

# Download images
for i, r in enumerate(all_news):
    if r['img']:
        ext = r['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = 'jpg'
        local = f"news_proper_{r['id']}.{ext}"
        try:
            req = urllib.request.Request(r['img'], headers={'User-Agent': 'Mozilla/5.0'})
            with open(local, 'wb') as f:
                f.write(urllib.request.urlopen(req, context=ctx).read())
            r['local_img'] = local
        except:
            r['local_img'] = "news1.webp"
    else:
        r['local_img'] = "news1.webp"

with open('news_proper_25.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)
