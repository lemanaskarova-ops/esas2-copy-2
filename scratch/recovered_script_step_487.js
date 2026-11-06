import json
import re
import os

in_json = "/Users/konul/.gemini/antigravity/brain/bf624dce-3b3d-42c7-811e-5c4c2ea8e6ff/scratch/all_official_news.json"
script_path = "/Users/konul/Documents/esas2 copy 2/script.js"

with open(in_json, "r", encoding="utf-8") as f:
    raw_posts = json.load(f)

with open(script_path, "r", encoding="utf-8") as f:
    script_text = f.read()

# Parse existing newsData from script.js to preserve hand-crafted EN/RU translations where URL matches
existing_by_url = {}
m_existing = re.search(r"const newsData = (\[.*?\]);\s*const libraryData", script_text, re.DOTALL)
if m_existing:
    try:
        old_list = json.loads(m_existing.group(1))
        for item in old_list:
            if item.get("url"):
                existing_by_url[item["url"]] = item
    except Exception as e:
        print("Could not parse old newsData:", e)

MONTHS_AZ = {
    1: "Yanvar", 2: "Fevral", 3: "Mart", 4: "Aprel", 5: "May", 6: "İyun",
    7: "İyul", 8: "Avqust", 9: "Sentyabr", 10: "Oktyabr", 11: "Noyabr", 12: "Dekabr"
}
MONTH_NAME_MAP = {
    "yanvar": 1, "fevral": 2, "mart": 3, "aprel": 4, "may": 5, "iyun": 6,
    "iyul": 7, "avqust": 8, "sentyabr": 9, "oktyabr": 10, "noyabr": 11, "dekabr": 12
}

def clean_full_text(t, title=""):
    if not t:
        return ""
    if "Ana səhifə Xəbərlər" in t:
        t = t.split("Ana səhifə Xəbərlər")[-1].strip()
    t = re.sub(
        r"^(Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kolleci\s*)*(Ana səhifə\s*)*(Xəbərlər\s*)*(Ümumi xəbərlər\s*)*",
        "",
        t,
        flags=re.IGNORECASE,
    ).strip()
    t = re.split(r"←\s*Предыдущая|Следующая\s*Запись|Добавить комментарий|Şərh bildir|Copyright\s*©", t)[0].strip()
    # Fix accidental spaced digits/suffixes from official WP editor
    t = re.sub(r"25\s*\.09\.202\s*6\s*-c\s*ı", "25.09.2025-ci", t)
    t = re.sub(r"1\s*2\s*\.12\.202\s*5\s*-ci", "12.12.2025-ci", t)
    t = re.sub(r"30\s*\.0\s*5\s*\.202\s*5\s*-c\s*i", "30.05.2025-ci", t)
    t = re.sub(r"Ü\s+mummilli\s+L\s+ideri", "Ümummilli Lideri", t)
    t = re.sub(r"Tələb\s+əsi", "Tələbəsi", t)
    t = re.sub(r"U\s+lu\s+Ö\s+ndər", "Ulu Öndər", t)
    if title and t.startswith(title):
        rest = t[len(title):].strip()
        if len(rest) > 40:
            t = rest
    return t.strip()

def extract_date(p, cleaned_text):
    txt = (p.get("title", "") + " " + cleaned_text)
    txt_norm = re.sub(r"(?<=\d)\s+(?=\d)", "", txt)
    txt_norm = re.sub(r"(?<=\d)\s*\.\s*(?=\d)", ".", txt_norm)
    m = re.search(r"\b(\d{1,2})\.(\d{1,2})\.(202\d)\b", txt_norm)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if 1 <= d <= 31 and 1 <= mo <= 12:
            return f"{d:02d} {MONTHS_AZ[mo]} {y}"
    m2 = re.search(
        r"\b(\d{1,2})\s+(yanvar|fevral|mart|aprel|may|iyun|iyul|avqust|sentyabr|oktyabr|noyabr|dekabr)\s+(202\d)\b",
        txt_norm,
        re.IGNORECASE,
    )
    if m2:
        d = int(m2.group(1))
        mo = MONTH_NAME_MAP[m2.group(2).lower()]
        y = int(m2.group(3))
        return f"{d:02d} {MONTHS_AZ[mo]} {y}"
    img = p.get("img_url", "")
    m3 = re.search(r"(202\d)-(\d{2})-(\d{2})", img)
    if m3:
        y, mo, d = int(m3.group(1)), int(m3.group(2)), int(m3.group(3))
        if 1 <= d <= 31 and 1 <= mo <= 12:
            return f"{d:02d} {MONTHS_AZ[mo]} {y}"
    m4 = re.search(r"/uploads/(202\d)/(\d{2})/", img)
    if m4:
        y, mo = int(m4.group(1)), int(m4.group(2))
        if 1 <= mo <= 12:
            return f"{MONTHS_AZ[mo]} {y}"
    return "2025"

