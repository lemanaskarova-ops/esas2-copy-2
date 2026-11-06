/**
 * 0. IMMEDIATE THEME CHECK (Prevent FOUC)
 */
(function () {
  const currentTheme = localStorage.getItem("bdrnk-theme");
  if (currentTheme === "dark" || currentTheme === "space") {
    document.documentElement.classList.add("dark-mode");
    document.body.classList.add("dark-mode");
  }
})();

/**
 * 1. MULTI-LANGUAGE DICTIONARY (AZ, EN, RU)
 * Instant DOM update without reload.
 */
const i18n = {
  az: {
    header_subtitle: "Bakı Dövlət Rabitə və Nəqliyyat Kolleci",
    nav_home: "Ana Səhifə",
    nav_about: "Haqqımızda",
    nav_structure: "Struktur",
    nav_library: "Kitabxana",
    nav_lectures: "Videodərslər",
    nav_sis: "Tələbə Portalı",
    nav_contact: "Əlaqə",
    nav_register: "Qeydiyyat",
    hero_badge: "Rəsmi Təhsil Portalı",
    hero_title:
      "AZƏRBAYCAN RESPUBLİKASI ELM VƏ TƏHSİL NAZİRLİYİ<br>ELM VƏ ALİ TƏHSİL ÜZRƏ DÖVLƏT AGENTLİYİ<br>AZƏRBAYCAN TEXNİKİ UNİVERSİTETİNİN NƏZDİNDƏ<br>BAKI DÖVLƏT RABİTƏ VƏ NƏQLİYYAT KOLLECİ<br>PUBLİK HÜQUQİ ŞƏXSİ",
    hero_desc:
      "Gələcəyin rabitə və nəqliyyat mütəxəssislərini yetişdirən müasir təhsil mərkəzi.",
    hero_cta_portal: "Tələbə Portalı",
    hero_cta_about: "Haqqımızda",
    stat_students: "Tələbə",
    stat_teachers: "Müəllim",
    stat_staff: "Digər işçilər",
    stat_years: "İl Təcrübə",

    about_badge: "Missiyamız",
    about_title: "Haqqımızda",
    about_p1_title: "Gələcəyin Mütəxəssisləri",
    about_p1:
      "Bakı Dövlət Rabitə və Nəqliyyat Kolleci Azərbaycanda orta ixtisas təhsili pilləsi üzrə fəaliyyət göstərən ən qocaman və zəngin ənənələrə malik təhsil müəssisələrindən biridir.",
    about_history_title: "Tarixi",
    about_history_text: "Kollecin əsası 1931-ci ildə mərkəzi teleqrafın nəzdində fabrik-zavod təhsili bazasında təşkil olunmuşdur. Sonradan keçmiş SSRİ Rabitə Nazirliyinin 157 saylı 02.04.1991-ci il tarixli əmrinə əsasən Bakı Rabitə Kolleci yaradılmışdır. Bakı Rabitə Kolleci və Bakı Dəmiryolu Texnikumu Azərbaycan Respublikasının Nazirlər Kabinetinin 26 avqust 2002-ci il 140 saylı və Azərbaycan Respublikasının Təhsil Nazirliyinin 786 saylı əmrlərinə əsasən birləşdirilərək Bakı Rabitə Kollecinin bazasında Bakı Dövlət Rabitə və Nəqliyyat Kolleci yaradılmışdır.",
    about_p2:
      "Hazırda kollecdə tədris prosesi müasir beynəlxalq standartlara uyğun, rəqəmsal texnologiyalar və praktiki təcrübə əsasında qurulmuşdur. Tələbələrimiz ən son laboratoriya avadanlıqları ilə təchiz olunmuş mühitdə gələcəyin peşəkarı gibi yetişirlər.",
    feature1_title: "Müasir Tədris",
    feature1_desc: "Beynəlxalq standartlara uyğun tədris proqramları",
    feature2_title: "Rəqəmsal Laboratoriya",
    feature2_desc: "Son texnologiya ilə təchiz olunmuş laboratoriyalar",
    feature3_title: "Tədbirlər",
    feature3_desc: "Kollecdə baş tutan ən son tədbirlər və yeniliklər",
    structure_badge: "Təşkilat",
    structure_title: "İnstitusional Struktur",
    structure_desc:
      "Rəhbərlik, İnzibati İdarə Heyəti və İxtisaslar bir baxışda.",
    cat_leadership: "Rəhbərlik",
    cat_leadership_sub: "Direktor və müavinlər",
    cat_departments: "İnzibati İdarə Heyəti",
    cat_departments_sub: "Rəhbər heyət və idarəçilər",
    cat_majors: "İxtisaslar",
    cat_majors_sub: "Tədris olunan ixtisaslar",
    th_code: "Kod",
    th_major: "İxtisasın Adı",
    th_field: "Sahə",
    library_badge: "Resurslar",
    library_title: "Elektron Kitabxana",
    library_desc: "Müəllimlərimizin dərs vəsaitləri və metodik materialları",
    filter_all: "Hamısı",
    filter_comm: "Rabitə",
    filter_transport: "Nəqliyyat",
    filter_it: "İT",
    library_search_placeholder: "Kitab axtar...",
    lectures_badge: "Video",
    lectures_title: "Videodərslər",
    lectures_desc:
      "Müəllimlərimizin hazırladığı video dərslər və tədris materialları.",
    sis_badge: "Portal",
    sis_title: "Tələbə Məlumat Sistemi",
    sis_desc:
      "İmtahan nəticələri, davamiyyət və performans göstəricilərini izləyin.",
    sis_login_title: "Daxil olun",
    sis_login_hint: "Tələbə ID nömrənizi daxil edin",
    sis_login_btn: "Daxil ol",
    sis_error: "Tələbə tapılmadı. Zəhmət olmasa ID-ni düzgün daxil edin.",
    sis_demo_hint: "Demo: STU001, STU002, STU003",
    sis_logout: "Çıxış",
    dash_gpa: "GPA",
    dash_attendance: "Davamiyyət",
    dash_rank: "Sıralama",
    dash_exam_title: "İmtahan Nəticələri",
    exam_subject: "Fənn",
    exam_score: "Bal",
    exam_grade: "Qiymət",
    dash_attend_title: "Aylıq Davamiyyət",
    contact_badge: "Əlaqə",
    contact_title: "Bizimlə Əlaqə",
    cf_name: "Ad və Soyad",
    cf_email: "E-poçt",
    cf_message: "Mesaj",
    cf_send: "Göndər",
    cf_success: "Mesajınız göndərildi!",
    marquee1: "📢 2025/2026 tədris ili üçün qəbul elan olunub!",
    marquee2: "🏆 Tələbələrimiz respublika olimpiadasında 1-ci yeri qazandı!",
    marquee3: "📚 Yeni elektron kitabxana xidməti istifadəyə verildi.",
    marquee4: "🎓 Məzunlarımızın 92%-i ilk il ərzində iş tapır.",
    marquee5: "🏢 Müasir Tədris Metodları",
    marquee6: "👨‍🏫 Təcrübəli Heyət",

    marquee8: "💎 95+ İl Təcrübə",
    marquee9: "📸 Instagram: @bdrnk__official",
    marquee10: "👥 Facebook: bdrnk.official",
    footer_desc:
      "Bakı Dövlət Rabitə və Nəqliyyat Kolleci — gələcəyin mütəxəssislərini yetişdiririk.",
    footer_quick: "Sürətli Keçidlər",
    footer_contact: "Əlaqə",
    dash_greeting: "Tədris Hesabatı",
    dash_group_prefix: "Qrup",
    sem1: "1-ci Semestr",
    sem2: "2-ci Semestr",
    th_n: "N",
    th_name: "Ad və Soyad",
    th_attendance: "Davamiyyət",
    th_exam: "İmtahan",
    th_final: "Yekun",
    th_grade: "Qiymət",
    grade_excellent: "Əla",
    grade_good: "Yaxşı",
    grade_satisfactory: "Kafi",
    grade_fail: "Qeyri-kafi",
    no_video: "Bu bölmədə hələlik video yoxdur.",
    no_book: "Təəssüf ki, nəticə tapılmadı.",
    btn_read: "Oxu",
    filter_informatika: "İnformatika",
    filter_tarix: "Tarix",
    filter_edebiyyat: "Ədəbiyyat",
    filter_huquq: "Hüquq",
    filter_azer_dili: "Azərbaycan dili və ədəbiyyat",
    filter_vaqonlar: "Vaqonların konstruksiyası",
    filter_riyaziyyat: "Riyaziyyat",
    filter_sxematexnika: "Sxematexnika",
    filter_materialsunasliq: "Materialşünaslıq",
    filter_rus_dili: "Rus dili",
    filter_anbar_logistikasi: "Anbar logistikası",
    filter_xarici_dil: "Xarici dil",
    filter_ekologiya: "Ekologiya",
    filter_fizika: "Fizika",
    filter_edne: "EDNƏ",
    filter_menecment: "Menecment",
    filter_rabite: "Rabitə",
    filter_sebeke_avadanliqlari: "Şəbəkə avadanlıqları",
    filter_emeyin_muhafizesi: "Əməyin mühafizəsi",
    filter_os: "Əməliyyat sistemləri",
    subj_tpt: "TPT",
    subj_os: "Əməliyyat sistemləri",
    subj_informatika: "İnformatika",
    subj_network: "Şəbəkə texnologiyaları",
    subj_architecture: "Kompüter arxitekturası",
    subj_database: "Verilənlər bazası",
    subj_math: "Riyaziyyat",
    subj_physics: "Fizika",
    fame_badge: "Uğurlarımız",
    fame_title: "Uğur Hekayələri",
    fame_desc: "Kollecimizin qürur mənbəyi olan tələbələrimiz və məzunlarımız.",
    calendar_badge: "Təqvim",
    calendar_title: "Akademik Təqvim",
    faq_badge: "Məlumat",
    faq_title: "Tez-tez verilən suallar",
    eyani: "Əyani",
    qiyabi: "Qiyabi",
    nav_gallery: "Qalereya",
    nav_news: "Xəbərlər",
    news_badge: "Yeniliklər",
    news_title: "Son Xəbərlər",
    news_desc: "Kollecimizdə baş verən ən son yeniliklər, elanlar və nailiyyətlər bir arada.",
    news_all: "Bütün Xəbərlər",
    news_read_more: "Ətraflı oxu →",
    gallery_badge: "Foto",
    gallery_title: "Qalereya",
    gallery_desc: "Kollecimizin müxtəlif anlarından seçilmiş fotoşəkillər.",
    gallery_cat_exam: "İmtahan Mühiti",
    gallery_cat_events: "Tədbirlər",
    gallery_cat_rooms: "Auditoriyalar",
    gallery_cat_study: "Dərs Mühiti",
    gallery_all: "Hamısı",
    gallery_view: "Böyüt",
    gallery_event_reel: "Kollec Tədbiri",
    gallery_exam_moment: "İmtahan Anı",
    roadmap_badge: "Bələdçi",
    roadmap_title: "Tələbənin Yol Xəritəsi",
    roadmap_desc: "Qəbuldan ilk dərs gününə qədər keçəcəyiniz addım-addım bələdçi.",
    roadmap_step1_title: "İxtisas Seçimi",
    roadmap_step1_desc: "DİM tərəfindən keçirilən imtahanlarda iştirak və kollecimizə ixtisas seçimi.",
    roadmap_step2_title: "Elektron Qeydiyyat",
    roadmap_step2_desc: "Portal.edu.az vasitəsilə onlayn qeydiyyatdan keçmək və təsdiq almaq.",
    roadmap_step3_title: "Sənəd Təqdimi",
    roadmap_step3_desc: "Tələb olunan sənədlərin (atestat, foto, tibbi arayış) kollecə təqdim edilməsi.",
    roadmap_step4_title: "Tanışlıq Günü",
    roadmap_step4_desc: "Kollec korpusları, auditoriyalar və müəllim heyəti ilə yaxından tanışlıq.",
    roadmap_step5_title: "İlk Dərs Günü",
    roadmap_step5_desc: "Tələbə biletinin alınması və dərslərin rəsmi olaraq başlanması!",
    entry_candidate_title: "Qəbul Portalı",
    entry_candidate_desc: "İxtisaslar, qəbul qaydaları və kollec həyatı ilə tanış olun.",
    entry_student_title: "Tələbə Portalı",
    entry_student_desc: "Dərs cədvəli, imtahan nəticələri və tələbə kabineti.",
    entry_btn: "Daxil ol",
    capsule_badge: "Zaman Kapsulu",
    capsule_title: "Gələcəyə Məktub",
    capsule_desc: "Gələcək kollec tələbələrinə öz arzularınızı və ismarıcınızı göndərin.",
    capsule_send: "Göndər",
    capsule_error: "Zəhmət olmasa nalayiq sözlərdən istifadə etməyin!",
    cm_theme: "Açıq / Tünd Rejim",
    cm_portal: "Tələbə Portalı",
    cm_totop: "Yuxarı Qayıt",
    footer_copyright:
      "© 2026 BDRNK - Müəllif hüquqları qorunur. Hazırlayan: Ləman Əskərova",
  },
  en: {
    fame_badge: "Our Success",
    fame_title: "Wall of Fame",
    fame_desc: "The pride of our college — students and alumni who inspire us.",
    calendar_badge: "Calendar",
    calendar_title: "Academic Calendar",
    header_subtitle: "Baku State Communications and Transport College",
    nav_home: "Home",
    nav_about: "About Us",
    nav_structure: "Structure",
    nav_library: "Library",
    nav_lectures: "Lectures",
    nav_sis: "Student Portal",
    nav_contact: "Contact",
    nav_register: "Registration",
    hero_badge: "Official Educational Portal",
    hero_title:
      "MINISTRY OF SCIENCE AND EDUCATION OF THE REPUBLIC OF AZERBAIJAN<br>STATE AGENCY FOR SCIENCE AND HIGHER EDUCATION<br>UNDER AZERBAIJAN TECHNICAL UNIVERSITY<br>BAKU STATE COMMUNICATIONS AND TRANSPORT COLLEGE<br>PUBLIC LEGAL ENTITY",
    hero_desc:
      "A modern educational center training future experts in communications and transport.",
    hero_cta_portal: "Student Portal",
    hero_cta_about: "About Us",
    stat_students: "Students",
    stat_teachers: "Teachers",
    stat_staff: "Other staff",
    stat_years: "Years Exp.",

    about_badge: "Our Mission",
    about_title: "About Us",
    about_p1_title: "Specialists of the Future",
    about_p1:
      "Baku State Communications and Transport College is one of the oldest and most tradition-rich educational institutions in Azerbaijan.",
    about_history_title: "History",
    about_history_text: "The college was founded in 1931 on the basis of factory-plant education under the Central Telegraph. Later, Baku Communications College was established by order No. 157 dated 02.04.1991 of the Ministry of Communications of the former USSR. On August 26, 2002, by Decree No. 140 of the Cabinet of Ministers and Order No. 786 of the Ministry of Education, Baku Communications College and Baku Railway Technical School were merged to form Baku State Communications and Transport College.",
    about_p2:
      "Currently, the educational process in the college is built according to modern international standards, based on digital technologies and practical experience. Our students grow as future professionals in an environment equipped with the latest laboratory equipment.",
    feature1_title: "Modern Education",
    feature1_desc: "Curricula aligned with international standards",
    feature2_title: "Digital Laboratories",
    feature2_desc: "Fully equipped with the latest tech",
    feature3_title: "Events",
    feature3_desc: "Latest events, seminars, and college news",
    structure_badge: "Organization",
    structure_title: "Institutional Structure",
    structure_desc:
      "Leadership, Administration and Majors at a glance.",
    cat_leadership: "Leadership",
    cat_leadership_sub: "Director and deputies",
    cat_departments: "Administrative Management",
    cat_departments_sub: "Leadership and administration",
    cat_majors: "Majors",
    cat_majors_sub: "Offered Specialties",
    th_code: "Code",
    th_major: "Specialty Name",
    th_field: "Field",
    library_badge: "Resources",
    library_title: "Digital Library",
    library_desc: "Textbooks and methodical materials from our teachers.",
    filter_all: "All",
    filter_comm: "Communications",
    filter_transport: "Transport",
    filter_it: "IT",
    library_search_placeholder: "Search books...",
    lectures_badge: "Video",
    lectures_title: "Video Lectures",
    lectures_desc:
      "Video lessons and educational materials prepared by our teachers.",
    sis_badge: "Portal",
    sis_title: "Student Information System",
    sis_desc: "Track exam results, attendance, and performance metrics.",
    sis_login_title: "Sign In",
    sis_login_hint: "Enter your Student ID",
    sis_login_btn: "Login",
    sis_error: "Student not found. Please check your ID.",
    sis_demo_hint: "Demo: STU001, STU002, STU003",
    sis_logout: "Logout",
    dash_gpa: "GPA",
    dash_attendance: "Attendance",
    dash_rank: "Rank",
    dash_exam_title: "Exam Results",
    exam_subject: "Subject",
    exam_score: "Score",
    exam_grade: "Grade",
    dash_attend_title: "Monthly Attendance",
    contact_badge: "Contact",
    contact_title: "Contact Us",
    cf_name: "Full Name",
    cf_email: "Email",
    cf_message: "Message",
    cf_send: "Send",
    cf_success: "Message sent successfully!",
    marquee1: "📢 Admissions open for the 2025/2026 academic year!",
    marquee2: "🏆 Our students won 1st place in the national olympiad!",
    marquee3: "📚 The new digital library service is now live.",
    marquee4: "🎓 92% of our graduates find a job within the first year.",
    marquee5: "🏢 Modern Teaching Methods",
    marquee6: "👨‍🏫 Experienced Staff",

    marquee8: "💎 95+ Years of Experience",
    marquee9: "📸 Instagram: @bdrnk__official",
    marquee10: "👥 Facebook: bdrnk.official",
    footer_desc:
      "Baku State Communications and Transport College — raising tomorrow's experts.",
    footer_quick: "Quick Links",
    footer_contact: "Contact",
    dash_greeting: "Academic Report",
    dash_group_prefix: "Group",
    sem1: "1st Semester",
    sem2: "2nd Semester",
    th_n: "N",
    th_name: "Full Name",
    th_attendance: "Attendance",
    th_exam: "Exam",
    th_final: "Final",
    th_grade: "Grade",
    grade_excellent: "Excellent",
    grade_good: "Good",
    grade_satisfactory: "Satisfactory",
    grade_fail: "Fail",
    no_video: "No videos available in this section yet.",
    no_book: "Sorry, no results found.",
    btn_read: "Read",
    filter_informatika: "Informatics",
    filter_tarix: "History",
    filter_edebiyyat: "Literature",
    filter_huquq: "Law",
    filter_azer_dili: "Azerbaijani Language and Literature",
    filter_vaqonlar: "Wagon Construction",
    filter_riyaziyyat: "Mathematics",
    filter_sxematexnika: "Schematics",
    filter_materialsunasliq: "Material Science",
    filter_rus_dili: "Russian Language",
    filter_anbar_logistikasi: "Warehouse Logistics",
    filter_xarici_dil: "Foreign Language",
    filter_ekologiya: "Ecology",
    filter_fizika: "Physics",
    filter_edne: "EDNA",
    filter_menecment: "Management",
    filter_rabite: "Communication",
    filter_sebeke_avadanliqlari: "Network Equipment",
    filter_emeyin_muhafizesi: "Labor Protection",
    filter_os: "Operating Systems",
    subj_tpt: "TPT",
    subj_os: "Operating Systems",
    subj_informatika: "Informatics",
    subj_network: "Network Technologies",
    subj_architecture: "Computer Architecture",
    subj_database: "Database",
    subj_math: "Mathematics",
    subj_physics: "Physics",
    faq_badge: "Information",
    faq_title: "Frequently Asked Questions",
    eyani: "Full-time",
    qiyabi: "Part-time",
    nav_gallery: "Gallery",
    nav_news: "News",
    news_badge: "Updates",
    news_title: "Latest News",
    news_desc: "The latest updates, announcements and achievements at our college.",
    news_all: "All News",
    news_read_more: "Read more →",
    gallery_badge: "Photos",
    gallery_title: "Gallery",
    gallery_desc: "A selection of moments captured across our college campus.",
    gallery_cat_exam: "Exam Environment",
    gallery_cat_events: "Events",
    gallery_cat_rooms: "Classrooms",
    gallery_cat_study: "Study Environment",
    gallery_all: "All",
    gallery_view: "Enlarge",
    gallery_event_reel: "College Event",
    gallery_exam_moment: "Exam Moment",
    roadmap_badge: "Guide",
    roadmap_title: "Student Roadmap",
    roadmap_desc: "A step-by-step guide from admission to your first day of class.",
    roadmap_step1_title: "Major Selection",
    roadmap_step1_desc: "Participation in SEC exams and choosing our college majors.",
    roadmap_step2_title: "Electronic Registration",
    roadmap_step2_desc: "Online registration and confirmation via Portal.edu.az.",
    roadmap_step3_title: "Document Submission",
    roadmap_step3_desc: "Submission of required documents (diploma, photo, medical certificate) to the college.",
    roadmap_step4_title: "Orientation Day",
    roadmap_step4_desc: "Getting to know college buildings, classrooms, and faculty.",
    roadmap_step5_title: "First Day of Class",
    roadmap_step5_desc: "Getting your student ID and officially starting your studies!",
    entry_candidate_title: "Admission Portal",
    entry_candidate_desc: "Learn about majors, requirements and college life.",
    entry_student_title: "Student Portal",
    entry_student_desc: "Access schedules, exam results and student records.",
    entry_btn: "Enter",
    capsule_badge: "Time Capsule",
    capsule_title: "Letter to the Future",
    capsule_desc: "Send your wishes and messages to future college students.",
    capsule_send: "Send",
    capsule_error: "Please do not use inappropriate language!",
    cm_theme: "Light / Dark Mode",
    cm_portal: "Student Portal",
    cm_totop: "Back to Top",
    footer_copyright: "© 2026 BDRNK - All rights reserved. Created by: Ləman Əskərova",
  },
  ru: {
    header_subtitle: "Бакинский Государственный Колледж Связи и Транспорта",
    nav_home: "Главная",
    nav_about: "О нас",
    nav_structure: "Структура",
    nav_library: "Библиотека",
    nav_lectures: "Видеоуроки",
    nav_sis: "Студенческий Портал",
    nav_contact: "Контакты",
    nav_register: "Регистрация",
    hero_badge: "Официальный Портал",
    hero_title:
      "МИНИСТЕРСТВО НАУКИ И ОБРАЗОВАНИЯ АЗЕРБАЙДЖАНСКОЙ РЕСПУБЛИКИ<br>ГОСУДАРСТВЕННОЕ АГЕНТСТВО ПО НАУКЕ И ВЫСШЕМУ ОБРАЗОВАНИЮ<br>ПРИ АЗЕРБАЙДЖАНСКОМ ТЕХНИЧЕСКОМ УНИВЕРСИТЕТЕ<br>БАКИНСКИЙ ГОСУДАРСТВЕННЫЙ КОЛЛЕДЖ СВЯЗИ И ТРАНСПОРТА<br>ПУБЛИЧНОЕ ЮРИДИЧЕСКОЕ ЛИЦО",
    hero_desc:
      "Современный центр, готовящий специалистов будущего в области связи и транспорта.",
    hero_cta_portal: "Портал Студента",
    hero_cta_about: "О нас",
    stat_students: "Студентов",
    stat_teachers: "Учителей",
    stat_staff: "Другие сотрудники",
    stat_years: "Лет Опыта",


    about_badge: "Наша Миссия",
    about_title: "О нас",
    about_p1_title: "Специалисты Будущего",
    about_p1:
      "Бакинский государственный колледж связи и транспорта является одним из старейших учебных заведений Азербайджана с богатыми традициями.",
    about_history_title: "История",
    about_history_text: "Колледж был основан в 1931 году на базе фабрично-заводского обучения при Центральном телеграфе. Позже Бакинский колледж связи был создан приказом № 157 от 02.04.1991 года Министерства связи бывшего СССР. 26 августа 2002 года постановлением Кабинета Министров № 140 и приказом Министерства образования № 786 Бакинский колледж связи и Бакинский железнодорожный техникум были объединены в Бакинский государственный колледж связи и транспорта.",
    about_p2:
      "В настоящее время учебный процесс в колледже построен в соответствии с современными международными стандартами, на основе цифровых технологий и практического опыта. Нашим студентам созданы все условия для становления профессионалами будущего в среде, оснащенной новейшим лабораторным оборудованием.",
    feature1_title: "Современное Обучение",
    feature1_desc: "Программы по международным стандартам",
    feature2_title: "Цифровая Лаборатория",
    feature2_desc: "Оборудование по последнему слову техники",
    feature3_title: "Мероприятия",
    feature3_desc: "Последние события, семинары и новости колледжа",
    structure_badge: "Организация",
    structure_title: "Институциональная Структура",
    structure_desc: "Руководство, начальники отделов и председатели комиссий.",
    cat_leadership: "Руководство",
    cat_leadership_sub: "Директор и заместители",
    cat_departments: "Административное руководство",
    cat_departments_sub: "Руководство и администрация",
    cat_majors: "Специальности",
    cat_majors_sub: "Предлагаемые специальности",
    th_code: "Код",
    th_major: "Название специальности",
    th_field: "Сфера",
    library_badge: "Ресурсы",
    library_title: "Электронная Библиотека",
    library_desc: "Учебные пособия и методические материалы наших преподавателей.",
    filter_all: "Все",
    filter_comm: "Связь",
    filter_transport: "Транспорт",
    filter_it: "ИТ",
    library_search_placeholder: "Поиск книг...",
    lectures_badge: "Видео",
    lectures_title: "Видеоуроки",
    lectures_desc: "Видеоуроки и материалы, подготовленные нашими учителями.",
    sis_badge: "Портал",
    sis_title: "Студенческая Информ. Система",
    sis_desc: "Оценки, посещаемость и показатели успеваемости.",
    sis_login_title: "Войти",
    sis_login_hint: "Введите ваш студенческий ID",
    sis_login_btn: "Войти",
    sis_error: "Студент не найден. Проверьте ваш ID.",
    sis_demo_hint: "Демо: STU001, STU002, STU003",
    sis_logout: "Выйти",
    dash_gpa: "GPA",
    dash_attendance: "Посещаемость",
    dash_rank: "Рейтинг",
    dash_exam_title: "Результаты Экзаменов",
    exam_subject: "Предмет",
    exam_score: "Балл",
    exam_grade: "Оценка",
    dash_attend_title: "Посещаемость за Месяц",
    contact_badge: "Контакты",
    contact_title: "Свяжитесь с нами",
    cf_name: "Имя Фамилия",
    cf_email: "E-mail",
    cf_message: "Сообщение",
    cf_send: "Отправить",
    cf_success: "Сообщение отправлено!",
    marquee1: "📢 Открыт прием на 2025/2026 учебный год!",
    marquee2: "🏆 Наши студенты заняли 1-е место на олимпиаде!",
    marquee3: "📚 Запущена новая электронная библиотека.",
    marquee4: "🎓 92% выпускников находят работу в первый год.",
    marquee5: "🏢 Современные Методы Обучения",
    marquee6: "👨‍🏫 Опытный Персонал",

    marquee8: "💎 95+ года опыта",
    marquee9: "📸 Instagram: @bdrnk__official",
    marquee10: "👥 Facebook: bdrnk.official",
    footer_desc:
      "Бакинский Государственный Колледж Связи и Транспорта — растим специалистов будущего.",
    footer_quick: "Быстрые Ссылки",
    footer_contact: "Контакты",
    dash_greeting: "Учебный Отчёт",
    dash_group_prefix: "Группа",
    sem1: "1-й Семестр",
    sem2: "2-й Семестр",
    th_n: "N",
    th_name: "Имя и Фамилия",
    th_attendance: "Посещаемость",
    th_exam: "Экзамен",
    th_final: "Итого",
    th_grade: "Оценка",
    grade_excellent: "Отлично",
    grade_good: "Хорошо",
    grade_satisfactory: "Удовл.",
    grade_fail: "Неуд.",
    no_video: "В этом разделе пока нет видео.",
    no_book: "К сожалению, ничего не найдено.",
    btn_read: "Читать",
    filter_informatika: "Информатика",
    filter_tarix: "История",
    filter_edebiyyat: "Литература",
    filter_huquq: "Право",
    filter_azer_dili: "Азербайджанский язык и литература",
    filter_vaqonlar: "Конструкция вагонов",
    filter_riyaziyyat: "Математика",
    filter_sxematexnika: "Схемотехника",
    filter_materialsunasliq: "Материаловедение",
    filter_rus_dili: "Русский язык",
    filter_anbar_logistikasi: "Складская логистика",
    filter_xarici_dil: "Иностранный язык",
    filter_ekologiya: "Экология",
    filter_fizika: "Физика",
    filter_edne: "ЭДНА",
    filter_menecment: "Менеджмент",
    filter_rabite: "Связь",
    filter_sebeke_avadanliqlari: "Сетевое оборудование",
    filter_emeyin_muhafizesi: "Охрана труда",
    filter_os: "Операционные системы",
    subj_tpt: "ТПТ",
    subj_os: "Операционные системы",
    subj_informatika: "Информатика",
    subj_network: "Сетевые технологии",
    subj_architecture: "Архитектура компьютера",
    subj_database: "Базы данных",
    subj_math: "Математика",
    subj_physics: "Физика",
    fame_badge: "Наши Успехи",
    fame_title: "История Успеха",
    fame_desc: "Студенты и выпускники, которыми гордится наш колледж.",
    calendar_badge: "Календарь",
    calendar_title: "Академический календарь",
    faq_badge: "Информация",
    faq_title: "Часто задаваемые вопросы",
    eyani: "Очное",
    qiyabi: "Заочное",
    nav_gallery: "Галерея",
    nav_news: "Новости",
    news_badge: "Обновления",
    news_title: "Последние Новости",
    news_desc: "Последние обновления, объявления и достижения нашего колледжа.",
    news_all: "Все Новости",
    news_read_more: "Подробнее →",
    gallery_badge: "Фото",
    gallery_title: "Галерея",
    gallery_desc: "Избранные моменты из жизни нашего колледжа.",
    gallery_cat_exam: "Среда Экзаменов",
    gallery_cat_events: "Мероприятия",
    gallery_cat_rooms: "Аудитории",
    gallery_cat_study: "Учебная Среда",
    gallery_all: "Все",
    gallery_view: "Увеличить",
    gallery_event_reel: "Мероприятие Колледжа",
    gallery_exam_moment: "Момент Экзамена",
    roadmap_badge: "Путеводитель",
    roadmap_title: "Дорожная карта студента",
    roadmap_desc: "Пошаговое руководство от поступления до первого учебного дня.",
    roadmap_step1_title: "Выбор специальности",
    roadmap_step1_desc: "Участие в экзаменах ГЭЦ и выбор специальностей нашего колледжа.",
    roadmap_step2_title: "Электронная регистрация",
    roadmap_step2_desc: "Онлайн-регистрация и подтверждение через Portal.edu.az.",
    roadmap_step3_title: "Подача документов",
    roadmap_step3_desc: "Подача необходимых документов (аттестат, фото, медсправка) в колледж.",
    roadmap_step4_title: "День знакомства",
    roadmap_step4_desc: "Знакомство с корпусами колледжа, аудиториями и преподавателями.",
    roadmap_step5_title: "Первый учебный день",
    roadmap_step5_desc: "Получение студенческого билета и официальное начало занятий!",
    entry_candidate_title: "Приемная комиссия",
    entry_candidate_desc: "Ознакомьтесь с специальностями и правилами приема.",
    entry_student_title: "Студенческий портал",
    entry_student_desc: "Расписание занятий, результаты экзаменов и профиль.",
    entry_btn: "Войти",
    capsule_badge: "Капсула Времени",
    capsule_title: "Письмо в Будущее",
    capsule_desc: "Отправьте свои пожелания и сообщения будущим студентам колледжа.",
    capsule_send: "Отправить",
    capsule_error: "Пожалуйста, не используйте ненормативную лексику!",
    cm_theme: "Светлая / Темная Тема",
    cm_portal: "Студенческий Портал",
    cm_totop: "Наверх",
    footer_copyright: "© 2026 BDRNK - Все права защищены. Разработчик: Ləman Əskərova",
  },
};

