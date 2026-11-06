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
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return ""

# Read newsData array from news_data_js.txt
with open('news_data_js.txt', 'r', encoding='utf-8') as f:
    text = f.read()

json_str = text.split('const newsData = ')[1].rsplit(';', 1)[0]
news_data = json.loads(json_str)

# Map to store dates: news_id -> date
dates_map = {}

# Scrape dates from news list pages
for page in range(1, 15):
    url = f'https://rabitakolleci.edu.az/news/' if page == 1 else f'https://rabitakolleci.edu.az/news/page/{page}/'
    html = get_html(url)
    if not html: break
    
    articles = re.findall(r'<article[^>]*>(.*?)</article>', html, re.DOTALL | re.IGNORECASE)
    if not articles: break
    
    for art in articles:
        link_match = re.search(r'href=[\"\']https://rabitakolleci.edu.az/news/(\d+)[\"\']', art)
        if link_match:
            news_id = int(link_match.group(1))
            date_match = re.search(r'(\d{1,2}\s+[a-zA-Zа-яА-Яəğıöçşü]+\s+\d{4})', art)
            if date_match:
                dates_map[news_id] = date_match.group(1).strip()
            else:
                date_match = re.search(r'class=[\"\']ast-date-published[\"\'][^>]*>(.*?)</span>', art)
                if date_match:
                    dates_map[news_id] = re.sub(r'<[^>]+>', '', date_match.group(1)).strip()

month_ru_az = {
    'Янв': 'Yanvar', 'Январь': 'Yanvar',
    'Фев': 'Fevral', 'Февраль': 'Fevral',
    'Мар': 'Mart', 'Март': 'Mart',
    'Апр': 'Aprel', 'Апрель': 'Aprel',
    'Май': 'May',
    'Июн': 'İyun', 'Июнь': 'İyun',
    'Июл': 'İyul', 'Июль': 'İyul',
    'Авг': 'Avqust', 'Август': 'Avqust',
    'Сен': 'Sentyabr', 'Сентябрь': 'Sentyabr',
    'Окт': 'Oktyabr', 'Октябрь': 'Oktyabr',
    'Ноя': 'Noyabr', 'Ноябрь': 'Noyabr',
    'Дек': 'Dekabr', 'Декабрь': 'Dekabr',
    'января': 'Yanvar', 'февраля': 'Fevral', 'марта': 'Mart', 'апреля': 'Aprel',
    'мая': 'May', 'июня': 'İyun', 'июля': 'İyul', 'августа': 'Avqust',
    'сентября': 'Sentyabr', 'октября': 'Oktyabr', 'ноября': 'Noyabr', 'декабря': 'Dekabr'
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
    else:
        # Check title if url_id is different
        pass

# Fix syntax in script.js by replacing the entire const newsData = [...]
with open("script.js", "r", encoding="utf-8", errors="ignore") as f:
    script_content = f.read()

# Make sure it's valid JSON
news_json = json.dumps(news_data, ensure_ascii=False, indent=2)
news_code = f"const newsData = {news_json};\n\n"

# Replace
script_content = re.sub(r'const newsData = \[.*?\].*?(?=const lecturesData =)', news_code, script_content, flags=re.DOTALL)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(script_content)

print("Done generating correct newsData and fixing script.js syntax!")
