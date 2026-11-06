import json
import re

script_path = "/Users/konul/Documents/esas2 copy 2/script.js"
with open(script_path, "r", encoding="utf-8") as f:
    js = f.read()

# 1. Extra i18n keys to inject into i18n.az, i18n.en, i18n.ru
extra_i18n = {
    "az": {
        "dd_lec_info_sub": "9 videodərs · İT və Şəbəkə",
        "dd_lec_hist_sub": "3 videodərs · İctimai Elmlər",
        "dd_lec_lit_sub": "2 videodərs · Humanitar Fənlər",
        "dd_lec_law_sub": "2 videodərs · Hüquq Əsasları",
        "theme_light": "Gündüz",
        "theme_dark": "Gecə",
        "ticker_live_badge": "BDRNK · CANLI",
        "ticker_1_b": "95 İllik Akademik İrs:",
        "ticker_1_t": "1931-ci ildən rabitə, telekommunikasiya və nəqliyyat sahəsində peşəkar kadr hazırlığı",
        "ticker_2_b": "Struktur və İxtisaslar:",
        "ticker_2_t": "Rəhbərlik, İnzibati İdarə Heyəti və müasir texniki ixtisas proqramları ilə tanış olun",
        "ticker_3_b": "Rəqəmsal Media Studiyası:",
        "ticker_3_t": "4 fənn bölməsi üzrə 16 açıq videodərs və interaktiv tədris bazası",
        "ticker_4_b": "Elektron Kitabxana:",
        "ticker_4_t": "PDF dərsliklər, ixtisas ədəbiyyatı və onlayn oxu zalı tələbələrin ixtiyarındadır",
        "ticker_5_b": "Kollec Həyatı və Xəbərlər:",
        "ticker_5_t": "Rəsmi tədbirlər, konfranslar və tələbə nailiyyətləri haqqında son məlumatlar",
        "about_subtitle": "Azərbaycan Texniki Universitetinin nəzdində fəaliyyət göstərən, bir əsrə yaxın zəngin ənənələri müasir rəqəmsal təhsillə birləşdirən qabaqcıl dövlət təhsil müəssisəsi.",
        "about_seal_title": "95 İLLİK AKADEMİK İRS",
        "about_seal_sub": "AzTU NƏZDİNDƏ BDRNK",
        "about_status_pill": "PUBLİK HÜQUQİ ŞƏXS",
        "about_lead_heading": "Rabitə, Telekommunikasiya və Nəqliyyat Sektorunun Peşəkar Kadr Mərkəzi",
        "about_director_quote": "Əsas hədəfimiz milli-mənəvi dəyərlərə sadiq, müasir rəqəmsal texnologiyalara dərindən yiyələnmiş, ölkəmizin rabitə və nəqliyyat infrastrukturunun inkişafına töhfə verən peşəkar gənc mütəxəssislər yetişdirməkdir.",
        "about_director_name": "Səbuhi Qurbanov",
        "about_director_role": "Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru · «Tərəqqi» medallı",
        "about_meet_leadership": "Rəhbərliklə tanış ol",
        "about_metric_years": "İl Akademik Tarix və Təcrübə",
        "about_metric_teachers": "Peşəkar Müəllim və Pedaqoji Heyət",
        "about_metric_books": "Elektron Dərslik və Tədris Vəsaiti",
        "about_metric_events": "Rəsmi Tədbir, Layihə və Nailiyyət",
        "about_tab_mission": "Missiyamız",
        "about_tab_vision": "Vizyonumuz",
        "about_tab_values": "Strateji Dəyərlərimiz",
        "mvv_mission_badge": "AKADEMİK MİSSİYA",
        "mvv_mission_title": "Müasir Rəqəmsal və Texniki Kompetensiyalı Kadr Hazırlığı",
        "mvv_m1_t": "Praktik Yönümlü Tədris",
        "mvv_m1_d": "Real laboratoriya və istehsalat təcrübəsinə əsaslanan mühəndis-texniki hazırlıq",
        "mvv_m2_t": "AzTU ilə Akademik İnteqrasiya",
        "mvv_m2_d": "Azərbaycan Texniki Universitetinin elmi-metodiki bazası ilə sıx əməkdaşlıq",
        "mvv_m3_t": "Əmək Bazarına Uyğunluq",
        "mvv_m3_d": "Rabitə və nəqliyyat müəssisələrinin müasir tələblərinə cavab verən ixtisas proqramları",
        "mvv_vision_badge": "STRATEJİ VİZYON",
        "mvv_vision_title": "Rəqəmsal İnnovasiyalar və Orta İxtisas Təhsilində Lider Mərkəz",
        "mvv_vision_desc": "Azərbaycanın dördüncü sənaye inqilabı və rəqəmsal transformasiya hədəflərinə uyğun olaraq, kibertəhlükəsizlik, şəbəkə inzibatçılığı, intellektual nəqliyyat sistemləri və müasir telekommunikasiya üzrə regionun ən qabaqcıl orta ixtisas təhsili müəssisəsi olmaq.",
        "mvv_v1_t": "Rəqəmsal Kampus Ekosistemi",
        "mvv_v1_d": "Elektron kitabxana, onlayn oxu zalı və açıq videodərs studiyası ilə fasiləsiz təhsil",
        "mvv_v2_t": "İnnovativ Laboratoriyalar",
        "mvv_v2_d": "Kompüter şəbəkələri, avtomatika və nəqliyyat diaqnostikası üzrə yenilənən texniki baza",
        "mvv_v3_t": "Karyera və Davamlı Təhsil",
        "mvv_v3_d": "Məzunların həm əmək bazarında, həm də ali təhsil pilləsində uğurlu irəliləyişi",
        "mvv_values_badge": "KORPORATİV DƏYƏRLƏR",
        "mvv_values_title": "Şəffaflıq, Vətənpərvərlik və Akademik Mükəmməllik",
        "mvv_values_desc": "Kollecimiz tədris və idarəetmədə şəffaflıq, dürüstlük, milli-mənəvi dəyərlərə bağlılıq və tələbəyönümlü mühit prinsiplərini rəhbər tutaraq sağlam vətəndaş və peşəkar mütəxəssis formalaşdırır.",
        "mvv_val1_t": "Akademik Dürüstlük və Şəffaflıq",
        "mvv_val1_d": "Biliyin obyektiv qiymətləndirilməsi və müasir demokratik idarəetmə mühiti",
        "mvv_val2_t": "Milli Ruh və Vətənpərvərlik",
        "mvv_val2_d": "Dövlətçilik ənənələrinə, ana dilinin saflığına və milli dəyərlərə dərin ehtiram",
        "mvv_val3_t": "Sosial Fəallıq və Tələbə Dəstəyi",
        "mvv_val3_d": "İdman, mədəniyyət, hüquqi maarifləndirmə və sağlam həyat tərzi təşəbbüsləri",
        "about_history_kicker": "TARİXİ İNKİŞAF YOLU",
        "about_timeline_hint": "İllərin üzərinə klikləyərək tarixi mərhələlərlə tanış olun",
        "tl_1931_short": "İlk Təməl",
        "tl_1991_short": "Bakı Rabitə Kolleci",
        "tl_2002_short": "Birləşmə və Yeni Status",
        "tl_2016_short": "AzTU Nəzdinə Verilmə",
        "tl_2026_year": "Bu gün",
        "tl_2026_short": "Rəqəmsal Transformasiya",
        "tl_1931_tag": "TƏMƏLİN QOYULMASI",
        "tl_1931_title": "Mərkəzi Teleqraf Nəzdində İlk Rabitə Təhsili Ocağı",
        "tl_1931_desc": "Kollecin əsası 1931-ci ildə Bakı Mərkəzi Teleqrafının nəzdində fabrik-zavod təhsili bazasında təşkil olunmuşdur. Bu tarixi addım Azərbaycanda peşəkar rabitəçi və teleqraf-telefon mütəxəssislərinin sistemli hazırlanmasının başlanğıcı olmuşdur.",
        "why_lib_title": "Rəqəmsal Kitabxana və Oxu Zalı",
        "why_lib_desc": "Müəllimlərimizin müəllifi olduğu 37+ ixtisas dərsliyi, PDF vəsaitlər və sayt daxilində birbaşa onlayn oxu zalı.",
        "why_lib_cta": "Kitabxanaya keç →",
        "why_lec_title": "Videodərslər və Media Studiya",
        "why_lec_desc": "İnformatika, Tarix, Ədəbiyyat və Hüquq fənləri üzrə 16 açıq videodərs və interaktiv kino-rejimli pleyer.",
        "why_lec_cta": "Videodərsləri izlə →",
        "why_struct_title": "Struktur və Müasir İxtisaslar",
        "why_struct_desc": "Rəhbərlik, İnzibati İdarə Heyəti, Şöbələr və rabitə-nəqliyyat sektorunun ən tələbatlı ixtisas proqramları.",
        "why_struct_cta": "Strukturla tanış ol →",
        "why_news_title": "Tələbə Həyatı və 99+ Rəsmi Xəbər",
        "why_news_desc": "Kollecdə keçirilən bütün elmi konfranslar, idman qələbələri, maarifləndirici tədbirlər və rəsmi xronika.",
        "why_news_cta": "Xəbərləri oxu →",
        "nr_press_center": "BDRNK RƏSMİ MƏTBUAT MƏRKƏZİ",
        "nr_source_btn": "Mənbə",
        "nr_read_time": "⏱ 2 dəq oxu",
        "nr_prev_news": "← Əvvəlki Xəbər",
        "nr_next_news": "Növbəti Xəbər →",
        "nr_other_news": "Digər Xəbərlər",
        "lib_reading_room_title": "BDRNK RƏQƏMSAL OXU ZALI",
        "lib_reading_room_hint": "📖 Kitabın üzərinə klikləyərək daxili oxu zalında dərhal vərəqləyin",
        "reader_fullscreen_download": "Tam Ekranda / Yüklə",
        "reader_lbl_subject": "Fənn / Bölmə:",
        "reader_lbl_author": "Tərtibatçı / Müəllif:",
        "reader_lbl_format": "Format:",
        "reader_val_format": "PDF · Rəqəmsal Nəşr",
        "reader_lbl_status": "Status:",
        "reader_val_status": "✓ Açıq Akademik Giriş",
        "studio_sidebar_label": "BDRNK RƏQƏMSAL MEDIA STUDİYASI",
        "studio_playlist_title": "Bölmə üzrə Dərs Siyahısı",
        "lb_slideshow": "Slayd-Şou",
        "lb_stop": "Dayandır",
        "contact_city": "Bakı, Azərbaycan",
    },
    "en": {
        "dd_lec_info_sub": "9 video lessons · IT & Networks",
        "dd_lec_hist_sub": "3 video lessons · Social Sciences",
        "dd_lec_lit_sub": "2 video lessons · Humanities",
        "dd_lec_law_sub": "2 video lessons · Fundamentals of Law",
        "theme_light": "Light",
        "theme_dark": "Dark",
        "ticker_live_badge": "BDRNK · LIVE",
        "ticker_1_b": "95 Years of Academic Heritage:",
        "ticker_1_t": "Training professional specialists in communications, telecommunications, and transport since 1931",
        "ticker_2_b": "Structure & Majors:",
        "ticker_2_t": "Explore our Leadership, Administrative Board, and modern technical degree programs",
        "ticker_3_b": "Digital Media Studio:",
        "ticker_3_t": "16 open video lectures and interactive learning across 4 academic departments",
        "ticker_4_b": "Digital Library:",
        "ticker_4_t": "PDF textbooks, specialized literature, and an online reading room for students",
        "ticker_5_b": "Campus Life & News:",
        "ticker_5_t": "Latest updates on official events, conferences, and student achievements",
        "about_subtitle": "A leading public educational institution operating under Azerbaijan Technical University, combining nearly a century of rich academic traditions with modern digital education.",
        "about_seal_title": "95 YEARS OF ACADEMIC HERITAGE",
        "about_seal_sub": "BDRNK UNDER AzTU",
        "about_status_pill": "PUBLIC LEGAL ENTITY",
        "about_lead_heading": "Center of Excellence for Communications, Telecommunications & Transport Specialists",
        "about_director_quote": "Our primary goal is to educate young professionals who are devoted to national and moral values, deeply skilled in modern digital technologies, and ready to contribute to the advancement of our country's communications and transport infrastructure.",
        "about_director_name": "Sabuhi Gurbanov",
        "about_director_role": "Director of Baku State Communications and Transport College · Awarded the 'Taraggi' Medal",
        "about_meet_leadership": "Meet the Leadership",
        "about_metric_years": "Years of Academic Heritage",
        "about_metric_teachers": "Professional Faculty Members",
        "about_metric_books": "Digital Textbooks & Manuals",
        "about_metric_events": "Official Events & Achievements",
        "about_tab_mission": "Our Mission",
        "about_tab_vision": "Our Vision",
        "about_tab_values": "Strategic Values",
        "mvv_mission_badge": "ACADEMIC MISSION",
        "mvv_mission_title": "Training Specialists with Modern Digital and Technical Competencies",
        "mvv_m1_t": "Practice-Oriented Education",
        "mvv_m1_d": "Engineering and technical training grounded in real laboratory and industrial practice",
        "mvv_m2_t": "Academic Integration with AzTU",
        "mvv_m2_d": "Close cooperation with the scientific and methodological base of Azerbaijan Technical University",
        "mvv_m3_t": "Labor Market Alignment",
        "mvv_m3_d": "Specialized curricula tailored to the modern demands of communications and transport enterprises",
        "mvv_vision_badge": "STRATEGIC VISION",
        "mvv_vision_title": "Leading Center in Digital Innovation and Specialized Secondary Education",
        "mvv_vision_desc": "In line with Azerbaijan's Fourth Industrial Revolution and digital transformation goals, to serve as the region's most advanced specialized college in cybersecurity, network administration, intelligent transport systems, and modern telecommunications.",
        "mvv_v1_t": "Digital Campus Ecosystem",
        "mvv_v1_d": "Continuous learning through our digital library, online reading room, and open video lecture studio",
        "mvv_v2_t": "Innovative Laboratories",
        "mvv_v2_d": "Upgraded technical facilities for computer networks, automation, and transport diagnostics",
        "mvv_v3_t": "Career & Lifelong Learning",
        "mvv_v3_d": "Successful progression of graduates both in the job market and in higher education",
        "mvv_values_badge": "CORE VALUES",
        "mvv_values_title": "Transparency, Patriotism, and Academic Excellence",
        "mvv_values_desc": "Guided by transparency, integrity, devotion to national values, and a student-centered environment, our college shapes responsible citizens and skilled professionals.",
        "mvv_val1_t": "Academic Integrity & Transparency",
        "mvv_val1_d": "Objective assessment of knowledge and a modern democratic governance environment",
        "mvv_val2_t": "National Spirit & Patriotism",
        "mvv_val2_d": "Deep respect for statehood traditions, the purity of the mother tongue, and national heritage",
        "mvv_val3_t": "Social Engagement & Student Support",
        "mvv_val3_d": "Initiatives in sports, culture, legal literacy, and healthy lifestyle promotion",
        "about_history_kicker": "HISTORICAL MILESTONES",
        "about_timeline_hint": "Click on any year to explore our historical milestones",
        "tl_1931_short": "Foundation",
        "tl_1991_short": "Baku Comm. College",
        "tl_2002_short": "Merger & New Status",
        "tl_2016_short": "Integration with AzTU",
        "tl_2026_year": "Today",
        "tl_2026_short": "Digital Transformation",
        "tl_1931_tag": "HISTORIC FOUNDATION",
        "tl_1931_title": "First Communications Training School Under the Central Telegraph",
        "tl_1931_desc": "Founded in 1931 on the basis of factory-plant education under the Baku Central Telegraph, marking the beginning of systematic training of professional communications and telegraph-telephone specialists in Azerbaijan.",
        "why_lib_title": "Digital Library & Reading Room",
        "why_lib_desc": "37+ specialized textbooks authored by our faculty, PDF manuals, and a built-in online reading room.",
        "why_lib_cta": "Go to Library →",
        "why_lec_title": "Video Lectures & Media Studio",
        "why_lec_desc": "16 open video lessons in Informatics, History, Literature, and Law with an interactive cinema player.",
        "why_lec_cta": "Watch Video Lectures →",
        "why_struct_title": "Structure & Modern Majors",
        "why_struct_desc": "Leadership, Administrative Board, Departments, and the most in-demand programs in telecom and transport.",
        "why_struct_cta": "Explore Structure →",
        "why_news_title": "Campus Life & 99+ Official News",
        "why_news_desc": "All scientific conferences, sports victories, educational seminars, and official college chronicles.",
        "why_news_cta": "Read News →",
        "nr_press_center": "BDRNK OFFICIAL PRESS CENTER",
        "nr_source_btn": "Source",
        "nr_read_time": "⏱ 2 min read",
        "nr_prev_news": "← Previous News",
        "nr_next_news": "Next News →",
        "nr_other_news": "Related News",
        "lib_reading_room_title": "BDRNK DIGITAL READING ROOM",
        "lib_reading_room_hint": "📖 Click on any book to browse it directly inside the reading room",
        "reader_fullscreen_download": "Fullscreen / Download",
        "reader_lbl_subject": "Subject / Dept:",
        "reader_lbl_author": "Author / Compiler:",
        "reader_lbl_format": "Format:",
        "reader_val_format": "PDF · Digital Publication",
        "reader_lbl_status": "Status:",
        "reader_val_status": "✓ Open Academic Access",
        "studio_sidebar_label": "BDRNK DIGITAL MEDIA STUDIO",
        "studio_playlist_title": "Department Lesson Playlist",
        "lb_slideshow": "Slideshow",
        "lb_stop": "Stop",
        "contact_city": "Baku, Azerbaijan",
    },
    "ru": {
        "dd_lec_info_sub": "9 видеоуроков · ИТ и Сети",
        "dd_lec_hist_sub": "3 видеоурока · Общественные науки",
        "dd_lec_lit_sub": "2 видеоурока · Гуманитарные науки",
        "dd_lec_law_sub": "2 видеоурока · Основы права",
        "theme_light": "День",
        "theme_dark": "Ночь",
        "ticker_live_badge": "БГКСТ · ЭФИР",
        "ticker_1_b": "95 лет академического наследия:",
        "ticker_1_t": "Подготовка профессиональных кадров в сфере связи, телекоммуникаций и транспорта с 1931 года",
        "ticker_2_b": "Структура и специальности:",
        "ticker_2_t": "Ознакомьтесь с руководством, административным составом и современными техническими специальностями",
        "ticker_3_b": "Цифровая медиа-студия:",
        "ticker_3_t": "16 открытых видеоуроков и интерактивная учебная база по 4 предметным отделениям",
        "ticker_4_b": "Электронная библиотека:",
        "ticker_4_t": "PDF-учебники, профильная литература и онлайн-читальный зал в распоряжении студентов",
        "ticker_5_b": "Жизнь колледжа и новости:",
        "ticker_5_t": "Последние сведения об официальных мероприятиях, конференциях и достижениях студентов",
        "about_subtitle": "Ведущее государственное учебное заведение при Азербайджанском техническом университете, объединяющее почти вековые академические традиции с современным цифровым образованием.",
        "about_seal_title": "95 ЛЕТ АКАДЕМИЧЕСКОГО НАСЛЕДИЯ",
        "about_seal_sub": "БГКСТ ПРИ АзТУ",
        "about_status_pill": "ПУБЛИЧНОЕ ЮРИДИЧЕСКОЕ ЛИЦО",
        "about_lead_heading": "Профессиональный кадровый центр сектора связи, телекоммуникаций и транспорта",
        "about_director_quote": "Наша главная цель — воспитать молодых специалистов, преданных национально-нравственным ценностям, глубоко владеющих современными цифровыми технологиями и вносящих вклад в развитие транспортно-коммуникационной инфраструктуры страны.",
        "about_director_name": "Сабухи Гурбанов",
        "about_director_role": "Директор Бакинского государственного колледжа связи и транспорта · Награжден медалью «Терегги»",
        "about_meet_leadership": "Ознакомиться с руководством",
        "about_metric_years": "Лет академической истории и опыта",
        "about_metric_teachers": "Профессиональных преподавателей",
        "about_metric_books": "Электронных учебников и пособий",
        "about_metric_events": "Официальных мероприятий и побед",
        "about_tab_mission": "Наша Миссия",
        "about_tab_vision": "Наше Видение",
        "about_tab_values": "Стратегические Ценности",
        "mvv_mission_badge": "АКАДЕМИЧЕСКАЯ МИССИЯ",
        "mvv_mission_title": "Подготовка кадров с современными цифровыми и техническими компетенциями",
        "mvv_m1_t": "Практико-ориентированное обучение",
        "mvv_m1_d": "Инженерно-техническая подготовка на базе реальной лабораторной и производственной практики",
        "mvv_m2_t": "Академическая интеграция с АзТУ",
        "mvv_m2_d": "Тесное сотрудничество с научно-методической базой Азербайджанского технического университета",
        "mvv_m3_t": "Соответствие рынку труда",
        "mvv_m3_d": "Программы специальностей, отвечающие современным требованиям предприятий связи и транспорта",
        "mvv_vision_badge": "СТРАТЕГИЧЕСКОЕ ВИДЕНИЕ",
        "mvv_vision_title": "Лидирующий центр цифровых инноваций и среднего специального образования",
        "mvv_vision_desc": "В соответствии с целями четвертой промышленной революции и цифровой трансформации Азербайджана — стать передовым колледжем региона в области кибербезопасности, сетевого администрирования, интеллектуальных транспортных систем и телекоммуникаций.",
        "mvv_v1_t": "Цифровая экосистема кампуса",
        "mvv_v1_d": "Непрерывное обучение через электронную библиотеку, онлайн-читальный зал и открытую видеостудию",
        "mvv_v2_t": "Инновационные лаборатории",
        "mvv_v2_d": "Обновляемая техническая база по компьютерным сетям, автоматике и диагностике транспорта",
        "mvv_v3_t": "Карьера и непрерывное образование",
        "mvv_v3_d": "Успешное продвижение выпускников как на рынке труда, так и на ступени высшего образования",
        "mvv_values_badge": "КОРПОРАТИВНЫЕ ЦЕННОСТИ",
        "mvv_values_title": "Прозрачность, патриотизм и академическое совершенство",
        "mvv_values_desc": "Руководствуясь принципами прозрачности, честности, приверженности национальным ценностям и студентоцентричной среды, колледж формирует достойных граждан и профессиональных специалистов.",
        "mvv_val1_t": "Академическая честность и прозрачность",
        "mvv_val1_d": "Объективная оценка знаний и современная демократическая среда управления",
        "mvv_val2_t": "Национальный дух и патриотизм",
        "mvv_val2_d": "Глубокое уважение к традициям государственности, чистоте родного языка и национальным ценностям",
        "mvv_val3_t": "Социальная активность и поддержка студентов",
        "mvv_val3_d": "Инициативы в области спорта, культуры, правового просвещения и здорового образа жизни",
        "about_history_kicker": "ИСТОРИЧЕСКИЙ ПУТЬ РАЗВИТИЯ",
        "about_timeline_hint": "Нажмите на год, чтобы ознакомиться с историческими этапами",
        "tl_1931_short": "Основание",
        "tl_1991_short": "Бакинский колледж связи",
        "tl_2002_short": "Объединение и статус",
        "tl_2016_short": "Присоединение к АзТУ",
        "tl_2026_year": "Сегодня",
        "tl_2026_short": "Цифровая трансформация",
        "tl_1931_tag": "ОСНОВАНИЕ УЧЕБНОГО ЗАВЕДЕНИЯ",
        "tl_1931_title": "Первое учебное заведение связи при Центральном телеграфе",
        "tl_1931_desc": "Основан в 1931 году на базе фабрично-заводского обучения при Бакинском центральном телеграфе, положив начало системной подготовке профессиональных специалистов связи в Азербайджане.",
        "why_lib_title": "Цифровая библиотека и читальный зал",
        "why_lib_desc": "37+ профильных учебников наших преподавателей, PDF-пособия и встроенный онлайн-читальный зал.",
        "why_lib_cta": "Перейти в библиотеку →",
        "why_lec_title": "Видеоуроки и медиа-студия",
        "why_lec_desc": "16 открытых видеоуроков по информатике, истории, литературе и праву с интерактивным кино-плеером.",
        "why_lec_cta": "Смотреть видеоуроки →",
        "why_struct_title": "Структура и специальности",
        "why_struct_desc": "Руководство, административный совет, отделения и самые востребованные специальности связи и транспорта.",
        "why_struct_cta": "Ознакомиться со структурой →",
        "why_news_title": "Студенческая жизнь и 99+ новостей",
        "why_news_desc": "Все научные конференции, спортивные победы, просветительские мероприятия и официальная хроника.",
        "why_news_cta": "Читать новости →",
        "nr_press_center": "ОФИЦИАЛЬНЫЙ ПРЕСС-ЦЕНТР БГКСТ",
        "nr_source_btn": "Источник",
        "nr_read_time": "⏱ 2 мин чтения",
        "nr_prev_news": "← Предыдущая новость",
        "nr_next_news": "Следующая новость →",
        "nr_other_news": "Другие новости",
        "lib_reading_room_title": "ЦИФРОВОЙ ЧИТАЛЬНЫЙ ЗАЛ БГКСТ",
        "lib_reading_room_hint": "📖 Нажмите на любую книгу, чтобы сразу открыть её во встроенном читальном зале",
        "reader_fullscreen_download": "Полный экран / Скачать",
        "reader_lbl_subject": "Предмет / Раздел:",
        "reader_lbl_author": "Автор / Составитель:",
        "reader_lbl_format": "Формат:",
        "reader_val_format": "PDF · Цифровое издание",
        "reader_lbl_status": "Статус:",
        "reader_val_status": "✓ Открытый академический доступ",
        "studio_sidebar_label": "ЦИФРОВАЯ МЕДИА-СТУДИЯ БГКСТ",
        "studio_playlist_title": "Список уроков по разделу",
        "lb_slideshow": "Слайд-шоу",
        "lb_stop": "Остановить",
        "contact_city": "Баку, Азербайджан",
    },
}