let currentLang = "az";

function gT(key) {
  return i18n[currentLang][key] || key;
}

function updateDOMTexts() {
  // Basic innerHTML translations
  document.querySelectorAll("[data-i18n]").forEach((el) => {
    const key = el.getAttribute("data-i18n");
    if (i18n[currentLang][key]) {
      el.innerHTML = i18n[currentLang][key];
    }
  });

  // Placeholder translations
  document.querySelectorAll("[data-i18n-placeholder]").forEach((el) => {
    const key = el.getAttribute("data-i18n-placeholder");
    if (i18n[currentLang][key]) {
      el.placeholder = i18n[currentLang][key];
    }
  });

  // Categories Sub-labels update explicitly (since they generated dynamically later sometimes)
  renderCategoriesCount();

  // Rerender active module texts
  const sisDash = document.getElementById("sis-dashboard");
  if (
    sisDash &&
    sisDash.style.display === "block" &&
    typeof currentGroup !== "undefined" &&
    currentGroup
  ) {
    renderGroupDashboard(currentGroup, activeSemester, activeSubject);
  }
}

/**
 * 2. CORE DATA MODULES (Mocking DB)
 * Institutional Structure
 */
const staffData = {
  leadership: [
    {
      id: "1",
      name_az: "Səbuhi Qurbanov Yusif oğlu",
      name_en: "Sabuhi Gurbanov Yusif",
      name_ru: "Сабухи Гурбанов Юсиф оглы",
      role_az: "Direktor<br>Tədris işləri üzrə direktor müavini",
      role_en: "Director<br>Vice-Director for Academic Affairs",
      role_ru: "Директор<br>Заместитель директора по учебной работе",
      img: "sebuhi1.png",
    },
    {
      id: "2",
      name_az: "Şahmurad Məmmədov Zöhtün oğlu",
      name_en: "Shahmurad Mammadov Zohtun",
      name_ru: "Шахмурад Мамедов Зехтюн оглы",
      role_az: "Tərbiyə işləri üzrə direktor müavini",
      role_en: "Vice-Director for Educational Affairs",
      role_ru: "Заместитель директора по воспитательной работе",
      img: "sahmurad2.png",
    },
    {
      id: "3",
      name_az: "İsmayıl Səfiyev Allahverdi oğlu",
      name_en: "Ismayil Safiyev Allahverdi",
      name_ru: "Исмаил Сафиев Аллахверди оглы",
      role_az: "Inzibati təsərüffat işləri üzrə direktor müavini",
      role_en: "Deputy Director for Administrative & Economic Affairs",
      role_ru: "Заместитель директора по административно-хозяйственной части",
      img: "ismayil4.png",
    },
  ],
  departments: [
    {
      id: "7",
      name_az: "Babək Əhmədli Yasin oğlu",
      name_en: "Babak Ahmadli Yasin",
      name_ru: "Бабек Ахмедли Ясин оглы",
      role_az: '"Telekommunikasiya şöbəsi"-Şöbə müdiri',
      role_en: 'Head of "Telecommunications" Dept',
      role_ru: 'Заведующая отделом "Телекоммуникации"',
      img: "babekson.jpeg",
    },
    {
      id: "9",
      name_az: "Səkinə Mayılova Oruc qızı",
      name_en: "Sakina Mayilova Oruj",
      name_ru: "Сакина Маилова Орудж гызы",
      role_az: '"Kompüter texnologiyaları şöbəsi"-Şöbə müdiri',
      role_en: 'Head of "Computer Technologies" Dept',
      role_ru: 'Заведующая отделом "Компьютерные технологии"',
      img: "sekine.jpeg",
    },
    {
      id: "11",
      name_az: "Ceyhun Cəfərov Müzəffər oğlu",
      name_en: "Jeyhun Jafarov Muzaffar",
      name_ru: "Джейхун Джафаров Музаффар оглы",
      role_az: '"Qiyabi şöbəsi"-Şöbə müdiri',
      role_en: 'Head of "Correspondence" Dept',
      role_ru: 'Заведующий "Заочным отделом"',
      img: "ceyhunson.jpg",
    },
    {
      id: "12",
      name_az: "Fizuli Qurbanov Şahmərdan oğlu",
      name_en: "Fizuli Gurbanov Shahmardan",
      name_ru: "Физули Гурбанов Шахмардан оглы",
      role_az: '"Qeydiyyat Qiymətləndirmə və Manitorinq Şöbəsi"-Şöbə müdiri',
      role_en: 'Head of "Registration, Evaluation and Monitoring" Dept',
      role_ru: 'Заведующий отделом "Регистрации, оценки и мониторинга"',
      img: "fizulison.png",
    },
    {
      id: "14",
      name_az: "Rəsmiyyə Həsənova Kamil qızı",
      name_en: "Rasmiyya Hasanova Kamil",
      name_ru: "Расмия Гасанова Камиль гызы",
      role_az: '"İnformasiya, kommunikasiya texnologiyaları şöbəsi"-Şöbə müdiri',
      role_en: 'Head of "Information and Communication Technologies" Dept',
      role_ru: 'Заведующая отделом "Информационных и коммуникационных технологий"',
      img: "resmiyyeson.png",
    },
    {
      id: "16",
      name_az: "Vəfa Hacıyeva Nizami qızı",
      name_en: "Vafa Hajiyeva Nizami",
      name_ru: "Вафа Гаджиева Низами гызы",
      role_az: "Hüquqşünas",
      role_en: "Legal Counsel",
      role_ru: "Юрист",
      img: "vefason.jpeg",
    },
    {
      id: "18",
      name_az: "Günay Əliyeva Zahid qızı",
      name_en: "Gunay Aliyeva Zahid",
      name_ru: "Гюнай Алиева Захид гызы",
      role_az: "Arxiv müdiri",
      role_en: "Head of Archive",
      role_ru: "Заведующая архивом",
      img: "gunayson.png",
    },
    {
      id: "22",
      name_az: "Aynur Qəniyeva Əliheydər qızı",
      name_en: "Aynur Ganiyeva Aliheydar",
      name_ru: "Айнур Ганиева Алигейдар гызы",
      role_az: "Kitabxana müdiri",
      role_en: "Head of Library",
      role_ru: "Заведующая библиотекой",
      img: "aynurson.jpeg",
    },
    {
      id: "20",
      name_az: "Ləman Ağalıyeva Həsən qızı",
      name_en: "Laman Agahaliyeva Hasan",
      name_ru: "Ляман Агазаде Гасан гызы",
      role_az: "Kadrlar üzrə mütəxəssis",
      role_en: "HR Specialist",
      role_ru: "Специалист по кадрам",
      img: "lemanson.jpg",
    },
    {
      id: "19",
      name_az: "Azər Rəhimov Tofiq oğlu",
      name_en: "Azer Rahimov Tofig",
      name_ru: "Азер Рагимов Тофиг оглы",
      role_az: "Baş mühasib",
      role_en: "Chief Accountant",
      role_ru: "Главный бухгалтер",
      img: "azerson.jpeg",
    },
    {
      id: "13",
      name_az: "Xəlil Süleymanov Süleyman oğlu",
      name_en: "Khalil Suleymanov Suleyman",
      name_ru: "Халил Сулейманов Сулейман оглы",
      role_az: "İstehsalat təcrübə rəhbəri",
      role_en: "Production Internship Supervisor",
      role_ru: "Руководитель производственной практики",
      img: "xelilson.jpeg",
    },
  ],
  commissions: [
    {
      id: "17",
      name_az: "Pənah Daşdəmirov",
      name_en: "Panah Dashdamirov",
      name_ru: "Панах Дашдамиров",
      role_az: "Mülki-müdafiə üzrə mühəndis",
      role_en: "Civil Defense Engineer",
      role_ru: "Инженер по гражданской обороне",
      img: "logo.jpg",
    },
  ],
  majors: {
    eyani: [
      {
        code: "040406",
        name_az: "Mühasibat uçotu",
        name_en: "Accounting",
        name_ru: "Бухгалтерский учет",
        field_az: "İqtisadiyyat",
        field_en: "Economics",
        field_ru: "Экономика",
      },
      {
        code: "040554",
        name_az: "Poçt rabitəsi",
        name_en: "Postal Communication",
        name_ru: "Почтовая связь",
        field_az: "Rabitə",
        field_en: "Communication",
        field_ru: "Связь",
      },
      {
        code: "040556",
        name_az: "Radio, televiziya vasitə və qurğuları",
        name_en: "Radio, TV Tools and Equipment",
        name_ru: "Радио, ТВ средства и оборудование",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040405",
        name_az: "Marketinq (sahələr üzrə)",
        name_en: "Marketing (by sectors)",
        name_ru: "Маркетинг (по отраслям)",
        field_az: "Biznes",
        field_en: "Business",
        field_ru: "Бизнес",
      },
      {
        code: "040544",
        name_az: "Mobil şəbəkə sistemləri və operatorluğu",
        name_en: "Mobile Network Systems and Operation",
        name_ru: "Системы мобильной связи и операторство",
        field_az: "Rabitə",
        field_en: "Communication",
        field_ru: "Связь",
      },
      {
        code: "040565",
        name_az: "Telekommunikasiya şəbəkələri və xətləri",
        name_en: "Telecommunication Networks and Lines",
        name_ru: "Телекоммуникационные сети и линии",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040508",
        name_az: "Çoxkanallı telekommunikasiya sistemlərinin istismarı",
        name_en: "Operation of Multi-channel Telecom Systems",
        name_ru: "Эксплуатация многоканальных телеком систем",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040572",
        name_az: "Vaqon və refrijerator sistemləri",
        name_en: "Wagon and Refrigerator Systems",
        name_ru: "Вагонные и рефрижераторные системы",
        field_az: "Nəqliyyat",
        field_en: "Transport",
        field_ru: "Транспорт",
      },
      {
        code: "040552",
        name_az: "Nəqliyyatın logistikası",
        name_en: "Transport Logistics",
        name_ru: "Транспортная логистика",
        field_az: "Logistika",
        field_en: "Logistics",
        field_ru: "Логистика",
      },
      {
        code: "040550",
        name_az: "Nəqliyyat vasitələrinin texniki istismarı",
        name_en: "Technical Operation of Vehicles",
        name_ru: "Техническая эксплуатация транспорта",
        field_az: "Nəqliyyat",
        field_en: "Transport",
        field_ru: "Транспорт",
      },
      {
        code: "040518",
        name_az: "Ətraf mühitin mühafizəsi və bərpası",
        name_en: "Environmental Protection and Restoration",
        name_ru: "Охрана и восстановление окружающей среды",
        field_az: "Ekologiya",
        field_en: "Ecology",
        field_ru: "Экология",
      },
      {
        code: "040529",
        name_az: "Kompüter sistemləri və kompleksləri",
        name_en: "Computer Systems and Complexes",
        name_ru: "Компьютерные системы и комплексы",
        field_az: "İKT",
        field_en: "ICT",
        field_ru: "ИКТ",
      },
      {
        code: "040533",
        name_az: "Kompüter şəbəkə avadanlıqlarının təmiri və servisi",
        name_en: "Repair and Service of Computer Network Equipment",
        name_ru: "Ремонт и сервис компьютерного сетевого оборудования",
        field_az: "İKT",
        field_en: "ICT",
        field_ru: "ИКТ",
      },
      {
        code: "040532",
        name_az: "Kompüter şəbəkələri və şəbəkə inzibatçılığı",
        name_en: "Computer Networks and Network Administration",
        name_ru: "Компьютерные сети и сетевое администрирование",
        field_az: "İKT",
        field_en: "ICT",
        field_ru: "ИКТ",
      },
    ],
    qiyabi: [
      {
        code: "040406",
        name_az: "Mühasibat uçotu",
        name_en: "Accounting",
        name_ru: "Бухгалтерский учет",
        field_az: "İqtisadiyyat",
        field_en: "Economics",
        field_ru: "Экономика",
      },
      {
        code: "040554",
        name_az: "Poçt rabitəsi",
        name_en: "Postal Communication",
        name_ru: "Почтовая связь",
        field_az: "Rabitə",
        field_en: "Communication",
        field_ru: "Связь",
      },
      {
        code: "040556",
        name_az: "Radio, televiziya vasitə və qurğuları",
        name_en: "Radio, TV Tools and Equipment",
        name_ru: "Радио, ТВ средства и оборудование",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040565",
        name_az: "Telekommunikasiya şəbəkələri və xətləri",
        name_en: "Telecommunication Networks and Lines",
        name_ru: "Телекоммуникационные сети и линии",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040508",
        name_az: "Çoxkanallı telekommunikasiya sistemlərinin istismarı",
        name_en: "Operation of Multi-channel Telecom Systems",
        name_ru: "Эксплуатация многоканальных телеком систем",
        field_az: "Telekommunikasiya",
        field_en: "Telecommunication",
        field_ru: "Телекоммуникации",
      },
      {
        code: "040572",
        name_az: "Vaqon və refrijerator sistemləri",
        name_en: "Wagon and Refrigerator Systems",
        name_ru: "Вагонные и рефрижераторные системы",
        field_az: "Nəqliyyat",
        field_en: "Transport",
        field_ru: "Транспорт",
      },
      {
        code: "040552",
        name_az: "Nəqliyyatın logistikası",
        name_en: "Transport Logistics",
        name_ru: "Транспортная логистика",
        field_az: "Logistika",
        field_en: "Logistics",
        field_ru: "Логистика",
      },
      {
        code: "040550",
        name_az: "Nəqliyyat vasitələrinin texniki istismarı",
        name_en: "Technical Operation of Vehicles",
        name_ru: "Техническая эксплуатация транспорта",
        field_az: "Nəqliyyat",
        field_en: "Transport",
        field_ru: "Транспорт",
      },
      {
        code: "040529",
        name_az: "Kompüter sistemləri və kompleksləri",
        name_en: "Computer Systems and Complexes",
        name_ru: "Компьютерные системы и комплексы",
        field_az: "İKT",
        field_en: "ICT",
        field_ru: "ИКТ",
      },
    ],
  }
};

