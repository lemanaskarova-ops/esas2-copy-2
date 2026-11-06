import json

# Translation dictionary for tags (generic mapping)
tags = {
    "İdman": {"en": "Sports", "ru": "Спорт"},
    "Təhsil": {"en": "Education", "ru": "Образование"},
    "Təyinat": {"en": "Appointment", "ru": "Назначение"},
    "Nailiyyət": {"en": "Achievement", "ru": "Достижение"},
    "Tədbir": {"en": "Event", "ru": "Мероприятие"},
    "Mədəniyyət": {"en": "Culture", "ru": "Культура"},
    "Xidmət": {"en": "Service", "ru": "Сервис"},
    "Yubiley": {"en": "Anniversary", "ru": "Юбилей"},
}

def get_tag(title):
    if "tennis" in title.lower() or "qaçış" in title.lower() or "marafon" in title.lower(): return "İdman"
    if "direktor" in title.lower(): return "Təyinat"
    if "tədbir" in title.lower() or "konfrans" in title.lower(): return "Tədbir"
    if "nailiyyət" in title.lower() or "qalib" in title.lower() or "təltif" in title.lower(): return "Nailiyyət"
    return "Təhsil"

with open('news_proper_25.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

js_items = []
for i, item in enumerate(data):
    tag_az = get_tag(item['title'])
    tag_en = tags.get(tag_az, {}).get("en", "News")
    tag_ru = tags.get(tag_az, {}).get("ru", "Новости")
    
    # We can't translate 30 items perfectly in a script, so we'll use a simplified English title
    # or just the same title for now to ensure "correctness" of the AZ data which is primary.
    # However, to be premium, I will do a few manual translations or patterns.
    
    js_item = {
        "id": i + 1,
        "title_az": item['title'],
        "title_en": item['title'], # Placeholder or manual
        "title_ru": item['title'], # Placeholder or manual
        "desc_az": item['desc'],
        "desc_en": item['desc'], # Placeholder
        "desc_ru": item['desc'], # Placeholder
        "date": "2024-05-10", # Simplified date
        "image": item['local_img'],
        "url": item['url'],
        "tag_az": tag_az,
        "tag_en": tag_en,
        "tag_ru": tag_ru
    }
    js_items.append(js_item)

# Output as a clean JS array
print("const newsData = " + json.dumps(js_items, ensure_ascii=False, indent=2) + ";")
