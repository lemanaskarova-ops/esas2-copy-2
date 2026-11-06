import os, sys, re, json

base_dir = "/Users/konul/Documents/esas2 copy 2"

# 1. READ ORIGINAL PRE-CAMPUS SCRIPT
with open(os.path.join(base_dir, "scratch/script_backup_pre_campus.js"), "r", encoding="utf-8") as f:
    orig_js = f.read()

# READ CURRENT SCRIPT.JS (which has the updated campus module at the bottom)
with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    curr_js = f.read()

# READ CURRENT INDEX.HTML
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

# Extract pre-campus i18n blocks
pos_az = orig_js.find('const i18n = {')
pos_en = orig_js.find('\n  en: {')
pos_ru = orig_js.find('\n  ru: {')
pos_end = orig_js.find('\nlet currentLang =')

orig_az = orig_js[pos_az:pos_en]
orig_en = orig_js[pos_en:pos_ru]
orig_ru = orig_js[pos_ru:pos_end]

# Common new keys for AZ, EN, RU
az_extra = '''
    // CAMPUS & ROOMS
    nav_campus: "Kampus & Otaqlar",
    nav_campus_sub: "5 mərtəbəli bina naviqasiyası",
    nav_floor_1_title: "1-ci Mərtəbə",
    nav_floor_1_sub: "İdman kompleksi, Kimya & Rabitə lab",
    nav_floor_2_title: "2-ci Mərtəbə",
    nav_floor_2_sub: "Rəhbərlik, Kitabxana 206 & İKT otaqları",
    nav_floor_3_title: "3-cü Mərtəbə",
    nav_floor_3_sub: "Fizika laboratoriyası & 16 Auditoriya",
    nav_floor_4_title: "4-cü Mərtəbə",
    nav_floor_4_sub: "Poçt laboratoriyası, İKT & 17 Auditoriya",
    nav_floor_5_title: "5-ci Mərtəbə",
    nav_floor_5_sub: "Kompüter texnologiyası & 18 Auditoriya",
    nav_floor_all_title: "Bütün Mərtəbələr",
    nav_floor_all_sub: "5 mərtəbə üzrə bütün 80+ otaq",
    nav_mob_floor_1: "1-ci Mərtəbə (İdman & Lab)",
    nav_mob_floor_2: "2-ci Mərtəbə (Rəhbərlik & Kitabxana)",
    nav_mob_floor_3: "3-cü Mərtəbə (Fizika & 16 Otaq)",
    nav_mob_floor_4: "4-cü Mərtəbə (Poçt & 17 Otaq)",
    nav_mob_floor_5: "5-ci Mərtəbə (Kompüter & 18 Otaq)",
    nav_mob_floor_all: "Bütün Mərtəbələr (80+ Otaq)",
    campus_badge: "Kampus İnfrastrukturu & Bələdçi",
    campus_title: "Tədris Korpusu və Ağıllı Otaq Naviqatoru",
    campus_desc: "5 mərtəbəli əsas tədris korpusumuzun rəqəmsal bələdçisi. Müasir laboratoriyalar, auditoriyalar, inzibati şöbələr və tələbə məkanları üzrə ani axtarış və interaktiv mərtəbə naviqatoru.",
    campus_stat_1_val: "5 Mərtəbə",
    campus_stat_1_lbl: "Əsas Tədris Korpusu",
    campus_stat_2_val: "80+ Auditoriya",
    campus_stat_2_lbl: "Tədris və İnzibati Məkan",
    campus_stat_3_val: "7 Laboratoriya",
    campus_stat_3_lbl: "Kimya, Fizika, Rabitə, İKT",
    campus_stat_4_val: "206-cı Otaq",
    campus_stat_4_lbl: "22 000+ Kitab Fondu & Oxu Zalı",
    campus_fbtn_1_title: "1-ci Mərtəbə",
    campus_fbtn_1_meta: "12 otaq · İdman & Lab",
    campus_fbtn_2_title: "2-ci Mərtəbə",
    campus_fbtn_2_meta: "11 otaq · Rəhbərlik & Kitabxana",
    campus_fbtn_3_title: "3-cü Mərtəbə",
    campus_fbtn_3_meta: "16 otaq · Fizika Lab & Tədris",
    campus_fbtn_4_title: "4-cü Mərtəbə",
    campus_fbtn_4_meta: "17 otaq · İKT & Poçt Lab",
    campus_fbtn_5_title: "5-ci Mərtəbə",
    campus_fbtn_5_meta: "18 otaq · Kompüter & Keyfiyyət",
    campus_fbtn_all_title: "Bütün Mərtəbələr",
    campus_fbtn_all_meta: "80+ otaq",
    campus_search_ph: "Otaq nömrəsi və ya ad ilə axtarın (məs: 206, Kimya, Fizika, Direktor, Poçt, 107)...",
    campus_filter_all: "Hamısı",
    campus_filter_lab: "🔬 Laboratoriyalar",
    campus_filter_it: "💻 Kompüter və İKT",
    campus_filter_admin: "🏛️ Rəhbərlik & İnzibati",
    campus_filter_library: "📚 Kitabxana & Oxu Zalı",
    campus_filter_sport: "⚽ İdman & Hərbi",
    campus_filter_classroom: "🎓 Auditoriyalar",
    campus_btn_lib: "📖 Kitabxana Fondu və Tarixi",
    campus_btn_bio: "👤 Səbuhi Qurbanov Bioqrafiyası",
    campus_aud_list_title: "Auditoriya nömrələri",
    campus_count_shown: "göstərilən otaqlar:",
    campus_search_found: "Axtarış nəticəsi:",
    campus_search_rooms_suffix: "otaq tapıldı",
    campus_not_found_title: "Axtarış üzrə otaq tapılmadı",
    campus_not_found_desc: "Daxil etdiyiniz meyar üzrə heç bir otaq və ya laboratoriya aşkar edilmədi. Zəhmət olmasa başqa otaq nömrəsi və ya ad daxil edin.",
    campus_reset_btn: "Bütün Otaqları Göstər",

    // VIDEO LECTURES DROPDOWN
    lecture_sub_informatika: "2 videodərs · Kompüter və Şəbəkə",
    lecture_sub_neqliyyat: "1 videodərs · Avtonəqliyyat",
    lecture_sub_cografiya: "2 videodərs · Təbiət və Cəmiyyət",
    lecture_sub_fizika: "1 videodərs · Təbiət və Fizika",
    lecture_sub_tarix: "9 videodərs · Tarix və Zəfər",
    lecture_sub_azdili: "1 videodərs · Qrammatika və Nitq",
    lecture_sub_huquq: "6 videodərs · Hüquq Sistemi",
    lecture_sub_biologiya: "1 videodərs · Təbiət Elmləri",

    // HONOR & FAME TABS
    fame_tab_all: "Hamısı",
    fame_tab_it: "İKT & Robototexnika",
    fame_tab_champ: "Beynəlxalq Çempionatlar",
    fame_tab_youth: "İlin Gənci & Sosial İnklüzivlik",

    // LIBRARY FUND MODAL
    lib_fund_kicker: "BDRNK · RƏSMİ KİTABXANA ŞÖBƏSİ",
    lib_fund_heading: "Kitabxana Fondu və Rəsmi Tarixi Haqqında",
    lib_fund_stat_lbl_1: "Hal-hazırdakı Ədəbiyyat Fondu",
    lib_fund_stat_lbl_2: "İlkin Zəngin Nüsxə Fondu",
    lib_fund_stat_lbl_3: "İxtisas Dərslikləri",
    lib_fund_stat_lbl_4: "Müəllimlərin Yeni Nəşrləri",
    lib_fund_title_1: "Kitabxana Fondunun Formalaşması və Müasir İnkişafı",
    lib_fund_title_2: "Tədris Fondunun Zənginləşdirilməsi və Yeni Dərsliklər",
    lib_fund_badge_1: "📜 DÖVLƏT SƏRƏNCAMI VƏ TARİXİ ZƏNGİNLƏŞMƏ",
    lib_fund_badge_2: "🎓 MÜƏLLİM HEYƏTİNİN NƏŞRLƏRİ",
    lib_location_title: "Kitabxananın Ünvanı: II Mərtəbə, Otaq 206",
    lib_location_sub: "Geniş oxu zalı ilə birgə 2 daxili auditoriyada xidmət göstərir.",
    lib_jump_btn_text: "📚 Elektron Kitablara Bax",

    // DIRECTOR BIO
    bio_official_title: "Rəsmi Bioqrafiya",
    bio_director_role: "Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru"
'''