const newsData = [
  {
    "id": 1,
    "title_az": "Stolüstü tennis üzrə Kollecin tələbələrdən ibarət komandasının uğuru!",
    "title_en": "College Table Tennis Team Achieves Great Success!",
    "title_ru": "Успех студенческой команды колледжа по настольному теннису!",
    "desc_az": "“Şəhərsalma və Memarlıq İli” çərçivəsində Ümummilli Lider Heydər Əliyevin anadan olmasının 103-cü ildönümünə həsr olunmuş stolüstü tennis birinciliyində tələbələrimiz fəxri kürsüyə yüksəlmişlər.",
    "desc_en": "In honor of the 103rd anniversary of National Leader Heydar Aliyev within the 'Year of Urban Planning and Architecture', our college table tennis team earned top honors.",
    "desc_ru": "В рамках «Года градостроительства и архитектуры», посвященного 103-й годовщине со дня рождения Гейдара Алиева, команда колледжа заняла призовые места по настольному теннису.",
    "date": "30 Aprel 2026",
    "image": "news_proper_3569.jpeg",
    "url": "https://rabitakolleci.edu.az/news/3569",
    "tag_az": "İdman",
    "tag_en": "Sports",
    "tag_ru": "Спорт"
  },
  {
    "id": 2,
    "title_az": "Kollecin yeni direktoru kollektivə təqdim olunub",
    "title_en": "The New Director of the College Introduced to the Staff",
    "title_ru": "Коллективу представлен новый директор колледжа",
    "desc_az": "Bakı Dövlət Rabitə və Nəqliyyat Kollecinə yeni təyin edilən direktor Səbuhi Qurbanov kollektivə təqdim olunub və qarşıda duran strateji hədəflər müzakirə edilib.",
    "desc_en": "Sabuhi Gurbanov, appointed as the new Director of Baku State Communications and Transport College, was officially introduced to the academic and administrative staff.",
    "desc_ru": "Вновь назначенный директор Бакинского государственного колледжа связи и транспорта Сабухи Гурбанов был официально представлен трудовому коллективу.",
    "date": "10 May 2026",
    "image": "news_proper_3554.webp",
    "url": "https://rabitakolleci.edu.az/news/3554",
    "tag_az": "Təyinat",
    "tag_en": "Appointment",
    "tag_ru": "Назначение"
  },
  {
    "id": 3,
    "title_az": "Müəllimimizin qaçış marafonunda qələbəsi",
    "title_en": "Our Teacher Victorious in the Sea Breeze Run Marathon",
    "title_ru": "Победа нашего преподавателя в марафоне Sea Breeze Run",
    "desc_az": "Sea Breeze-də təşkil olunan 'Sea Breeze Run #2' yarışının 10 km məsafəsində kollecimizin əməkdaşı fəal iştirak edərək mükafatçılar sırasına daxil olub.",
    "desc_en": "In the 'Sea Breeze Run #2' competition held at Sea Breeze, our college faculty member successfully completed the 10 km race and earned an honorary award.",
    "desc_ru": "В рамках забега 'Sea Breeze Run #2' на дистанции 10 км преподаватель нашего колледжа показал высокий результат и завоевал призовое место.",
    "date": "12 Aprel 2026",
    "image": "news_proper_3422.jpeg",
    "url": "https://rabitakolleci.edu.az/news/3422",
    "tag_az": "Nailiyyət",
    "tag_en": "Achievement",
    "tag_ru": "Достижение"
  },
  {
    "id": 4,
    "title_az": "Kollecdə “Narkomaniyaya yox deyək” mövzusunda geniş maarifləndirici tədbir",
    "title_en": "Awareness Campaign Titled 'Say No to Drugs' Held at the College",
    "title_ru": "В колледже прошло масштабное мероприятие «Скажем нет наркомании»",
    "desc_az": "Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecində gənclərin sağlam həyat tərzinə təşviqi məqsədilə geniş tədbir keçirilib.",
    "desc_en": "A comprehensive educational event was organized at Baku State Communications and Transport College under AzTU to promote wellness and substance abuse prevention.",
    "desc_ru": "В Бакинском государственном колледже связи и транспорта при АзТУ состоялось просветительское мероприятие, направленное на пропаганду здорового образа жизни среди молодежи.",
    "date": "16 Aprel 2026",
    "image": "news_proper_3464.jpeg",
    "url": "https://rabitakolleci.edu.az/news/3464",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 5,
    "title_az": "BMT-nin Ümumdünya Şəhərsalma Forumunun (WUF13) təşkili ilə əlaqədar tədbir",
    "title_en": "Event on the Organization of the UN World Urban Forum (WUF13)",
    "title_ru": "Мероприятие, посвященное Всемирному форуму городов ООН (WUF13)",
    "desc_az": "Kollecdə Birləşmiş Millətlər Təşkilatının Ümumdünya Şəhərsalma Forumunun XIII sessiyasının (WUF13) ölkəmizdə təşkilinə dair dəyirmi masa keçirilib.",
    "desc_en": "A roundtable discussion was hosted at the college regarding the organization of the 13th session of the World Urban Forum (WUF13) by the United Nations.",
    "desc_ru": "В колледже прошел круглый стол, посвященный проведению в Баку XIII сессии Всемирного форума городов (WUF13) Организации Объединенных Наций.",
    "date": "10 May 2026",
    "image": "news_proper_3294.jpeg",
    "url": "https://rabitakolleci.edu.az/news/3294",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 6,
    "title_az": "Kollecin bir qrup əməkdaşı fəxri fərmanla təltif olunub",
    "title_en": "Group of College Staff Awarded Certificates of Honor",
    "title_ru": "Группа сотрудников колледжа награждена почетными грамотами",
    "desc_az": "Kollecdə uzunmüddətli səmərəli pedaqoji fəaliyyətinə və gənc nəslin tərbiyəsində xidmətlərinə görə fərqlənən müəllimlər fəxri fərmanlarla mükafatlandırılıb.",
    "desc_en": "Academic and administrative employees were presented with certificates of honor recognizing their long-standing dedication to high-quality education.",
    "desc_ru": "За плодотворную педагогическую деятельность и вклад в воспитание подрастающего поколения ряду сотрудников колледжа были вручены почетные грамоты.",
    "date": "10 May 2026",
    "image": "news_proper_2819.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2819",
    "tag_az": "Nailiyyət",
    "tag_en": "Achievement",
    "tag_ru": "Достижение"
  },
  {
    "id": 7,
    "title_az": "Ümummilli Lider Heydər Əliyevin Anım Gününə həsr olunmuş tədbir",
    "title_en": "Commemoration Event Dedicated to National Leader Heydar Aliyev",
    "title_ru": "Мероприятие памяти Общенационального Лидера Гейдара Алиева",
    "desc_az": "Müasir müstəqil Azərbaycan dövlətinin memarı və qurucusu Heydər Əliyevin əziz xatirəsi kollecdə dərin ehtiram və qürur hissi ilə yad edilib.",
    "desc_en": "Faculty and students gathered to pay tribute to the founder of modern independent Azerbaijan, National Leader Heydar Aliyev, with deep reverence.",
    "desc_ru": "В колледже состоялось торжественное собрание, посвященное Дню памяти основателя современного Азербайджанского государства Гейдара Алиева.",
    "date": "12 Dekabr 2025",
    "image": "news_proper_2676.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2676",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 8,
    "title_az": "«Ultra və Treyl Qaçışları» Klubu tərəfindən təşkil olunan 10 km yarışında iştirak",
    "title_en": "Participation in the 10K Race by the Ultra & Trail Running Club",
    "title_ru": "Участие в забеге на 10 км клуба «Ультра и трейлраннинг»",
    "desc_az": "Gənclər və İdman Nazirliyinin təşkilatçılığı ilə Bakıda keçirilən 10 km məsafəyə qaçış yarışında kollecimizin tələbə və müəllimləri fəal çıxış ediblər.",
    "desc_en": "Students and instructors actively participated in the 10-kilometer cross-country run supported by the Ministry of Youth and Sports in Baku.",
    "desc_ru": "Студенты и педагоги колледжа успешно выступили в 10-километровом забеге, организованном при поддержке Министерства молодежи и спорта.",
    "date": "07 Dekabr 2025",
    "image": "news_proper_2659.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2659",
    "tag_az": "İdman",
    "tag_en": "Sports",
    "tag_ru": "Спорт"
  },
  {
    "id": 9,
    "title_az": "«Parlaq Gələcək Naminə Qaç» şüarı altında kütləvi marafon keçirilib",
    "title_en": "Mass Race Organized Under the Banner 'Run for a Bright Future'",
    "title_ru": "Массовый забег под девизом «Беги ради светлого будущего»",
    "desc_az": "Azərbaycan Atletika Federasiyası və Gənclər Nazirliyinin təşkil etdiyi qaçış turnirində kollecimizin tələbələri sağlam həyat tərzini nümayiş etdiriblər.",
    "desc_en": "College youth actively competed in the athletics tournament organized by the Athletics Federation and the Ministry of Youth, showcasing sportsmanship.",
    "desc_ru": "Студенты колледжа продемонстрировали отличную физическую подготовку в спортивном турнире Федерации легкой атлетики и Министерства молодежи.",
    "date": "23 Noyabr 2025",
    "image": "news_proper_2589.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2589",
    "tag_az": "İdman",
    "tag_en": "Sports",
    "tag_ru": "Спорт"
  },
  {
    "id": 10,
    "title_az": "İstanbul Beynəlxalq Marafonunda kollec təmsilçisinin iştirakı",
    "title_en": "College Representative Participated in the Istanbul International Marathon",
    "title_ru": "Участие представителя колледжа в Стамбульском международном марафоне",
    "desc_az": "İstanbulda Asiya və Avropa qitələrini birləşdirən məşhur Beynəlxalq marafonda kollecimizin nümayəndəsi məsafəni uğurla başa vurub medal qazanıb.",
    "desc_en": "Our college faculty member completed the prestigious marathon uniting Asia and Europe across the Bosphorus, earning a commemorative medal.",
    "desc_ru": "Представитель нашего колледжа успешно преодолел историческую дистанцию международного марафона в Стамбуле, соединяющего Азию и Европу.",
    "date": "02 Noyabr 2025",
    "image": "news_proper_2581.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2581",
    "tag_az": "İdman",
    "tag_en": "Sports",
    "tag_ru": "Спорт"
  },
  {
    "id": 11,
    "title_az": "Kollec ilə Həmkarlar İttifaqı Komitəsi arasında yeni Kollektiv Müqavilə imzalandı",
    "title_en": "New Collective Agreement Signed with College Trade Union Committee",
    "title_ru": "Подписан коллективный договор между колледжем и комитетом профсоюза",
    "desc_az": "Kollecdə işçilərin əmək, sosial və iqtisadi hüquqlarının yüksək səviyyədə təmin edilməsi məqsədilə rəsmi Kollektiv Müqavilə təntənəli şəkildə imzalanmışdır.",
    "desc_en": "A new comprehensive collective agreement was ratified to safeguard the socioeconomic rights and optimal working conditions of college employees.",
    "desc_ru": "Состоялось официальное подписание коллективного договора, гарантирующего социальные, трудовые права и достойные условия труда для сотрудников.",
    "date": "25 Noyabr 2025",
    "image": "news_proper_2566.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2566",
    "tag_az": "Təşkilat",
    "tag_en": "Organization",
    "tag_ru": "Организация"
  },
  {
    "id": 12,
    "title_az": "Kollecdə «Sağlam həyat tərzi və gənclik» mövzusunda maarifləndirici seminar",
    "title_en": "Educational Seminar on 'Healthy Lifestyle and Youth' at the College",
    "title_ru": "Семинар на тему «Здоровый образ жизни и молодежь» в колледже",
    "desc_az": "Sosial-iqtisadi inkişaf Strategiyasına uyğun olaraq gənclər arasında zərərli vərdişlərdən uzaq durmaq və idmanı gündəlik həyata daxil etmək mövzusunda seminar keçirildi.",
    "desc_en": "In accordance with national development strategies, an interactive seminar encouraged youth to adopt healthy habits and active physical lifestyles.",
    "desc_ru": "В рамках государственной программы состоялся семинар, нацеленный на укрепление здоровья молодежи и популяризацию физической культуры.",
    "date": "17 Noyabr 2025",
    "image": "news_proper_2540.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2540",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 13,
    "title_az": "Kollecdə «Azərbaycan dilinin saflığı və zənginliyi» mövzusunda açıq dərs",
    "title_en": "Open Lesson on 'Purity and Richness of the Azerbaijani Language'",
    "title_ru": "Открытый урок «Чистота и богатство азербайджанского языка»",
    "desc_az": "Dövlət dilimizin qorunması, ədəbi dil qaydalarına düzgün riayət olunması və nitq mədəniyyətinin təşviqi məqsədilə tələbələrlə interaktiv dərs keçirildi.",
    "desc_en": "An open interactive lecture engaged students on the preservation, expressive vocabulary, and proper linguistic norms of the native language.",
    "desc_ru": "Проведен открытый урок, направленный на сохранение чистоты государственного языка, развитие культуры речи и уважения к национальному наследию.",
    "date": "19 Noyabr 2025",
    "image": "news_proper_2532.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2532",
    "tag_az": "Təhsil",
    "tag_en": "Education",
    "tag_ru": "Образование"
  },
  {
    "id": 14,
    "title_az": "«Narkomaniyaya qarşı mübarizə və sağlam gələcək» mövzusunda tədbir",
    "title_en": "Forum on 'Combating Drug Addiction for a Healthy Future'",
    "title_ru": "Форум на тему «Борьба с наркоманией ради здорового будущего»",
    "desc_az": "Kollecdə səhiyyə və hüquq orqanlarının nümayəndələri ilə birlikdə zərərli meyillərin qarşısının alınması və gənclərin maarifləndirilməsi üzrə görüş keçirildi.",
    "desc_en": "Legal authorities and medical experts joined students in a vital discourse covering addiction prevention and maintaining holistic wellness.",
    "desc_ru": "С участием медицинских специалистов и юристов прошла встреча со студентами, посвященная профилактике пагубных привычек и поддержке молодежи.",
    "date": "11 Noyabr 2025",
    "image": "news_proper_2522.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2522",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 15,
    "title_az": "Xalq şairi Bəxtiyar Vahabzadənin 100 illiyinə həsr olunmuş ədəbi-bədii gecə",
    "title_en": "Literary Evening Dedicated to the Centennial of Bakhtiyar Vahabzada",
    "title_ru": "Литературный вечер к 100-летию народного поэта Бахтияра Вахабзаде",
    "desc_az": "Azərbaycan poeziyasının fəxri Bəxtiyar Vahabzadənin 100 illik yubileyinə həsr olunan gecədə tələbələr şairin vətənpərvərlik şeirlərini ifa etdilər.",
    "desc_en": "Honoring the 100th anniversary of national poet Bakhtiyar Vahabzada, students commemorated his enduring poetic legacy with moving recitations.",
    "desc_ru": "В честь векового юбилея народного поэта Бахтияра Вахабзаде студенты проникновенно декламировали его бессмертные патриотические произведения.",
    "date": "13 Noyabr 2025",
    "image": "news_proper_2483.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2483",
    "tag_az": "Mədəniyyət",
    "tag_en": "Culture",
    "tag_ru": "Культура"
  },
  {
    "id": 16,
    "title_az": "Kollecdə 8 Noyabr — Zəfər Gününə həsr olunmuş təntənəli bayram tədbiri",
    "title_en": "Festive Celebration of November 8 — Victory Day at the College",
    "title_ru": "Торжественный праздник к 8 Ноября — Дню Победы в колледже",
    "desc_az": "Vətən müharibəsində qazanılan şanlı Zəfərin ildönümü münasibətilə qazilər və şəhid ailələrinin iştirakı ilə zəngin ədəbi-musiqili kompozisiya nümayiş etdirildi.",
    "desc_en": "A celebration featuring patriotic music and inspiring performances marked the glorious anniversary of Victory Day alongside respected veterans.",
    "desc_ru": "Торжественный вечер с участием ветеранов войны и семей шехидов был посвящен исторической Победе и величию национального духа.",
    "date": "08 Noyabr 2025",
    "image": "news_proper_2441.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2441",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 17,
    "title_az": "«Uşaq Hüquqları Aylığı» çərçivəsində hüquqi maarifləndirmə tədbiri",
    "title_en": "Legal Awareness Session Within 'Children's Rights Month'",
    "title_ru": "Семинар по правовому информированию в рамках «Месячника прав ребенка»",
    "desc_az": "Kollecdə 20 oktyabr-20 noyabr «Uşaq Hüquqları Aylığı» münasibətilə tələbələrin hüquqi biliklərinin artırılmasına həsr olunmuş tədbir təşkil olundu.",
    "desc_en": "An interactive workshop deepened students' comprehension of fundamental human rights, constitutional laws, and protections guaranteed to young citizens.",
    "desc_ru": "В рамках месячника прав ребенка со студентами проведен семинар, посвященный основным правам человека и механизмам их защиты.",
    "date": "06 Noyabr 2025",
    "image": "news_proper_2419.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2419",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 18,
    "title_az": "Gənclərin hüquqlarının müdafiəsi və vətəndaşlıq məsuliyyəti mövzusunda seminar",
    "title_en": "Workshop on Youth Rights Protection and Civic Responsibility",
    "title_ru": "Семинар по защите прав молодежи и гражданской ответственности",
    "desc_az": "Tələbələrlə hüquqi bərabərlik, təhsil hüququ və vətəndaş cəmiyyətində fərdin rolu mövzusunda geniş maarifləndirici fikir mübadiləsi aparıldı.",
    "desc_en": "Students and legal educators explored civil rights, educational opportunities, and social obligations within a progressive society.",
    "desc_ru": "Состоялся открытый диалог со студентами о гражданской позиции, праве на образование и правовой культуре современного общества.",
    "date": "05 Noyabr 2025",
    "image": "news_proper_2391.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2391",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 19,
    "title_az": "Hüquqi dövlət və insan haqları mövzusunda dəyirmi masa",
    "title_en": "Roundtable on the Rule of Law and Fundamental Human Rights",
    "title_ru": "Круглый стол о правовом государстве и правах человека",
    "desc_az": "Kollecin tələbələri dövlət strukturlarının nümayəndələri ilə bir araya gələrək gənclər siyasəti və hüquqların təminatı məsələlərini müzakirə etdilər.",
    "desc_en": "Faculty and students deliberated key aspects of state youth policy, equitable representation, and human rights enforcement.",
    "desc_ru": "Студенты и эксперты обсудили реализацию государственной молодежной политики, верховенство закона и защиту социальных прав.",
    "date": "03 Noyabr 2025",
    "image": "news_proper_2365.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2365",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 20,
    "title_az": "Tələbələrin hüquqi şüurunun inkişafına dair interaktiv görüş",
    "title_en": "Interactive Session on Cultivating Legal Consciousness Among Students",
    "title_ru": "Интерактивная встреча по развитию правосознания студентов",
    "desc_az": "Qanunvericiliyin tələbləri, tələbə etikası və intizam qaydaları haqqında tələbələrə ətraflı məlumat verildi və sualları cavablandırıldı.",
    "desc_en": "Guidelines on college ethical standards, academic integrity, and civic laws were discussed comprehensively with student representatives.",
    "desc_ru": "Студентам подробно рассказали об этических нормах колледжа, академической честности и правовых аспектах студенческой жизни.",
    "date": "30 Oktyabr 2025",
    "image": "news_proper_2318.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2318",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 21,
    "title_az": "«Qızıl payız» qaçış festivalında kollec tələbələrinin uğurlu çıxışı",
    "title_en": "College Athletes Excel at the 'Golden Autumn' Running Festival",
    "title_ru": "Успешное выступление студентов на фестивале «Золотая осень»",
    "desc_az": "Əməkdar məşqçi Sadıq Sadıqovun 71-ci ildönümü münasibətilə keçirilən 'Qızıl payız' yarışında tələbələrimiz fəxri yerlərə layiq görüldülər.",
    "desc_en": "Commemorating honored coach Sadig Sadigov, our athletic students delivered impressive performances at the annual autumn cross-country championship.",
    "desc_ru": "В легкоатлетическом кроссе памяти заслуженного тренера Садыга Садыгова команда колледжа продемонстрировала блестящие спортивные результаты.",
    "date": "19 Oktyabr 2025",
    "image": "news_proper_2186.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2186",
    "tag_az": "İdman",
    "tag_en": "Sports",
    "tag_ru": "Спорт"
  },
  {
    "id": 22,
    "title_az": "5 Oktyabr — Beynəlxalq Müəllimlər Gününə həsr edilmiş təntənə",
    "title_en": "Celebration of October 5 — International Teachers' Day",
    "title_ru": "Празднование 5 Октября — Международного дня учителя",
    "desc_az": "Kollecdə çalışan fədakar müəllimlərə təşəkkürnamələr təqdim edilib, tələbələrin hazırladığı musiqili təbrik proqramı nümayiş olunub.",
    "desc_en": "Dedicated educators were awarded certificates of gratitude, accompanied by festive musical tributes orchestrated by talented students.",
    "desc_ru": "Преподаватели колледжа были награждены благодарственными грамотами в сопровождении праздничной музыкальной программы студентов.",
    "date": "05 Oktyabr 2025",
    "image": "news_proper_2098.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2098",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 23,
    "title_az": "27 Sentyabr — Anım Günü münasibətilə qəhrəman şəhidlərimiz yad edildi",
    "title_en": "September 27 — Remembrance Day: Honoring Our Heroic Martyrs",
    "title_ru": "27 Сентября — День Памяти: Почтение памяти павших героев",
    "desc_az": "Vətənimizin müstəqilliyi və suverenliyi uğrunda canından keçmiş şəhidlərimizin xatirəsi kollecdə bir dəqiqəlik sükutla yad edilmişdir.",
    "desc_en": "The entire college stood for a solemn minute of silence in honoring the sacred memory of martyrs who fell for the nation's independence.",
    "desc_ru": "Коллектив колледжа минутой молчания почтил бессмертную память шехидов, отдавших жизни за независимость и территориальную целостность Родины.",
    "date": "27 Sentyabr 2025",
    "image": "news_proper_2082.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2082",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 24,
    "title_az": "«Reproduktiv sağlamlıq və sağlam ailə modeli» mövzusunda maarifləndirici seminar",
    "title_en": "Educational Seminar on 'Reproductive Health and Positive Family Values'",
    "title_ru": "Семинар на тему «Репродуктивное здоровье и культура семейных ценностей»",
    "desc_az": "Tibb mütəxəssislərinin iştirakı ilə gənclərə fərdi gigiyena, sağlam həyat tərzi və gələcək ailə məsuliyyətləri haqqında mühazirə oxundu.",
    "desc_en": "Healthcare professionals delivered an informative lecture on preventive health, wellness routines, and fostering solid family foundations.",
    "desc_ru": "Медицинские эксперты провели со студентами полезную беседу о профилактике заболеваний, здоровом образе жизни и семейных ценностях.",
    "date": "19 May 2025",
    "image": "news_proper_2077.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2077",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 25,
    "title_az": "«Səssiz Qatil: Narkomaniya» mövzusunda maarifləndirici tədbir keçirildi",
    "title_en": "Educational Forum: 'Silent Killer — The Fight Against Addiction'",
    "title_ru": "Просветительский форум «Тихий убийца: Борьба с наркоманией»",
    "desc_az": "Kollecdə zərərli maddələrin orqanizmə və cəmiyyətə vurduğu faciəvi zərərlərə dair videoçarxlar göstərildi və gənclərlə profilaktik söhbət aparıldı.",
    "desc_en": "Documentary screenings illustrated the devastating physical and social fallout of substance addiction, reinforcing peer prevention strategies.",
    "desc_ru": "Наглядные видеоматериалы продемонстрировали опасность пагубных зависимостей, подчеркнув важность здорового выбора в жизни молодежи.",
    "date": "03 İyun 2025",
    "image": "news_proper_2072.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2072",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 26,
    "title_az": "Heydər Əliyevin 102-ci ildönümünə həsr olunmuş Şeir və Mahnı Müsabiqəsi",
    "title_en": "Poetry and Song Contest Commemorating the 102nd Anniversary of Heydar Aliyev",
    "title_ru": "Конкурс стихов и песен к 102-й годовщине со дня рождения Гейдара Алиева",
    "desc_az": "Kollecdə keçirilən istedadlar müsabiqəsində tələbələr Vətənə və Ümummilli Liderin irsinə həsr edilmiş şeirlər oxuyub musiqi nömrələri təqdim etdilər.",
    "desc_en": "Students showcased artistic gifts through vocal numbers and inspiring poetry dedicated to love of the homeland and the legacy of Heydar Aliyev.",
    "desc_ru": "Студенты колледжа проявили свои таланты, исполнив патриотические музыкальные и поэтические произведения в честь Общенационального Лидера.",
    "date": "30 May 2025",
    "image": "news_proper_2068.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2068",
    "tag_az": "Təhsil",
    "tag_en": "Education",
    "tag_ru": "Образование"
  },
  {
    "id": 27,
    "title_az": "«Korrupsiya – gələcəyimizi məhv edir» mövzusunda maarifləndirici seminar",
    "title_en": "Anti-Corruption Workshop: 'Corruption Destroys Our Future'",
    "title_ru": "Семинар «Коррупция разрушает наше будущее»",
    "desc_az": "Kollecdə şəffaflıq, dürüstlük və qanunun aliliyi prinsiplərinin tədris mühitində tətbiqi ilə bağlı geniş seminar təşkil olundu.",
    "desc_en": "A seminar emphasized institutional transparency, academic honesty, and civic opposition to bribery across all learning spheres.",
    "desc_ru": "В колледже организован семинар по внедрению принципов прозрачности, честности и верховенства закона в образовательной среде.",
    "date": "02 İyun 2025",
    "image": "news_proper_2058.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2058",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 28,
    "title_az": "«İnsan Hüquqları Aylığı» çərçivəsində hüquqi konfrans keçirilmişdir",
    "title_en": "Legal Conference Convened Within 'Human Rights Month'",
    "title_ru": "Правовая конференция в рамках «Месячника прав человека»",
    "desc_az": "Tələbələrə insan hüquqları konvensiyaları, təhsil alanların hüquqi zəmanətləri və dövlət himayəsi haqqında geniş məlumat verildi.",
    "desc_en": "Lectures detailed human rights conventions, statutory protections for scholars, and the civic obligations of youthful learners.",
    "desc_ru": "Студенты ознакомились с международными конвенциями о правах человека, правовыми гарантиями учащихся и государственными институтами защиты.",
    "date": "30 May 2025",
    "image": "news_proper_2053.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2053",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 29,
    "title_az": "«Şəffaflıq və dürüstlük: Korrupsiyaya qarşı birgə mübarizə» tədbiri",
    "title_en": "Forum: 'Transparency and Integrity — Collective Fight Against Corruption'",
    "title_ru": "Мероприятие «Прозрачность и честность: совместная борьба с коррупцией»",
    "desc_az": "Kollecdə təhsilin keyfiyyətinin yüksəldilməsi, obyektiv qiymətləndirmə və korrupsiyaya qarşı qətiyyətli mövqe məsələləri müzakirə edildi.",
    "desc_en": "Faculty members convened to discuss fair grading standards, high academic ethics, and continuous enhancement of administrative transparency.",
    "desc_ru": "Обсуждались вопросы повышения качества образования, объективной оценки знаний студентов и неукоснительного соблюдения антикоррупционных стандартов.",
    "date": "29 May 2025",
    "image": "news_proper_2039.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2039",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  },
  {
    "id": 30,
    "title_az": "Kollecdə «Azərbaycan dilinin saflığı və nitq mədəniyyəti» mövzusunda tədbir",
    "title_en": "Celebration of 'Purity of the Azerbaijani Language and Speech Culture'",
    "title_ru": "Мероприятие «Чистота азербайджанского языка и культура речи»",
    "desc_az": "Ana dilimizin zəngin söz ehtiyatının düzgün işlədilməsi, yad sözlərdən təmizlənməsi və natiqlik sənəti üzrə elmi çıxışlar dinlənildi.",
    "desc_en": "Faculty and students presented insightful papers on eloquence, terminology standards, and preserving linguistic heritage in modern times.",
    "desc_ru": "Были заслушаны доклады о правильном употреблении богатого словарного запаса родного языка, искусстве ораторского мастерства и культуре общения.",
    "date": "27 May 2025",
    "image": "news_proper_2030.jpeg",
    "url": "https://rabitakolleci.edu.az/news/2030",
    "tag_az": "Tədbir",
    "tag_en": "Event",
    "tag_ru": "Мероприятие"
  }
];