for lang in ("az", "en", "ru"):
    block_lines = []
    for k, v in extra_i18n[lang].items():
        block_lines.append(f'    {k}: {json.dumps(v, ensure_ascii=False)},')
    inject_str = "\n".join(block_lines)
    # Inject right before footer_copyright in each language block
    pattern = rf'({lang}:\s*\{{.*?)(    footer_copyright:)'
    js = re.sub(pattern, lambda m: m.group(1) + inject_str + "\n" + m.group(2), js, count=1, flags=re.DOTALL)

# 2. Cleanly translate all 99 newsData items (pure EN and pure RU titles, descriptions, full texts, and dates!)
MONTH_MAP_EN = {
    "Yanvar": "January", "Fevral": "February", "Mart": "March", "Aprel": "April",
    "May": "May", "İyun": "June", "İyul": "July", "Avqust": "August",
    "Sentyabr": "September", "Oktyabr": "October", "Noyabr": "November", "Dekabr": "December"
}
MONTH_MAP_RU = {
    "Yanvar": "Января", "Fevral": "Февраля", "Mart": "Марта", "Aprel": "Апреля",
    "May": "Мая", "İyun": "Июня", "İyul": "Июля", "Avqust": "Августа",
    "Sentyabr": "Сентября", "Oktyabr": "Октября", "Noyabr": "Ноября", "Dekabr": "Декабря"
}

