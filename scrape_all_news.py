import urllib.request
import re
import ssl
import json
import os
from html import unescape

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return unescape(cleantext.strip())

def get_news_from_page(page_url):
    try:
        req = urllib.request.Request(page_url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        
        # Look for article blocks
        # Based on previous output, news items are in <article> tags
        items = []
        # Find article contents
        articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
        
        for art in articles:
            # Link & ID
            link_match = re.search(r'href=[\"\'](https://rabitakolleci.edu.az/news/(\d+))[\"\']', art)
            if not link_match: continue
            url = link_match.group(1)
            news_id = link_match.group(2)
            
            # Title
            title_match = re.search(r'<h[23][^>]*><a[^>]*>(.*?)</a>', art)
            if not title_match:
                title_match = re.search(r'<h[23][^>]*>(.*?)</h[23]>', art)
            title = clean_html(title_match.group(1)) if title_match else 'Xəbər'
            
            # Image
            img_match = re.search(r'<img[^>]+src=[\"\']([^\'\"]+)[\"\']', art)
            img_url = img_match.group(1) if img_match else None
            
            # Description (excerpt)
            desc_match = re.search(r'<div[^>]*class=[\"\']entry-content[^>]*>(.*?)</div>', art, re.DOTALL)
            if not desc_match:
                desc_match = re.search(r'<p>(.*?)</p>', art, re.DOTALL)
            
            desc = ""
            if desc_match:
                desc = clean_html(desc_match.group(1))
                # remove excessive spaces/newlines
                desc = " ".join(desc.split())
                if len(desc) > 150:
                    desc = desc[:147] + "..."
            
            # Date
            # Usually in a span or time tag
            date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', art)
            date = date_match.group(1) if date_match else "2024"
            
            items.append({
                'id': news_id,
                'title': title,
                'desc': desc,
                'img': img_url,
                'url': url,
                'date': date
            })
        return items
    except Exception as e:
        print(f"Error on {page_url}: {e}")
        return []

all_news = []
page = 1
while len(all_news) < 25 and page < 6:
    url = f'https://rabitakolleci.edu.az/news' if page == 1 else f'https://rabitakolleci.edu.az/news/{page}'
    print(f"Scraping page {page}...")
    page_news = get_news_from_page(url)
    if not page_news: break
    for item in page_news:
        if item['id'] not in [x['id'] for x in all_news]:
            all_news.append(item)
    page += 1

# Limit to 24 for a nice grid
all_news = all_news[:24]

print(f"Found {len(all_news)} unique news items.")

# Now download images and prepare data for JS
final_data = []
for i, item in enumerate(all_news):
    ext = 'jpg'
    if item['img']:
        if '.png' in item['img'].lower(): ext = 'png'
        elif '.webp' in item['img'].lower(): ext = 'webp'
        elif '.jpeg' in item['img'].lower(): ext = 'jpeg'
    
    filename = f"news_auto_{i+1}.{ext}"
    if item['img']:
        try:
            print(f"Downloading {item['img']} -> {filename}")
            img_req = urllib.request.Request(item['img'], headers={'User-Agent': 'Mozilla/5.0'})
            img_data = urllib.request.urlopen(img_req, context=ctx).read()
            with open(filename, 'wb') as f:
                f.write(img_data)
            item['local_img'] = filename
        except:
            item['local_img'] = "news1.webp" # fallback
    else:
        item['local_img'] = "news1.webp"

with open('scraped_news.json', 'w', encoding='utf-8') as f:
    json.dump(all_news, f, ensure_ascii=False, indent=2)

print("Scraping complete.")