const libraryData = [
  {
    id: 3,
    title_az: "Microsoft Excel",
    title_en: "Microsoft Excel",
    title_ru: "Майкрософт Эксель",
    author_az: "Müəllif: Rəhmətov İlkin",
    author_en: "Author: Rahmetov Ilkin",
    author_ru: "Автор: Рахметов Илькин",
    category: "informatika",
    icon: "📊",
    url:
      "https://azontest.runasp.net/book/SpecialRead?id=38" +
      "&key=ABCD1234SECRET",
  },
  {
    id: 4,
    title_az: "Microsoft Word",
    title_en: "Microsoft Word",
    title_ru: "Майкрософт Ворд",
    author_az: "Müəllif: Rəhmətov İlkin",
    author_en: "Author: Rahmetov Ilkin",
    author_ru: "Автор: Рахметов Илькин",
    category: "informatika",
    icon: "📝",
    url:
      "https://azontest.runasp.net/book/SpecialRead?id=7" +
      "&key=ABCD1234SECRET",
  },
  {
    id: 5,
    title_az: "Kommunikasiya",
    title_en: "Communication",
    title_ru: "Коммуникация",
    author_az: "Müəllif: Hüseynova Natavan",
    author_en: "Author: Huseynova Natavan",
    author_ru: "Автор: Гусейнова Натаван",
    category: "azer_dili",
    icon: "📢",
    url: "KOMMUNİKASİYA DF 2.docx",
  },
  {
    id: 6,
    title_az: "Vaqonların konstruksiyası",
    title_en: "Wagon Construction",
    title_ru: "Конструкция вагонов",
    author_az: "Müəllif: Tağıyev Farid",
    author_en: "Author: Taghiyev Farid",
    author_ru: "Автор: Тагиев Фарид",
    category: "vaqonlar",
    icon: "🏗️",
    url: "vaqonların konstruksiyası son variant.pdf",
  },
  {
    id: 7,
    title_az: "Informasiya sistemlərinin təhlükəsizliyinin təmini",
    title_en: "Ensuring security of information systems",
    title_ru: "Обеспечение безопасности информационных систем",
    author_az: "Müəlliflər: F.V.Vəliyeva M.Ə.Məlikova",
    author_en: "Authors: F.V.Valiyeva M.A.Malikova",
    author_ru: "Авторы: Ф.В.Велиева М.А.Меликова",
    category: "informatika",
    icon: "🔒",
    url: "ISTT_dərslik — əsas.docx",
  },
  {
    id: 8,
    title_az: "Kompyuter qrafikası",
    title_en: "Computer Graphics",
    title_ru: "Компьютерная графика",
    author_az: "Müəllif: Məmmədova Fəridə",
    author_en: "Author: Mammadova Farida",
    author_ru: "Автор: Мамедова Фарида",
    category: "informatika",
    icon: "🎨",
    url: "Kompyuter qrafikası.docx",
  },
  {
    id: 9,
    title_az: "İnformatika",
    title_en: "Informatics",
    title_ru: "Информатика",
    author_az: "Müəllif: Əliyeva Gülnarə",
    author_en: "Author: Aliyeva Gulnara",
    author_ru: "Автор: Алиева Гульнара",
    category: "informatika",
    icon: "💻",
    url: "İnformatika Dərs Vəsaiti.pdf",
  },
  {
    id: 10,
    title_az: "Kompyuter şəbəkəsinin proqram təminatı",
    title_en: "Computer Network Software",
    title_ru: "Программное обеспечение компьютерных сетей",
    author_az: "Müəllif: Məmmədova Fəridə",
    author_en: "Author: Mammadova Farida",
    author_ru: "Автор: Мамедова Фарида",
    category: "informatika",
    icon: "🌐",
    url: "Kompyuter şəbəkəsinin proqram  təminatı.docx",
  },
  {
    id: 11,
    title_az: "Kompyuter şəbəkələri",
    title_en: "Computer Networks",
    title_ru: "Компьютерные сети",
    author_az: "Müəllif: Əliyeva Gülnarə",
    author_en: "Author: Aliyeva Gulnara",
    author_ru: "Автор: Алиева Гульнара",
    category: "informatika",
    icon: "📡",
    url: "Kompüter şəbəkələri  derslik.docx",
  },
  {
    id: 12,
    title_az: "İnformasiya Texnologiyaları",
    title_en: "Information Technologies",
    title_ru: "Информационные технологии",
    author_az: "Müəllif: Leyla Mahmudbəyli",
    author_en: "Author: Leyla Mahmudbeyli",
    author_ru: "Автор: Лейла Махмудбейли",
    category: "informatika",
    icon: "💻",
    url: "DƏRSLİK  İT 3.docx",
  },
  {
    id: 13,
    title_az: "Kompyuterin Arxitekturası",
    title_en: "Computer Architecture",
    title_ru: "Архитектура компьютера",
    author_az: "Müəllif: Quliyeva Gültəkin",
    author_en: "Author: Guliyeva Gultekin",
    author_ru: "Автор: Кулиева Гюльтекин",
    category: "informatika",
    icon: "🏛️",
    url: "KİTAB.pdf",
  },
  {
    id: 14,
    title_az: "Xətti cəbr və riyazi analiz",
    title_en: "Linear Algebra and Mathematical Analysis",
    title_ru: "Линейная алгебра и математический анализ",
    author_az: "Müəllif: Kərimova Aysel",
    author_en: "Author: Kerimova Aysel",
    author_ru: "Автор: Керимова Айсель",
    category: "riyaziyyat",
    icon: "📐",
    url: "xətti cəbr və riyazi analiz .pdf",
  },
  {
    id: 15,
    title_az: "Azərbaycan tarixi",
    title_en: "History of Azerbaijan",
    title_ru: "История Азербайджана",
    author_az: "Müəllif: Quliyeva Səidə",
    author_en: "Author: Guliyeva Saida",
    author_ru: "Автор: Кулиева Саида",
    category: "tarix",
    icon: "📜",
    url: "Azərbaycan tarxi  SƏİDƏ QULİYEVA.pdf",
  },
  {
    id: 16,
    title_az: "Sxematexnika-1",
    title_en: "Schematics-1",
    title_ru: "Схемотехника-1",
    author_az: "Müəllif: Siracova Aidə",
    author_en: "Author: Sirajova Aida",
    author_ru: "Автор: Сираджова Аида",
    category: "sxematexnika",
    icon: "🔌",
    url: "DƏRSLİK  SXEMATEXNİKA-1 (2) (2).docx",
  },
  {
    id: 17,
    title_az: "Konstruksiya materiallarının texnologiyası və materialşünaslıq",
    title_en: "Technology of Construction Materials and Material Science",
    title_ru: "Технология конструкционных материалов и материаловедение",
    author_az: "Müəllif: Əliyeva Yeganə",
    author_en: "Author: Aliyeva Yegana",
    author_ru: "Автор: Алиева Егяна",
    category: "materialsunasliq",
    icon: "🔬",
    url: "Tam son (2).pdf",
  },
  {
    id: 18,
    title_az: "İnformasiya sistemləri və verilənlər bazası",
    title_en: "Information Systems and Databases",
    title_ru: "Информационные системы и базы данных",
    author_az: "Müəlliflər: İsayev Məzahir, Mahmudbəyli Leyla, Qurbanov Fizuli",
    author_en: "Authors: Isayev Mazahir, Mahmudbeyli Leyla, Gurbanov Fizuli",
    author_ru: "Авторы: Исаев Мазахир, Махмудбейли Лейла, Гурбанов Физули",
    category: "informatika",
    icon: "🗄️",
    url: "D_RSL_K infor sis və ver baz 1.pdf",
  },
  {
    id: 19,
    title_az: "Rus dili 1 kurs (mühazirələr)",
    title_en: "Russian Language 1st course (lectures)",
    title_ru: "1Русский язык 1 курс (лекции)",
    author_az: "Müəllif: İmaməliyeva Samirə",
    author_en: "Author: Imameliyeva Samire",
    author_ru: "Автор: Имамелиева Самире",
    category: "rus_dili",
    icon: "🇷🇺",
    url: "1Русский язык 1 курс (лекции) (1).docx",
  },
  {
    id: 20,
    title_az: "Rus dili 2 kurs (mühazirələr kitab)",
    title_en: "Russian Language 2nd course (lecture book)",
    title_ru: "2Русский язык 2 курс лекции книга",
    author_az: "Müəlliflər: Qocayeva Aygün, İmaməliyeva Samirə",
    author_en: "Authors: Gojayeva Aygun, Imameliyeva Samire",
    author_ru: "Авторы: Годжаева Айгюн, Имамелиева Самире",
    category: "rus_dili",
    icon: "🇷🇺",
    url: "2Русский язык 2 курс лекции книга  (1).docx",
  },
  {
    id: 21,
    title_az: "Anbar logistikası",
    title_en: "Warehouse Logistics",
    title_ru: "Складская логистика",
    author_az: "Müəlliflər: Sadıqlı Əliağa, Sadıqlı Elmira",
    author_en: "Authors: Sadigli Aliagha, Sadigli Elmira",
    author_ru: "Авторы: Садыглы Алиага, Садыглы Эльмира",
    category: "anbar_logistikasi",
    icon: "📦",
    url: "Anbar Logistikası Kitabb SON (1).pdf",
  },
  {
    id: 22,
    title_az: "Xarici dildə işgüzar və akademik kommunikasiya 2",
    title_en: "Business and academic communication in the foreign language 2",
    title_ru: "Деловое и академическое общение на иностранном языке 2",
    author_az: "Müəllif: Mayılova Səkinə",
    author_en: "Author: Mayilova Sakina",
    author_ru: "Автор: Маилова Сакина",
    category: "xarici_dil",
    icon: "🇬🇧",
    url: "Business_and_academic_communication_in_the_foreign_language 2 (1).pdf",
  },
  {
    id: 23,
    title_az: "Ekoloji monitorinq",
    title_en: "Ecological Monitoring",
    title_ru: "Экологический мониторинг",
    author_az: "Müəlliflər: Eminəliyeva Əntiqə, Mahmudova Könül",
    author_en: "Authors: Emineliyeva Antiga, Mahmudova Konul",
    author_ru: "Авторы: Эминалиева Антига, Махмудова Кенуль",
    category: "ekologiya",
    icon: "🌱",
    url: "EKOLOJİ MONİTORİNQ.DƏRSLİK.Yeni (1).docx",
  },
  {
    id: 24,
    title_az: "Fizika",
    title_en: "Physics",
    title_ru: "Физика",
    author_az: "Müəlliflər: Mirzəyeva Günel, Mürşüdova Cəvahir",
    author_en: "Authors: Mirzayeva Gunel, Murshudova Javahir",
    author_ru: "Авторы: Мирзаева Гюнель, Муршудова Джавахир",
    category: "fizika",
    icon: "⚛️",
    url: "Fizika Dərslik (1).pdf",
  },
  {
    id: 25,
    title_az: "TPT",
    title_en: "TPT",
    title_ru: "ТПТ",
    author_az: "Müəllif: Rəhmətov İlkin",
    author_en: "Author: Rahmatov Ilkin",
    author_ru: "Автор: Рахметов Илькин",
    category: "informatika",
    icon: "🖥️",
    url: "kitab tpt (1).pdf",
  },
  {
    id: 26,
    title_az: "Kompüter sistemlərinin təmiri və servisi",
    title_en: "Repair and Maintenance of Computer Systems",
    title_ru: "Ремонт и обслуживание компьютерных систем",
    author_az: "Müəllif: Rəhmətov İlkin",
    author_en: "Author: Rahmatov Ilkin",
    author_ru: "Автор: Рахметов Илькин",
    category: "informatika",
    icon: "🛠️",
    url: "Komputer sistemlərinin təmiri və servisi. ALL (1).pdf",
  },
  {
    id: 27,
    title_az: "Kompüter şəbəkələrinin idarə etməsinin təşkili",
    title_en: "Organization of Computer Network Management",
    title_ru: "Организация управления компьютерными сетями",
    author_az: "Müəllif: Pənahova Aysel",
    author_en: "Author: Panahova Aysel",
    author_ru: "Автор: Панахова Айсель",
    category: "informatika",
    icon: "🌐",
    url: "Kompyüter şəbəkələrinin idarə etməsinin təşkili 1 (1).pdf",
  },
  {
    id: 28,
    title_az: "Riyaziyyat",
    title_en: "Mathematics",
    title_ru: "Математика",
    author_az: "Müəlliflər: Əliyeva Bikə, Məzimzadə Aynur",
    author_en: "Authors: Aliyeva Bika, Mazimzada Aynur",
    author_ru: "Авторы: Алиева Бика, Мазимзаде Айнур",
    category: "riyaziyyat",
    icon: "📐",
    url: "Riyaziyyat kitab (1) (1).pdf",
  },
  {
    id: 29,
    title_az: "Riyaziyyat",
    title_en: "Mathematics",
    title_ru: "Математика",
    author_az: "Müəllif: Alıyeva Susanna",
    author_en: "Author: Aliyeva Susanna",
    author_ru: "Автор: Алыева Сусанна",
    category: "riyaziyyat",
    icon: "📐",
    url: "Riyaziyyat.docx (1).pdf",
  },
  {
    id: 30,
    title_az: "Elektrik Dövrələri Nəzəriyyəsinin Əsasları",
    title_en: "Fundamentals of Electric Circuit Theory",
    title_ru: "Основы теории электрических цепей",
    author_az: "Müəllif: Alıyeva Şükufə",
    author_en: "Author: Aliyeva Shukufe",
    author_ru: "Автор: Алыева Шукуфа",
    category: "edne",
    icon: "⚡",
    url: "Ş.M. Alıyeva EDNƏ dərslik 2023 (1).docx",
  },
  {
    id: 31,
    title_az: "Menecment",
    title_en: "Management",
    title_ru: "Менеджмент",
    author_az: "Müəllif: Abbaslı İlahə",
    author_en: "Author: Abbasli Ilaha",
    author_ru: "Автор: Аббаслы Илаха",
    category: "menecment",
    icon: "📊",
    url: "Abbaslı İlahə Akif qızı (1) (1) (1).docx",
  },
  {
    id: 32,
    title_az: "Beynəlxalq poçt rabitəsi",
    title_en: "International Postal Communication",
    title_ru: "Международная почтовая связь",
    author_az: "Müəllif: Salayev Oktay",
    author_en: "Author: Salayev Oktay",
    author_ru: "Автор: Салаев Октай",
    category: "rabite",
    icon: "✉️",
    url: "Beynelxalq_pocht_rabitesi (1).PDF",
  },
  {
    id: 33,
    title_az: "Şəbəkə avadanlıqları",
    title_en: "Network Equipment",
    title_ru: "Сетевое оборудование",
    author_az: "Müəlliflər: Həsənli Ləman, Əliyeva Natəvan",
    author_en: "Authors: Hasanli Laman, Aliyeva Natavan",
    author_ru: "Авторы: Гасанлы Ламан, Алиева Натаван",
    category: "sebeke_avadanliqlari",
    icon: "🔌",
    url: "BÖLMƏ Kitab Natavan mm Ləman m (1).docx",
  },
  {
    id: 34,
    title_az: "Poçt rabitəsində bank əməliyyatları xidməti",
    title_en: "Bank Operations Service in Postal Communication",
    title_ru: "Служба банковских операций в почтовой связи",
    author_az: "Müəlliflər: Salayev Oktay, Əliyev Vidadi",
    author_en: "Authors: Salayev Oktay, Aliyev Vidadi",
    author_ru: "Авторы: Салаев Октай, Алиев Видади",
    category: "rabite",
    icon: "🏦",
    url: "Pocht_rabitesinde_bank_emeliyyatlari_xidmeti (1).PDF",
  },
  {
    id: 35,
    title_az: "Poçt rabitəsinin təhlükəsizliyi",
    title_en: "Security of Postal Communication",
    title_ru: "Безопасность почтовой связи",
    author_az: "Müəlliflər: Salayev Oktay, Əliyev Vidadi",
    author_en: "Authors: Salayev Oktay, Aliyev Vidadi",
    author_ru: "Авторы: Салаев Октай, Алиев Видади",
    category: "rabite",
    icon: "🛡️",
    url: "Pocht_rabitesinin_tehlukesizliyi (1).PDF",
  },
  {
    id: 36,
    title_az: "Poçt rabitəsinin təşkili və istismarı",
    title_en: "Organization and Operation of Postal Communication",
    title_ru: "Организация и эксплуатация почтовой связи",
    author_az: "Müəlliflər: Salayev Oktay, Əliyev Vidadi, Kərimli Emin",
    author_en: "Authors: Salayev Oktay, Aliyev Vidadi, Karimli Emin",
    author_ru: "Авторы: Салаев Октай, Алиев Видади, Керимли Эмин",
    category: "rabite",
    icon: "📬",
    url: "Pocht_rabitesinin_teshkili_ve_istismari (1).PDF",
  },
  {
    id: 37,
    title_az: "Əməyin mühafizəsi",
    title_en: "Labor Protection",
    title_ru: "Охрана труда",
    author_az: "Müəllif: Mahmudova Alidə",
    author_en: "Author: Mahmudova Alida",
    author_ru: "Автор: Махмудова Алида",
    category: "emeyin_muhafizesi",
    icon: "🛡️",
    url: "ƏMƏYİN MÜHAFİZƏSİ-DƏRSLİK-MAHMUDOVA ALIDƏ (1).pdf",
  },
  {
    id: 38,
    title_az: "Əməliyyat sistemləri",
    title_en: "Operating Systems",
    title_ru: "Операционные системы",
    author_az: "Müəlliflər: Salayev Oktay, Ağayev Munir",
    author_en: "Authors: Salayev Oktay, Agayev Munir",
    author_ru: "Авторы: Салаев Октай, Агаев Мунир",
    category: "os",
    icon: "💻",
    url: "Əməliyyat sistemləri (1).pdf",
  },
  {
    id: 39,
    title_az: "Nəqliyyat vasitələrinin diaqnostikası 1",
    title_en: "Diagnosis of Transport Vehicles 1",
    title_ru: "Диагностика транспортных средств 1",
    author_az: "Müəlliflər: Əhmədli Babək, Mustafayeva Gülər",
    author_en: "Authors: Ahmadli Babak, Mustafayeva Gular",
    author_ru: "Авторы: Ахмедли Бабек, Мустафаева Гюляр",
    category: "transport",
    icon: "🚗",
    url: "Nəqliyyat vasitələrinin diaqnostikası 1 (2) (1).docx",
  },
];

const lecturesData = [
  {
    id: 4,
    title_az: "Ədəbiyyat dərsi — Video dərs",
    title_en: "Literature Lesson — Video",
    title_ru: "Урок литературы — Видео",
    duration: "10:30",
    thumb: "https://img.youtube.com/vi/l0DMdzdPozI/hqdefault.jpg",
    category: "edebiyyat",
    url: "https://youtu.be/l0DMdzdPozI?si=HjWFGL-E3RriJTXx",
  },
  {
    id: 5,
    title_az: "Ədəbiyyat dərsi — 2-ci video",
    title_en: "Literature Lesson — Part 2",
    title_ru: "Урок литературы — Часть 2",
    duration: "12:00",
    thumb: "https://img.youtube.com/vi/tp0ACtSnR5g/hqdefault.jpg",
    category: "edebiyyat",
    url: "https://youtu.be/tp0ACtSnR5g?si=LC36Lg7fFTeBCbpU",
  },
  {
    id: 6,
    title_az: "İnformatika dərsi — 1",
    title_en: "Informatics Lesson — 1",
    title_ru: "Урок информатики — 1",
    duration: "15:00",
    thumb: "https://img.youtube.com/vi/drQpergnCEo/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/drQpergnCEo?si=ZAgRJrLMe6meCQRs",
  },
  {
    id: 7,
    title_az: "İnformatika dərsi — 2",
    title_en: "Informatics Lesson — 2",
    title_ru: "Урок информатики — 2",
    duration: "18:00",
    thumb: "https://img.youtube.com/vi/_cwUDtCh_vk/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/_cwUDtCh_vk?si=F_3-i4WRzk14fVv_",
  },
  {
    id: 8,
    title_az: "Tarix dərsi — 1",
    title_en: "History Lesson — 1",
    title_ru: "Урок истории — 1",
    duration: "20:00",
    thumb: "https://img.youtube.com/vi/GrOgYgtzTKQ/hqdefault.jpg",
    category: "tarix",
    url: "https://youtu.be/GrOgYgtzTKQ?si=4WPfJYPGYVLVLg_9",
  },
  {
    id: 9,
    title_az: "Tarix dərsi — 2",
    title_en: "History Lesson — 2",
    title_ru: "Урок истории — 2",
    duration: "22:00",
    thumb: "https://img.youtube.com/vi/UZrba576_T8/hqdefault.jpg",
    category: "tarix",
    url: "https://youtu.be/UZrba576_T8?si=jB3IiQ9BSK5sXcwT",
  },
  {
    id: 10,
    title_az: "Tarix dərsi — 3",
    title_en: "History Lesson — 3",
    title_ru: "Урок истории — 3",
    duration: "25:00",
    thumb: "https://img.youtube.com/vi/xc6hIRqRyHs/hqdefault.jpg",
    category: "tarix",
    url: "https://youtu.be/xc6hIRqRyHs?si=3DSY_C5XctpV7U_a",
  },
  {
    id: 11,
    title_az: "Hüquq dərsi — 1",
    title_en: "Law Lesson — 1",
    title_ru: "Урок права — 1",
    duration: "16:00",
    thumb: "https://img.youtube.com/vi/sq1g6Dj-yGk/hqdefault.jpg",
    category: "huquq",
    url: "https://youtu.be/sq1g6Dj-yGk?si=tpbGyNT3g7I7T6xP",
  },
  {
    id: 12,
    title_az: "Hüquq dərsi — 2",
    title_en: "Law Lesson — 2",
    title_ru: "Урок права — 2",
    duration: "19:00",
    thumb: "https://img.youtube.com/vi/T1mFmYSRAdM/hqdefault.jpg",
    category: "huquq",
    url: "https://youtu.be/T1mFmYSRAdM?si=sPCrU7S4sikahNW8",
  },
  {
    id: 13,
    title_az: "İnformatika dərsi — 3",
    title_en: "Informatics Lesson — 3",
    title_ru: "Урок информатики — 3",
    duration: "12:45",
    thumb: "https://img.youtube.com/vi/-bpQkFT9qao/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/-bpQkFT9qao?si=UkUZfxgGFBAtelvG",
  },
  {
    id: 14,
    title_az: "İnformatika dərsi — 4",
    title_en: "Informatics Lesson — 4",
    title_ru: "Урок информатики — 4",
    duration: "14:20",
    thumb: "https://img.youtube.com/vi/UQIMGcuo9Ps/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/UQIMGcuo9Ps?si=AI-y329U2EVxtaNt",
  },
  {
    id: 15,
    title_az: "İnformatika dərsi — 5",
    title_en: "Informatics Lesson — 5",
    title_ru: "Урок информатики — 5",
    duration: "11:15",
    thumb: "https://img.youtube.com/vi/TovJNHIAqbg/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/TovJNHIAqbg?si=oFfEqfXAqwp1O9z0",
  },
  {
    id: 16,
    title_az: "İnformatika dərsi — 6",
    title_en: "Informatics Lesson — 6",
    title_ru: "Урок информатики — 6",
    duration: "13:50",
    thumb: "https://img.youtube.com/vi/WXGqqm38Fds/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/WXGqqm38Fds?si=MkodiQ6xn2J12tId",
  },
  {
    id: 17,
    title_az: "İnformatika dərsi — 7",
    title_en: "Informatics Lesson — 7",
    title_ru: "Урок информатики — 7",
    duration: "10:30",
    thumb: "https://img.youtube.com/vi/LWspjOSwp5U/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/LWspjOSwp5U?si=mLCSj8Ff8qU-04_S",
  },
  {
    id: 18,
    title_az: "İnformatika dərsi — 8",
    title_en: "Informatics Lesson — 8",
    title_ru: "Урок информатики — 8",
    duration: "15:10",
    thumb: "https://img.youtube.com/vi/JVimOCoDHZY/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/JVimOCoDHZY?si=Jk-hxZvqcaWeaUPz",
  },
  {
    id: 19,
    title_az: "İnformatika dərsi — 9",
    title_en: "Informatics Lesson — 9",
    title_ru: "Урок информатики — 9",
    duration: "12:00",
    thumb: "https://img.youtube.com/vi/VSflfqWc8OM/hqdefault.jpg",
    category: "informatika",
    url: "https://youtu.be/VSflfqWc8OM?si=8eaahqUqc87qDh3j",
  },
];