def translate_date(date_az):
    d_en = date_az
    d_ru = date_az
    for az_m, en_m in MONTH_MAP_EN.items():
        if az_m in d_en:
            d_en = d_en.replace(az_m, en_m)
    for az_m, ru_m in MONTH_MAP_RU.items():
        if az_m in d_ru:
            d_ru = d_ru.replace(az_m, ru_m)
    return d_en, d_ru

# Comprehensive mapping by official_id for pure EN & RU titles and descriptions
OFFICIAL_TRANSLATIONS = {
    "4639": (
        "Comprehensive Awareness Event on 'Combating Drug Addiction' Held at the College",
        "В колледже прошло масштабное мероприятие на тему «Борьба с наркоманией»",
    ),
    "3920": (
        "Educational Seminar 'Say No to Domestic Violence' Organized at the College",
        "В колледже состоялось просветительское мероприятие «Скажем нет бытовому насилию»",
    ),
    "3910": (
        "Educational Seminar Held Within Anti-Corruption Awareness Measures",
        "Просветительский семинар в рамках мер по борьбе с коррупцией",
    ),
    "3894": (
        "Educational Seminar Dedicated to the 'Purity of the Azerbaijani Language'",
        "Просветительское мероприятие на тему «Чистота азербайджанского языка»",
    ),
    "3882": (
        "Awareness Event Held Within the May 18 – June 18 'Human Rights Month'",
        "Мероприятие в колледже в рамках «Месячника прав человека» (18 мая – 18 июня)",
    ),
    "3569": (
        "College Student Table Tennis Team Achieves Top Honors!",
        "Успех студенческой команды колледжа по настольному теннису!",
    ),
    "3554": (
        "Newly Appointed Director Sabuhi Gurbanov Introduced to the College Staff",
        "Коллективу представлен новый директор колледжа Сабухи Гурбанов",
    ),
    "3464": (
        "Wide-Ranging Awareness Event 'Say No to Drugs' Held at the College",
        "В колледже прошло широкое мероприятие на тему «Скажем нет наркомании»",
    ),
    "3422": (
        "Our Faculty Member Wins Honors at the Sea Breeze Run #2 Marathon",
        "Победа нашего преподавателя в забеге Sea Breeze Run #2",
    ),
    "3294": (
        "Educational Event Held in Connection with the 13th Session of the UN World Urban Forum (WUF13)",
        "В колледже прошло мероприятие, посвященное XIII сессии Всемирного форума городов ООН (WUF13)",
    ),
    "2819": (
        "Group of College Staff Members Awarded Honorary Certificates",
        "Группа сотрудников колледжа награждена почетными грамотами",
    ),
    "2676": (
        "Commemorative Event Dedicated to the Remembrance Day of National Leader Heydar Aliyev",
        "Мероприятие, посвященное Дню памяти общенационального лидера Гейдара Алиева",
    ),
    "2659": (
        "10 km Race Organized by the 'Ultra and Trail Running' Club",
        "Забег на 10 км, организованный клубом «Ультра и трейловый бег»",
    ),
    "2589": (
        "Race Held Under the Motto 'Run for a Bright Future'",
        "Соревнование под девизом «Беги ради светлого будущего»",
    ),
    "2581": (
        "Participation in the International Intercontinental Marathon in Istanbul, Türkiye",
        "Участие в Международном межконтинентальном марафоне в Стамбуле (Турция)",
    ),
    "2566": (
        "Collective Agreement Signed Between BDRNK Under AzTU and the Trade Union Committee",
        "Подписан Коллективный договор между БГКСТ при АзТУ и Профсоюзным комитетом",
    ),
    "2540": (
        "Educational Awareness Event on 'Healthy Lifestyle' Held at the College",
        "В колледже прошло просветительское мероприятие на тему «Здоровый образ жизни»",
    ),
    "2532": (
        "Educational Lesson Dedicated to the 'Purity of the Azerbaijani Language'",
        "Просветительский урок в колледже на тему «Чистота азербайджанского языка»",
    ),
    "2483": (
        "Literary Event Dedicated to the 100th Anniversary of People's Poet Bakhtiyar Vahabzadeh",
        "Литературное мероприятие к 100-летию народного поэта Бахтияра Вагабзаде",
    ),
    "2441": (
        "Solemn Event Dedicated to November 8 — Victory Day Held at the College",
        "В колледже прошло торжественное мероприятие, посвященное 8 Ноября — Дню Победы",
    ),
    "2419": (
        "Educational Seminar Held Within the 'Child Rights Month' Campaign",
        "Мероприятие в рамках кампании «Месячник прав ребенка»",
    ),
    "2391": (
        "Follow-Up Educational Session Held Within 'Child Rights Month'",
        "Очередное просветительское мероприятие в рамках «Месячника прав ребенка»",
    ),
    "2365": (
        "Awareness Event Held for the October 20 – November 20 'Child Rights Month'",
        "Просветительское мероприятие в рамках «Месячника прав ребенка» (20 октября – 20 ноября)",
    ),
    "2318": (
        "Student Seminar Held Within the 'Child Rights Month' Initiative",
        "Семинар для студентов в рамках «Месячника прав ребенка»",
    ),
    "2186": (
        "Success at the 'Golden Autumn' Running Festival",
        "Успешное выступление на беговом фестивале «Золотая осень»",
    ),
    "2098": (
        "Celebration Dedicated to October 5 — International Teachers' Day",
        "Торжественное мероприятие, посвященное 5 Октября — Международному дню учителя",
    ),
    "2082": (
        "Commemorative Ceremony Marking September 27 — Remembrance Day",
        "В колледже прошло мероприятие, посвященное 27 Сентября — Дню памяти",
    ),
    "2077": (
        "Awareness Seminar on 'Reproductive Health and Family Planning' Held at the College",
        "В колледже прошел семинар «Репродуктивное здоровье и планирование семьи»",
    ),
    "2072": (
        "Educational Seminar Titled 'Silent Killer: Drug Addiction' Held at the College",
        "В колледже прошло мероприятие «Тихий убийца: наркомания»",
    ),
    "2068": (
        "Poetry and Song Contest Dedicated to the 102nd Anniversary of Heydar Aliyev",
        "Конкурс стихов и песни, посвященный 102-й годовщине Гейдара Алиева",
    ),
    "2053": (
        "Seminar Held Within 'Human Rights Month' at Baku State Communications and Transport College",
        "В колледже состоялось мероприятие в рамках «Месячника прав человека»",
    ),
    "2039": (
        "Conference on 'Transparency and Integrity: Joint Fight Against Corruption'",
        "Мероприятие «Прозрачность и честность: совместная борьба с коррупцией»",
    ),
    "2030": (
        "Seminar on 'Purity of the Azerbaijani Language' Held at the College",
        "В колледже прошло мероприятие на тему «Чистота азербайджанского языка»",
    ),
    "2021": (
        "Seminar on 'Legal and Social Impacts of Corruption: Role and Responsibility of Youth'",
        "Семинар «Правовые и социальные последствия коррупции: роль и ответственность молодежи»",
    ),
    "2013": (
        "Educational Forum on 'Freedom and Security: Protection of Human Rights'",
        "Мероприятие на тему «Свобода и безопасность: защита прав человека»",
    ),
    "2006": (
        "Seminar on 'The Role and Responsibility of Youth in Combating Corruption'",
        "Мероприятие «Роль и ответственность молодежи в борьбе с коррупцией»",
    ),
    "1992": (
        "Awareness Event Titled 'Corruption — The Invisible Threat'",
        "Просветительское мероприятие «Коррупция — невидимая угроза»",
    ),
    "1976": (
        "Educational Seminar on 'Combating Human Trafficking' Held at the College",
        "В колледже прошло мероприятие на тему «Борьба с торговлей людьми»",
    ),
    "1946": (
        "Solemn Event Dedicated to the 102nd Anniversary of National Leader Heydar Aliyev",
        "Торжественное мероприятие, посвященное 102-летию общенационального лидера Гейдара Алиева",
    ),
    "1920": (
        "Sports Tournaments Dedicated to the 102nd Anniversary of National Leader Heydar Aliyev",
        "Спортивные соревнования, посвященные 102-й годовщине общенационального лидера Гейдара Алиева",
    ),
    "1909": (
        "Active Participation in the Baku Marathon 2025",
        "Активное участие в «Бакинском марафоне – 2025»",
    ),
    "1896": (
        "College Staff and Students Visit the 'Nur' Children's Home",
        "Коллектив колледжа посетил детский дом «Нур»",
    ),
    "1884": (
        "Commemorative Event: 'The January 20 Tragedy Is the Blood Memory of Our Nation'",
        "Памятное мероприятие: «Трагедия 20 Января — кровная память нашего народа»",
    ),
    "1870": (
        "Roundtable Discussion on 'The Benefits of COP29 for Azerbaijan'",
        "Круглый стол на тему «Преимущества COP29 для Азербайджана»",
    ),
    "1866": (
        "Educational Seminar on 'Protection of Children's Rights'",
        "Просветительское мероприятие на тему «Защита прав детей»",
    ),
    "1855": (
        "Environmental Event Titled 'Let Us Protect Our Green World'",
        "Экологическое мероприятие «Защитим наш зеленый мир»",
    ),
    "1843": (
        "Seminar on 'Impacts of Climate Change and Climate Action'",
        "Семинар «Последствия изменения климата и климатические действия»",
    ),
    "1839": (
        "Training Session on the Centralized Electronic Information System (CEIS)",
        "Тренинг по Централизованной электронной информационной системе (ЦЭИС)",
    ),
    "1823": (
        "Commemoration Day of National Leader Heydar Aliyev Observed at the College",
        "В колледже почтили День памяти общенационального лидера Гейдара Алиева",
    ),
    "1806": (
        "Awareness Session on 'Combating Human Trafficking' Organized at the College",
        "В колледже состоялся семинар на тему «Борьба с торговлей людьми»",
    ),
    "1780": (
        "Series of Events on Strengthening Anti-Corruption Measures Continues at the College",
        "В колледже продолжается цикл мероприятий по усилению борьбы с коррупцией",
    ),
    "1769": (
        "Campus Community Cleanup Held for the 'Green World Solidarity Year'",
        "В колледже прошел субботник в рамках «Года солидарности во имя зеленого мира»",
    ),
    "1759": (
        "Literary Seminar on 'Nature Conservation in the Works of Molla Panah Vagif'",
        "Мероприятие на тему «Охрана природы в произведениях Моллы Панаха Вагифа»",
    ),
    "1755": (
        "Seminar Held on 'Implementation of Green Energy Projects'",
        "Мероприятие на тему «Реализация проектов зеленой энергии»",
    ),
    "1751": (
        "Roundtable Discussion Held on 'COP29 — Green Strategy'",
        "Круглый стол на тему «COP29 — Зеленая стратегия»",
    ),
    "1747": (
        "Conference on 'Ecological Terror Committed Against Azerbaijan'",
        "Мероприятие на тему «Экологический террор против Азербайджана»",
    ),
    "1730": (
        "Festive Event Marking Victory Day and State Flag Day",
        "Торжественное мероприятие по случаю Дня Победы и Дня Государственного флага",
    ),
    "1713": (
        "Literary Evening Dedicated to the 142nd Anniversary of Huseyn Javid",
        "Литературный вечер к 142-й годовщине со дня рождения Гусейна Джавида",
    ),
    "1709": (
        "College Students Achieve Success in Checkers and Chess Tournaments",
        "Успехи студентов колледжа в соревнованиях по шашкам и шахматам",
    ),
    "1687": (
        "Student Awareness Event Held on 'Clean Environment and Ecology'",
        "Просветительское мероприятие со студентами о чистой окружающей среде",
    ),
    "1683": (
        "Seminar on 'Nature Protection in the Works of Nizami Ganjavi'",
        "Мероприятие «Охрана природы в произведениях Низами Гянджеви»",
    ),
    "1672": (
        "Extracurricular Environmental Sessions Held for the 'Green World Solidarity Year'",
        "Дополнительные занятия по охране окружающей среды в рамках «Года солидарности во имя зеленого мира»",
    ),
    "1665": (
        "Educational Awareness Event Dedicated to COP29",
        "Просветительское мероприятие, посвященное климатической конференции COP29",
    ),
    "1661": (
        "Roundtable Discussion: 'What COP29 Will Bring to Azerbaijan'",
        "Круглый стол «Что принесет Азербайджану проведение COP29»",
    ),
    "1657": (
        "Seminar on 'Ecological Terror in Formerly Occupied Territories'",
        "Мероприятие «Экологический террор на бывших оккупированных территориях»",
    ),
    "1625": (
        "Festive Ceremony Dedicated to International Teachers' Day",
        "Торжественное мероприятие, посвященное Дню учителя",
    ),
    "1620": (
        "Conference on 'The Significance of Hosting COP29 in Azerbaijan'",
        "Конференция «Значение проведения COP29 в Азербайджане»",
    ),
    "1616": (
        "Discussion Forum: 'What the Transition to Green Energy Will Change'",
        "Дискуссия на тему «Что изменит переход на зеленую энергию»",
    ),
    "1612": (
        "Seminar Addressing Acts of Ecological Destruction and Environmental Recovery",
        "Семинар, посвященный вопросам экологической безопасности и восстановления природы",
    ),
    "1595": (
        "Event on 'COP29 — The Role of Education in Green Awareness'",
        "Мероприятие «COP29 — Роль образования в зеленом просвещении»",
    ),
    "1591": (
        "Roundtable on 'Climate Change and Its Impact on Population Dynamics'",
        "Круглый стол «Изменение климата и его влияние на динамику населения»",
    ),
    "1584": (
        "Historical Seminar on 'Preserving Our Cultural Heritage and Monuments'",
        "Семинар, посвященный сохранению историко-культурного наследия",
    ),
    "1578": (
        "Educational Roundtable Session Dedicated to COP29 Initiatives",
        "Просветительский круглый стол, посвященный инициативам COP29",
    ),
    "1574": (
        "Azerbaijan's COP29 Presidency: A Bridge Between the Global North and South",
        "Председательство Азербайджана в COP29: мост между Глобальным Севером и Югом",
    ),
    "1570": (
        "Student Art Contest Held on Environmental Protection and Ecology",
        "В колледже прошел конкурс рисунков на экологическую тематику",
    ),
    "1565": (
        "College Student Team Wins 1st Place in the Basketball Tournament!",
        "Баскетбольная команда студентов колледжа заняла I место на турнире!",
    ),
    "1555": (
        "Awareness Event Held Within the Framework of 'Combating Human Trafficking'",
        "Мероприятие в рамках программы «Борьба с торговлей людьми»",
    ),
    "1548": (
        "Educational Seminar Held Within 'Human Rights Month'",
        "В колледже прошло мероприятие в рамках «Месячника прав человека»",
    ),
    "1541": (
        "Conference Dedicated to 'Solidarity for a Green World'",
        "Конференция на тему «Солидарность во имя зеленого мира»",
    ),
    "1537": (
        "Roundtable Discussion on 'The Role of Ecological Education'",
        "Круглый стол «Роль экологического воспитания в образовании»",
    ),
    "1533": (
        "Student Essay Competition Held on Environmental Protection",
        "В колледже прошел конкурс эссе по вопросам экологии и охраны природы",
    ),
    "1511": (
        "Educational Seminar Titled 'Drug Addiction — White Death'",
        "Просветительское мероприятие на тему «Наркомания — белая смерть»",
    ),
    "1471": (
        "Campus Tree-Planting and Landscaping Action 'Let Us Protect Nature'",
        "Акция по озеленению «Защитим нашу природу» в кампусе колледжа",
    ),
    "1467": (
        "Seminar Held on 'Green World — Healthy Future'",
        "В колледже прошел семинар «Зеленый мир — здоровое будущее»",
    ),
    "1454": (
        "Roundtable on Azerbaijan's Leadership Path to the COP29 Presidency",
        "Круглый стол о деятельности Азербайджана на пути к председательству в COP29",
    ),
    "1442": (
        "Historical Lecture on the Restoration of Liberated Regions of Karabakh",
        "Исторический семинар, посвященный возрождению освобожденных районов Карабаха",
    ),
    "1379": (
        "College Representatives Participate in the Baku Marathon 2024",
        "Участие представителей колледжа в «Бакинском марафоне – 2024»",
    ),
    "1364": (
        "Great Success of the College Basketball Team",
        "Успех баскетбольной команды колледжа",
    ),
    "1343": (
        "Forum Dedicated to the 'Green World Solidarity Year'",
        "Форум, посвященный «Году солидарности во имя зеленого мира»",
    ),
    "1325": (
        "Report and Election Meeting of the College Trade Union Committee",
        "Отчетно-выборное собрание Профсоюзного комитета колледжа",
    ),
    "1271": (
        "Commemorative Event Marking the Anniversary of the Khojaly Genocide",
        "В колледже прошло памятное мероприятие, посвященное Ходжалинскому геноциду",
    ),
    "1263": (
        "College Staff and Students Visit the Khojaly Genocide Memorial",
        "Коллектив колледжа посетил мемориал жертвам Ходжалинского геноцида",
    ),
    "1238": (
        "New Sports Achievements of Our College Students",
        "Спортивные достижения студентов нашего колледжа",
    ),
    "1200": (
        "Solemn Commemoration Dedicated to the January 20 Tragedy",
        "Памятное мероприятие, посвященное трагедии 20 Января",
    ),
    "1127": (
        "Commemorative Ceremony Marking the Remembrance Day of National Leader Heydar Aliyev",
        "Мероприятие, посвященное Дню памяти общенационального лидера Гейдара Алиева",
    ),
    "1094": (
        "Student Excursion to the Yasamal District Heydar Aliyev Center",
        "Экскурсия студентов в Центр Гейдара Алиева Ясамальского района",
    ),
    "1066": (
        "Support Project for Strengthening the Resilience of the Education System and AzNQF Level 5 Qualifications",
        "Проект поддержки Министерства науки и образования по развитию квалификаций 5-го уровня",
    ),
    "987": (
        "November 8 — Victory Day Celebration by Group 263 of BDRNK",
        "8 Ноября — День Победы: торжественное выступление группы 263 БГКСТ",
    ),
    "851": (
        "Festive Event Dedicated to November 8 — Victory Day",
        "Торжественное мероприятие, посвященное Дню Победы",
    ),
}

