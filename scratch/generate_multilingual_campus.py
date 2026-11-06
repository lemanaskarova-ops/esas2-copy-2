import os, sys, re, json

base_dir = "/Users/konul/Documents/esas2 copy 2"

with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

# ══════════════════════════════════════════════════════════════
# 1. UPDATE INDEX.HTML WITH DATA-I18N ATTRIBUTES
# ══════════════════════════════════════════════════════════════

# Desktop nav dropdown items
html_src = html_src.replace(
    '<span class="nav-dd-title">1-ci Mərtəbə</span>\n                                <span class="nav-dd-sub">İdman kompleksi, Kimya & Rabitə lab</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_1_title">1-ci Mərtəbə</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_1_sub">İdman kompleksi, Kimya & Rabitə lab</span>'
)
html_src = html_src.replace(
    '<span class="nav-dd-title">2-ci Mərtəbə</span>\n                                <span class="nav-dd-sub">Rəhbərlik, Kitabxana 206 & İKT otaqları</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_2_title">2-ci Mərtəbə</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_2_sub">Rəhbərlik, Kitabxana 206 & İKT otaqları</span>'
)
html_src = html_src.replace(
    '<span class="nav-dd-title">3-cü Mərtəbə</span>\n                                <span class="nav-dd-sub">Fizika laboratoriyası & 16 Auditoriya</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_3_title">3-cü Mərtəbə</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_3_sub">Fizika laboratoriyası & 16 Auditoriya</span>'
)
html_src = html_src.replace(
    '<span class="nav-dd-title">4-cü Mərtəbə</span>\n                                <span class="nav-dd-sub">Poçt laboratoriyası, İKT & 17 Auditoriya</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_4_title">4-cü Mərtəbə</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_4_sub">Poçt laboratoriyası, İKT & 17 Auditoriya</span>'
)
html_src = html_src.replace(
    '<span class="nav-dd-title">5-ci Mərtəbə</span>\n                                <span class="nav-dd-sub">Kompüter texnologiyası & 18 Auditoriya</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_5_title">5-ci Mərtəbə</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_5_sub">Kompüter texnologiyası & 18 Auditoriya</span>'
)
html_src = html_src.replace(
    '<span class="nav-dd-title">Bütün Mərtəbələr</span>\n                                <span class="nav-dd-sub">5 mərtəbə üzrə bütün 80+ otaq</span>',
    '<span class="nav-dd-title" data-i18n="nav_floor_all_title">Bütün Mərtəbələr</span>\n                                <span class="nav-dd-sub" data-i18n="nav_floor_all_sub">5 mərtəbə üzrə bütün 80+ otaq</span>'
)

# Mobile nav items
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="1">1-ci Mərtəbə (İdman & Lab)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="1" data-i18n="nav_mob_floor_1">1-ci Mərtəbə (İdman & Lab)</a>'
)
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="2">2-ci Mərtəbə (Rəhbərlik & Kitabxana)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="2" data-i18n="nav_mob_floor_2">2-ci Mərtəbə (Rəhbərlik & Kitabxana)</a>'
)
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="3">3-cü Mərtəbə (Fizika & 16 Otaq)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="3" data-i18n="nav_mob_floor_3">3-cü Mərtəbə (Fizika & 16 Otaq)</a>'
)
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="4">4-cü Mərtəbə (Poçt & 17 Otaq)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="4" data-i18n="nav_mob_floor_4">4-cü Mərtəbə (Poçt & 17 Otaq)</a>'
)
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="5">5-ci Mərtəbə (Kompüter & 18 Otaq)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="5" data-i18n="nav_mob_floor_5">5-ci Mərtəbə (Kompüter & 18 Otaq)</a>'
)
html_src = html_src.replace(
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="all">Bütün Mərtəbələr (80+ Otaq)</a>',
    '<a href="#campus-navigator" class="mobile-nav-sublink" data-campus-floor="all" data-i18n="nav_mob_floor_all">Bütün Mərtəbələr (80+ Otaq)</a>'
)