/**
 * 3. CORE LOGIC / INITIALIZATION
 * Initialization unified at the end of the file
 */

// Calculate metrics
function getGrade(score) {
  if (score >= 91) return "A";
  if (score >= 81) return "B";
  if (score >= 71) return "C";
  if (score >= 61) return "D";
  if (score >= 51) return "E";
  return "F";
}
function scoreToPoint(score) {
  if (score >= 91) return 4.0;
  if (score >= 81) return 3.0;
  if (score >= 71) return 2.0;
  if (score >= 61) return 1.0;
  return 0.0;
}

/**
 * SCROLL & UI ENGINE (Antigravity Adaptability)
 */
function initScrollEngine() {
  const header = document.getElementById("site-header");
  const toggle = document.getElementById("mobile-toggle");
  const overlay = document.getElementById("mobile-nav");
  const links = document.querySelectorAll(".mobile-nav-link");
  const html = document.documentElement;

  // Parallax Elements
  const heroBg = document.querySelector(".fluid-bg");
  const heroCanvas = document.getElementById("particles-canvas");
  const heroContent = document.querySelector(".hero-content");

  // Header Blur Effect & Parallax
  window.addEventListener(
    "scroll",
    () => {
      const scrolled = window.scrollY;

      // Header
      if (scrolled > 20) {
        header.classList.add("scrolled");
      } else {
        header.classList.remove("scrolled");
      }

      // Hero Parallax Effect (only apply if in viewport)
      if (scrolled < window.innerHeight) {
        if (heroBg) heroBg.style.transform = `translateY(${scrolled * 0.4}px)`;
        if (heroCanvas)
          heroCanvas.style.transform = `translateY(${scrolled * 0.2}px)`;
        if (heroContent) {
          heroContent.style.transform = `translateY(${scrolled * 0.15}px)`;
          heroContent.style.opacity = Math.max(
            0,
            1 - scrolled / (window.innerHeight * 0.8),
          );
        }
      }
    },
    { passive: true },
  );

  // Mobile Toggle
  toggle.addEventListener("click", () => {
    const isActive = toggle.classList.toggle("active");
    overlay.classList.toggle("active");
    html.classList.toggle("scroll-locked");
  });

  links.forEach((link) => {
    link.addEventListener("click", () => {
      toggle.classList.remove("active");
      overlay.classList.remove("active");
      html.classList.remove("scroll-locked");
    });
  });

  // Reveal Animation
  const reveals = document.querySelectorAll(".reveal");
  const revealOptions = { threshold: 0.15, rootMargin: "0px 0px -50px 0px" };
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        revealObserver.unobserve(entry.target);
      }
    });
  }, revealOptions);

  reveals.forEach((r) => revealObserver.observe(r));
}

/**
 * THEME ENGINE (Multi-Theme Support)
 */
function setTheme(theme) {
  document.body.classList.remove("light-mode", "dark-mode", "space-mode");

  const normalized = theme === "space" ? "dark" : theme;
  if (normalized === "dark") {
    document.body.classList.add("dark-mode");
  }

  localStorage.setItem("bdrnk-theme", normalized);
  document.documentElement.setAttribute("data-theme", normalized);
  document.dispatchEvent(new CustomEvent("themeChanged"));
}

function initThemeEngine() {
  const themeToggleBtn = document.getElementById("theme-toggle");
  const dropdownBtns = document.querySelectorAll(
    ".theme-dropdown button[data-theme-set]",
  );
  if (!themeToggleBtn) return;

  themeToggleBtn.addEventListener("click", (e) => {
    e.stopPropagation();
    const wrap = themeToggleBtn.parentElement;
    wrap.classList.toggle("active");
  });

  document.addEventListener("click", (e) => {
    if (!e.target.closest(".theme-switcher-wrap")) {
      document
        .querySelector(".theme-switcher-wrap")
        ?.classList.remove("active");
    }
  });

  // Handle theme toggle via data-theme-set
  dropdownBtns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      const targetTheme = btn.getAttribute("data-theme-set");
      const wrap = themeToggleBtn.parentElement;
      wrap.classList.remove("active"); // Close dropdown

      if (!document.startViewTransition) {
        setTheme(targetTheme);
        return;
      }

      // Get click coordinates for the ripple origin
      const x = e.clientX;
      const y = e.clientY;

      // Calculate distance to furthest corner to ensure ripple covers the screen
      const endRadius = Math.hypot(
        Math.max(x, window.innerWidth - x),
        Math.max(y, window.innerHeight - y),
      );

      const transition = document.startViewTransition(() => {
        setTheme(targetTheme);
      });

      transition.ready.then(() => {
        const isDark = targetTheme === "dark" || targetTheme === "space";

        // Animate the clip-path from standard circle to full screen
        document.documentElement.animate(
          {
            clipPath: [
              `circle(0px at ${x}px ${y}px)`,
              `circle(${endRadius}px at ${x}px ${y}px)`,
            ],
          },
          {
            duration: 500,
            easing: "ease-out",
            // Specify which pseudo-element to animate based on whether we are moving
            // to a dark theme or light theme. By default the 'new' state is on top.
            pseudoElement: "::view-transition-new(root)",
          },
        );
      });
    });
  });

  // Check saved theme initially
  const savedTheme =
    localStorage.getItem("bdrnk-theme") ||
    (window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light");
  setTheme(savedTheme);
}
const faqData = [
  {
    "q": {
      "az": "Qəbul prosesi necə aparılır?",
      "ru": "Как проходит процесс поступления?",
      "en": "How is the admission process conducted?"
    },
    "a": {
      "az": "Qəbul prosesi Dövlət İmtahan Mərkəzi (DİM) tərəfindən keçirilən ümumi (9 illik) və ya tam (11 illik) orta təhsil bazasında buraxılış imtahanlarının nəticələrinə əsasən aparılır. Müsabiqə şərtlərini ödəyən abituriyentlər portal.edu.az vasitəsilə kollecimizin ixtisaslarını seçərək elektron qeydiyyatdan keçirlər.",
      "ru": "Процесс поступления осуществляется на основе результатов выпускных экзаменов на базе общего (9-летнего) или полного (11-летнего) среднего образования, проводимых ГЭЦ. Абитуриенты, набравшие проходной балл, выбирают специальности нашего колледжа и регистрируются онлайн через portal.edu.az.",
      "en": "The admission process is based on entrance examination scores administered by the State Examination Center (SEC) on the basis of 9-year or 11-year secondary education. Eligible applicants select our college majors and register electronically via portal.edu.az."
    }
  },
  {
    "q": {
      "az": "Dərs qrafiki və növbələri necədir?",
      "ru": "Каков график и смены занятий?",
      "en": "What is the class schedule and shifts?"
    },
    "a": {
      "az": "Dərslər həftənin 5 günü iki növbəli rejimdə (I növbə: 08:30 – 13:40, II növbə: 14:00 – 19:10) keçirilir. Hər bir qrupun dərslər, laboratoriya və praktiki məşğələ cədvəli tədris ili əvvəlində tədris hissəsi tərəfindən təsdiq olunur və tələbə portalında əks etdirilir.",
      "ru": "Занятия проводятся 5 дней в неделю в две смены (I смена: 08:30 – 13:40, II смена: 14:00 – 19:10). Расписание лекций, лабораторных и практических занятий для каждой группы утверждается учебной частью и доступно в студенческом портале.",
      "en": "Classes are held 5 days a week across two daily shifts (1st shift: 08:30 – 13:40, 2nd shift: 14:00 – 19:10). The schedule of lectures, laboratory works, and seminars is approved by the academic department and accessible via the student portal."
    }
  },
  {
    "q": {
      "az": "Tələbələr üçün təqaüd imkanları necədir?",
      "ru": "Какие стипендиальные возможности есть для студентов?",
      "en": "What scholarship opportunities are available for students?"
    },
    "a": {
      "az": "Kollecdə dövlət sifarişi və ya ödənişli əsaslarla təhsil almasından asılı olmayaraq, semestr imtahanlarının nəticələrinə (GPA göstəricilərinə) əsasən tələbələrə 'Əlaçı', 'Həvəsləndirici' və 'Adi' dərəcəli dövlət təqaüdləri verilir.",
      "ru": "Независимо от формы обучения (на бюджетной или платной основе), по результатам экзаменационной сессии (показателям GPA) успевающим студентам ежемесячно выплачиваются государственные стипендии: «Отличная», «Поощрительная» и «Обычная».",
      "en": "Regardless of tuition status (state-funded or fee-paying), students earn monthly state scholarships ('Honors', 'Encouragement', and 'Standard') based on their semester exam performance (GPA metrics)."
    }
  },
  {
    "q": {
      "az": "İstehsalat təcrübəsi harada və necə təşkil olunur?",
      "ru": "Где и как организуется производственная практика?",
      "en": "Where and how is practical internship organized?"
    },
    "a": {
      "az": "Tələbələrimiz sonuncu tədris ilində 'Azərpoçt' MMC, 'Bakı Metropoliteni' QSC, 'Azərbaycan Dəmir Yolları' QSC, telekommunikasiya şirkətləri, banklar və İT müəssisələrində istehsalat təcrübəsi keçərək praktiki iş vərdişləri qazanır və bir çoxu elə orada işlə təmin olunur.",
      "ru": "На выпускном курсе наши студенты проходят производственную практику в ООО «Азерпочта», ЗАО «Бакинский метрополитен», ЗАО «Азербайджанские железные дороги», телекоммуникационных компаниях, банках и ИТ-корпорациях с перспективой дальнейшего трудоустройства.",
      "en": "During their final academic year, our students complete field internships at 'Azerpost' LLC, 'Baku Metro' CJSC, 'Azerbaijan Railways' CJSC, leading telecom operators, banks, and IT companies, often securing full-time employment."
    }
  },
  {
    "q": {
      "az": "Kolleci bitirdikdən sonra universitetə imtahansız qəbul mümkündürmü?",
      "ru": "Возможно ли поступление в университет без экзаменов после колледжа?",
      "en": "Can graduates enter university without entrance exams?"
    },
    "a": {
      "az": "Bəli! Kolleci uğurla bitirən məzunlar subbakalavr dərəcəsi alırlar və DİM-in qaydalarına uyğun olaraq imtahan vermədən, orta müvəffəqiyyət göstəricisi (ÜOMG) əsasında müvafiq ixtisaslar üzrə ali təhsil müəssisələrinə birbaşa müsabiqə yolu ilə qəbul ola bilirlər.",
      "ru": "Да! Выпускники, успешно окончившие колледж, получают квалификацию суббакалавра и в соответствии с правилами ГЭЦ могут без сдачи вступительных экзаменов поступить в вузы по профильным специальностям на основе среднего балла успеваемости (ÜOMG).",
      "en": "Yes! Graduates earn a sub-bachelor degree and, pursuant to SEC regulations, can gain direct admission to higher education institutions (universities) in aligned majors without entrance exams, based on their cumulative GPA (ÜOMG)."
    }
  },
  {
    "q": {
      "az": "Elektron kitabxana və dərs resurslarından necə istifadə etmək olar?",
      "ru": "Как пользоваться электронной библиотекой и учебными ресурсами?",
      "en": "How can I access the digital library and learning materials?"
    },
    "a": {
      "az": "Saytımızın 'Kitabxana' və 'Videodərslər' bölməsindən ixtisasınıza uyğun bütün dərslikləri, metodik vəsaitləri və mühazirələri heç bir ödəniş olmadan onlayn oxuya, yükləyə və videodərslərə baxa bilərsiniz.",
      "ru": "В разделах 'Библиотека' и 'Видеоуроки' нашего сайта вы можете в любое время бесплатно читать онлайн или скачивать все профильные учебники, методические пособия и лекционные видеоматериалы.",
      "en": "In the 'Library' and 'Lectures' sections of our portal, you can freely view, read online, or download all textbook manuals, syllabus guidelines, and lecture video recordings suited to your major."
    }
  },

  {
    "q": {
      "az": "Təhsil haqqını hissə-hissə ödəmək mümkündürmü?",
      "ru": "Возможна ли оплата обучения частями?",
      "en": "Can tuition fees be paid in installments?"
    },
    "a": {
      "az": "Bəli, ödənişli əsaslarla təhsil alan tələbələrimiz üçün təhsil haqqı illik məbləğ şəklində və ya hər semestr üzrə hissə-hissə rahatlıqla ödənilə bilər. Həmçinin sosial baxımdan həssas qruplardan olan tələbələrə dövlət tərəfindən tam güzəştlər tətbiq edilir.",
      "ru": "Да, для студентов платного отделения предусмотрена удобная возможность поэтапной оплаты обучения по семестрам. Кроме того, студентам из социально уязвимых категорий предоставляются государственные льготы и компенсации.",
      "en": "Yes, students enrolled in fee-paying programs can conveniently pay their tuition in semester installments. Furthermore, full state waivers and social benefits apply to students from vulnerable socioeconomic categories."
    }
  }
];

function initFAQModule() {
  const faqAccordion = document.getElementById("faq-accordion");
  if (!faqAccordion) return;

  function renderFAQ() {
    const openedIndices = [];
    faqAccordion.querySelectorAll(".faq-item.active").forEach((item, index) => {
      // We can map DOM position back if needed, but for simplicity let's just close all on language switch
      // or keep the structure simple:
    });

    faqAccordion.innerHTML = faqData
      .map(
        (item, index) => `
            <div class="faq-item reveal" style="transition-delay: ${index * 0.1}s">
                <button class="faq-question">
                    <span>${item.q[currentLang] || item.q.az}</span>
                    <div class="faq-icon"></div>
                </button>
                <div class="faq-answer">
                    <div class="faq-answer-content">
                        ${item.a[currentLang] || item.a.az}
                    </div>
                </div>
            </div>
        `,
      )
      .join("");

    // Re-init toggle listeners
    faqAccordion.querySelectorAll(".faq-question").forEach((btn, index) => {
      // Force reveal class to visible since they might be in viewport already after re-render
      setTimeout(() => btn.parentElement.classList.add("visible"), index * 100);

      btn.addEventListener("click", () => {
        const item = btn.parentElement;
        const isActive = item.classList.contains("active");

        // Close all others
        faqAccordion
          .querySelectorAll(".faq-item")
          .forEach((i) => i.classList.remove("active"));

        if (!isActive) {
          item.classList.add("active");
        }
      });
    });
  }

  renderFAQ();

  // Listen for language changes and completely re-render FAQ contents
  document.addEventListener("languageChanged", renderFAQ);
}

function animateValue(obj, start, end, duration) {
  let startTimestamp = null;
  const step = (timestamp) => {
    if (!startTimestamp) startTimestamp = timestamp;
    const progress = Math.min((timestamp - startTimestamp) / duration, 1);
    const easeOut = 1 - Math.pow(1 - progress, 3); // Cubic ease out
    obj.innerHTML =
      Math.floor(easeOut * (end - start) + start) + (end > 1000 ? "+" : "");
    if (progress < 1) {
      window.requestAnimationFrame(step);
    }
  };
  window.requestAnimationFrame(step);
}

/**
 * SIS LOGIN TILT — 3D Motion (Digital ID Experience)
 */
function initSISTilt() {
  const card = document.getElementById("sis-login");
  if (!card || window.matchMedia("(hover: none)").matches) return;

  card.addEventListener("mousemove", (e) => {
    const rect = card.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    // Subtle Perspective Tilt
    const rotateX = (centerY - y) / 25;
    const rotateY = (x - centerX) / 25;

    // Magnetic Attraction (Floating effect)
    const moveX = (x - centerX) / 15;
    const moveY = (y - centerY) / 15;

    // Update CSS variables for the Glow
    card.style.setProperty("--mx", `${(x / rect.width) * 100}%`);
    card.style.setProperty("--my", `${(y / rect.height) * 100}%`);

    card.style.transform = `perspective(1500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translate3d(${moveX}px, ${moveY}px, 0) scale(1.02)`;
  });

  card.addEventListener("mouseleave", () => {
    card.style.transform = `perspective(1500px) rotateX(0deg) rotateY(0deg) translate3d(0, 0, 0) scale(1)`;
  });
}

/**
 * LANGUAGE ENGINE (Language Orb)
 */
function initLanguageEngine() {
  const btns = document.querySelectorAll(".lang-btn");
  btns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      // UI Toggle
      btns.forEach((b) => b.classList.remove("active"));
      const target = e.target;
      target.classList.add("active");

      // Set state & update DOM
      currentLang = target.getAttribute("data-lang");
      document.documentElement.lang = currentLang;
      updateDOMTexts();
      document.dispatchEvent(new CustomEvent("languageChanged"));
    });
  });
}

/**
 * PARTICLES ENGINE (CSS/Canvas Canvas - Institutional Blue)
 */
function initParticlesEngine() {
  const canvas = document.getElementById("particles-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let width, height;
  let particles = [];

  function resize() {
    width = window.innerWidth;
    height = window.innerHeight;
    canvas.width = width * window.devicePixelRatio;
    canvas.height = height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  }

  class Particle {
    constructor() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.size = Math.random() * 2 + 1;
      this.speedX = Math.random() * 0.4 - 0.2;
      this.speedY = Math.random() * 0.4 - 0.2;

      // Theme-based particle colors
      const isSpace = document.body.classList.contains("space-mode");
      const isDark = document.body.classList.contains("dark-mode");
      const baseColor = isSpace
        ? "168, 85, 247"
        : isDark
          ? "52, 152, 219"
          : "27, 79, 114";
      const alpha = Math.random() * 0.4 + 0.1;
      this.color = `rgba(${baseColor}, ${alpha})`;
      this.baseColor = baseColor;
    }
    update() {
      this.x += this.speedX;
      this.y += this.speedY;

      if (this.x > width || this.x < 0) this.speedX *= -1;
      if (this.y > height || this.y < 0) this.speedY *= -1;
    }
    draw() {
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function init() {
    resize();
    particles = [];
    const count = window.innerWidth < 768 ? 20 : 50;
    for (let i = 0; i < count; i++) {
      particles.push(new Particle());
    }
  }

  function animate() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < particles.length; i++) {
      particles[i].update();
      particles[i].draw();

      // Connect lines
      for (let j = i; j < particles.length; j++) {
        const dx = particles[i].x - particles[j].x;
        const dy = particles[i].y - particles[j].y;
        const distance = Math.sqrt(dx * dx + dy * dy);

        if (distance < 150) {
          ctx.beginPath();
          // Softer connecting lines using dynamic color
          ctx.strokeStyle = `rgba(${particles[i].baseColor}, ${0.1 - distance / 1500})`;
          ctx.lineWidth = 0.8;
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.stroke();
        }
      }
    }
    requestAnimationFrame(animate);
  }

  window.addEventListener("resize", init);
  init();
  animate();
}

/**
 * STRUCTURE MODULE (Direct Rendering UI & Air-Flow Modal)
 */
function renderCategoriesCount() {
  const l = document.getElementById("count-leadership");
  const d = document.getElementById("count-departments");
  const c = document.getElementById("count-commissions");
  const m = document.getElementById("count-majors");

  if (l) l.textContent = staffData.leadership.length;
  if (d) d.textContent = staffData.departments.length;
  if (c) c.textContent = staffData.commissions.length;
  if (m) m.textContent = (staffData.majors.eyani?.length || 0) + (staffData.majors.qiyabi?.length || 0);
}

