import re
import json

with open("script.js", "r", encoding="utf-8") as f:
    content = f.read()

# Fix syntax error at id: 13
content = content.replace(
    '];"desc_az":',
    '},{\n    "id": 13,\n    "title_az": "Açıq dərs",\n    "title_en": "Open Lesson",\n    "title_ru": "Открытый урок",\n    "desc_az":'
)

with open("script.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Fixed syntax error")