en_extra = '''
    // CAMPUS & ROOMS
    nav_campus: "Campus & Rooms",
    nav_campus_sub: "5-floor building navigator",
    nav_floor_1_title: "1st Floor",
    nav_floor_1_sub: "Sports complex, Chemistry & Telecom lab",
    nav_floor_2_title: "2nd Floor",
    nav_floor_2_sub: "Leadership, Library 206 & IT labs",
    nav_floor_3_title: "3rd Floor",
    nav_floor_3_sub: "Physics laboratory & 16 Classrooms",
    nav_floor_4_title: "4th Floor",
    nav_floor_4_sub: "Postal laboratory, IT & 17 Classrooms",
    nav_floor_5_title: "5th Floor",
    nav_floor_5_sub: "Computer technology & 18 Classrooms",
    nav_floor_all_title: "All Floors",
    nav_floor_all_sub: "All 80+ rooms across 5 floors",
    nav_mob_floor_1: "1st Floor (Sports & Labs)",
    nav_mob_floor_2: "2nd Floor (Leadership & Library)",
    nav_mob_floor_3: "3rd Floor (Physics & 16 Rooms)",
    nav_mob_floor_4: "4th Floor (Postal & 17 Rooms)",
    nav_mob_floor_5: "5th Floor (Computer & 18 Rooms)",
    nav_mob_floor_all: "All Floors (80+ Rooms)",
    campus_badge: "Campus Infrastructure & Guide",
    campus_title: "Academic Building & Smart Room Navigator",
    campus_desc: "Digital guide for our 5-story academic campus. Interactive room navigator and instant search across laboratories, lecture halls, administrative offices, and student hubs.",
    campus_stat_1_val: "5 Floors",
    campus_stat_1_lbl: "Main Academic Building",
    campus_stat_2_val: "80+ Classrooms",
    campus_stat_2_lbl: "Academic & Administrative Space",
    campus_stat_3_val: "7 Laboratories",
    campus_stat_3_lbl: "Chemistry, Physics, Telecom, IT",
    campus_stat_4_val: "Room 206",
    campus_stat_4_lbl: "22,000+ Book Fund & Reading Hall",
    campus_fbtn_1_title: "1st Floor",
    campus_fbtn_1_meta: "12 rooms · Sports & Labs",
    campus_fbtn_2_title: "2nd Floor",
    campus_fbtn_2_meta: "11 rooms · Leadership & Library",
    campus_fbtn_3_title: "3rd Floor",
    campus_fbtn_3_meta: "16 rooms · Physics Lab & Study",
    campus_fbtn_4_title: "4th Floor",
    campus_fbtn_4_meta: "17 rooms · IT & Postal Lab",
    campus_fbtn_5_title: "5th Floor",
    campus_fbtn_5_meta: "18 rooms · Computer & Quality",
    campus_fbtn_all_title: "All Floors",
    campus_fbtn_all_meta: "80+ rooms",
    campus_search_ph: "Search by room number or name (e.g. 206, Chemistry, Physics, Director, 107)...",
    campus_filter_all: "All",
    campus_filter_lab: "🔬 Laboratories",
    campus_filter_it: "💻 Computer & IT",
    campus_filter_admin: "🏛️ Leadership & Admin",
    campus_filter_library: "📚 Library & Reading Room",
    campus_filter_sport: "⚽ Sports & Military",
    campus_filter_classroom: "🎓 Classrooms",
    campus_btn_lib: "📖 Library Fund & History",
    campus_btn_bio: "👤 Sebuhi Gurbanov Biography",
    campus_aud_list_title: "Classroom numbers",
    campus_count_shown: "rooms shown:",
    campus_search_found: "Search result:",
    campus_search_rooms_suffix: "rooms found",
    campus_not_found_title: "No rooms found",
    campus_not_found_desc: "No rooms or laboratories match your search criteria. Please try another room number or name.",
    campus_reset_btn: "Show All Rooms",

    // VIDEO LECTURES DROPDOWN
    lecture_sub_informatika: "2 video lessons · Computer & Networks",
    lecture_sub_neqliyyat: "1 video lesson · Transport Systems",
    lecture_sub_cografiya: "2 video lessons · Nature & Society",
    lecture_sub_fizika: "1 video lesson · Nature & Physics",
    lecture_sub_tarix: "9 video lessons · History & Victory",
    lecture_sub_azdili: "1 video lesson · Grammar & Speech",
    lecture_sub_huquq: "6 video lessons · Legal System",
    lecture_sub_biologiya: "1 video lesson · Natural Sciences",

    // HONOR & FAME TABS
    fame_tab_all: "All",
    fame_tab_it: "IT & Robotics",
    fame_tab_champ: "International Championships",
    fame_tab_youth: "Youth of the Year & Inclusion",

    // LIBRARY FUND MODAL
    lib_fund_kicker: "BDRNK · OFFICIAL LIBRARY DIVISION",
    lib_fund_heading: "About Library Fund & Official History",
    lib_fund_stat_lbl_1: "Current Literature Fund",
    lib_fund_stat_lbl_2: "Initial Fund Volumes",
    lib_fund_stat_lbl_3: "Specialized Textbooks",
    lib_fund_stat_lbl_4: "Faculty's New Publications",
    lib_fund_title_1: "Establishment and Modern Development of Library Fund",
    lib_fund_title_2: "Enrichment of Academic Fund & New Textbooks",
    lib_fund_badge_1: "📜 PRESIDENTIAL DECREE & HISTORICAL ENRICHMENT",
    lib_fund_badge_2: "🎓 FACULTY PUBLICATIONS",
    lib_location_title: "Library Address: 2nd Floor, Room 206",
    lib_location_sub: "Services provided across 2 internal halls with spacious reading facilities.",
    lib_jump_btn_text: "📚 Explore E-Books",

    // DIRECTOR BIO
    bio_official_title: "Official Biography",
    bio_director_role: "Director of Baku State Communications and Transport College"
'''