function initStructureModule() {
  const triggers = document.querySelectorAll(".cat-trigger");
  const modal = document.getElementById("modal");
  const closeBtn = document.getElementById("modal-close");
  const grid = document.getElementById("grid");
  const modalTitle = document.getElementById("modal-title");
  const html = document.documentElement;

  // Formal Institutional Cards (No 3D sci-fi tilt)
  const cards = document.querySelectorAll(".hologram-card");
  cards.forEach((card) => {
    card.style.transform = "";
  });

  // Add event listener for majors tabs
  grid.addEventListener("click", (e) => {
    const tab = e.target.closest(".major-tab");
    if (tab) {
      const target = tab.getAttribute("data-target");
      grid.querySelectorAll(".major-tab").forEach(t => t.classList.remove("active"));
      tab.classList.add("active");
      grid.querySelectorAll(".major-section").forEach(s => s.classList.remove("active"));
      const targetSection = grid.querySelector(`#major-section-${target}`);
      if (targetSection) targetSection.classList.add("active");
    }
  });

  function openModal(category) {
    const data = staffData[category];
    grid.innerHTML = "";

    let titleKey = "cat_" + category;
    modalTitle.textContent = gT(titleKey);

    if (category === "majors") {
      grid.classList.add("table-mode");

      const renderSection = (type, list, isActive) => {
        if (!list || list.length === 0) return "";
        return `
              <div class="major-section ${isActive ? 'active' : ''}" id="major-section-${type}">
                  <div class="majors-table-wrap">
                      <table class="majors-table">
                          <thead>
                              <tr>
                                  <th>${gT("th_code")}</th>
                                  <th>${gT("th_major")}</th>
                                  <th>${gT("th_field")}</th>
                              </tr>
                          </thead>
                          <tbody>
                              ${list.map((m, i) => `
                                  <tr style="animation-delay: ${i * 0.03}s">
                                      <td class="m-code" data-label="${gT("th_code")}">${m.code}</td>
                                      <td class="m-name" data-label="${gT("th_major")}">${m[`name_${currentLang}`]}</td>
                                      <td class="m-field" data-label="${gT("th_field")}">
                                          <span class="field-badge">${m[`field_${currentLang}`]}</span>
                                      </td>
                                  </tr>
                              `).join("")}
                          </tbody>
                      </table>
                  </div>
              </div>
          `;
      };

      grid.innerHTML = `
          <div class="majors-tabs">
              <button class="major-tab active" data-target="eyani">${gT("eyani")}</button>
              <button class="major-tab" data-target="qiyabi">${gT("qiyabi")}</button>
          </div>
          <div class="majors-content">
              ${renderSection("eyani", data.eyani, true)}
              ${renderSection("qiyabi", data.qiyabi, false)}
          </div>
      `;
    } else {
      grid.classList.remove("table-mode");
      data.forEach((person, index) => {
        const delay = index * 0.05;
        const name = person[`name_${currentLang}`];
        const role = person[`role_${currentLang}`];
        const card = document.createElement("div");
        card.className = "staff-card";
        if (person.id === "1") card.classList.add("director-card");
        if (person.id === "12") card.classList.add("fizuli-card");
        if (person.id === "7") card.classList.add("babek-card");
        if (person.id === "16") card.classList.add("vefa-card");
        if (person.id === "18") card.classList.add("gunay-card");
        card.style.animationDelay = `${delay}s`;
        card.innerHTML = `
                <div class="card-img-wrap">
                    <img src="${person.img}" alt="${name}" loading="lazy" onerror="this.onerror=null;this.src='logo.jpg';">
                </div>
                <div class="card-info">
                    <div class="card-accent-bar"></div>
                    <h4 class="card-name">${name}</h4>
                    <span class="card-role">${role}</span>
                </div>
            `;
        grid.appendChild(card);
      });
    }

    modal.classList.add("active");
    html.classList.add("scroll-locked");
  }

  function closeModal() {
    modal.classList.remove("active");
    html.classList.remove("scroll-locked");
    setTimeout(() => {
      grid.innerHTML = "";
    }, 500); // clear after transition
  }

  let currentOpenCategory = null;
  triggers.forEach((btn) => {
    btn.addEventListener("click", () => {
      const cat = btn.getAttribute("data-category");
      currentOpenCategory = cat;
      openModal(cat);
    });
  });

  // Wire up Header & Mobile "Struktur" Dropdown Items
  const navStructItems = document.querySelectorAll("[data-struct-cat]");
  navStructItems.forEach((item) => {
    item.addEventListener("click", (e) => {
      const cat = item.getAttribute("data-struct-cat");
      if (!cat) return;
      currentOpenCategory = cat;
      // Blur focus so the CSS :focus-within dropdown closes cleanly
      if (document.activeElement && typeof document.activeElement.blur === "function") {
        document.activeElement.blur();
      }
      // Open the corresponding modal right after the scene/scroll transition
      setTimeout(() => {
        openModal(cat);
      }, 450);
    });
  });

  document.addEventListener("languageChanged", () => {
    if (modal.classList.contains("active") && currentOpenCategory) {
      openModal(currentOpenCategory);
    }
  });

  closeBtn.addEventListener("click", closeModal);
  modal.addEventListener("click", (e) => {
    if (e.target === modal) closeModal();
  });
}

/**
 * DIGITAL LIBRARY (Search & Filter Logic)
 */
function initLibraryModule() {
  const grid = document.getElementById("books-grid");
  const searchInput = document.getElementById("library-search");
  const totalCounter = document.getElementById("lib-total-counter");

  // Reading Room Modal refs
  const readerModal = document.getElementById("book-reader-modal");
  const readerBackdrop = document.getElementById("book-reader-backdrop");
  const readerClose = document.getElementById("book-reader-close");
  const readerIcon = document.getElementById("reader-book-icon");
  const readerCat = document.getElementById("reader-book-cat");
  const readerTitle = document.getElementById("reader-book-title");
  const readerOpenExt = document.getElementById("reader-open-ext");
  const readerCoverEmoji = document.getElementById("reader-cover-emoji");
  const readerCoverName = document.getElementById("reader-cover-name");
  const readerCoverAuthor = document.getElementById("reader-cover-author");
  const readerMetaCat = document.getElementById("reader-meta-cat");
  const readerMetaAuthor = document.getElementById("reader-meta-author");
  const readerViewport = document.getElementById("book-reader-viewport");

  function getCategoryDisplayName(catKey) {
    const btn = document.querySelector(`#library-filter .filter-badge[data-filter="${catKey}"]`);
    return btn ? btn.textContent.trim() : catKey;
  }

  function openBookReader(book) {
    if (!readerModal) return;
    const title = book[`title_${currentLang}`] || book.title_az;
    const author = book[`author_${currentLang}`] || book.author_az;
    const catLabel = getCategoryDisplayName(book.category);
    const url = book.url || "#";
    const isPdf = /\.pdf$/i.test(url);

    if (readerIcon) readerIcon.textContent = book.icon || "📘";
    if (readerCat) readerCat.textContent = `BDRNK Rəqəmsal Oxu Zalı · ${catLabel}`;
    if (readerTitle) readerTitle.textContent = title;
    if (readerOpenExt) readerOpenExt.href = url;
    if (readerCoverEmoji) readerCoverEmoji.textContent = book.icon || "📘";
    if (readerCoverName) readerCoverName.textContent = title;
    if (readerCoverAuthor) readerCoverAuthor.textContent = author;
    if (readerMetaCat) readerMetaCat.textContent = catLabel;
    if (readerMetaAuthor) readerMetaAuthor.textContent = author.replace(/^Müəllif:\s*|^Author:\s*|^Автор:\s*/i, "");

    if (readerViewport) {
      if (isPdf) {
        readerViewport.innerHTML = `<iframe class="book-reader-iframe" src="${encodeURI(url)}" title="${title}"></iframe>`;
      } else {
        readerViewport.innerHTML = `
          <div class="reader-doc-fallback">
            <div class="reader-doc-badge">WORD / DOCX TƏDRİS VƏSAİTİ</div>
            <div class="reader-doc-icon">${book.icon || "📄"}</div>
            <h4>${title}</h4>
            <p>${author}</p>
            <p class="reader-doc-note">Bu dərs vəsaiti Microsoft Word (DOCX) formatında tərtib edilmişdir. Tam mətni oxumaq və ya çap etmək üçün faylı birbaşa yükləyə bilərsiniz.</p>
            <a href="${encodeURI(url)}" download class="btn btn-primary reader-doc-dl-btn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
              <span>Dərs Vəsaitini Yüklə (.DOCX)</span>
            </a>
          </div>
        `;
      }
    }

    readerModal.classList.add("active");
    readerModal.setAttribute("aria-hidden", "false");
    document.documentElement.classList.add("scroll-locked");
  }

  function closeBookReader() {
    if (!readerModal) return;
    readerModal.classList.remove("active");
    readerModal.setAttribute("aria-hidden", "true");
    document.documentElement.classList.remove("scroll-locked");
    if (readerViewport) readerViewport.innerHTML = "";
  }

  readerClose?.addEventListener("click", closeBookReader);
  readerBackdrop?.addEventListener("click", closeBookReader);

  function renderBooks(data) {
    grid.innerHTML = "";
    if (totalCounter) {
      totalCounter.textContent = `${data.length} Rəsmi Dərs Vəsaiti`;
    }

    if (data.length === 0) {
      grid.innerHTML = `<p style="grid-column: 1/-1; text-align: center; color: var(--text-dim);">${gT("no_book")}</p>`;
      return;
    }

    data.forEach((book) => {
      const title = book[`title_${currentLang}`] || book.title_az;
      const author = book[`author_${currentLang}`] || book.author_az;
      const catLabel = getCategoryDisplayName(book.category);
      const isPdf = /\.pdf$/i.test(book.url || "");
      const formatTag = isPdf ? "PDF · OXU ZALI" : "DOCX · VƏSAİT";

      const card = document.createElement("div");
      card.className = "book-card reveal visible";

      card.innerHTML = `
        <div class="book-card-inner">
          <div class="book-cover">
            <div class="book-3d-spine" aria-hidden="true"></div>
            <div class="book-top-bar">
              <span class="book-cat-tag">${catLabel}</span>
              <span class="book-format-pill">${formatTag}</span>
            </div>
            <div class="book-emoji-wrap">
              <span class="book-emoji">${book.icon}</span>
            </div>
            <div class="book-info">
              <h4 class="book-title">${title}</h4>
              <span class="book-author">${author}</span>
              <div class="book-actions">
                <button type="button" class="book-btn book-btn-preview">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                  <span>Oxu Zalı</span>
                </button>
                <a href="${book.url || "#"}" target="_blank" rel="noopener noreferrer" class="book-btn-ext" title="Yeni pəncərədə aç / Yüklə">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
              </div>
            </div>
          </div>
        </div>
      `;

      card.querySelector(".book-cover")?.addEventListener("click", (e) => {
        if (e.target.closest(".book-btn-ext")) return;
        openBookReader(book);
      });

      grid.appendChild(card);
    });
  }

  function applyFilter() {
    const raw = searchInput.value || "";
    const query = raw
      .trim()
      .toLowerCase()
      .replace(/ı/g, "i")
      .replace(/ə/g, "e");

    const activeBtn = document.querySelector(
      "#library-filter .filter-badge.active",
    );
    const activeFilter = activeBtn
      ? activeBtn.getAttribute("data-filter")
      : "all";

    const filtered = libraryData.filter((book) => {
      const matchCategory =
        activeFilter === "all" || book.category === activeFilter;
      if (!query) return matchCategory;

      // Combine all text content and normalize for search
      const textToSearch = [
        book.title_az,
        book.title_en,
        book.title_ru,
        book.author_az,
        book.author_en,
        book.author_ru,
        book.category,
      ]
        .map((s) =>
          (s || "").toLowerCase().replace(/ı/g, "i").replace(/ə/g, "e"),
        )
        .join(" ");

      return matchCategory && textToSearch.includes(query);
    });

    renderBooks(filtered);
  }

  searchInput.addEventListener("input", applyFilter);

  const filterContainer = document.getElementById("library-filter");
  filterContainer.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-badge");
    if (!btn) return;
    filterContainer
      .querySelectorAll(".filter-badge")
      .forEach((b) => b.classList.remove("active"));
    btn.classList.add("active");
    applyFilter();
  });

  renderBooks(libraryData);

  // Re-render when language changes
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      setTimeout(applyFilter, 50);
    });
  });
}

/**
 * LECTURES HUB — ACADEMIC MEDIA STUDIO
 */
function initLecturesModule() {
  const grid = document.getElementById("lectures-grid");
  const filterContainer = document.getElementById("lecture-filter");
  const deptGrid = document.getElementById("lecture-dept-grid");
  const searchInput = document.getElementById("lecture-search");
  const stage = document.getElementById("lecture-stage");
  const studioDetails = document.getElementById("studio-current-details");
  const studioPlaylist = document.getElementById("studio-playlist");

  if (!grid || !filterContainer) return;

  let activeCategory = "all";
  let currentLecture = lecturesData[0] || null;
  let isPlayingEmbed = false;

  function getYoutubeId(url) {
    if (!url) return "";
    const match = url.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([A-Za-z0-9_-]{11})/);
    return match ? match[1] : "";
  }

  function getCategoryLabel(cat) {
    const map = {
      informatika: gT("filter_informatika") || "İnformatika",
      tarix: gT("filter_tarix") || "Tarix",
      edebiyyat: gT("filter_edebiyyat") || "Ədəbiyyat",
      huquq: gT("filter_huquq") || "Hüquq",
    };
    return map[cat] || cat;
  }

  function getUIText() {
    if (currentLang === "en") {
      return {
        watchStudio: "Watch in Studio",
        playingNow: "Now Playing",
        prevLesson: "← Prev",
        nextLesson: "Next →",
        openYT: "YouTube ↗",
        searchPlaceholder: "Search video lectures...",
        modulePrefix: "MODULE",
        lessonsWord: "Video Lectures",
      };
    }
    if (currentLang === "ru") {
      return {
        watchStudio: "Смотреть в студии",
        playingNow: "Сейчас играет",
        prevLesson: "← Пред.",
        nextLesson: "След. →",
        openYT: "YouTube ↗",
        searchPlaceholder: "Поиск видеоуроков...",
        modulePrefix: "МОДУЛЬ",
        lessonsWord: "Видеоуроков",
      };
    }
    return {
      watchStudio: "Studiyada İzlə",
      playingNow: "İndi Oxudulur",
      prevLesson: "← Əvvəlki",
      nextLesson: "Növbəti →",
      openYT: "YouTube ↗",
      searchPlaceholder: "Videodərs axtar...",
      modulePrefix: "MODUL",
      lessonsWord: "Videodərs",
    };
  }

  function getFilteredList() {
    const raw = (searchInput && searchInput.value) || "";
    const query = raw
      .trim()
      .toLowerCase()
      .replace(/ı/g, "i")
      .replace(/ə/g, "e");

    return lecturesData.filter((l) => {
      const matchCat = activeCategory === "all" || l.category === activeCategory;
      if (!query) return matchCat;
      const text = [l.title_az, l.title_en, l.title_ru, l.category]
        .map((s) => (s || "").toLowerCase().replace(/ı/g, "i").replace(/ə/g, "e"))
        .join(" ");
      return matchCat && text.includes(query);
    });
  }

  function renderStudio(filteredList) {
    if (!stage || !studioDetails || !studioPlaylist) return;
    const list = filteredList && filteredList.length > 0 ? filteredList : lecturesData;
    if (!currentLecture || !list.some((item) => item.id === currentLecture.id)) {
      currentLecture = list[0];
      isPlayingEmbed = false;
    }
    if (!currentLecture) return;

    const ui = getUIText();
    const title = currentLecture[`title_${currentLang}`] || currentLecture.title_az;
    const catLabel = getCategoryLabel(currentLecture.category);
    const currentIndex = list.findIndex((item) => item.id === currentLecture.id);
    const modCode = `${ui.modulePrefix} #${String(currentIndex + 1).padStart(2, "0")}`;
    const ytId = getYoutubeId(currentLecture.url);

    if (isPlayingEmbed && ytId) {
      stage.innerHTML = `
        <iframe
          src="https://www.youtube.com/embed/${ytId}?autoplay=1&rel=0"
          title="${title}"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
          allowfullscreen>
        </iframe>
      `;
    } else {
      stage.innerHTML = `
        <div class="stage-cover" id="stage-cover-trigger" role="button" tabindex="0" aria-label="${title}">
          <img src="${currentLecture.thumb}" alt="${title}" />
          <div class="stage-top-badges">
            <span class="stage-cat-pill">${catLabel}</span>
            <span class="stage-mod-pill">${modCode} · ${currentLecture.duration}</span>
          </div>
          <div class="stage-play-btn">
            <svg viewBox="0 0 24 24" fill="currentColor">
              <polygon points="5 3 19 12 5 21 5 3"></polygon>
            </svg>
          </div>
          <div class="stage-bottom-bar">
            <div>
              <span class="stage-bottom-sub">BDRNK RƏQƏMSAL AKADEMİYA</span>
              <h3 class="stage-bottom-title">${title}</h3>
            </div>
          </div>
        </div>
      `;
      const coverTrigger = document.getElementById("stage-cover-trigger");
      if (coverTrigger) {
        coverTrigger.addEventListener("click", () => {
          isPlayingEmbed = true;
          renderStudio(list);
        });
      }
    }

    studioDetails.innerHTML = `
      <span class="studio-curr-tag">${catLabel} · ${modCode} (${currentLecture.duration})</span>
      <h4 class="studio-curr-title">${title}</h4>
      <div class="studio-curr-controls">
        <button type="button" class="studio-ctrl-btn" id="studio-prev-btn">${ui.prevLesson}</button>
        <button type="button" class="studio-ctrl-btn" id="studio-next-btn">${ui.nextLesson}</button>
        <a href="${currentLecture.url}" target="_blank" rel="noopener noreferrer" class="studio-ctrl-btn primary">${ui.openYT}</a>
      </div>
    `;

    const prevBtn = document.getElementById("studio-prev-btn");
    const nextBtn = document.getElementById("studio-next-btn");
    if (prevBtn) {
      prevBtn.addEventListener("click", () => {
        const prevIdx = (currentIndex - 1 + list.length) % list.length;
        currentLecture = list[prevIdx];
        isPlayingEmbed = false;
        renderStudio(list);
        highlightActiveCard();
      });
    }
    if (nextBtn) {
      nextBtn.addEventListener("click", () => {
        const nextIdx = (currentIndex + 1) % list.length;
        currentLecture = list[nextIdx];
        isPlayingEmbed = false;
        renderStudio(list);
        highlightActiveCard();
      });
    }

    studioPlaylist.innerHTML = list
      .map((lec, idx) => {
        const lTitle = lec[`title_${currentLang}`] || lec.title_az;
        const activeCls = currentLecture && lec.id === currentLecture.id ? "active" : "";
        return `
          <button type="button" class="studio-pl-item ${activeCls}" data-pl-id="${lec.id}">
            <span class="studio-pl-num">#${String(idx + 1).padStart(2, "0")}</span>
            <span class="studio-pl-name">${lTitle}</span>
            <span class="studio-pl-dur">${lec.duration}</span>
          </button>
        `;
      })
      .join("");

    studioPlaylist.querySelectorAll(".studio-pl-item").forEach((btn) => {
      btn.addEventListener("click", () => {
        const targetId = parseInt(btn.getAttribute("data-pl-id"), 10);
        const found = list.find((item) => item.id === targetId);
        if (found) {
          currentLecture = found;
          isPlayingEmbed = true;
          renderStudio(list);
          highlightActiveCard();
        }
      });
    });
  }

  function highlightActiveCard() {
    grid.querySelectorAll(".lecture-card").forEach((card) => {
      const id = parseInt(card.getAttribute("data-lec-id"), 10);
      const btn = card.querySelector(".lecture-watch-btn span");
      const ui = getUIText();
      if (currentLecture && id === currentLecture.id) {
        card.classList.add("active-playing");
        if (btn) btn.textContent = ui.playingNow;
      } else {
        card.classList.remove("active-playing");
        if (btn) btn.textContent = ui.watchStudio;
      }
    });
  }

  function renderLectures(data) {
    grid.innerHTML = "";
    const ui = getUIText();
    if (searchInput) searchInput.placeholder = ui.searchPlaceholder;

    if (data.length === 0) {
      grid.innerHTML = `<p style="grid-column: 1/-1; text-align: center; color: var(--text-dim); padding: 32px 0;">${gT("no_video")}</p>`;
      return;
    }

    data.forEach((lec, index) => {
      const title = lec[`title_${currentLang}`] || lec.title_az;
      const catLabel = getCategoryLabel(lec.category);
      const modNum = `#${String(index + 1).padStart(2, "0")}`;
      const isActive = currentLecture && lec.id === currentLecture.id;

      const card = document.createElement("div");
      card.className = `lecture-card reveal visible${isActive ? " active-playing" : ""}`;
      card.setAttribute("data-lec-id", lec.id);

      card.innerHTML = `
        <div class="lecture-thumb">
          <span class="lecture-cat-badge">${catLabel}</span>
          <span class="lecture-mod-badge">${modNum}</span>
          <img src="${lec.thumb}" alt="${title}" loading="lazy" />
          <div class="lecture-play">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor">
              <polygon points="5 3 19 12 5 21 5 3"></polygon>
            </svg>
          </div>
          <span class="lecture-dur-pill">
            <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
              <circle cx="12" cy="12" r="10"></circle>
              <polyline points="12 6 12 12 16 14"></polyline>
            </svg>
            ${lec.duration}
          </span>
        </div>
        <div class="lecture-info">
          <h4 class="lecture-title">${title}</h4>
          <div class="lecture-actions">
            <button type="button" class="lecture-watch-btn">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor">
                <polygon points="5 3 19 12 5 21 5 3"></polygon>
              </svg>
              <span>${isActive ? ui.playingNow : ui.watchStudio}</span>
            </button>
            <a href="${lec.url}" target="_blank" rel="noopener noreferrer" class="lecture-ext-link" onclick="event.stopPropagation();">
              ${ui.openYT}
            </a>
          </div>
        </div>
      `;

      const selectAndPlayInStudio = () => {
        currentLecture = lec;
        isPlayingEmbed = true;
        renderStudio(data);
        highlightActiveCard();
        const studioEl = document.getElementById("lecture-studio");
        if (studioEl) {
          const headerOffset = (document.getElementById("site-header")?.offsetHeight || 112) + 16;
          const top = studioEl.getBoundingClientRect().top + window.pageYOffset - headerOffset;
          window.scrollTo({ top, behavior: "smooth" });
        }
      };

      const thumbEl = card.querySelector(".lecture-thumb");
      const watchBtn = card.querySelector(".lecture-watch-btn");
      if (thumbEl) thumbEl.addEventListener("click", selectAndPlayInStudio);
      if (watchBtn) watchBtn.addEventListener("click", selectAndPlayInStudio);

      grid.appendChild(card);
    });
  }

  function setCategory(cat) {
    activeCategory = cat || "all";

    // Sync filter badges
    filterContainer.querySelectorAll(".filter-badge").forEach((b) => {
      b.classList.toggle("active", b.getAttribute("data-filter") === activeCategory);
    });

    // Sync department cards
    if (deptGrid) {
      deptGrid.querySelectorAll(".lecture-dept-card").forEach((c) => {
        c.classList.toggle("active", c.getAttribute("data-filter") === activeCategory);
      });
    }

    const filtered = getFilteredList();
    if (filtered.length > 0) {
      currentLecture = filtered[0];
      isPlayingEmbed = false;
    }
    renderStudio(filtered);
    renderLectures(filtered);
  }

  // Filter badges click
  filterContainer.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-badge");
    if (!btn) return;
    setCategory(btn.getAttribute("data-filter"));
  });

  // Department cards click
  if (deptGrid) {
    deptGrid.addEventListener("click", (e) => {
      const card = e.target.closest(".lecture-dept-card");
      if (!card) return;
      setCategory(card.getAttribute("data-filter"));
    });
  }

  // Search input
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      const filtered = getFilteredList();
      renderStudio(filtered);
      renderLectures(filtered);
    });
  }

  // Header & Mobile dropdown links for Videodərslər ([data-lecture-cat])
  document.querySelectorAll("[data-lecture-cat]").forEach((item) => {
    item.addEventListener("click", () => {
      const cat = item.getAttribute("data-lecture-cat");
      if (!cat) return;
      if (document.activeElement && typeof document.activeElement.blur === "function") {
        document.activeElement.blur();
      }
      const mobileNav = document.getElementById("mobile-nav");
      const mobileToggle = document.getElementById("mobile-toggle");
      if (mobileNav && mobileNav.classList.contains("active")) {
        mobileNav.classList.remove("active");
        if (mobileToggle) mobileToggle.classList.remove("active");
        document.documentElement.classList.remove("scroll-locked");
      }
      setCategory(cat);
    });
  });

  // Initial render
  const initialList = getFilteredList();
  renderStudio(initialList);
  renderLectures(initialList);

  // Re-render when language changes
  document.addEventListener("languageChanged", () => {
    const list = getFilteredList();
    renderStudio(list);
    renderLectures(list);
  });
}


/**
 * POST FORM (Contact Hub)
 */
function initForm() {
  const form = document.getElementById("contact-form");
  const msg = document.getElementById("form-success");
  if (!form) return;

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const formData = new FormData(form);

    fetch(form.action, {
      method: "POST",
      body: formData,
      headers: { Accept: "application/json" },
    })
      .then((res) => {
        msg.textContent = (gT("cf_success") || "Mesajınız uğurla göndərildi!") + " ✓";
        msg.classList.add("show");
        form.reset();
        setTimeout(() => {
          msg.classList.remove("show");
        }, 5000);
      })
      .catch(() => {
        msg.textContent = "Xəta baş verdi. Yenidən cəhd edin.";
        msg.classList.add("show");
        setTimeout(() => {
          msg.classList.remove("show");
        }, 5000);
      });
  });
}