# Stats items
html_src = html_src.replace(
    '<span class="campus-stat-val">5 Mərtəbə</span>\n                        <span class="campus-stat-label">Əsas Tədris Korpusu</span>',
    '<span class="campus-stat-val" data-i18n="campus_stat_1_val">5 Mərtəbə</span>\n                        <span class="campus-stat-label" data-i18n="campus_stat_1_lbl">Əsas Tədris Korpusu</span>'
)
html_src = html_src.replace(
    '<span class="campus-stat-val">80+ Auditoriya</span>\n                        <span class="campus-stat-label">Tədris və İnzibati Məkan</span>',
    '<span class="campus-stat-val" data-i18n="campus_stat_2_val">80+ Auditoriya</span>\n                        <span class="campus-stat-label" data-i18n="campus_stat_2_lbl">Tədris və İnzibati Məkan</span>'
)
html_src = html_src.replace(
    '<span class="campus-stat-val">7 Laboratoriya</span>\n                        <span class="campus-stat-label">Kimya, Fizika, Rabitə, İKT</span>',
    '<span class="campus-stat-val" data-i18n="campus_stat_3_val">7 Laboratoriya</span>\n                        <span class="campus-stat-label" data-i18n="campus_stat_3_lbl">Kimya, Fizika, Rabitə, İKT</span>'
)
html_src = html_src.replace(
    '<span class="campus-stat-val">206-cı Otaq</span>\n                        <span class="campus-stat-label">22 000+ Kitab Fondu & Oxu Zalı</span>',
    '<span class="campus-stat-val" data-i18n="campus_stat_4_val">206-cı Otaq</span>\n                        <span class="campus-stat-label" data-i18n="campus_stat_4_lbl">22 000+ Kitab Fondu & Oxu Zalı</span>'
)

# Floor switcher buttons
html_src = html_src.replace(
    '<span class="floor-title-text">1-ci Mərtəbə</span>\n                        <span class="floor-meta-count">12 otaq · İdman & Lab</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_1_title">1-ci Mərtəbə</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_1_meta">12 otaq · İdman & Lab</span>'
)
html_src = html_src.replace(
    '<span class="floor-title-text">2-ci Mərtəbə</span>\n                        <span class="floor-meta-count">11 otaq · Rəhbərlik & Kitabxana</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_2_title">2-ci Mərtəbə</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_2_meta">11 otaq · Rəhbərlik & Kitabxana</span>'
)
html_src = html_src.replace(
    '<span class="floor-title-text">3-cü Mərtəbə</span>\n                        <span class="floor-meta-count">16 otaq · Fizika Lab & Tədris</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_3_title">3-cü Mərtəbə</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_3_meta">16 otaq · Fizika Lab & Tədris</span>'
)
html_src = html_src.replace(
    '<span class="floor-title-text">4-cü Mərtəbə</span>\n                        <span class="floor-meta-count">17 otaq · İKT & Poçt Lab</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_4_title">4-cü Mərtəbə</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_4_meta">17 otaq · İKT & Poçt Lab</span>'
)
html_src = html_src.replace(
    '<span class="floor-title-text">5-ci Mərtəbə</span>\n                        <span class="floor-meta-count">18 otaq · Kompüter & Keyfiyyət</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_5_title">5-ci Mərtəbə</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_5_meta">18 otaq · Kompüter & Keyfiyyət</span>'
)
html_src = html_src.replace(
    '<span class="floor-title-text">Bütün Mərtəbələr</span>\n                        <span class="floor-meta-count">80+ otaq</span>',
    '<span class="floor-title-text" data-i18n="campus_fbtn_all_title">Bütün Mərtəbələr</span>\n                        <span class="floor-meta-count" data-i18n="campus_fbtn_all_meta">80+ otaq</span>'
)

# Search input placeholder
html_src = html_src.replace(
    '<input type="text" id="campus-search-input" placeholder="Otaq nömrəsi və ya ad ilə axtarın (məs: 206, Kimya, Fizika, Direktor, Poçt, 107)..." aria-label="Otaq axtarışı">',
    '<input type="text" id="campus-search-input" data-i18n-placeholder="campus_search_ph" placeholder="Otaq nömrəsi və ya ad ilə axtarın (məs: 206, Kimya, Fizika, Direktor, Poçt, 107)..." aria-label="Otaq axtarışı">'
)