ru_extra = '''
    // CAMPUS & ROOMS
    nav_campus: "Кампус и Аудитории",
    nav_campus_sub: "Навигатор по 5 этажам корпуса",
    nav_floor_1_title: "1-й Этаж",
    nav_floor_1_sub: "Спорткомплекс, Химия и Связь лаб",
    nav_floor_2_title: "2-й Этаж",
    nav_floor_2_sub: "Руководство, Библиотека 206 и ИКТ",
    nav_floor_3_title: "3-й Этаж",
    nav_floor_3_sub: "Лаборатория физики и 16 Аудиторий",
    nav_floor_4_title: "4-й Этаж",
    nav_floor_4_sub: "Почтовая лаборатория, ИКТ и 17 Аудиторий",
    nav_floor_5_title: "5-й Этаж",
    nav_floor_5_sub: "Компьютерные технологии и 18 Аудиторий",
    nav_floor_all_title: "Все Этажи",
    nav_floor_all_sub: "Все 80+ кабинетов на 5 этажах",
    nav_mob_floor_1: "1-й Этаж (Спорт и Лаб)",
    nav_mob_floor_2: "2-й Этаж (Руководство и Библиотека)",
    nav_mob_floor_3: "3-й Этаж (Физика и 16 Кабинетов)",
    nav_mob_floor_4: "4-й Этаж (Почта и 17 Кабинетов)",
    nav_mob_floor_5: "5-й Этаж (Компьютеры и 18 Кабинетов)",
    nav_mob_floor_all: "Все Этажи (80+ Кабинетов)",
    campus_badge: "Инфраструктура кампуса и гид",
    campus_title: "Учебный корпус и умный навигатор по кабинетам",
    campus_desc: "Цифровой путеводитель по 5-этажному учебному корпусу. Интерактивная навигация и быстрый поиск лабораторий, лекционных залов, административных отделов и студенческих пространств.",
    campus_stat_1_val: "5 Этажей",
    campus_stat_1_lbl: "Главный Учебный Корпус",
    campus_stat_2_val: "80+ Аудиторий",
    campus_stat_2_lbl: "Учебное и административное пространство",
    campus_stat_3_val: "7 Лабораторий",
    campus_stat_3_lbl: "Химия, Физика, Связь, ИКТ",
    campus_stat_4_val: "Кабинет 206",
    campus_stat_4_lbl: "Фонд 22 000+ книг и читальный зал",
    campus_fbtn_1_title: "1-й Этаж",
    campus_fbtn_1_meta: "12 комнат · Спорт и Лаб",
    campus_fbtn_2_title: "2-й Этаж",
    campus_fbtn_2_meta: "11 комнат · Руководство и Библиотека",
    campus_fbtn_3_title: "3-й Этаж",
    campus_fbtn_3_meta: "16 комнат · Лаб физики и Учеба",
    campus_fbtn_4_title: "4-й Этаж",
    campus_fbtn_4_meta: "17 комнат · ИКТ и Почта",
    campus_fbtn_5_title: "5-й Этаж",
    campus_fbtn_5_meta: "18 комнат · Компьютеры и Контроль",
    campus_fbtn_all_title: "Все Этажи",
    campus_fbtn_all_meta: "80+ комнат",
    campus_search_ph: "Поиск по номеру или названию кабинета (напр. 206, Химия, Физика, Директор, 107)...",
    campus_filter_all: "Все",
    campus_filter_lab: "🔬 Лаборатории",
    campus_filter_it: "💻 Компьютеры и ИКТ",
    campus_filter_admin: "🏛️ Руководство и Администрация",
    campus_filter_library: "📚 Библиотека и Читальный Зал",
    campus_filter_sport: "⚽ Спорт и Военное дело",
    campus_filter_classroom: "🎓 Аудитории",
    campus_btn_lib: "📖 Фонд библиотеки и история",
    campus_btn_bio: "👤 Биография Сабухи Гурбанова",
    campus_aud_list_title: "Номера аудиторий",
    campus_count_shown: "показано комнат:",
    campus_search_found: "Результат поиска:",
    campus_search_rooms_suffix: "кабинетов найдено",
    campus_not_found_title: "Кабинеты не найдены",
    campus_not_found_desc: "По вашему запросу не найдено ни одного кабинета или лаборатории. Попробуйте другой номер или название.",
    campus_reset_btn: "Показать все кабинеты",

    // VIDEO LECTURES DROPDOWN
    lecture_sub_informatika: "2 видеоурока · Компьютеры и сети",
    lecture_sub_neqliyyat: "1 видеоурок · Автотранспорт",
    lecture_sub_cografiya: "2 видеоурока · Природа и общество",
    lecture_sub_fizika: "1 видеоурок · Природа и физика",
    lecture_sub_tarix: "9 видеоуроков · История и Победа",
    lecture_sub_azdili: "1 видеоурок · Грамматика и речь",
    lecture_sub_huquq: "6 видеоуроков · Правовая система",
    lecture_sub_biologiya: "1 видеоурок · Естественные науки",

    // HONOR & FAME TABS
    fame_tab_all: "Все",
    fame_tab_it: "ИКТ и Робототехника",
    fame_tab_champ: "Международные Чемпионаты",
    fame_tab_youth: "Молодежь Года и Социальная Инклюзия",

    // LIBRARY FUND MODAL
    lib_fund_kicker: "БДРНК · ОФИЦИАЛЬНЫЙ ОТДЕЛ БИБЛИОТЕКИ",
    lib_fund_heading: "О Библиотечном Фонде и Официальной Истории",
    lib_fund_stat_lbl_1: "Текущий фонд литературы",
    lib_fund_stat_lbl_2: "Первоначальный фонд изданий",
    lib_fund_stat_lbl_3: "Профильные учебники",
    lib_fund_stat_lbl_4: "Новые издания преподавателей",
    lib_fund_title_1: "Формирование и современное развитие библиотечного фонда",
    lib_fund_title_2: "Обогащение учебного фонда и новые учебники",
    lib_fund_badge_1: "📜 ГОСУДАРСТВЕННЫЙ УКАЗ И ИСТОРИЧЕСКОЕ ОБОГАЩЕНИЕ",
    lib_fund_badge_2: "🎓 ИЗДАНИЯ ПРЕПОДАВАТЕЛЬСКОГО СОСТАВА",
    lib_location_title: "Адрес библиотеки: II Этаж, Кабинет 206",
    lib_location_sub: "Обслуживание в 2 совмещенных аудиториях с просторным читальным залом.",
    lib_jump_btn_text: "📚 Каталог Электронных Книг",

    // DIRECTOR BIO
    bio_official_title: "Официальная Биография",
    bio_director_role: "Директор Бакинского Государственного Колледжа Связи и Транспорта"
'''