// Bootstrap App
document.addEventListener("DOMContentLoaded", () => {
  console.log("--- BDRNK App Bootstrap ---");

  function safeInit(name, fn) {
    try {
      console.log(`Initializing ${name}...`);
      fn();
      console.log(`${name} OK.`);
    } catch (e) {
      console.error(`ERROR in ${name}:`, e);
      // Non-blocking error reporting
    }
  }

  /**
   * NEWS MODULE — Hover-Reveal Cards
   */
  function initNewsModule() {
    const grid = document.getElementById("news-grid");
    const allNewsBtn = document.getElementById("btn-all-news");
    if (!grid) return;

    let showAll = false;
    let currentArticleIdx = 0;
    let articleFontSize = 1.05; // rem

    // In-Page Article Reader Modal refs
    const nrModal = document.getElementById("news-reader-modal");
    const nrBackdrop = document.getElementById("news-reader-backdrop");
    const nrClose = document.getElementById("news-reader-close");
    const nrTag = document.getElementById("nr-tag");
    const nrDate = document.getElementById("nr-date");
    const nrTitle = document.getElementById("nr-title");
    const nrImg = document.getElementById("nr-img");
    const nrContent = document.getElementById("nr-content");
    const nrSourceLink = document.getElementById("news-source-link");
    const nrRelatedList = document.getElementById("nr-related-list");
    const nrPrevBtn = document.getElementById("nr-prev-btn");
    const nrNextBtn = document.getElementById("nr-next-btn");
    const nrPrevTitle = document.getElementById("nr-prev-title");
    const nrNextTitle = document.getElementById("nr-next-title");
    const nrFontDec = document.getElementById("news-font-dec");
    const nrFontInc = document.getElementById("news-font-inc");
    const nrPrintBtn = document.getElementById("news-print-btn");

    function openNewsReader(index) {
      if (!nrModal || !newsData[index]) return;
      currentArticleIdx = index;
      const item = newsData[index];
      const title = item[`title_${currentLang}`] || item.title_az;
      const desc = item[`desc_${currentLang}`] || item.desc_az;
      const tag = item[`tag_${currentLang}`] || item.tag_az;

      if (nrTag) nrTag.textContent = tag;
      if (nrDate) nrDate.textContent = item.date || "";
      if (nrTitle) nrTitle.textContent = title;
      if (nrImg) {
        nrImg.src = item.image;
        nrImg.alt = title;
        nrImg.onerror = function () {
          this.onerror = null;
          this.src = "news1.webp";
        };
      }
      if (nrSourceLink) nrSourceLink.href = item.url || "#";

      const officialFooter =
        currentLang === "en"
          ? "Baku State Communications and Transport College under Azerbaijan Technical University continues to implement consistent educational, scientific, and social initiatives aimed at preparing highly qualified specialists and supporting student development."
          : currentLang === "ru"
            ? "Бакинский государственный колледж связи и транспорта при Азербайджанском техническом университете продолжает реализацию последовательных образовательных, научных и социальных инициатив, направленных на подготовку высококвалифицированных специалистов."
            : "Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kolleci tələbələrin hərtərəfli inkişafı, yüksəkixtisaslı kadr hazırlığı və ictimai-mədəni fəallığın artırılması istiqamətində ardıcıl tədbirləri davam etdirir.";

      if (nrContent) {
        nrContent.style.fontSize = `${articleFontSize}rem`;
        nrContent.innerHTML = `
          <p class="nr-lead-para">${desc}</p>
          <p class="nr-body-para">${officialFooter}</p>
          <div class="nr-official-stamp">
            <span class="nr-stamp-seal">BDRNK · MƏTBUAT XİDMƏTİ</span>
            <span class="nr-stamp-date">${item.date || ""}</span>
          </div>
        `;
      }

      // Prev / Next buttons
      const prevIdx = (index - 1 + newsData.length) % newsData.length;
      const nextIdx = (index + 1) % newsData.length;
      if (nrPrevTitle) nrPrevTitle.textContent = newsData[prevIdx][`title_${currentLang}`] || newsData[prevIdx].title_az;
      if (nrNextTitle) nrNextTitle.textContent = newsData[nextIdx][`title_${currentLang}`] || newsData[nextIdx].title_az;

      // Related news list
      if (nrRelatedList) {
        nrRelatedList.innerHTML = newsData
          .map((n, idx) => {
            if (idx === index) return "";
            const nTitle = n[`title_${currentLang}`] || n.title_az;
            const nTag = n[`tag_${currentLang}`] || n.tag_az;
            return `
              <button type="button" class="nr-related-card" data-news-idx="${idx}">
                <img src="${n.image}" alt="" loading="lazy" onerror="this.onerror=null;this.src='news1.webp';" />
                <div class="nr-related-info">
                  <span class="nr-related-tag">${nTag} · ${n.date || ""}</span>
                  <h5>${nTitle}</h5>
                </div>
              </button>
            `;
          })
          .join("");

        nrRelatedList.querySelectorAll(".nr-related-card").forEach((btn) => {
          btn.addEventListener("click", () => {
            const targetIdx = parseInt(btn.getAttribute("data-news-idx"), 10);
            openNewsReader(targetIdx);
            document.getElementById("news-reader-article")?.scrollTo({ top: 0, behavior: "smooth" });
          });
        });
      }

      nrModal.classList.add("active");
      nrModal.setAttribute("aria-hidden", "false");
      document.documentElement.classList.add("scroll-locked");
    }

    function closeNewsReader() {
      if (!nrModal) return;
      nrModal.classList.remove("active");
      nrModal.setAttribute("aria-hidden", "true");
      document.documentElement.classList.remove("scroll-locked");
    }

    nrClose?.addEventListener("click", closeNewsReader);
    nrBackdrop?.addEventListener("click", closeNewsReader);
    nrPrevBtn?.addEventListener("click", () => {
      openNewsReader((currentArticleIdx - 1 + newsData.length) % newsData.length);
      document.getElementById("news-reader-article")?.scrollTo({ top: 0, behavior: "smooth" });
    });
    nrNextBtn?.addEventListener("click", () => {
      openNewsReader((currentArticleIdx + 1) % newsData.length);
      document.getElementById("news-reader-article")?.scrollTo({ top: 0, behavior: "smooth" });
    });
    nrFontDec?.addEventListener("click", () => {
      articleFontSize = Math.max(0.88, +(articleFontSize - 0.08).toFixed(2));
      if (nrContent) nrContent.style.fontSize = `${articleFontSize}rem`;
    });
    nrFontInc?.addEventListener("click", () => {
      articleFontSize = Math.min(1.38, +(articleFontSize + 0.08).toFixed(2));
      if (nrContent) nrContent.style.fontSize = `${articleFontSize}rem`;
    });
    nrPrintBtn?.addEventListener("click", () => window.print());

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && nrModal?.classList.contains("active")) {
        closeNewsReader();
      }
    });

    function renderNews() {
      grid.innerHTML = "";
      const itemsToRender = showAll ? newsData : newsData.slice(0, 3);

      itemsToRender.forEach((item, idx) => {
        const title = item[`title_${currentLang}`] || item.title_az;
        const desc = item[`desc_${currentLang}`] || item.desc_az;
        const tag = item[`tag_${currentLang}`] || item.tag_az;
        const readMore = gT("news_read_more");

        const card = document.createElement("div");
        card.className = "news-card";
        card.style.cursor = "pointer";
        card.innerHTML = `
          <div class="news-card-media">
            <img class="news-card-img" src="${item.image}" alt="${title}" loading="lazy" onerror="this.onerror=null;this.src='news1.webp';" />
            <span class="news-card-tag">${tag}</span>
          </div>
          <div class="news-card-overlay">
            ${item.date ? `<span class="news-card-date">${item.date}</span>` : ""}
            <h3 class="news-card-title">${title}</h3>
            <div class="news-card-reveal">
              <p>${desc}</p>
              <button type="button" class="news-card-link news-open-reader-btn">${readMore}</button>
            </div>
          </div>
        `;
        card.addEventListener("click", (e) => {
          e.preventDefault();
          openNewsReader(idx);
        });
        grid.appendChild(card);
      });

      if (allNewsBtn) {
        if (showAll || newsData.length <= 3) {
          allNewsBtn.style.display = "none";
        } else {
          allNewsBtn.style.display = "inline-block";
        }
      }
    }

    if (allNewsBtn) {
      allNewsBtn.addEventListener("click", (e) => {
        if (e) e.preventDefault();
        showAll = true;
        // Keep current scroll position by preventing layout collapse
        const currentHeight = grid.offsetHeight;
        grid.style.minHeight = `${currentHeight}px`;
        renderNews();
        // Remove min-height after rendering
        setTimeout(() => { grid.style.minHeight = ""; }, 100);
      });
    }

    renderNews();

    // Re-render on language and theme change
    document.addEventListener("themeChanged", renderNews);
    document.addEventListener("languageChanged", renderNews);
    const langBtns = document.querySelectorAll(".lang-btn");
    langBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        setTimeout(renderNews, 50);
      });
    });
  }


  function initRoadmapModule() {
    const roadmapSection = document.getElementById("roadmap");
    const items = document.querySelectorAll(".roadmap-item");
    if (!roadmapSection) return;

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
          }
        });
      },
      { threshold: 0.2 },
    );

    items.forEach((item) => observer.observe(item));
  }

  const admissionScores = {
    "040406": 110.5, // Mühasibat uçotu
    "040554": 102.4, // Poçt rabitəsi
    "040556": 100.2, // Radio, televiziya
    "040405": 92.6,  // Marketinq
    "040544": 105.8, // Mobil şəbəkə
    "040565": 101.5, // Telekom şəbəkələri
    "040508": 103.1, // Çoxkanallı
    "040572": 88.4,  // Vaqon
    "040552": 98.7,  // Nəqliyyat logistikası
    "040550": 85.3,  // Nəqliyyat vasitələri
    "040518": 75.0,  // Ekologiya
    "040529": 112.4, // Kompüter sistemləri
    "040533": 108.2, // Kompüter avadanlıqları
    "040532": 115.6  // Kompüter şəbəkələri
  };

  function initAdmissionCalculator() {
    const scoreInput = document.getElementById("calc-score");
    const majorSelect = document.getElementById("calc-major");
    const calcBtn = document.getElementById("btn-calculate");
    const percentSpan = document.getElementById("calc-percent");
    const gaugeFill = document.getElementById("gauge-path");
    const msgPara = document.getElementById("calc-message");

    if (!calcBtn || !majorSelect) return;

    // Populate majors
    function populateMajors() {
      const currentLabel = (majorSelect.options[0] && majorSelect.options[0].textContent) || (currentLang === 'az' ? 'İxtisası seçin...' : (currentLang === 'en' ? 'Select a major...' : 'Выберите специальность...'));
      majorSelect.innerHTML = `<option value="">${currentLabel}</option>`;

      const allMajors = [];
      if (staffData.majors.eyani) allMajors.push(...staffData.majors.eyani);
      if (staffData.majors.qiyabi) allMajors.push(...staffData.majors.qiyabi);

      allMajors.forEach(m => {
        const opt = document.createElement("option");
        opt.value = m.code;
        const isQiyabi = staffData.majors.qiyabi && staffData.majors.qiyabi.some(qm => qm.code === m.code);
        const mode = isQiyabi ? (currentLang === 'az' ? ' (Qiyabi)' : (currentLang === 'en' ? ' (Part-time)' : ' (Заочно)')) : '';
        opt.textContent = m[`name_${currentLang}`] + mode;
        majorSelect.appendChild(opt);
      });
    }

    populateMajors();

    // Re-populate on language change
    document.querySelectorAll(".lang-btn").forEach(btn => {
      btn.addEventListener("click", () => setTimeout(populateMajors, 100));
    });

    calcBtn.addEventListener("click", () => {
      const score = parseFloat(scoreInput.value) || 0;
      const majorCode = majorSelect.value;

      if (!majorCode) {
        msgPara.textContent = currentLang === "az" ? "Zəhmət olmasa ixtisas seçin." : "Please select a major.";
        return;
      }

      const minScore = admissionScores[majorCode] || 100;

      // Calculate chance based on real scores
      // If score is >= minScore, chance is high (80-100%)
      // If score is < minScore, chance drops
      let chance = 0;
      const diff = score - minScore;

      if (diff >= 0) {
        // Above min score
        chance = 85 + (diff / (300 - minScore)) * 15;
      } else {
        // Below min score
        chance = Math.max(5, 80 + (diff / minScore) * 80);
      }

      if (score === 0) chance = 0;

      const roundedChance = Math.round(Math.min(100, chance));
      percentSpan.textContent = roundedChance;

      const dash = 126;
      const offset = dash - (dash * roundedChance) / 100;
      gaugeFill.style.strokeDasharray = dash;
      gaugeFill.style.strokeDashoffset = offset;

      if (roundedChance < 40) msgPara.textContent = gT("calc_msg_low");
      else if (roundedChance < 80) msgPara.textContent = gT("calc_msg_mid");
      else msgPara.textContent = gT("calc_msg_high");
    });
  }

  safeInit("Scroll", initScrollEngine);
  safeInit("Theme", initThemeEngine);
  safeInit("Language", initLanguageEngine);
  safeInit("Texts", updateDOMTexts);
  safeInit("SISTilt", initSISTilt);
  safeInit("Particles", initParticlesEngine);
  safeInit("Structure", initStructureModule);
  safeInit("Library", initLibraryModule);
  safeInit("Lectures", initLecturesModule);
  safeInit("News", initNewsModule);
  safeInit("Roadmap", initRoadmapModule);
  safeInit("Stats", initStatsCounter);
  safeInit("AdmissionCalc", initAdmissionCalculator);

  safeInit("Form", initForm);
  safeInit("FAQ", initFAQModule);
  safeInit("VideoCarousel", initVideoCarousel);
  safeInit("Preloader", initPreloader);
  safeInit("SceneTransition", initSceneTransition);
  safeInit("ContextMenu", initContextMenu);
  safeInit("SpotlightCards", initSpotlightCards);
  safeInit("Ticker", initTicker);
  safeInit("FluxEngine", initFluxEngine);
  safeInit("HeroParallax", initHeroParallax);
  safeInit("Gallery", initGalleryModule);
});

/* ═══════════════ GALLERY MODULE ═══════════════ */
function initGalleryModule() {
  // ─── Data Store: add your images/videos here ───────────────────────
  // type: "image" | "video"
  // src:  path to the file  (relative to index.html)
  // label: short caption shown inside the info bar
  const galleryData = {
    exam: [
      {
        type: "instagram",
        id: "DTPdz9wCPRi",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DTPPFBLiHgL",
        postType: "p",
        i18n: "gallery_exam_moment",
        suffix: " - 2",
      },
      {
        type: "instagram",
        id: "DVtLaPLDLWF",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 3",
      },
      {
        type: "instagram",
        id: "DVsUMDqiPY9rcm20_fLGyIBjXu8YEz-Jz4fCZM0",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 4",
      },
      {
        type: "instagram",
        id: "DVtBka2iEe1",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 5",
      },
      {
        type: "instagram",
        id: "DXYt9QPCNf1",
        postType: "reel",
        i18n: "gallery_exam_moment",
        suffix: " - 6",
      }

    ],
    events: [
      {
        type: "instagram",
        id: "DVQe09OCPIJ",
        i18n: "gallery_event_reel",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DVN0zoCCP--",
        i18n: "gallery_event_reel",
        suffix: " - 2",
      },
      {
        type: "instagram",
        id: "DU-Yz-siM5I",
        i18n: "gallery_event_reel",
        suffix: " - 3",
      },
      {
        type: "instagram",
        id: "DU-YmfmCKGP",
        i18n: "gallery_event_reel",
        suffix: " - 4",
      },
      {
        type: "instagram",
        id: "DTu46kkCHYI",
        i18n: "gallery_event_reel",
        suffix: " - 5",
      },
      {
        type: "instagram",
        id: "DWEtsj0CMBQ",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 6",
      },
      {
        type: "instagram",
        id: "DViLLrEiBdz",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 7",
      },
      {
        type: "instagram",
        id: "DXJtGCoCORp",
        postType: "reel",
        i18n: "gallery_event_reel",
        suffix: " - 8",
      }

    ],
    rooms: [
      {
        type: "instagram",
        id: "DVyqJSNCGt_",
        postType: "reel",
        i18n: "gallery_cat_rooms",
        suffix: " - 1",
      }
    ],
    study: [
      {
        type: "instagram",
        id: "DVtecLDiJMR",
        postType: "reel",
        i18n: "gallery_cat_study",
        suffix: " - 1",
      },
      {
        type: "instagram",
        id: "DVtfSl_iLqE",
        postType: "reel",
        i18n: "gallery_cat_study",
        suffix: " - 2",
      }
    ],
  };

  const catMeta = {
    exam: { icon: "🎓", i18n: "gallery_cat_exam" },
    events: { icon: "🎉", i18n: "gallery_cat_events" },
    rooms: { icon: "🏫", i18n: "gallery_cat_rooms" },
    study: { icon: "📚", i18n: "gallery_cat_study" },
  };

  // ─── DOM refs ────────────────────────────────────────────────────────
  const overlay = document.getElementById("gal-panel-overlay");
  const backdrop = document.getElementById("gal-panel-backdrop");
  const panelBody = document.getElementById("gal-panel-body");
  const panelIcon = document.getElementById("gal-panel-icon");
  const panelTitle = document.getElementById("gal-panel-title");
  const closeBtn = document.getElementById("gal-panel-close");

  const lightbox = document.getElementById("gallery-lightbox");
  const lightboxImg = document.getElementById("lightbox-img");
  const lightboxCaption = document.getElementById("lightbox-caption");
  const lightboxClose = document.getElementById("lightbox-close");
  const lightboxBg = document.getElementById("lightbox-backdrop");

  if (!overlay) return;

  // update media counts on cards
  Object.entries(galleryData).forEach(([cat, items]) => {
    const countEl = document.getElementById(`gal-count-${cat}`);
    if (countEl) countEl.textContent = `${items.length} media`;
  });

  // ─── Open / Close Panel ──────────────────────────────────────────────
  function openPanel(cat) {
    const meta = catMeta[cat] || {};
    const items = galleryData[cat] || [];

    // Update header
    if (panelIcon) panelIcon.textContent = meta.icon || "📷";
    if (panelTitle) panelTitle.textContent = gT(meta.i18n || cat);

    // Build media grid
    if (panelBody) {
      if (items.length === 0) {
        panelBody.innerHTML = `
          <div class="gal-panel-empty">
            <span class="gal-panel-empty-icon">📂</span>
            <p>Bu bölmə üçün hələ media əlavə edilməyib.</p>
          </div>`;
      } else {
        const gridHTML = items.map((item, i) => {
          const delay = `${i * 0.07}s`;

          let label = item.label || "";
          if (item.i18n) {
            label = gT(item.i18n) + (item.suffix || "");
          }

          if (item.type === "instagram") {
            const path = item.postType === "p" ? "p" : "reel";
            return `
              <div class="gal-media-item gal-media-embed" style="animation-delay:${delay}">
                <div class="instagram-embed-container">
                  <iframe src="https://www.instagram.com/${path}/${item.id}/embed" frameborder="0" scrolling="no" allowtransparency="true"></iframe>
                </div>
                <div class="gal-media-info">
                  <span class="gal-media-label">${label || "Instagram Post"}</span>
                  <a href="https://www.instagram.com/${path}/${item.id}/" target="_blank" class="gal-media-zoom" aria-label="Instagramda bax">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>
                  </a>
                </div>
              </div>`;
          }

          if (item.type === "video") {
            return `
              <div class="gal-media-item" style="animation-delay:${delay}" data-src="${item.src}" data-type="video" data-label="${label}">
                <video src="${item.src}" muted loop preload="metadata" playsinline></video>
                <span class="gal-video-badge">▶ VIDEO</span>
                <div class="gal-media-info">
                  <span class="gal-media-label">${label}</span>
                  <button class="gal-media-zoom" aria-label="Böyüt">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                  </button>
                </div>
              </div>`;
          }
          return `
            <div class="gal-media-item" style="animation-delay:${delay}" data-src="${item.src}" data-type="image" data-label="${label}">
              <img src="${item.src}" alt="${label}" loading="lazy">
              <div class="gal-media-info">
                <span class="gal-media-label">${label}</span>
                <button class="gal-media-zoom" aria-label="Böyüt">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                </button>
              </div>
            </div>`;
        }).join("");
        panelBody.innerHTML = `<div class="gal-media-grid">${gridHTML}</div>`;

        // Build lightbox media list (images & videos in this category)
        const viewableItems = [];
        panelBody.querySelectorAll(".gal-media-item:not(.gal-media-embed)").forEach((el, idx) => {
          viewableItems.push({
            src: el.dataset.src,
            label: el.dataset.label || "",
            type: el.dataset.type || "image",
            catTitle: gT(meta.i18n || cat),
          });
          const zoomBtn = el.querySelector(".gal-media-zoom");
          const doOpen = () => openCinemaLightbox(viewableItems, idx);
          el.querySelector("img,video")?.addEventListener("click", doOpen);
          zoomBtn?.addEventListener("click", (e) => {
            e.stopPropagation();
            doOpen();
          });
        });

        // Auto-play videos on hover
        panelBody.querySelectorAll("video").forEach((vid) => {
          vid.closest(".gal-media-item")?.addEventListener("mouseenter", () => vid.play());
          vid.closest(".gal-media-item")?.addEventListener("mouseleave", () => vid.pause());
        });
      }
    }

    overlay.classList.add("active");
    document.documentElement.classList.add("scroll-locked");

    // ── Iris Expand ──────────────────────────────────────
    // origin defaults to center if no event coords
    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    // compute max distance from origin to any corner
    const r = Math.hypot(
      Math.max(ox, window.innerWidth - ox),
      Math.max(oy, window.innerHeight - oy)
    );
    overlay.style.clipPath = `circle(0px at ${ox}px ${oy}px)`;
    overlay.style.transition = 'none';
    // force reflow
    void overlay.offsetHeight;
    overlay.style.transition = 'clip-path 0.55s cubic-bezier(0.4, 0, 0.2, 1)';
    overlay.style.clipPath = `circle(${r * 1.1}px at ${ox}px ${oy}px)`;
  }

  function closePanel() {
    const ox = overlay._irisX ?? window.innerWidth / 2;
    const oy = overlay._irisY ?? window.innerHeight / 2;
    const r = Math.hypot(
      Math.max(ox, window.innerWidth - ox),
      Math.max(oy, window.innerHeight - oy)
    );
    overlay.style.transition = 'clip-path 0.45s cubic-bezier(0.4, 0, 0.2, 1)';
    overlay.style.clipPath = `circle(0px at ${ox}px ${oy}px)`;
    setTimeout(() => {
      overlay.classList.remove("active");
      overlay.style.clipPath = '';
      overlay.style.transition = '';
      document.documentElement.classList.remove("scroll-locked");
      panelBody?.querySelectorAll("video").forEach((v) => v.pause());
    }, 460);
  }

  // ─── Card Click Listeners ────────────────────────────────────────────
  document.querySelectorAll(".gal-card").forEach((card) => {
    card.addEventListener("click", (e) => {
      // store click origin for iris animation
      const rect = card.getBoundingClientRect();
      overlay._irisX = rect.left + rect.width / 2;
      overlay._irisY = rect.top + rect.height / 2;
      openPanel(card.dataset.panel);
    });
  });

  closeBtn?.addEventListener("click", closePanel);
  backdrop?.addEventListener("click", closePanel);

  // ─── Cinema Lightbox & Fullscreen Slideshow (Upgrade 6) ──────────────
  const lightboxVideo = document.getElementById("lightbox-video");
  const lightboxCounter = document.getElementById("lightbox-counter");
  const lightboxCatPill = document.getElementById("lightbox-cat-pill");
  const lightboxPrev = document.getElementById("lightbox-prev");
  const lightboxNext = document.getElementById("lightbox-next");
  const lightboxThumbs = document.getElementById("lightbox-thumbs");
  const lbSlideshowBtn = document.getElementById("lb-slideshow-btn");
  const lbSlideshowLabel = document.getElementById("lb-slideshow-label");
  const lbZoomBtn = document.getElementById("lb-zoom-btn");

  let lbList = [];
  let lbIndex = 0;
  let lbSlideshowTimer = null;
  let lbZoomed = false;

  function stopSlideshow() {
    if (lbSlideshowTimer) {
      clearInterval(lbSlideshowTimer);
      lbSlideshowTimer = null;
    }
    lbSlideshowBtn?.classList.remove("active");
    if (lbSlideshowLabel) lbSlideshowLabel.textContent = "Slayd-Şou";
  }

  function toggleSlideshow() {
    if (lbSlideshowTimer) {
      stopSlideshow();
    } else {
      lbSlideshowBtn?.classList.add("active");
      if (lbSlideshowLabel) lbSlideshowLabel.textContent = "Dayandır";
      lbSlideshowTimer = setInterval(() => {
        stepLightbox(1);
      }, 3600);
    }
  }

  function toggleZoom() {
    lbZoomed = !lbZoomed;
    lightboxImg?.classList.toggle("zoomed", lbZoomed);
    lbZoomBtn?.classList.toggle("active", lbZoomed);
  }

  function renderLightboxItem() {
    if (!lightbox || lbList.length === 0) return;
    const item = lbList[lbIndex];
    lbZoomed = false;
    lightboxImg?.classList.remove("zoomed");
    lbZoomBtn?.classList.remove("active");

    if (lightboxImg) {
      lightboxImg.classList.remove("active");
      lightboxImg.src = "";
    }
    if (lightboxVideo) {
      lightboxVideo.classList.remove("active");
      lightboxVideo.pause();
      lightboxVideo.src = "";
    }

    if (item.type === "video") {
      if (lightboxVideo) {
        lightboxVideo.src = item.src;
        lightboxVideo.classList.add("active");
        lightboxVideo.play().catch(() => { });
      }
    } else {
      if (lightboxImg) {
        lightboxImg.src = item.src;
        lightboxImg.alt = item.label || "BDRNK Qalereya";
        lightboxImg.classList.add("active");
      }
    }

    if (lightboxCaption) lightboxCaption.textContent = item.label || "";
    if (lightboxCounter) lightboxCounter.textContent = `${lbIndex + 1} / ${lbList.length}`;
    if (lightboxCatPill) lightboxCatPill.textContent = item.catTitle || "BDRNK Qalereya";

    if (lightboxThumbs) {
      lightboxThumbs.querySelectorAll(".lb-thumb").forEach((t, idx) => {
        t.classList.toggle("active", idx === lbIndex);
      });
      const activeThumb = lightboxThumbs.querySelector(".lb-thumb.active");
      activeThumb?.scrollIntoView({ behavior: "smooth", inline: "center", block: "nearest" });
    }
  }

  function openCinemaLightbox(list, startIndex = 0) {
    if (!lightbox || !list || list.length === 0) return;
    lbList = list;
    lbIndex = startIndex;
    stopSlideshow();

    if (lightboxThumbs) {
      lightboxThumbs.innerHTML = lbList
        .map((it, idx) => {
          if (it.type === "video") {
            return `<button type="button" class="lb-thumb ${idx === lbIndex ? "active" : ""}" data-idx="${idx}" title="${it.label || "Video"}">
              <span class="lb-thumb-vid">▶</span>
            </button>`;
          }
          return `<button type="button" class="lb-thumb ${idx === lbIndex ? "active" : ""}" data-idx="${idx}" title="${it.label || ""}">
            <img src="${it.src}" alt="" loading="lazy" />
          </button>`;
        })
        .join("");

      lightboxThumbs.querySelectorAll(".lb-thumb").forEach((btn) => {
        btn.addEventListener("click", (e) => {
          e.stopPropagation();
          lbIndex = parseInt(btn.getAttribute("data-idx"), 10) || 0;
          renderLightboxItem();
        });
      });
    }

    renderLightboxItem();
    lightbox.classList.add("active");
  }

  function stepLightbox(dir) {
    if (!lbList.length) return;
    lbIndex = (lbIndex + dir + lbList.length) % lbList.length;
    renderLightboxItem();
  }

  function closeLightbox() {
    stopSlideshow();
    lbZoomed = false;
    lightboxImg?.classList.remove("zoomed");
    lightbox?.classList.remove("active");
    setTimeout(() => {
      if (lightboxImg) lightboxImg.src = "";
      if (lightboxVideo) {
        lightboxVideo.pause();
        lightboxVideo.src = "";
      }
    }, 300);
  }

  lightboxPrev?.addEventListener("click", (e) => {
    e.stopPropagation();
    stepLightbox(-1);
  });
  lightboxNext?.addEventListener("click", (e) => {
    e.stopPropagation();
    stepLightbox(1);
  });
  lbSlideshowBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleSlideshow();
  });
  lbZoomBtn?.addEventListener("click", (e) => {
    e.stopPropagation();
    toggleZoom();
  });
  lightboxImg?.addEventListener("dblclick", toggleZoom);

  // Touch swipe support for mobile devices in Cinema Lightbox
  let lbTouchStartX = 0;
  let lbTouchStartY = 0;
  lightbox?.addEventListener(
    "touchstart",
    (e) => {
      if (!e.touches || !e.touches.length) return;
      lbTouchStartX = e.touches[0].clientX;
      lbTouchStartY = e.touches[0].clientY;
    },
    { passive: true },
  );
  lightbox?.addEventListener(
    "touchend",
    (e) => {
      if (!e.changedTouches || !e.changedTouches.length || lbZoomed) return;
      const dx = e.changedTouches[0].clientX - lbTouchStartX;
      const dy = e.changedTouches[0].clientY - lbTouchStartY;
      if (Math.abs(dx) > 48 && Math.abs(dx) > Math.abs(dy) * 1.4) {
        if (dx < 0) stepLightbox(1);
        else stepLightbox(-1);
      }
    },
    { passive: true },
  );

  lightboxClose?.addEventListener("click", closeLightbox);
  lightboxBg?.addEventListener("click", closeLightbox);
  document.addEventListener("keydown", (e) => {
    if (lightbox?.classList.contains("active")) {
      if (e.key === "Escape") closeLightbox();
      else if (e.key === "ArrowRight") stepLightbox(1);
      else if (e.key === "ArrowLeft") stepLightbox(-1);
      else if (e.key === " ") {
        e.preventDefault();
        toggleSlideshow();
      }
    } else if (e.key === "Escape") {
      const readerModal = document.getElementById("book-reader-modal");
      if (readerModal?.classList.contains("active")) {
        readerModal.classList.remove("active");
        document.documentElement.classList.remove("scroll-locked");
      } else if (overlay?.classList.contains("active")) {
        closePanel();
      }
    }
  });
}