def classify_tag(title, text):
    comb = (title + " " + text).lower()
    if any(k in comb for k in ["idman", "qaçış", "marafon", "tennis", "turnir", "yarış", "şahmat", "voleybol", "futbol"]):
        return ("İdman", "Sports", "Спорт")
    if any(k in comb for k in ["direktor", "təyinat", "təyin edil", "kollektivə təqdim"]):
        return ("Təyinat", "Appointment", "Назначение")
    if any(k in comb for k in ["fəxri fərman", "təltif", "qalib", "uğur", "mükafat", "yerə layiq"]):
        return ("Nailiyyət", "Achievement", "Достижение")
    if any(k in comb for k in ["müqavilə", "memorandum", "əməkdaşlıq"]):
        return ("Əməkdaşlıq", "Partnership", "Сотрудничество")
    if any(k in comb for k in ["imtahan", "dərs", "tədris", "ixtisas", "tələbə qəbulu", "açıq dərs"]):
        return ("Tədris", "Academics", "Образование")
    if any(k in comb for k in ["anım günü", "şəhid", "heydər əliyev", "zəfər günü", "20 yanvar", "xocalı", "konstitusiya", "bayraq"]):
        return ("Anım və Tarix", "Commemoration", "Памятная дата")
    return ("Tədbir", "Event", "Мероприятие")

def make_excerpt(text, max_len=185):
    if not text:
        return ""
    if len(text) <= max_len:
        return text
    cut = text[:max_len].rsplit(" ", 1)[0].rstrip(",;:")
    return cut + "..."

def split_into_paragraphs(text):
    if not text:
        return []
    # Split long single-block text into natural paragraphs of ~2-3 sentences
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-ZƏÖÜĞÇŞİ“«\"0-9])", text)
    if len(sentences) <= 2:
        return [text]
    paras = []
    buf = []
    char_count = 0
    for s in sentences:
        buf.append(s)
        char_count += len(s)
        if len(buf) >= 2 and char_count >= 240:
            paras.append(" ".join(buf))
            buf = []
            char_count = 0
    if buf:
        paras.append(" ".join(buf))
    return paras

def auto_translate_en(title_az, tag_en, date_str):
    t = title_az
    low = t.lower()
    if "narkomaniya" in low:
        return (
            "Educational Awareness Seminar on 'Say No to Drug Addiction' Held at the College",
            "An educational awareness event was organized at Baku State Communications and Transport College under AzTU with the participation of faculty, experts, and students to promote a healthy lifestyle.",
        )
    if "məişət zorakılığı" in low:
        return (
            "Conference Titled 'Say No to Domestic Violence' Organized at the College",
            "A comprehensive seminar addressing legal protection, social support mechanisms, and prevention of domestic violence was held at Baku State Communications and Transport College.",
        )
    if "korrupsiya" in low:
        return (
            "Anti-Corruption Awareness and Academic Integrity Seminar at the College",
            "Baku State Communications and Transport College hosted an awareness session focused on transparency, ethical governance, and youth responsibility in combating corruption.",
        )
    if "azərbaycan dilinin saflığı" in low or "ana dili" in low:
        return (
            "Seminar Dedicated to the Purity of the Azerbaijani Language and Speech Culture",
            "Faculty and students gathered at Baku State Communications and Transport College to discuss the preservation, rich heritage, and proper usage of the Azerbaijani state language.",
        )
    if "insan hüquqları" in low:
        return (
            "Educational Event Held Within the Framework of 'Human Rights Month'",
            "Within the 'Human Rights Month' campaign, Baku State Communications and Transport College held an interactive session on constitutional rights and student responsibilities.",
        )
    if "uşaq hüquqları" in low:
        return (
            "Awareness Event Held Within the 'Child Rights Month' Campaign",
            "As part of the October 20 – November 20 'Child Rights Month', an educational seminar was organized at Baku State Communications and Transport College under AzTU.",
        )
    if "heydər əliyev" in low:
        return (
            "Commemorative Event Dedicated to National Leader Heydar Aliyev",
            "Baku State Communications and Transport College under AzTU held a solemn event honoring the legacy and historic statehood contributions of National Leader Heydar Aliyev.",
        )
    if "zəfər günü" in low or "8 noyabr" in low:
        return (
            "Solemn Event Dedicated to November 8 — Victory Day Held at the College",
            "Faculty and students of Baku State Communications and Transport College celebrated the historic Victory Day of Azerbaijan with patriotic speeches and performances.",
        )
    if "20 yanvar" in low:
        return (
            "Commemorative Event Marking the January 20 National Day of Mourning",
            "The memory of the heroic martyrs of January 20 was solemnly honored by the administration, faculty, and students of Baku State Communications and Transport College.",
        )
    if "xocalı" in low:
        return (
            "Commemorative Event Dedicated to the Anniversary of the Khojaly Genocide",
            "Baku State Communications and Transport College held a remembrance ceremony honoring the victims of the Khojaly tragedy with the participation of staff and students.",
        )
    return (
        f"Official College {tag_en}: {title_az}",
        "An official event and educational initiative was organized at Baku State Communications and Transport College under Azerbaijan Technical University with active participation of faculty and students.",
    )