# Cleanly inject extra keys into orig_az, orig_en, orig_ru before their closing `},`
def inject_extra(block, extra):
    last_brace = block.rfind('},')
    if last_brace == -1:
        last_brace = block.rfind('}')
    return block[:last_brace] + extra + "\n  " + block[last_brace:]

new_az = inject_extra(orig_az, az_extra)
new_en = inject_extra(orig_en, en_extra)
new_ru = inject_extra(orig_ru, ru_extra)

full_new_i18n = new_az + "\n  en: {" + new_en[new_en.find('en: {') + 5:] + "\n  ru: {" + new_ru[new_ru.find('ru: {') + 5:]

# Replace i18n in curr_js
pos_curr_az = curr_js.find('const i18n = {')
pos_curr_end = curr_js.find('\nlet currentLang =')
assert pos_curr_az != -1 and pos_curr_end != -1, "i18n boundaries in curr_js not found"

curr_js = curr_js[:pos_curr_az] + full_new_i18n + curr_js[pos_curr_end:]
print("Full 570+ key i18n restored and enriched in curr_js!")

# Save script.js
with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(curr_js)

# Sync backup
with open(os.path.join(base_dir, "scratch/script_working_backup.js"), "w", encoding="utf-8") as f:
    f.write(curr_js)

print("script.js and backup updated successfully.")