function initTicker() {
  const track = document.getElementById("marquee-track");
  if (!track) return;

  let speedFactor = 1;
  let scrollTimeout;

  // Faster scroll on window scroll
  window.addEventListener(
    "scroll",
    () => {
      speedFactor = 4;
      track.style.animationDuration = `${40 / speedFactor}s`;

      clearTimeout(scrollTimeout);
      scrollTimeout = setTimeout(() => {
        speedFactor = 1;
        track.style.animationDuration = `40s`;
      }, 150);
    },
    { passive: true },
  );

  // Pause on hover
  track.addEventListener("mouseenter", () => {
    track.style.animationPlayState = "paused";
  });
  track.addEventListener("mouseleave", () => {
    track.style.animationPlayState = "running";
  });
}

function initSpotlightCards() {
  const cards = document.querySelectorAll(".bento-cell");
  if (!cards.length) return;

  cards.forEach((card) => {
    card.addEventListener("mousemove", (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.setProperty("--mouse-x", `${x}px`);
      card.style.setProperty("--mouse-y", `${y}px`);
    });

    // Optional: Reset on mouse leave so it doesn't stay glowing at the edge
    card.addEventListener("mouseleave", () => {
      card.style.setProperty("--mouse-x", `50%`);
      card.style.setProperty("--mouse-y", `50%`);
    });
  });
}

function initContextMenu() {
  const cm = document.getElementById("custom-context-menu");
  if (!cm) return;

  // Open Custom Menu
  document.addEventListener("contextmenu", (e) => {
    // Prevent default browser menu
    e.preventDefault();

    let x = e.clientX;
    let y = e.clientY;

    // Keep inside viewport (Width ~ 220px, Height ~ 160px from CSS)
    if (x + 220 > window.innerWidth) x = window.innerWidth - 230;
    if (y + 160 > window.innerHeight) y = window.innerHeight - 170;

    cm.style.left = `${x}px`;
    cm.style.top = `${y}px`;
    cm.classList.add("active");
  });

  // Close Menu on Click Outside
  document.addEventListener("click", (e) => {
    if (!e.target.closest("#custom-context-menu")) {
      cm.classList.remove("active");
    }
  });

  // Close Menu on scroll
  document.addEventListener(
    "scroll",
    () => {
      cm.classList.remove("active");
    },
    { passive: true },
  );

  // Actions
  const btnTheme = document.getElementById("cm-theme-toggle");
  const btnTop = document.getElementById("cm-top");

  if (btnTheme) {
    btnTheme.addEventListener("click", (e) => {
      cm.classList.remove("active");

      // Check current theme and toggle it
      const current = localStorage.getItem("bdrnk-theme") || "light";
      const nextTheme =
        current === "dark" || current === "space" ? "light" : "dark";

      // Re-trigger the modern ripple effect using the header's buttons
      const targetRippleBtn = document.querySelector(
        `.theme-dropdown button[data-theme-set="${nextTheme}"]`,
      );
      if (targetRippleBtn) {
        // Fake the mouse event coordinates so the ripple starts center of screen
        const fakeEvent = new MouseEvent("click", {
          clientX: window.innerWidth / 2,
          clientY: window.innerHeight / 2,
          bubbles: true,
        });
        targetRippleBtn.dispatchEvent(fakeEvent);
      }
    });
  }

  if (btnTop) {
    btnTop.addEventListener("click", () => {
      cm.classList.remove("active");
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }
}

function initPreloader() {
  const preloader = document.getElementById("preloader");
  if (!preloader) return;

  // Minimum display time for effect (e.g. 800ms) + window load time
  const minTime = 800;
  const startTime = Date.now();

  const hidePreloader = () => {
    const elapsed = Date.now() - startTime;
    const remaining = Math.max(0, minTime - elapsed);

    setTimeout(() => {
      preloader.classList.add("fade-out");
      setTimeout(() => {
        preloader.style.display = "none";
      }, 800); // Wait for CSS transition to finish
    }, remaining);
  };

  if (document.readyState === "complete") {
    hidePreloader();
  } else {
    window.addEventListener("load", hidePreloader);
  }
}

function initVideoCarousel() {
  const section = document.getElementById("video-carousel");
  if (!section) return;

  const slides = section.querySelectorAll(".carousel-slide");
  const indicators = section.querySelectorAll(".indicator");
  const progressBars = section.querySelectorAll(".progress");
  let currentSlide = 0;
  const slideDuration = 6000; // 6 seconds per slide
  let timer = null;
  let progressAnimation = null;
  let startTime = null;

  if (slides.length === 0) return;

  // Helper: Pause all videos
  const pauseAllVideos = () => {
    slides.forEach((slide) => {
      const vid = slide.querySelector("video");
      if (vid) vid.pause();
    });
  };

  const goToSlide = (index) => {
    // Stop current animations & timers
    clearTimeout(timer);
    cancelAnimationFrame(progressAnimation);
    progressBars.forEach((p) => (p.style.width = "0%"));

    // Reset old slide
    slides[currentSlide].classList.remove("active");
    indicators[currentSlide].classList.remove("active");

    currentSlide = index;

    // Activate new slide
    slides[currentSlide].classList.add("active");
    indicators[currentSlide].classList.add("active");

    // Play the active video from start
    pauseAllVideos();
    const activeVid = slides[currentSlide].querySelector("video");
    if (activeVid) {
      activeVid.playbackRate = 1.0;
      activeVid.currentTime = 0;
      activeVid.play().catch((e) => console.log("Video autoplay blocked:", e));
    }

    // Start progress bar animation
    startTime = performance.now();
    const activeProgress = indicators[currentSlide].querySelector(".progress");

    const animateProgress = (timestamp) => {
      const elapsed = timestamp - startTime;
      const percentage = Math.min((elapsed / slideDuration) * 100, 100);
      activeProgress.style.width = `${percentage}%`;

      if (elapsed < slideDuration) {
        progressAnimation = requestAnimationFrame(animateProgress);
      }
    };
    progressAnimation = requestAnimationFrame(animateProgress);

    // Schedule next slide
    timer = setTimeout(() => {
      goToSlide((currentSlide + 1) % slides.length);
    }, slideDuration);
  };

  // Indicator Click Events
  indicators.forEach((ind, idx) => {
    ind.addEventListener("click", () => {
      goToSlide(idx);
    });
  });

  // Intersection Observer to Pause/Play when out of view
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // In view: restart slider
          goToSlide(currentSlide);
          // Set lower playback rate for specifically the active slide on load
          const activeVid = slides[currentSlide]?.querySelector("video");
          if (activeVid) activeVid.playbackRate = 1.0;
        } else {
          // Out of view: pause
          clearTimeout(timer);
          cancelAnimationFrame(progressAnimation);
          pauseAllVideos();
        }
      });
    },
    { threshold: 0.1 },
  );

  observer.observe(section);

  // Independent force for main video if script acts as single static video
  const mainVid = document.getElementById("main-carousel-vid");
  if (mainVid) {
    mainVid.playbackRate = 0.25;
  }
}

function initStatsCounter() {
  const stats = document.querySelectorAll(".stat-number");
  const observerOptions = { threshold: 0.5 };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const target = entry.target;
        const countTo = parseInt(target.getAttribute("data-target"));
        const duration = 2000; // 2 seconds
        let startTime = null;

        const step = (timestamp) => {
          if (!startTime) startTime = timestamp;
          const progress = Math.min((timestamp - startTime) / duration, 1);
          target.innerText = Math.floor(progress * countTo);
          if (progress < 1) {
            window.requestAnimationFrame(step);
          } else {
            target.innerText = countTo;
          }
        };

        window.requestAnimationFrame(step);
        observer.unobserve(target);
      }
    });
  }, observerOptions);

  stats.forEach((stat) => observer.observe(stat));
}

/**
 * HERO PARALLAX — Deep 3D Motion (Mouse follow)
 */
function initHeroParallax() {
  const hero = document.getElementById("hero");
  if (!hero || window.matchMedia("(hover: none)").matches) return;

  const glassShapes = hero.querySelectorAll(".glass-shape");

  window.addEventListener("mousemove", (e) => {
    const scrolled = window.scrollY;
    if (scrolled > window.innerHeight) return;

    const { width, height } = hero.getBoundingClientRect();
    const x = e.clientX / width - 0.5;
    const y = e.clientY / height - 0.5;

    // Glass Shapes (Deep Parallax)
    glassShapes.forEach((shape, i) => {
      const factor = (i + 1) * 60;
      const rotate = x * 15;
      shape.style.transform = `translate3d(${x * factor}px, ${y * factor}px, 0) rotate(${rotate}deg)`;
    });

    // Particles Canvas (Medium Parallax)
    const pCanvas = document.getElementById("particles-canvas");
    if (pCanvas) {
      pCanvas.style.transform = `translate3d(${x * 30}px, ${y * 30}px, 0)`;
    }
  });
}

/**
 * GENERATIVE FLUX ENGINE — Noise-based energy flows
 */
function initFluxEngine() {
  const canvas = document.getElementById("flux-canvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");
  let width, height;
  let particles = [];
  let flowField = [];
  let cols, rows;
  let mouse = { x: -1000, y: -1000 };
  const scale = 30; // Scale of the grid
  const particleCount = window.innerWidth < 768 ? 400 : 1200;

  // Simple Noise Implementation
  const noise = {
    seed: Math.random(),
    perlin: function (x, y) {
      return (
        (Math.sin(x * 0.1 + this.seed) + Math.cos(y * 0.1 + this.seed)) * 0.5 +
        0.5
      );
    },
  };

  function resize() {
    width = canvas.parentElement.offsetWidth;
    height = canvas.parentElement.offsetHeight;
    canvas.width = width * window.devicePixelRatio;
    canvas.height = height * window.devicePixelRatio;
    ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
    cols = Math.floor(width / scale) + 1;
    rows = Math.floor(height / scale) + 1;
  }

  class FluxParticle {
    constructor() {
      this.reset();
    }
    reset() {
      this.x = Math.random() * width;
      this.y = Math.random() * height;
      this.prevX = this.x;
      this.prevY = this.y;
      this.vel = { x: 0, y: 0 };
      this.acc = { x: 0, y: 0 };
      this.maxSpeed = Math.random() * 2 + 1;
      this.color = "";
      this.updateColor();
      this.life = Math.random() * 100 + 50;
    }
    updateColor() {
      const isDark = document.body.classList.contains("dark-mode");
      const isSpace = document.body.classList.contains("space-mode");
      if (isSpace)
        this.color = `rgba(168, 85, 247, ${Math.random() * 0.3 + 0.1})`;
      else if (isDark)
        this.color = `rgba(52, 152, 219, ${Math.random() * 0.4 + 0.1})`;
      else this.color = `rgba(27, 79, 114, ${Math.random() * 0.08 + 0.02})`;
    }
    update() {
      const c = Math.floor(this.x / scale);
      const r = Math.floor(this.y / scale);
      const index = c + r * cols;
      const force = flowField[index];

      if (force) {
        this.acc.x += force.x;
        this.acc.y += force.y;
      }

      this.vel.x += this.acc.x;
      this.vel.y += this.acc.y;
      const speed = Math.sqrt(this.vel.x ** 2 + this.vel.y ** 2);
      if (speed > this.maxSpeed) {
        this.vel.x = (this.vel.x / speed) * this.maxSpeed;
        this.vel.y = (this.vel.y / speed) * this.maxSpeed;
      }

      this.prevX = this.x;
      this.prevY = this.y;
      this.x += this.vel.x;
      this.y += this.vel.y;

      // Mouse Vortex Interaction
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < 200) {
        const force = (200 - dist) / 2000;
        this.acc.x += dx * force;
        this.acc.y += dy * force;
      }

      this.acc.x = 0;
      this.acc.y = 0;
      this.life -= 0.5;

      if (
        this.x < 0 ||
        this.x > width ||
        this.y < 0 ||
        this.y > height ||
        this.life < 0
      ) {
        this.reset();
      }
    }
    draw() {
      ctx.beginPath();
      ctx.strokeStyle = this.color;
      ctx.lineWidth = 0.8;
      ctx.moveTo(this.prevX, this.prevY);
      ctx.lineTo(this.x, this.y);
      ctx.stroke();
    }
  }

  function init() {
    resize();
    particles = [];
    for (let i = 0; i < particleCount; i++) {
      particles.push(new FluxParticle());
    }
  }

  function updateFlowField(time) {
    flowField = [];
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const angle =
          noise.perlin(c * 0.5, r * 0.5 + time * 0.001) * Math.PI * 4;
        flowField.push({ x: Math.cos(angle) * 0.1, y: Math.sin(angle) * 0.1 });
      }
    }
  }

  let lastTime = 0;
  function animate(time) {
    if (window.scrollY > window.innerHeight) {
      requestAnimationFrame(animate);
      return;
    }

    const isDark = document.body.classList.contains("dark-mode");
    const isSpace = document.body.classList.contains("space-mode");
    ctx.fillStyle = isSpace
      ? "rgba(5,5,16,0.05)"
      : isDark
        ? "rgba(0,0,0,0.05)"
        : "rgba(255,255,255,0.05)";
    ctx.fillRect(0, 0, width, height);

    updateFlowField(time);

    particles.forEach((p) => {
      p.update();
      p.draw();
    });

    requestAnimationFrame(animate);
  }

  window.addEventListener("resize", init);
  window.addEventListener("mousemove", (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  document.addEventListener("themeChanged", () =>
    particles.forEach((p) => p.updateColor()),
  );
  init();
  requestAnimationFrame(animate);
}

/**
 * 22. SCENE TRANSITION LOGIC
 */
function initSceneTransition() {
  const overlay = document.getElementById("scene-transition");
  if (!overlay) return;

  const triggerTransition = (targetId) => {
    overlay.classList.add("active");

    setTimeout(() => {
      if (targetId === "#") {
        window.scrollTo({ top: 0, behavior: "smooth" });
      } else {
        const target = document.querySelector(targetId);
        if (target) {
          const headerOffset = document.getElementById("site-header")?.offsetHeight || 112;
          const elementPosition = target.getBoundingClientRect().top;
          const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

          window.scrollTo({
            top: offsetPosition,
            behavior: "smooth"
          });
        }
      }

      setTimeout(() => {
        overlay.classList.remove("active");
      }, 600);
    }, 400);
  };

  // Intercept all hash links for the transition effect
  document.addEventListener("click", (e) => {
    const link = e.target.closest('a[href^="#"]');
    if (link) {
      const href = link.getAttribute("href");

      // Ignore if it's a functional link like lightbox/panel triggers without actual hash targets
      if (href.length > 1 || href === "#") {
        e.preventDefault();

        // Close mobile nav if open
        const mobileToggle = document.getElementById("mobile-toggle");
        const mobileNav = document.getElementById("mobile-nav");
        if (mobileToggle && mobileNav && mobileNav.classList.contains("active")) {
          mobileToggle.classList.remove("active");
          mobileNav.classList.remove("active");
          document.documentElement.classList.remove("scroll-locked");
        }

        triggerTransition(href);
      }
    }
  });
}

/* ══════════════════════════════════════════════════════════════
   2. SCROLL REVEAL — IntersectionObserver
   ══════════════════════════════════════════════════════════════ */
(function initScrollReveal() {
  // Auto-tag main sections and cards for reveal
  const REVEAL_SELECTORS = [
    "section",
    ".about-card",
    ".stat-card",
    ".news-card",
    ".team-card",
    ".faq-item",
    ".contact-card",
    ".lib-book",
    ".gal-card",
    ".timeline-item",
    ".major-card",
    ".calendar-item",
    ".lecture-card",
  ];

  REVEAL_SELECTORS.forEach((sel) => {
    document.querySelectorAll(sel).forEach((el, i) => {
      if (!el.classList.contains("reveal") && !el.classList.contains("reveal-group")) {
        el.classList.add("reveal");
        el.style.transitionDelay = `${Math.min(i * 0.06, 0.4)}s`;
      }
    });
  });

  // Stagger grid containers
  [".gal-cards", ".stats-grid", ".news-grid", ".team-grid"].forEach((sel) => {
    document.querySelectorAll(sel).forEach((el) => {
      el.classList.add("reveal-group");
      // Remove individual reveal from direct children if parent is a group
      el.querySelectorAll(":scope > .reveal").forEach((c) => c.classList.remove("reveal"));
    });
  });

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
        observer.unobserve(entry.target); // animate once
      }
    });
  }, { threshold: 0.1, rootMargin: "0px 0px -40px 0px" });

  document.querySelectorAll(".reveal, .reveal-group").forEach((el) => observer.observe(el));
})();

/* ══════════════════════════════════════════════════════════════
   FORMAL HEADING PRESERVATION (Keep <br> and i18n intact)
   ══════════════════════════════════════════════════════════════ */
(function initTextSplit() {
  // Intentionally disabled character-splitting so official multi-line headings
  // and dynamic AZ/RU/EN translations preserve their exact formatting.
})();

/* ══════════════════════════════════════════════════════════════
   GOLDEN HOUR CINEMATIC HERO — 3D PARALLAX & INTERACTIVE LIGHT
   ══════════════════════════════════════════════════════════════ */
(function initGoldenHourHero() {
  const hero = document.getElementById("hero");
  if (!hero) return;

  let rafId = null;

  hero.addEventListener("mousemove", (e) => {
    if (rafId) cancelAnimationFrame(rafId);
    rafId = requestAnimationFrame(() => {
      const rect = hero.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const nx = x / rect.width - 0.5;
      const ny = y / rect.height - 0.5;

      // Spotlight position
      hero.style.setProperty("--mouse-x", `${x}px`);
      hero.style.setProperty("--mouse-y", `${y}px`);

      // Campus background opposite parallax depth
      hero.style.setProperty("--parallax-x", `${(-nx * 22).toFixed(2)}px`);
      hero.style.setProperty("--parallax-y", `${(-ny * 14).toFixed(2)}px`);

      // Subtle 3D perspective tilt on the central glass card
      hero.style.setProperty("--tilt-x", `${(nx * 2.4).toFixed(2)}deg`);
      hero.style.setProperty("--tilt-y", `${(-ny * 1.8).toFixed(2)}deg`);
    });
  });

  hero.addEventListener("mouseleave", () => {
    hero.style.setProperty("--parallax-x", "0px");
    hero.style.setProperty("--parallax-y", "0px");
    hero.style.setProperty("--tilt-x", "0deg");
    hero.style.setProperty("--tilt-y", "0deg");
  });
})();