def auto_translate_ru(title_az, tag_ru, date_str):
    low = title_az.lower()
    if "narkomaniya" in low:
        return (
            "В колледже прошло просветительское мероприятие «Скажем нет наркомании»",
            "В Бакинском государственном колледже связи и транспорта при АзТУ состоялось просветительское мероприятие, направленное на пропаганду здорового образа жизни среди студентов.",
        )
    if "məişət zorakılığı" in low:
        return (
            "В колледже состоялось мероприятие на тему «Скажем нет бытовому насилию»",
            "В Бакинском государственном колледже связи и транспорта при участии экспертов, юристов, преподавателей и студентов прошло широкое обсуждение правовой защиты и социальных проектов.",
        )
    if "korrupsiya" in low:
        return (
            "Просветительское мероприятие в рамках борьбы с коррупцией и обеспечения прозрачности",
            "В Бакинском государственном колледже связи и транспорта при АзТУ состоялся семинар, посвященный принципам прозрачности, честности и правовой ответственности молодежи.",
        )
    if "azərbaycan dilinin saflığı" in low or "ana dili" in low:
        return (
            "Мероприятие на тему «Чистота азербайджанского языка и культура речи»",
            "В Бакинском государственном колледже связи и транспорта состоялся научно-просветительский семинар, посвященный сохранению чистоты государственного языка.",
        )
    if "insan hüquqları" in low:
        return (
            "Просветительское мероприятие в рамках «Месячника прав человека»",
            "В рамках «Месячника прав человека» в колледже состоялась встреча со студентами, посвященная защите прав и свобод человека и правовому просвещению.",
        )
    if "uşaq hüquqları" in low:
        return (
            "Просветительское мероприятие в рамках «Месячника прав ребенка»",
            "В Бакинском государственном колледже связи и транспорта при АзТУ прошло мероприятие в рамках кампании «Месячник прав ребенка».",
        )
    if "heydər əliyev" in low:
        return (
            "Мероприятие, посвященное памяти общенационального лидера Гейдара Алиева",
            "В Бакинском государственном колледже связи и транспорта при АзТУ состоялось торжественное мероприятие, посвященное наследию общенационального лидера Гейдара Алиева.",
        )
    if "zəfər günü" in low or "8 noyabr" in low:
        return (
            "Торжественное мероприятие, посвященное 8 Ноября — Дню Победы",
            "Преподаватели и студенты Бакинского государственного колледжа связи и транспорта торжественно отметили исторический День Победы Азербайджана.",
        )
    return (
        f"Официальная хроника колледжа: {title_az}",
        "В Бакинском государственном колледже связи и транспорта при Азербайджанском техническом университете состоялось мероприятие с участием преподавателей и студентов.",
    )

final_news = []
for idx, p in enumerate(raw_posts, start=1):
    title_az = p.get("title", "").strip().rstrip("—").strip()
    title_az = title_az.replace("Stolüste", "Stolüstü").replace("Naminə Qaç)", "Naminə Qaç»")
    full_az = clean_full_text(p.get("full_text", ""), title_az)
    if not full_az:
        full_az = title_az
    if not title_az:
        title_az = make_excerpt(full_az, 90)

    paras_az = split_into_paragraphs(full_az)
    full_az_formatted = "\n\n".join(paras_az)
    desc_az = make_excerpt(full_az, 185)
    date_str = extract_date(p, full_az)
    tag_az, tag_en, tag_ru = classify_tag(title_az, full_az)

    old = existing_by_url.get(p["url"], {})
    auto_t_en, auto_d_en = auto_translate_en(title_az, tag_en, date_str)
    auto_t_ru, auto_d_ru = auto_translate_ru(title_az, tag_ru, date_str)

    title_en = old.get("title_en") or auto_t_en
    title_ru = old.get("title_ru") or auto_t_ru
    desc_en = old.get("desc_en") or auto_d_en
    desc_ru = old.get("desc_ru") or auto_d_ru

    final_news.append({
        "id": idx,
        "official_id": p["id"],
        "title_az": title_az,
        "title_en": title_en,
        "title_ru": title_ru,
        "desc_az": desc_az,
        "desc_en": desc_en,
        "desc_ru": desc_ru,
        "full_az": full_az_formatted,
        "full_en": f"{desc_en}\n\n{full_az_formatted}",
        "full_ru": f"{desc_ru}\n\n{full_az_formatted}",
        "date": date_str,
        "image": p.get("local_img", "news1.webp"),
        "url": p["url"],
        "tag_az": old.get("tag_az") or tag_az,
        "tag_en": old.get("tag_en") or tag_en,
        "tag_ru": old.get("tag_ru") or tag_ru,
    })

news_json_str = json.dumps(final_news, ensure_ascii=False, indent=2)
new_script = re.sub(
    r"const newsData = \[.*?\];(?=\s*const libraryData)",
    f"const newsData = {news_json_str};",
    script_text,
    count=1,
    flags=re.DOTALL,
)

with open(script_path, "w", encoding="utf-8") as f:
    f.write(new_script)

print(f"Successfully updated script.js with {len(final_news)} official news articles!")