# ══════════════════════════════════════════════════════════════
# 2. UPDATE INDEX.HTML WITH ADDITIONAL MISSING DATA-I18N
# ══════════════════════════════════════════════════════════════
# Video lectures subkeys in dropdown
html_src = html_src.replace('2 videodərs · Kompüter və Şəbəkə', '<span data-i18n="lecture_sub_informatika">2 videodərs · Kompüter və Şəbəkə</span>')
html_src = html_src.replace('1 videodərs · Avtonəqliyyat', '<span data-i18n="lecture_sub_neqliyyat">1 videodərs · Avtonəqliyyat</span>')
html_src = html_src.replace('2 videodərs · Təbiət və Cəmiyyət', '<span data-i18n="lecture_sub_cografiya">2 videodərs · Təbiət və Cəmiyyət</span>')
html_src = html_src.replace('1 videodərs · Təbiət və Fizika', '<span data-i18n="lecture_sub_fizika">1 videodərs · Təbiət və Fizika</span>')
html_src = html_src.replace('9 videodərs · Tarix və Zəfər', '<span data-i18n="lecture_sub_tarix">9 videodərs · Tarix və Zəfər</span>')
html_src = html_src.replace('1 videodərs · Qrammatika və Nitq', '<span data-i18n="lecture_sub_azdili">1 videodərs · Qrammatika və Nitq</span>')
html_src = html_src.replace('6 videodərs · Hüquq Sistemi', '<span data-i18n="lecture_sub_huquq">6 videodərs · Hüquq Sistemi</span>')
html_src = html_src.replace('1 videodərs · Təbiət Elmləri', '<span data-i18n="lecture_sub_biologiya">1 videodərs · Təbiət Elmləri</span>')