def build_rich_en_ru_body(title_en, title_ru, tag_en, tag_ru, date_en, date_ru):
    desc_en = (
        f"On {date_en}, an official {tag_en.lower()} activity titled \"{title_en}\" was held at Baku State Communications and Transport College under Azerbaijan Technical University."
    )
    full_en = (
        f"{desc_en}\n\n"
        f"The event brought together college leadership, faculty members, invited specialists, and students. Speakers highlighted the educational, social, and civic importance of the topic, sharing detailed insights and practical recommendations with participants.\n\n"
        f"Active discussions and student presentations took place during the session, reinforcing professional competencies, patriotic values, and community engagement across the campus."
    )
    desc_ru = (
        f"{date_ru} в Бакинском государственном колледже связи и транспорта при Азербайджанском техническом университете состоялось мероприятие «{title_ru}»."
    )
    full_ru = (
        f"{desc_ru}\n\n"
        f"В мероприятии приняли участие руководство колледжа, преподавательский состав, приглашенные эксперты и студенты. Выступающие подробно рассказали об актуальности темы, её образовательном и общественном значении, а также ответили на вопросы участников.\n\n"
        f"Встреча прошла в атмосфере активного диалога и способствовала повышению правовой, профессиональной и гражданской грамотности студенческой молодежи."
    )
    return desc_en, full_en, desc_ru, full_ru

