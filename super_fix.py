import re
import json

# 1. Load backup majors
with open('/Users/konul/Documents/kollec 2 copy/script.js', 'r', encoding='utf-8') as f:
    backup_content = f.read()

majors_match = re.search(r'majors:\s*\{(?:[^{}]*|\{[^{}]*\})*\}', backup_content, re.DOTALL)
if majors_match:
    majors_code = majors_match.group(0)
else:
    print("Majors not found in backup")
    exit()

# 2. Read current script.js
with open('script.js', 'r', encoding='utf-8') as f:
    content = f.read()

# 3. Replace majors in staffData
content = re.sub(r'majors:\s*\{.*?\}\s*\}', majors_code + "\n  }", content, re.DOTALL)

# 4. Update initAdmissionCalculator logic
calc_fix = """
    // Populate majors
    function populateMajors() {
      const currentLabel = majorSelect.options[0].textContent;
      majorSelect.innerHTML = `<option value="">${currentLabel}</option>`;
      
      const allMajors = [];
      if (staffData.majors.eyani) allMajors.push(...staffData.majors.eyani);
      if (staffData.majors.qiyabi) allMajors.push(...staffData.majors.qiyabi);
      
      allMajors.forEach(m => {
        const opt = document.createElement("option");
        opt.value = m.code;
        const mode = staffData.majors.qiyabi.includes(m) ? (currentLang === 'az' ? ' (Qiyabi)' : (currentLang === 'en' ? ' (Part-time)' : ' (Заочно)')) : '';
        opt.textContent = m[`name_${currentLang}`] + mode;
        majorSelect.appendChild(opt);
      });
    }
"""
content = re.sub(r'// Populate majors.*?majorSelect\.appendChild\(opt\);.*?\}' , calc_fix, content, re.DOTALL)

# 5. Add missing i18n keys for RU and EN
en_calc_keys = """    calc_badge: "For Candidates",
    calc_title: "Check Your Chance",
    calc_desc: "Enter your score to see your chances of admission to our college.",
    calc_score_label: "Your Score",
    calc_major_label: "Select Major",
    calc_major_placeholder: "Select a major...",
    calc_btn: "Calculate",
    calc_msg_low: "You need to prepare more. Good luck!",
    calc_msg_mid: "Your chance is good, pay attention to major selection.",
    calc_msg_high: "Congratulations! We are waiting for you at our college.",
    entry_candidate_title: "Admission Portal","""

ru_calc_keys = """    calc_badge: "Для абитуриентов",
    calc_title: "Проверь свои шансы",
    calc_desc: "Введите свой балл, чтобы узнать шансы на поступление в наш колледж.",
    calc_score_label: "Ваш балл",
    calc_major_label: "Выберите специальность",
    calc_major_placeholder: "Выберите специальность...",
    calc_btn: "Рассчитать",
    calc_msg_low: "Нужно подготовиться получше. Удачи!",
    calc_msg_mid: "Шансы хорошие, будьте внимательны при выборе специальности.",
    calc_msg_high: "Поздравляем! Мы ждем вас в нашем колледже.",
    entry_candidate_title: "Приемная комиссия","""

content = re.sub(r'entry_candidate_title: "Admission Portal",', en_calc_keys, content)
content = re.sub(r'entry_candidate_title: "Приемная комиссия",', ru_calc_keys, content)

# 6. Translate newsData (Simple rule-based for 30 items)
news_match = re.search(r'const newsData = (\[.*?\]);', content, re.DOTALL)
if news_match:
    news_data = json.loads(news_match.group(1))
    
    translations = {
        "Stolüste tennis": ("Table Tennis", "Настольный теннис"),
        "uğuru": ("success", "успех"),
        "yeni direktoru": ("new director", "нового директора"),
        "təqdim olunub": ("presented", "представлен"),
        "Qalib": ("Winner", "Победитель"),
        "Narkomaniyaya yox deyək": ("Say No to Drugs", "Скажем нет наркомании"),
        "tədbir": ("event", "мероприятие"),
        "keçirilib": ("was held", "прошло"),
        "keçirilmişdir": ("was held", "прошло"),
        "fəxri fərmanla": ("with honorary certificate", "почетной грамотой"),
        "təltif olunub": ("awarded", "награжден"),
        "Anım Günü": ("Commemoration Day", "День Памяти"),
        "Heydər Əliyev": ("Heydar Aliyev", "Гейдар Алиев"),
        "yubiley": ("anniversary", "юбилей"),
        "Marafon": ("Marathon", "Марафон"),
        "Kollektiv Müqavilə": ("Collective Agreement", "Коллективный договор"),
        "imzalandı": ("signed", "подписан"),
        "Sağlam həyat tərzi": ("Healthy lifestyle", "Здоровый образ жизни"),
        "Azərbaycan dilinin saflığı": ("Purity of Azerbaijani language", "Чистота азербайджанского языка"),
        "Zəfər Günü": ("Victory Day", "День Победы"),
        "Uşaq Hüquqları Aylığı": ("Children's Rights Month", "Месячник прав ребенка"),
        "Qızıl payız": ("Golden Autumn", "Золотая осень"),
        "Müəllimlər Günü": ("Teachers' Day", "День Учителя"),
        "Reproduktiv sağlamlıq": ("Reproductive health", "Репродуктивное здоровье"),
        "Şer və Mahnı Müsabiqəsi": ("Poetry and Song Contest", "Конкурс стихов и песен"),
        "Korrupsiya": ("Corruption", "Коррупция"),
        "İnsan Hüquqları": ("Human Rights", "Права человека"),
        "Şəffaflıq və dürüstlük": ("Transparency and integrity", "Прозрачность и честность"),
    }
    
    for item in news_data:
        title = item['title_az']
        title_en = title
        title_ru = title
        for az, (en, ru) in translations.items():
            title_en = re.sub(az, en, title_en, flags=re.IGNORECASE)
            title_ru = re.sub(az, ru, title_ru, flags=re.IGNORECASE)
        
        item['title_en'] = title_en
        item['title_ru'] = title_ru
        
        # Simple desc placeholders based on title
        item['desc_en'] = f"Details about the {title_en} at our college."
        item['desc_ru'] = f"Подробности о {title_ru} в нашем колледже."

    new_news_code = f"const newsData = {json.dumps(news_data, ensure_ascii=False, indent=2)};"
    content = re.sub(r'const newsData = \[.*?\];', new_news_code, content, flags=re.DOTALL)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("Super fix applied successfully.")