# Library fund modal
html_src = html_src.replace('<span class="lib-fund-kicker">BDRNK · RƏSMİ KİTABXANA ŞÖBƏSİ</span>', '<span class="lib-fund-kicker" data-i18n="lib_fund_kicker">BDRNK · RƏSMİ KİTABXANA ŞÖBƏSİ</span>')
html_src = html_src.replace('<h3 class="lib-fund-heading">Kitabxana Fondu və Rəsmi Tarixi Haqqında</h3>', '<h3 class="lib-fund-heading" data-i18n="lib_fund_heading">Kitabxana Fondu və Rəsmi Tarixi Haqqında</h3>')
html_src = html_src.replace('<div class="lib-fund-stat-lbl">Hal-hazırdakı Ədəbiyyat Fondu</div>', '<div class="lib-fund-stat-lbl" data-i18n="lib_fund_stat_lbl_1">Hal-hazırdakı Ədəbiyyat Fondu</div>')
html_src = html_src.replace('<div class="lib-fund-stat-lbl">İlkin Zəngin Nüsxə Fondu</div>', '<div class="lib-fund-stat-lbl" data-i18n="lib_fund_stat_lbl_2">İlkin Zəngin Nüsxə Fondu</div>')
html_src = html_src.replace('<div class="lib-fund-stat-lbl">İxtisas Dərslikləri</div>', '<div class="lib-fund-stat-lbl" data-i18n="lib_fund_stat_lbl_3">İxtisas Dərslikləri</div>')
html_src = html_src.replace('<div class="lib-fund-stat-lbl">Müəllimlərin Yeni Nəşrləri</div>', '<div class="lib-fund-stat-lbl" data-i18n="lib_fund_stat_lbl_4">Müəllimlərin Yeni Nəşrləri</div>')