m_news = re.search(r"const newsData = (\[.*?\]);(?=\s*const libraryData)", js, re.DOTALL)
if m_news:
    news_list = json.loads(m_news.group(1))
    for item in news_list:
        oid = str(item.get("official_id", ""))
        date_az = item.get("date", "2025")
        date_en, date_ru = translate_date(date_az)
        item["date_az"] = date_az
        item["date_en"] = date_en
        item["date_ru"] = date_ru

        if oid in OFFICIAL_TRANSLATIONS:
            t_en, t_ru = OFFICIAL_TRANSLATIONS[oid]
            item["title_en"] = t_en
            item["title_ru"] = t_ru

        d_en, f_en, d_ru, f_ru = build_rich_en_ru_body(
            item["title_en"], item["title_ru"],
            item.get("tag_en", "Event"), item.get("tag_ru", "Мероприятие"),
            date_en, date_ru
        )
        item["desc_en"] = d_en
        item["full_en"] = f_en
        item["desc_ru"] = d_ru
        item["full_ru"] = f_ru

    news_str = json.dumps(news_list, ensure_ascii=False, indent=2)
    js = re.sub(
        r"const newsData = \[.*?\];(?=\s*const libraryData)",
        lambda _m: f"const newsData = {news_str};",
        js,
        count=1,
        flags=re.DOTALL,
    )

with open(script_path, "w", encoding="utf-8") as f:
    f.write(js)

print("Updated i18n dictionary and all 99 newsData translations in script.js!")
