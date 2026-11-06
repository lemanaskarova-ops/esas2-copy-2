import urllib.request
import re
import ssl
import json
import time
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return unescape(cleantext.strip())

def get_html(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    except:
        return ""

all_news = []
page = 1
while len(all_news) < 22 and page < 8:
    url = f'https://rabitakolleci.edu.az/news/' if page == 1 else f'https://rabitakolleci.edu.az/news/page/{page}/'
    print(f"Scraping {url}")
    html = get_html(url)
    if not html: break
    
    # Extract article blocks
    articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if not articles: break
    
    for art in articles:
        link_match = re.search(r'href=[\"\'](https://rabitakolleci.edu.az/news/(\d+))[\"\']', art)
        if not link_match: continue
        news_url = link_match.group(1)
        news_id = link_match.group(2)
        
        if news_id in [x['id'] for x in all_news]: continue
        
        title_match = re.search(r'<h[23][^>]*><a[^>]*>(.*?)</a>', art)
        title = clean_html(title_match.group(1)) if title_match else "Xəbər"
        
        img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', art)
        img_url = img_match.group(1) if img_match else ""
        
        desc_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', art, re.DOTALL)
        if not desc_match: desc_match = re.search(r'<p>(.*?)</p>', art, re.DOTALL)
        desc = clean_html(desc_match.group(1))[:150] + "..." if desc_match else ""
        
        date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', art)
        date_str = date_match.group(1) if date_match else "2024"
        
        all_news.append({
            'id': news_id,
            'title': title,
            'url': news_url,
            'img': img_url,
            'desc': desc,
            'date': date_str
        })
    page += 1

print(f"Found {len(all_news)} news items.")

# Download images
for i, item in enumerate(all_news):
    if item['img']:
        ext = item['img'].split('.')[-1].split('?')[0]
        if len(ext) > 4: ext = 'jpg'
        local_name = f"news_real_{i+1}.{ext}"
        try:
            req = urllib.request.Request(item['img'], headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(req, context=ctx).read()
            with open(local_name, 'wb') as f:
                f.write(data)
            item['local_img'] = local_name
        except:
            item['local_img'] = "news1.webp"
    else:
        item['local_img'] = "news1.webp"

with open('news_batch.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)
