import urllib.request
import re
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_html(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        return urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    except:
        return ""

# Read script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract newsData JSON
match = re.search(r'const newsData = (\[.*?\]);', content, re.DOTALL)
if not match:
    print("Could not find newsData")
    exit()

news_data = json.loads(match.group(1))

# Map to store dates: news_id -> date
dates_map = {}

# Scrape first few pages of news to get dates
for page in range(1, 12):
    url = f'https://rabitakolleci.edu.az/news/' if page == 1 else f'https://rabitakolleci.edu.az/news/page/{page}/'
    html = get_html(url)
    if not html: break
    
    articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    for art in articles:
        link_match = re.search(r'href=[\"\']https://rabitakolleci.edu.az/news/(\d+)[\"\']', art)
        if link_match:
            news_id = int(link_match.group(1))
            date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', art)
            if date_match:
                dates_map[news_id] = date_match.group(1).strip()

month_ru_az = {
    'Янв': 'Yanvar', 'Январь': 'Yanvar', 'Фев': 'Fevral', 'Февраль': 'Fevral',
    'Мар': 'Mart', 'Март': 'Mart', 'Апр': 'Aprel', 'Апрель': 'Aprel', 'Май': 'May',
    'Июн': 'İyun', 'Июнь': 'İyun', 'Июл': 'İyul', 'Июль': 'İyul', 'Авг': 'Avqust',
    'Август': 'Avqust', 'Сен': 'Sentyabr', 'Сентябрь': 'Sentyabr', 'Окт': 'Oktyabr',
    'Октябрь': 'Oktyabr', 'Ноя': 'Noyabr', 'Ноябрь': 'Noyabr', 'Дек': 'Dekabr',
    'января': 'Yanvar', 'февраля': 'Fevral', 'марта': 'Mart', 'апреля': 'Aprel',
    'мая': 'May', 'июня': 'İyun', 'июlya': 'İyul', 'августа': 'Avqust',
    'сentyabrя': 'Sentyabr', 'октября': 'Oktyabr', 'ноября': 'Noyabr', 'декабря': 'Dekabr'
}

def translate_date(d_str):
    for ru, az in month_ru_az.items():
        if ru.lower() in d_str.lower():
            return re.sub(ru, az, d_str, flags=re.IGNORECASE)
    return d_str

# Update dates in news_data
for item in news_data:
    url_id = int(item['url'].rstrip('/').split('/')[-1])
    if url_id in dates_map:
        item['date'] = translate_date(dates_map[url_id])

# Save back to script.js
new_news_code = f"const newsData = {json.dumps(news_data, ensure_ascii=False, indent=2)};"
new_content = re.sub(r'const newsData = \[.*?\];', new_news_code, content, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Dates updated and script fixed.")