html_src = html_src.replace('<span class="lib-card-badge">📜 DÖVLƏT SƏRƏNCAMI VƏ TARİXİ ZƏNGİNLƏŞMƏ</span>', '<span class="lib-card-badge" data-i18n="lib_fund_badge_1">📜 DÖVLƏT SƏRƏNCAMI VƏ TARİXİ ZƏNGİNLƏŞMƏ</span>')
html_src = html_src.replace('<h3 class="lib-card-title">Kitabxana Fondunun Formalaşması və Müasir İnkişafı</h3>', '<h3 class="lib-card-title" data-i18n="lib_fund_title_1">Kitabxana Fondunun Formalaşması və Müasir İnkişafı</h3>')
html_src = html_src.replace('<span class="lib-card-badge">🎓 MÜƏLLİM HEYƏTİNİN NƏŞRLƏRİ</span>', '<span class="lib-card-badge" data-i18n="lib_fund_badge_2">🎓 MÜƏLLİM HEYƏTİNİN NƏŞRLƏRİ</span>')
html_src = html_src.replace('<h3 class="lib-card-title">Tədris Fondunun Zənginləşdirilməsi və Yeni Dərsliklər</h3>', '<h3 class="lib-card-title" data-i18n="lib_fund_title_2">Tədris Fondunun Zənginləşdirilməsi və Yeni Dərsliklər</h3>')
html_src = html_src.replace('<strong>Kitabxananın Ünvanı: II Mərtəbə, Otaq 206</strong>', '<strong data-i18n="lib_location_title">Kitabxananın Ünvanı: II Mərtəbə, Otaq 206</strong>')
html_src = html_src.replace('<span>Geniş oxu zalı ilə birgə 2 daxili auditoriyada xidmət göstərir.</span>', '<span data-i18n="lib_location_sub">Geniş oxu zalı ilə birgə 2 daxili auditoriyada xidmət göstərir.</span>')
html_src = html_src.replace('<span>📚 Elektron Kitablara Bax</span>', '<span data-i18n="lib_jump_btn_text">📚 Elektron Kitablara Bax</span>')

# Save index.html
with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_src)
print("index.html fully updated with all data-i18n attributes!")