# Category chips
html_src = html_src.replace(
    '<button type="button" class="campus-chip active" data-cat="all">Hamısı</button>',
    '<button type="button" class="campus-chip active" data-cat="all" data-i18n="campus_filter_all">Hamısı</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="lab">🔬 Laboratoriyalar</button>',
    '<button type="button" class="campus-chip" data-cat="lab" data-i18n="campus_filter_lab">🔬 Laboratoriyalar</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="it">💻 Kompüter və İKT</button>',
    '<button type="button" class="campus-chip" data-cat="it" data-i18n="campus_filter_it">💻 Kompüter və İKT</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="admin">🏛️ Rəhbərlik & İnzibati</button>',
    '<button type="button" class="campus-chip" data-cat="admin" data-i18n="campus_filter_admin">🏛️ Rəhbərlik & İnzibati</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="library">📚 Kitabxana & Oxu Zalı</button>',
    '<button type="button" class="campus-chip" data-cat="library" data-i18n="campus_filter_library">📚 Kitabxana & Oxu Zalı</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="sport">⚽ İdman & Hərbi</button>',
    '<button type="button" class="campus-chip" data-cat="sport" data-i18n="campus_filter_sport">⚽ İdman & Hərbi</button>'
)
html_src = html_src.replace(
    '<button type="button" class="campus-chip" data-cat="classroom">🎓 Auditoriyalar</button>',
    '<button type="button" class="campus-chip" data-cat="classroom" data-i18n="campus_filter_classroom">🎓 Auditoriyalar</button>'
)

# Bump cache version
html_src = re.sub(r'style\.css\?v=[a-zA-Z0-9_]+', 'style.css?v=20261106_34', html_src)
html_src = re.sub(r'script\.js\?v=[a-zA-Z0-9_]+', 'script.js?v=20261106_34', html_src)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_src)
print("index.html updated with data-i18n.")

# ══════════════════════════════════════════════════════════════
# 2. UPDATE SCRIPT.JS I18N DICTIONARY
# ══════════════════════════════════════════════════════════════

campus_i18n_az = '''    nav_campus: "Kampus & Otaqlar",
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
    campus_reset_btn: "Bütün Otaqları Göstər",'''

campus_i18n_en = '''    nav_campus: "Campus & Rooms",
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
    campus_reset_btn: "Show All Rooms",'''

campus_i18n_ru = '''    nav_campus: "Кампус и Аудитории",
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
    campus_reset_btn: "Показать все кабинеты",'''

# Replace previous nav_campus blocks in i18n
pattern_az = r'nav_campus:\s*"Kampus & Otaqlar",.*?(?=header_subtitle:|footer_|category_all:|\n  \},|\n  en:)'
# Let's replace cleanly
old_az = re.search(r'nav_campus:\s*"Kampus & Otaqlar",.*?(?=category_all:|nav_home:|"nav_home"|\n  \},)', js_src, re.DOTALL)
if old_az:
    js_src = js_src[:old_az.start()] + campus_i18n_az + "\n" + js_src[old_az.end():]
else:
    js_src = js_src.replace('nav_library: "Kitabxana",', 'nav_library: "Kitabxana",\n' + campus_i18n_az, 1)

old_en = re.search(r'nav_campus:\s*"Campus & Rooms",.*?(?=category_all:|nav_home:|"nav_home"|\n  \},)', js_src, re.DOTALL)
if old_en:
    js_src = js_src[:old_en.start()] + campus_i18n_en + "\n" + js_src[old_en.end():]
else:
    js_src = js_src.replace('nav_library: "Library",', 'nav_library: "Library",\n' + campus_i18n_en, 1)

old_ru = re.search(r'nav_campus:\s*"Кампус и Аудитории",.*?(?=category_all:|nav_home:|"nav_home"|\n  \},)', js_src, re.DOTALL)
if old_ru:
    js_src = js_src[:old_ru.start()] + campus_i18n_ru + "\n" + js_src[old_ru.end():]
else:
    js_src = js_src.replace('nav_library: "Библиотека",', 'nav_library: "Библиотека",\n' + campus_i18n_ru, 1)

print("i18n dictionaries updated.")

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_src)

print("Saved script.js intermediate.")
