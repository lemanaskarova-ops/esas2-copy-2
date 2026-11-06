import os, sys, re, json

base_dir = "/Users/konul/Documents/esas2 copy 2"

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

# 1. Add translations
az_insert = '''    nav_campus: "Kampus & Otaqlar",
    nav_campus_sub: "5 mərtəbəli bina naviqasiyası",
    campus_badge: "Kampus İnfrastrukturu & Bələdçi",
    campus_title: "Tədris Korpusu və Ağıllı Otaq Naviqatoru",
    campus_desc: "5 mərtəbəli əsas tədris korpusumuzun rəqəmsal bələdçisi. Müasir laboratoriyalar, auditoriyalar, inzibati şöbələr və tələbə məkanları üzrə ani axtarış və interaktiv mərtəbə naviqatoru.",'''

en_insert = '''    nav_campus: "Campus & Rooms",
    nav_campus_sub: "5-floor building navigator",
    campus_badge: "Campus Infrastructure & Guide",
    campus_title: "Academic Building & Smart Room Navigator",
    campus_desc: "Digital guide for our 5-story academic campus. Interactive room navigator and instant search across laboratories, lecture halls, administrative offices, and student hubs.",'''

ru_insert = '''    nav_campus: "Кампус и Аудитории",
    nav_campus_sub: "Навигатор по 5 этажам корпуса",
    campus_badge: "Инфраструктура кампуса и гид",
    campus_title: "Учебный корпус и умный навигатор по кабинетам",
    campus_desc: "Цифровой путеводитель по 5-этажному учебному корпусу. Интерактивная навигация и быстрый поиск лабораторий, лекционных залов, административных отделов и студенческих пространств.",'''

if 'nav_campus:' not in js_src:
    # insert into az
    js_src = js_src.replace('nav_library: "Kitabxana",', 'nav_library: "Kitabxana",\n' + az_insert, 1)
    # insert into en
    js_src = js_src.replace('nav_library: "Library",', 'nav_library: "Library",\n' + en_insert, 1)
    # insert into ru
    js_src = js_src.replace('nav_library: "Библиотека",', 'nav_library: "Библиотека",\n' + ru_insert, 1)
    print("Added translations to script.js")

# 2. Add Campus Module at the end of script.js
campus_module_js = r'''
/**
 * ═══════════════════════════════════════════════════════════
 * CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)
 * İnteraktiv Rəqəmsal Kampus Bələdçisi və Ağıllı Otaq Naviqatoru
 * ═══════════════════════════════════════════════════════════
 */
(function initCampusNavigatorModule() {
  const CAMPUS_ROOMS = [
    // ═════════════ I MƏRTƏBƏ (12 Otaq) ═════════════
    {
      id: "f1_107",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 107",
      name: "Qiyabi şöbə",
      cat: "admin",
      catLabel: "İnzibati Şöbə",
      icon: "📋",
      desc: "Qiyabi təhsil alan tələbələrin sənədləşməsi, tədris cədvəli və sessiya imtahanlarının təşkili mərkəzi.",
      features: ["Qiyabi təhsil kabineti", "Tələbə sənədlər fondu", "İmtahan qeydiyyatı"],
      wing: "Qərb qanadı",
      guide: "1-ci mərtəbə, mərkəzi foyedən sola dönərək dəhliz boyu irəliləyin."
    },
    {
      id: "f1_106a",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 106A",
      name: "Hərbi otağı",
      cat: "sport",
      catLabel: "Hərbi Hazırlıq",
      icon: "🎖️",
      desc: "Gənclərin çağırışaqədərki hazırlığı və hərbi vətənpərvərlik tədrisi kabineti.",
      features: ["Tədris stendləri", "Hərbi hazırlıq vəsaitləri", "Mülki müdafiə bazası"],
      wing: "Qərb qanadı",
      guide: "1-ci mərtəbə, 106-cı laboratoriyanın yaxınlığında."
    },
    {
      id: "f1_106",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 106",
      name: "Kimya laboratoriyası №1",
      cat: "lab",
      catLabel: "Laboratoriya",
      icon: "🧪",
      desc: "Kimyəvi tədqiqatlar, reaktivlər və tələbələrin laboratoriya təcrübələri üçün xüsusi avadanlıqlar.",
      features: ["Dartıcı şkaf", "Reaktivlər guşəsi", "Təhlükəsizlik avadanlıqları", "Təcrübə masaları"],
      wing: "Qərb qanadı",
      guide: "1-ci mərtəbə, sol dəhlizdə yerləşir."
    },
    {
      id: "f1_113",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 113",
      name: "Mühasibat şöbəsi (2 otaq daxilində)",
      cat: "admin",
      catLabel: "Maliyyə & Uçot",
      icon: "💰",
      desc: "Kollecin maliyyə-təsərrüfat fəaliyyəti, təqaüd və əməkhaqqı əməliyyatları mərkəzi (2 otaq daxilində).",
      features: ["2 otaq daxilində", "Maliyyə arxivi", "Mühasibat uçotu sistemi"],
      wing: "Şərq qanadı",
      guide: "1-ci mərtəbə, mərkəzi foyedən sağa dönün."
    },
    {
      id: "f1_114",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 114",
      name: "Təsərrüfat işləri üzrə direktor müavini",
      cat: "admin",
      catLabel: "Rəhbərlik & İnzibati",
      icon: "🛠️",
      desc: "Kollecin maddi-texniki təminatı, abadlıq, təhlükəsizlik və infrastruktur idarəetməsi.",
      features: ["İnzibati kabinet", "Təsərrüfat təchizatı", "Texniki nəzarət"],
      wing: "Şərq qanadı",
      guide: "1-ci mərtəbə, sağ dəhlizdə 113-cü otağın yanında."
    },
    {
      id: "f1_115",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 115",
      name: "İstehsalat təcrübə rəhbəri",
      cat: "admin",
      catLabel: "Təcrübə Şöbəsi",
      icon: "🤝",
      desc: "Tələbələrin müəssisələrdə istehsalat və diplomqabağı təcrübələrinin təşkili, karyera mərkəzi.",
      features: ["Təcrübə müqavilələri bazası", "İstehsalat koordinasiyası", "Müəssisələrlə əməkdaşlıq"],
      wing: "Şərq qanadı",
      guide: "1-ci mərtəbə, sağ dəhlizdə yerləşir."
    },
    {
      id: "f1_116",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 116",
      name: "Tərbiyə işləri üzrə direktor müavini",
      cat: "admin",
      catLabel: "Rəhbərlik & İnzibati",
      icon: "🎗️",
      desc: "Tələbələrin sosial-mədəni fəallığı, tədbirlər və vətənpərvərlik layihələrinin koordinasiyası.",
      features: ["İnzibati kabinet", "Gənclər təşkilatı ilə əlaqə", "Tələbə tədbirləri mərkəzi"],
      wing: "Şərq qanadı",
      guide: "1-ci mərtəbə, 115-ci otaqla yanaşı."
    },
    {
      id: "f1_107a",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 107A",
      name: "Telekommunikasiya laboratoriyası",
      cat: "lab",
      catLabel: "Laboratoriya",
      icon: "📡",
      desc: "Simli və simsiz rabitə, optik lifli rabitə xətləri və kommutasiya stendləri ilə təchiz olunmuş laboratoriya.",
      features: ["Optik lif stendləri", "Siqnal generatorları", "Şəbəkə analizatorları", "Ölçmə cihazları"],
      wing: "Qərb qanadı",
      guide: "1-ci mərtəbə, 107-ci otağın qarşısında."
    },
    {
      id: "f1_103",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "№ 103",
      name: "Kimya laboratoriyası №2",
      cat: "lab",
      catLabel: "Laboratoriya",
      icon: "⚗️",
      desc: "Qeyri-üzvi və analitik kimya fənləri üzrə tələbələrin praktiki dərsləri və kimyəvi sınaqlar.",
      features: ["Mikroskoplar", "Analitik tərəzilər", "Kimyəvi reaktivlər fondu"],
      wing: "Qərb qanadı",
      guide: "1-ci mərtəbə, sol qanadın giriş hissəsi."
    },
    {
      id: "f1_kadrlar",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "Kadrlar",
      name: "Kadrlar şöbəsi",
      cat: "admin",
      catLabel: "İnzibati Şöbə",
      icon: "👥",
      desc: "Kollec əməkdaşlarının, professor-müəllim heyətinin şəxsi işləri, əmr layihələri və kadr qeydiyyatı.",
      features: ["Şəxsi işlər arxivi", "Kadr kargüzarlığı", "Müqavilələr fondu"],
      wing: "Mərkəzi korpus",
      guide: "1-ci mərtəbə, mərkəzi pilləkən yaxınlığı."
    },
    {
      id: "f1_comp_lab",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "Komp. Lab",
      name: "Kompüter laboratoriyası",
      cat: "it",
      catLabel: "Kompüter & İKT",
      icon: "🖥️",
      desc: "Yüksək sürətli lokal şəbəkə, proqramlaşdırma və rəqəmsal bacarıqlar üçün kompüter laboratoriyası.",
      features: ["Lokal şəbəkə", "Yüksəksürətli internet", "Proqramlaşdırma mühiti", "Kondisioner"],
      wing: "Mərkəzi korpus",
      guide: "1-ci mərtəbə, tədris bloku."
    },
    {
      id: "f1_sport",
      floor: 1,
      floorText: "I Mərtəbə",
      no: "ZAL",
      name: "İdman zalı (daxilində geyinmə otağı)",
      cat: "sport",
      catLabel: "İdman Kompleksi",
      icon: "⚽",
      desc: "Basketbol, voleybol, mini-futbol, stolüstü tennis və gimnastika üçün geniş müasir idman kompleksi.",
      features: ["Daxilində geyinmə otaqları", "Duş və sanitar qovşaq", "Basketbol və voleybol meydançası", "İdman inventarı"],
      wing: "İdman qanadı",
      guide: "1-ci mərtəbə, mərkəzi dəhlizin sonundan idman korpusuna keçid."
    },

    // ═════════════ II MƏRTƏBƏ (11 Otaq) ═════════════
    {
      id: "f2_director",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "Direktor",
      name: "Direktor otağı (Səbuhi Qurbanov)",
      cat: "admin",
      catLabel: "Rəhbərlik",
      icon: "🏛️",
      desc: "BDRNK direktoru dos. Səbuhi Qurbanovun iş və qəbul otağı, kollecin strateji idarəetmə mərkəzi.",
      features: ["Rəhbərlik kabineti", "Qəbul otağı", "Müşavirə və iclas masası"],
      wing: "Mərkəzi qanad",
      guide: "2-ci mərtəbə, mərkəzi pilləkənlə qalxdıqda qarşıda.",
      action: "director_bio"
    },
    {
      id: "f2_engineer",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "Mühəndis",
      name: "Mühəndis otağı (daxilində FBK otağı 2 otaq)",
      cat: "admin",
      catLabel: "Mühəndislik & FBK",
      icon: "⚙️",
      desc: "Fənn Birləşmə Komissiyası (FBK) və baş mühəndisin texniki xidmət otaqları (2 otaq daxilində).",
      features: ["2 otaq daxilində", "FBK mərkəzi", "Texniki mühəndislik sənədləri"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, sol dəhlizdə yerləşir."
    },
    {
      id: "f2_214",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 214",
      name: "Qeydiyyat, qiymətləndirmə və monitorinq şöbəsi",
      cat: "admin",
      catLabel: "Akademik Qeydiyyat",
      icon: "📊",
      desc: "Tələbələrin akademik göstəriciləri, imtahan nəticələri, transkriptlər və monitorinq sistemi.",
      features: ["Elektron qiymətləndirmə bazası", "İmtahan qeydiyyatı", "Akademik monitorinq"],
      wing: "Şərq qanadı",
      guide: "2-ci mərtəbə, sağ dəhlizdə 214-cü otaq."
    },
    {
      id: "f2_217",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 217",
      name: "Metodiki kabinet",
      cat: "classroom",
      catLabel: "Metodika Kabineti",
      icon: "📑",
      desc: "Tədris proqramları, sillabuslar, metodik vəsaitlər və müəllimlərin ixtisasartırma mərkəzi.",
      features: ["Metodik vəsaitlər fondu", "Tədris planları", "Sillabus arxivi"],
      wing: "Şərq qanadı",
      guide: "2-ci mərtəbə, sağ dəhlizdə yerləşir."
    },
    {
      id: "f2_205",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 205",
      name: "Tədris işləri üzrə direktor müavini",
      cat: "admin",
      catLabel: "Rəhbərlik",
      icon: "🎓",
      desc: "Tədris prosesinin təşkili, akademik cədvəllər və tədris keyfiyyətinin təminatı rəhbərliyi.",
      features: ["İnzibati kabinet", "Tədris idarəetməsi", "Qəbul masası"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, direktor kabinetinə yaxın dəhliz."
    },
    {
      id: "f2_hemkar",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "Həmkar",
      name: "Həmkarlar İttifaqı Komitəsi (Həmkar otağı)",
      cat: "admin",
      catLabel: "Həmkarlar Təşkilatı",
      icon: "🤝",
      desc: "Əməkdaşların və müəllimlərin əmək hüquqlarının və sosial rifahının təminatı otağı.",
      features: ["Həmkarlar təşkilatı", "Sosial dəstək", "Kollektiv müqavilələr"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, sol dəhliz."
    },
    {
      id: "f2_203",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 203",
      name: "Kompüter otağı №1",
      cat: "it",
      catLabel: "Kompüter & İKT",
      icon: "💻",
      desc: "İKT və kompüter texnologiyaları ixtisası tələbələri üçün praktiki dərslər otağı.",
      features: ["Fərdi kompüterlər", "Lokal şəbəkə", "İnternet təminatı"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, sol dəhliz boyunca 203-cü otaq."
    },
    {
      id: "f2_202",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 202",
      name: "Müəllim kabineti (Ceyhun m.)",
      cat: "classroom",
      catLabel: "Müəllim Kabineti",
      icon: "👨‍🏫",
      desc: "İxtisas fənni müəlliminin fərdi iş və tələbələrə fərdi məsləhət kabineti.",
      features: ["Müəllim iş yeri", "Məsləhət güşəsi", "Metodik vəsaitlər"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, 203-cü otağın yanında."
    },
    {
      id: "f2_211",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 211",
      name: "Kompüter otağı №2",
      cat: "it",
      catLabel: "Kompüter & İKT",
      icon: "🖥️",
      desc: "Kompüter qrafikası, şəbəkə inzibatçılığı və proqramlaşdırma dərsləri üçün sinif.",
      features: ["Qrafik kompüterlər", "Proyektor", "Tədris proqramları"],
      wing: "Şərq qanadı",
      guide: "2-ci mərtəbə, sağ dəhlizdə 211-ci otaq."
    },
    {
      id: "f2_201",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 201",
      name: "Kompüter otağı №3",
      cat: "it",
      catLabel: "Kompüter & İKT",
      icon: "💻",
      desc: "İnformasiya texnologiyaları və verilənlər bazası fənlərinin tədrisi üçün müasir kompüter otağı.",
      features: ["İKT avadanlıqları", "Lokal şəbəkə", "İnteraktiv tədris mühiti"],
      wing: "Qərb qanadı",
      guide: "2-ci mərtəbə, sol qanadın başlanğıcı."
    },
    {
      id: "f2_206",
      floor: 2,
      floorText: "II Mərtəbə",
      no: "№ 206",
      name: "Kollec Kitabxanası və Oxu Zalı (2 otaq)",
      cat: "library",
      catLabel: "Kitabxana & Oxu Zalı",
      icon: "📚",
      desc: "22 000-dən çox ümumi kitab fondu, 10 000-dən artıq dərslik və işıqlı oxu zalı (oxu zalı ilə bir yerdə 2 otaq).",
      features: ["2 otaq daxilində", "Geniş oxu zalı", "22 000+ kitab fondu", "Prezident sərəncamı ilə dərsliklər"],
      wing: "Mərkəzi / Şərq",
      guide: "2-ci mərtəbə, mərkəzi foyedən keçərək 206-cı otaq.",
      action: "library_fund"
    },

    // ═════════════ III MƏRTƏBƏ (Cəmi 16 Otaq) ═════════════
    {
      id: "f3_307",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 307",
      name: "Telekommunikasiya şöbəsi",
      cat: "admin",
      catLabel: "Tədris Şöbəsi",
      icon: "📡",
      desc: "Telekommunikasiya sistemləri və rabitə ixtisaslarının tədris və təşkilati idarəetmə mərkəzi.",
      features: ["Şöbə rəhbərliyi", "Tələbə sənədləşməsi", "İxtisas koordinasiyası"],
      wing: "Qərb qanadı",
      guide: "3-cü mərtəbə, sol dəhlizdə 307-ci otaq."
    },
    {
      id: "f3_309",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 309",
      name: "Mühəndis otağı",
      cat: "admin",
      catLabel: "Mühəndislik",
      icon: "📐",
      desc: "Kollecin mühəndis-texniki heyətinin iş və texniki layihələndirmə kabineti.",
      features: ["Texniki avadanlıqlar", "Çertyoj və planlar", "Mühəndis masaları"],
      wing: "Qərb qanadı",
      guide: "3-cü mərtəbə, 307-ci otaqla yanaşı."
    },
    {
      id: "f3_301",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 301",
      name: "Fizika laboratoriyası",
      cat: "lab",
      catLabel: "Laboratoriya",
      icon: "🔬",
      desc: "Mexanika, optika, elektromaqnetizm və dalğa fizikası üzrə praktiki təcrübə stendləri.",
      features: ["Optika qurğuları", "Elektrik ölçmə cihazları", "Laboratoriya stendləri", "Təcrübə masaları"],
      wing: "Qərb qanadı",
      guide: "3-cü mərtəbə, pilləkəndən sola dönərək ilk böyük laboratoriya."
    },
    {
      id: "f3_306",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 306",
      name: "Elektron lövhə otağı",
      cat: "it",
      catLabel: "İnteraktiv Tədris",
      icon: "🖥️",
      desc: "Ağıllı lövhə (Smart Board) və interaktiv multimedia dərs vəsaitləri ilə təchiz olunmuş qabaqcıl auditoriya.",
      features: ["Smart Board elektron lövhə", "Proyektor", "Multimedia tədris proqramları"],
      wing: "Qərb qanadı",
      guide: "3-cü mərtəbə, 306-cı interaktiv auditoriya."
    },
    {
      id: "f3_302",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 302",
      name: "Tədris şöbəsi",
      cat: "admin",
      catLabel: "Tədris Şöbəsi",
      icon: "📚",
      desc: "Dərs cədvəllərinin tərtibi, pedaqoji yükün bölüşdürülməsi və auditoriya fondu idarəçiliyi.",
      features: ["Dərs cədvəli monitoru", "Auditoriya fondu uçotu", "Akademik qrafik"],
      wing: "Mərkəzi korpus",
      guide: "3-cü mərtəbə, mərkəzi pilləkən yaxınlığı."
    },
    {
      id: "f3_303",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "№ 303",
      name: "Müəllimlər otağı",
      cat: "classroom",
      catLabel: "Müəllimlər Otağı",
      icon: "☕",
      desc: "Pedaqoji heyətin dərslərarası istirahəti, metodiki müzakirələr və hazırlıq mərkəzi.",
      features: ["Müəllimlər üçün istirahət guşəsi", "Metodik ədəbiyyat", "İş masaları"],
      wing: "Mərkəzi korpus",
      guide: "3-cü mərtəbə, 302-ci otağın qarşısı."
    },
    {
      id: "f3_auditoriyalar",
      floor: 3,
      floorText: "III Mərtəbə",
      no: "Auditoriyalar",
      name: "10 Mühazirə və Seminar Auditoriyası (Cəmi 16 otaq)",
      cat: "classroom",
      catLabel: "Tədris Fondu",
      icon: "🏛️",
      desc: "III mərtəbə üzrə ümumilikdə 16 otaq mövcuddur; 10 müasir tədris auditoriyası burada yerləşir.",
      features: ["Cəmi 16 otaq fondu", "İşıqlı və geniş mühazirə otaqları", "Müasir partalar və yazı lövhələri"],
      classrooms: ["304", "305", "308", "310", "311", "312", "313", "314", "315", "316"],
      wing: "Bütün mərtəbə boyu",
      guide: "3-cü mərtəbənin sağ və sol qanadlarında yerləşən auditoriyalar."
    },

    // ═════════════ IV MƏRTƏBƏ (Cəmi 17 Otaq) ═════════════
    {
      id: "f4_410",
      floor: 4,
      floorText: "IV Mərtəbə",
      no: "№ 410",
      name: "Poçt laboratoriyası",
      cat: "lab",
      catLabel: "Laboratoriya",
      icon: "📮",
      desc: "Poçt əməliyyatları, bank xidmətləri simulyatorları və logistika qeydiyyatı təlim laboratoriyası.",
      features: ["Poçt əməliyyat stendi", "Barkod və qeydiyyat terminalları", "Tədris kassa simulyatoru"],
      wing: "Şərq qanadı",
      guide: "4-cü mərtəbə, sağ dəhlizdə 410-cu laboratoriya."
    },
    {
      id: "f4_409",
      floor: 4,
      floorText: "IV Mərtəbə",
      no: "№ 409",
      name: "İKT şöbəsi",
      cat: "admin",
      catLabel: "İKT Şöbəsi",
      icon: "💻",
      desc: "İnformasiya-Kommunikasiya Texnologiyaları ixtisaslarının tədris prosesi və şöbə rəhbərliyi.",
      features: ["İKT rəhbərliyi", "Tələbə layihələri arxivi", "Server bağlantısı"],
      wing: "Şərq qanadı",
      guide: "4-cü mərtəbə, 410-cu otaqla yanaşı."
    },
    {
      id: "f4_413",
      floor: 4,
      floorText: "IV Mərtəbə",
      no: "№ 413",
      name: "Poçt rabitəsi və mühasibat uçotu şöbəsi",
      cat: "admin",
      catLabel: "Tədris Şöbəsi",
      icon: "📊",
      desc: "Poçt rabitəsi və mühasibat uçotu ixtisasları üzrə akademik koordinasiya və tələbə qeydiyyatı.",
      features: ["Şöbə müdirliyi", "İxtisas qeydiyyatı", "Tələbə sənədləşməsi"],
      wing: "Şərq qanadı",
      guide: "4-cü mərtəbə, sağ qanadın sonu."
    },
    {
      id: "f4_408",
      floor: 4,
      floorText: "IV Mərtəbə",
      no: "№ 408",
      name: "Proyektor otağı",
      cat: "it",
      catLabel: "Multimedia Auditoriyası",
      icon: "📽️",
      desc: "Mühazirələrin proyektor və audio sistem vasitəsilə vizual təqdimatı üçün multimedia auditoriyası.",
      features: ["Yüksək dəqiqlikli proyektor", "Böyük proyeksiya ekranı", "Audio akustika sistemi"],
      wing: "Qərb qanadı",
      guide: "4-cü mərtəbə, 408-ci multimedia otağı."
    },
    {
      id: "f4_auditoriyalar",
      floor: 4,
      floorText: "IV Mərtəbə",
      no: "Auditoriyalar",
      name: "13 Tədris və Mühazirə Auditoriyası (Cəmi 17 otaq)",
      cat: "classroom",
      catLabel: "Tədris Fondu",
      icon: "🏛️",
      desc: "IV mərtəbə üzrə ümumilikdə 17 otaq mövcuddur; 13 tədris və mühazirə auditoriyası burada fəaliyyət göstərir.",
      features: ["Cəmi 17 otaq fondu", "Təbii havalandırma və işıqlanma", "Akademik mühit"],
      classrooms: ["401", "402", "403", "404", "405", "406", "407", "411", "412", "414", "415", "416", "417"],
      wing: "Bütün mərtəbə boyu",
      guide: "4-cü mərtəbənin dəhlizləri boyu yerləşən tədris auditoriyaları."
    },

    // ═════════════ V MƏRTƏBƏ (Cəmi 18 Otaq) ═════════════
    {
      id: "f5_508",
      floor: 5,
      floorText: "V Mərtəbə",
      no: "№ 508",
      name: "Proyektor otağı",
      cat: "it",
      catLabel: "Multimedia Auditoriyası",
      icon: "📽️",
      desc: "Multimedia təqdimatları, açıq dərslər və seminar mühazirələri üçün proyektorlu auditoriya.",
      features: ["HD Proyektor", "Mühazirə tribunası", "Motorlu proyeksiya pərdəsi"],
      wing: "Qərb qanadı",
      guide: "5-ci mərtəbə, 508-ci auditoriya."
    },
    {
      id: "f5_512",
      floor: 5,
      floorText: "V Mərtəbə",
      no: "№ 512",
      name: "Kompüter texnologiyası şöbəsi",
      cat: "admin",
      catLabel: "İxtisas Şöbəsi",
      icon: "💻",
      desc: "Kompüter sistemləri, şəbəkə inzibatçılığı və proqram təminatı ixtisaslarının akademik rəhbərliyi.",
      features: ["Şöbə müdirliyi", "İxtisas komissiyası", "Tələbə layihələri laboratoriyası"],
      wing: "Şərq qanadı",
      guide: "5-ci mərtəbə, sağ dəhlizdə 512-ci otaq."
    },
    {
      id: "f5_514",
      floor: 5,
      floorText: "V Mərtəbə",
      no: "№ 514",
      name: "Təhsildə keyfiyyətə nəzarət və monitorinq şöbəsi",
      cat: "admin",
      catLabel: "Keyfiyyət & Monitorinq",
      icon: "🎯",
      desc: "Tədrisin keyfiyyət standartlarına uyğunluğunun qiymətləndirilməsi, daxili audit və akkreditasiya mərkəzi.",
      features: ["Keyfiyyət təminatı", "Monitorinq və daxili audit", "Tədris statistikası bazası"],
      wing: "Şərq qanadı",
      guide: "5-ci mərtəbə, sağ dəhlizdə 514-cü otaq."
    },
    {
      id: "f5_auditoriyalar",
      floor: 5,
      floorText: "V Mərtəbə",
      no: "Auditoriyalar",
      name: "15 Tədris və İxtisas Auditoriyası (Cəmi 18 otaq)",
      cat: "classroom",
      catLabel: "Tədris Fondu",
      icon: "🏛️",
      desc: "V mərtəbə üzrə ümumilikdə 18 otaq mövcuddur; 15 mühazirə və qrup seminar otağı fəaliyyət göstərir.",
      features: ["Cəmi 18 otaq fondu", "Sakit və konsentrasiyalı mühit", "Geniş mühazirə otaqları"],
      classrooms: ["501", "502", "503", "504", "505", "506", "507", "509", "510", "511", "513", "515", "516", "517", "518"],
      wing: "Bütün mərtəbə boyu",
      guide: "5-ci mərtəbənin sağ və sol qanadlarında yerləşən auditoriyalar."
    }
  ];

  const FLOOR_CONFIGS = {
    "1": {
      title: "I MƏRTƏBƏ — İdman Kompleksi, Kimya & Rabitə Laboratoriyaları",
      desc: "Kollecin 1-ci mərtəbəsində tələbələrin fiziki hazırlığı üçün idman zalı, 2 kimya laboratoriyası, telekommunikasiya laboratoriyası və inzibati şöbələr yerləşir.",
      countBadge: "12 Əsas Otaq və Məkan",
      icon: "🏢",
      wings: [
        { label: "Qərb Qanadı", text: "107 (Qiyabi), 106A (Hərbi), 106 (Kimya-1), 107A (Telekom), 103 (Kimya-2)", icon: "⬅️" },
        { label: "Mərkəzi", text: "Kadrlar şöbəsi, Kompüter laboratoriyası", icon: "🏛️" },
        { label: "Şərq Qanadı", text: "113 (Mühasibat - 2 otaq), 114 (Təsərrüfat), 115 (Təcrübə), 116 (Tərbiyə)", icon: "➡️" },
        { label: "İdman", text: "İdman zalı (geyinmə otağı ilə)", icon: "⚽" }
      ]
    },
    "2": {
      title: "II MƏRTƏBƏ — Kollec Rəhbərliyi, Əsas Kitabxana & Kompüter Mərkəzləri",
      desc: "2-ci mərtəbədə direktorluq, müavinliklər, 3 kompüter otağı, metodiki kabinet və 22 000-dən çox kitab fondu olan zəngin Kitabxana & Oxu Zalı (206) fəaliyyət göstərir.",
      countBadge: "11 Əsas Otaq və Mərkəz",
      icon: "🏛️",
      wings: [
        { label: "Mərkəzi Qanad", text: "Direktor otağı (dos. Səbuhi Qurbanov)", icon: "🏛️" },
        { label: "Qərb Qanadı", text: "205 (Tədris müavini), Həmkar otağı, Mühəndis (FBK 2 otaq), 201, 203 (Kompüter), 202 (Ceyhun m.)", icon: "⬅️" },
        { label: "Şərq Qanadı", text: "214 (Qeydiyyat & Monitorinq), 217 (Metodiki kabinet), 211 (Kompüter otağı)", icon: "➡️" },
        { label: "Kitabxana", text: "206 - Kitabxana və Oxu Zalı (2 otaq daxilində)", icon: "📚" }
      ]
    },
    "3": {
      title: "III MƏRTƏBƏ — Fizika Laboratoriyası, Tədris Şöbəsi & 16 Auditoriya",
      desc: "3-cü mərtəbə tələbələrin əsas mühazirə və təcrübə məkanlarındandır. Burada müasir fizika laboratoriyası, elektron smart-lövhə otağı və cəmi 16 otaq fondu yerləşir.",
      countBadge: "Cəmi 16 Otaq Fondu",
      icon: "🔬",
      wings: [
        { label: "Qərb Qanadı", text: "301 (Fizika lab), 306 (Elektron lövhə), 307 (Telekom şöbəsi), 309 (Mühəndis)", icon: "⬅️" },
        { label: "Mərkəzi Korpus", text: "302 (Tədris şöbəsi), 303 (Müəllimlər otağı)", icon: "🏛️" },
        { label: "Tədris Fondu", text: "10 Mühazirə və Seminar Auditoriyası (Cəmi 16 otaq)", icon: "🎓" }
      ]
    },
    "4": {
      title: "IV MƏRTƏBƏ — İKT və Poçt Rabitəsi Şöbələri, Poçt Laboratoriyası & 17 Auditoriya",
      desc: "4-cü mərtəbədə rabitə və informasiya texnologiyaları ixtisaslarının tədris mərkəzi, poçt laboratoriyası, multimedia proyektor otağı və 17 auditoriya yerləşir.",
      countBadge: "Cəmi 17 Otaq Fondu",
      icon: "📮",
      wings: [
        { label: "Şərq Qanadı", text: "410 (Poçt laboratoriyası), 409 (İKT şöbəsi), 413 (Poçt rabitəsi və mühasibat)", icon: "➡️" },
        { label: "Qərb Qanadı", text: "408 (Proyektor multimedia auditoriyası)", icon: "⬅️" },
        { label: "Tədris Fondu", text: "13 Tədris və Mühazirə Auditoriyası (Cəmi 17 otaq)", icon: "🎓" }
      ]
    },
    "5": {
      title: "V MƏRTƏBƏ — Kompüter Texnologiyaları Şöbəsi, Keyfiyyət Təminatı & 18 Auditoriya",
      desc: "5-ci mərtəbə proqramlaşdırma və kompüter ixtisasları, təhsildə keyfiyyətə nəzarət və monitorinq şöbəsi və 18 geniş auditoriyadan ibarətdir.",
      countBadge: "Cəmi 18 Otaq Fondu",
      icon: "🎯",
      wings: [
        { label: "Şərq Qanadı", text: "512 (Kompüter texnologiyası şöbəsi), 514 (Keyfiyyətə nəzarət və monitorinq)", icon: "➡️" },
        { label: "Qərb Qanadı", text: "508 (Proyektorlu konfrans və tədris auditoriyası)", icon: "⬅️" },
        { label: "Tədris Fondu", text: "15 Tədris və İxtisas Seminar Otağı (Cəmi 18 otaq)", icon: "🎓" }
      ]
    },
    "all": {
      title: "BÜTÜN MƏRTƏBƏLƏR — Əsas Tədris Korpusu Üzrə Tam Rəqəmsal Xəritə",
      desc: "I mərtəbədən V mərtəbəyədək bütün 80+ auditoriya, ixtisas laboratoriyaları, rəhbərlik otaqları və kitabxana kompleksinin vahid bələdçisi.",
      countBadge: "5 Mərtəbə · 80+ Otaq",
      icon: "🏢",
      wings: [
        { label: "I Mərtəbə", text: "İdman kompleksi, Kimya və Telekommunikasiya laboratoriyaları", icon: "1️⃣" },
        { label: "II Mərtəbə", text: "Direktorluq, Kitabxana və Oxu Zalı (206), Kompüter otaqları", icon: "2️⃣" },
        { label: "III Mərtəbə", text: "Fizika laboratoriyası (301), Elektron lövhə (306), 16 otaq", icon: "3️⃣" },
        { label: "IV Mərtəbə", text: "Poçt laboratoriyası (410), İKT şöbəsi (409), 17 otaq", icon: "4️⃣" },
        { label: "V Mərtəbə", text: "Kompüter texnologiyası (512), Keyfiyyət (514), 18 otaq", icon: "5️⃣" }
      ]
    }
  };

  let activeFloor = "1";
  let activeCat = "all";
  let searchQuery = "";

  const floorBtns = document.querySelectorAll(".campus-floor-btn");
  const catBtns = document.querySelectorAll("#campus-cat-filters .campus-chip");
  const searchInput = document.getElementById("campus-search-input");
  const clearSearchBtn = document.getElementById("campus-search-clear");
  const roomsGrid = document.getElementById("campus-rooms-grid");
  const countText = document.getElementById("campus-rooms-count-text");
  const floorBanner = document.getElementById("campus-floor-banner");

  // Modal elements
  const modal = document.getElementById("campus-room-modal");
  const modalClose = document.getElementById("crm-close-btn");
  const modalFooterClose = document.getElementById("crm-footer-close");
  const mFloorBadge = document.getElementById("crm-floor-badge");
  const mRoomBadge = document.getElementById("crm-room-badge");
  const mCatBadge = document.getElementById("crm-cat-badge");
  const mIconBox = document.getElementById("crm-icon-box");
  const mTitle = document.getElementById("crm-title");
  const mDesc = document.getElementById("crm-desc");
  const mFeatures = document.getElementById("crm-features");
  const mLoc = document.getElementById("crm-loc");
  const mRoute = document.getElementById("crm-route");
  const mFooter = document.getElementById("crm-footer");

  function openRoomModal(room) {
    if (!modal || !room) return;
    if (mFloorBadge) mFloorBadge.textContent = room.floorText || (room.floor + "-ci Mərtəbə");
    if (mRoomBadge) mRoomBadge.textContent = room.no;
    if (mCatBadge) {
      mCatBadge.textContent = room.catLabel || room.cat;
      mCatBadge.className = "campus-modal-cat-badge cat-" + room.cat;
    }
    if (mIconBox) mIconBox.textContent = room.icon || "🚪";
    if (mTitle) mTitle.textContent = room.name;
    if (mDesc) mDesc.textContent = room.desc;

    if (mFeatures) {
      mFeatures.innerHTML = "";
      if (room.features && room.features.length) {
        room.features.forEach(feat => {
          const tag = document.createElement("span");
          tag.className = "room-feature-tag";
          tag.textContent = feat;
          mFeatures.appendChild(tag);
        });
      }
      if (room.classrooms && room.classrooms.length) {
        const audBlock = document.createElement("div");
        audBlock.className = "room-aud-pills-wrap";
        audBlock.style.width = "100%";
        audBlock.style.marginTop = "10px";
        audBlock.innerHTML = "<span class=\"room-aud-pills-title\">Mərtəbədəki auditoriyalar:</span>";
        const grid = document.createElement("div");
        grid.className = "room-aud-pills-grid";
        room.classrooms.forEach(aud => {
          const pill = document.createElement("span");
          pill.className = "room-aud-num";
          pill.textContent = "№ " + aud;
          grid.appendChild(pill);
        });
        audBlock.appendChild(grid);
        mFeatures.appendChild(audBlock);
      }
    }

    if (mLoc) mLoc.textContent = (room.floorText || (room.floor + "-ci Mərtəbə")) + ", " + (room.wing || "Əsas bina");
    if (mRoute) mRoute.textContent = room.guide || "Mərkəzi pilləkən və ya dəhliz boyu yönəlin.";

    // Modal action buttons
    if (mFooter) {
      mFooter.innerHTML = "";
      if (room.action === "library_fund") {
        const btnFund = document.createElement("button");
        btnFund.type = "button";
        btnFund.className = "btn room-card-btn-action";
        btnFund.innerHTML = "📖 Kitabxana Fondunu Aç";
        btnFund.addEventListener("click", () => {
          closeRoomModal();
          if (typeof window.openLibraryFundModal === "function") {
            window.openLibraryFundModal();
          }
        });
        mFooter.appendChild(btnFund);
      } else if (room.action === "director_bio") {
        const btnBio = document.createElement("button");
        btnBio.type = "button";
        btnBio.className = "btn room-card-btn-action";
        btnBio.innerHTML = "👤 Səbuhi Qurbanov Bioqrafiyasını Oxu";
        btnBio.addEventListener("click", () => {
          closeRoomModal();
          if (typeof window.openDirectorBioModal === "function") {
            window.openDirectorBioModal();
          }
        });
        mFooter.appendChild(btnBio);
      }
      const btnClose = document.createElement("button");
      btnClose.type = "button";
      btnClose.className = "btn btn-secondary";
      btnClose.textContent = "Bağla";
      btnClose.addEventListener("click", closeRoomModal);
      mFooter.appendChild(btnClose);
    }

    modal.classList.add("active");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeRoomModal() {
    if (!modal) return;
    modal.classList.remove("active");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
  }

  window.openCampusRoomModal = openRoomModal;
  window.closeCampusRoomModal = closeRoomModal;

  if (modalClose) modalClose.addEventListener("click", closeRoomModal);
  if (modalFooterClose) modalFooterClose.addEventListener("click", closeRoomModal);
  if (modal) {
    modal.addEventListener("click", (e) => {
      if (e.target === modal) closeRoomModal();
    });
  }
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal && modal.classList.contains("active")) {
      closeRoomModal();
    }
  });

  function updateFloorBanner() {
    if (!floorBanner) return;
    const cfg = FLOOR_CONFIGS[activeFloor] || FLOOR_CONFIGS["all"];
    let wingsHtml = "";
    if (cfg.wings && cfg.wings.length) {
      wingsHtml = cfg.wings.map(w =>
        `<span class="cfb-wing-chip">${w.icon} <strong>${w.label}:</strong> ${w.text}</span>`
      ).join("");
    }
    floorBanner.innerHTML = `
      <div class="cfb-header">
        <div class="cfb-title-wrap">
          <span class="cfb-floor-icon">${cfg.icon}</span>
          <div>
            <h3 class="cfb-title">${cfg.title}</h3>
            <p class="cfb-desc">${cfg.desc}</p>
          </div>
        </div>
        <span class="cfb-badge-count">${cfg.countBadge}</span>
      </div>
      <div class="cfb-wings">${wingsHtml}</div>
    `;
  }

  function renderRooms() {
    if (!roomsGrid) return;

    const q = (searchQuery || "").trim().toLowerCase();

    // Check if query is looking for a specific classroom number (e.g., "305", "410", "514")
    let targetRooms = CAMPUS_ROOMS.filter(room => {
      // 1. Floor match
      if (activeFloor !== "all" && String(room.floor) !== String(activeFloor)) {
        // If there's an active query matching this room specifically, we can still include it or let user search all floors
        if (!q) return false;
      }

      // 2. Category match
      if (activeCat !== "all" && room.cat !== activeCat) {
        if (!q) return false;
      }

      // 3. Search query match
      if (q) {
        const matchNo = (room.no || "").toLowerCase().includes(q);
        const matchName = (room.name || "").toLowerCase().includes(q);
        const matchDesc = (room.desc || "").toLowerCase().includes(q);
        const matchWing = (room.wing || "").toLowerCase().includes(q);
        const matchFeatures = (room.features || []).some(f => f.toLowerCase().includes(q));
        const matchClassrooms = (room.classrooms || []).some(c => c.toLowerCase().includes(q));
        if (!matchNo && !matchName && !matchDesc && !matchWing && !matchFeatures && !matchClassrooms) {
          return false;
        }
      }

      return true;
    });

    if (countText) {
      if (q) {
        countText.innerHTML = `Axtarış nəticəsi: <strong>${targetRooms.length}</strong> otaq tapıldı`;
      } else {
        const floorLabel = activeFloor === "all" ? "Bütün mərtəbələr üzrə" : `${activeFloor}-ci Mərtəbə üzrə`;
        countText.innerHTML = `${floorLabel} göstərilən otaqlar: <strong>${targetRooms.length}</strong>`;
      }
    }

    if (targetRooms.length === 0) {
      roomsGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; background: var(--surface); border: 1px dashed var(--border); border-radius: 14px;">
          <div style="font-size: 2.5rem; margin-bottom: 12px;">🔍</div>
          <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--text); margin-bottom: 6px;">Axtarış üzrə otaq tapılmadı</h4>
          <p style="font-size: 0.88rem; color: var(--text-dim); max-width: 450px; margin: 0 auto 16px;">
            Daxil etdiyiniz meyar üzrə heç bir otaq və ya laboratoriya aşkar edilmədi. Zəhmət olmasa başqa otaq nömrəsi və ya ad daxil edin.
          </p>
          <button type="button" class="btn btn-secondary" id="campus-reset-filters-btn">Bütün Otaqları Göstər</button>
        </div>
      `;
      const resetBtn = document.getElementById("campus-reset-filters-btn");
      if (resetBtn) {
        resetBtn.addEventListener("click", () => {
          activeFloor = "1";
          activeCat = "all";
          searchQuery = "";
          if (searchInput) searchInput.value = "";
          if (clearSearchBtn) clearSearchBtn.style.display = "none";
          floorBtns.forEach(b => b.classList.toggle("active", b.getAttribute("data-floor") === "1"));
          catBtns.forEach(b => b.classList.toggle("active", b.getAttribute("data-cat") === "all"));
          updateFloorBanner();
          renderRooms();
        });
      }
      return;
    }

    roomsGrid.innerHTML = targetRooms.map(room => {
      const featTags = (room.features || []).map(f => `<span class="room-feature-tag">${escapeHTML ? escapeHTML(f) : f}</span>`).join("");
      let audPills = "";
      if (room.classrooms && room.classrooms.length) {
        const audBadges = room.classrooms.map(c => `<span class="room-aud-num" data-room-num="${c}">№ ${c}</span>`).join("");
        audPills = `
          <div class="room-aud-pills-wrap">
            <span class="room-aud-pills-title">Auditoriya nömrələri (${room.classrooms.length} otaq):</span>
            <div class="room-aud-pills-grid">${audBadges}</div>
          </div>
        `;
      }

      let extraActionBtn = "";
      if (room.action === "library_fund") {
        extraActionBtn = `<button type="button" class="room-card-btn room-card-btn-action" data-action="library_fund">📖 Kitabxana Fondu</button>`;
      } else if (room.action === "director_bio") {
        extraActionBtn = `<button type="button" class="room-card-btn room-card-btn-action" data-action="director_bio">👤 Bioqrafiya</button>`;
      }

      return `
        <article class="campus-room-card" data-room-id="${room.id}">
          <div class="room-card-top">
            <div class="room-badge-group">
              <span class="room-num-pill">${room.no}</span>
              <span class="room-cat-tag cat-${room.cat}">${room.catLabel}</span>
            </div>
            <span class="room-floor-tag">${room.floorText}</span>
          </div>

          <div class="room-title-row">
            <div class="room-icon-box">${room.icon}</div>
            <div>
              <h3 class="room-title">${escapeHTML ? escapeHTML(room.name) : room.name}</h3>
              <p class="room-desc">${escapeHTML ? escapeHTML(room.desc) : room.desc}</p>
            </div>
          </div>

          <div class="room-tags-wrap">${featTags}</div>
          ${audPills}

          <div class="room-wing-hint">
            <span>📍</span>
            <span>${escapeHTML ? escapeHTML(room.wing) : room.wing}</span>
          </div>

          <div class="room-card-actions">
            ${extraActionBtn}
            <button type="button" class="room-card-btn room-card-btn-primary" data-action="inspect">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line><line x1="12" y1="8" x2="12.01" y2="8"></line></svg>
              Ətraflı Bələdçi
            </button>
          </div>
        </article>
      `;
    }).join("");

    // Attach event listeners to card buttons and classroom numbers
    roomsGrid.querySelectorAll(".campus-room-card").forEach(card => {
      const roomId = card.getAttribute("data-room-id");
      const room = CAMPUS_ROOMS.find(r => r.id === roomId);
      if (!room) return;

      const inspectBtn = card.querySelector('[data-action="inspect"]');
      if (inspectBtn) {
        inspectBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          openRoomModal(room);
        });
      }

      const libBtn = card.querySelector('[data-action="library_fund"]');
      if (libBtn) {
        libBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          if (typeof window.openLibraryFundModal === "function") {
            window.openLibraryFundModal();
          }
        });
      }

      const bioBtn = card.querySelector('[data-action="director_bio"]');
      if (bioBtn) {
        bioBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          if (typeof window.openDirectorBioModal === "function") {
            window.openDirectorBioModal();
          }
        });
      }

      // Clicking anywhere on card (except buttons) opens modal
      card.addEventListener("click", (e) => {
        if (!e.target.closest("button") && !e.target.closest(".room-aud-num")) {
          openRoomModal(room);
        }
      });

      // Clicking individual classroom numbers
      card.querySelectorAll(".room-aud-num").forEach(numEl => {
        numEl.addEventListener("click", (e) => {
          e.stopPropagation();
          const audNum = numEl.getAttribute("data-room-num");
          openRoomModal({
            floor: room.floor,
            floorText: room.floorText,
            no: "№ " + audNum,
            name: "Auditoriya № " + audNum,
            cat: "classroom",
            catLabel: "Tədris Auditoriyası",
            icon: "🎓",
            desc: room.floorText + " üzrə yerləşən işıqlı və tədris vəsaitləri ilə təchiz olunmuş auditoriya.",
            features: ["Tədris lövhəsi", "Partalar", "Təbii havalandırma", "İşıqlandırma sistemi"],
            wing: room.wing,
            guide: room.floorText + ", dəhliz boyunca " + audNum + "-ci otaq qapısına yaxınlaşın."
          });
        });
      });
    });
  }

  // Bind Floor Buttons
  floorBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const floor = btn.getAttribute("data-floor");
      activeFloor = floor;
      floorBtns.forEach(b => {
        const isCurrent = b === btn;
        b.classList.toggle("active", isCurrent);
        b.setAttribute("aria-selected", isCurrent ? "true" : "false");
      });
      updateFloorBanner();
      renderRooms();
    });
  });

  // Bind Category Chips
  catBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const cat = btn.getAttribute("data-cat");
      activeCat = cat;
      catBtns.forEach(b => b.classList.toggle("active", b === btn));
      renderRooms();
    });
  });

  // Bind Search Input
  if (searchInput) {
    searchInput.addEventListener("input", () => {
      searchQuery = searchInput.value;
      if (clearSearchBtn) {
        clearSearchBtn.style.display = searchQuery ? "block" : "none";
      }
      renderRooms();
    });
  }

  if (clearSearchBtn) {
    clearSearchBtn.addEventListener("click", () => {
      searchQuery = "";
      if (searchInput) {
        searchInput.value = "";
        searchInput.focus();
      }
      clearSearchBtn.style.display = "none";
      renderRooms();
    });
  }

  // Initial render
  updateFloorBanner();
  renderRooms();

  // Re-render on language change
  document.addEventListener("languageChanged", () => {
    updateFloorBanner();
    renderRooms();
  });
})();
'''

if "CAMPUS & ROOM NAVIGATOR CONTROLLER" not in js_src:
    js_src += "\n\n" + campus_module_js
    print("Appended Campus Navigator Module to script.js")

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(js_src)

# Also update scratch backup
with open(os.path.join(base_dir, "scratch/script_working_backup.js"), "w", encoding="utf-8") as f:
    f.write(js_src)

print("script.js and scratch/script_working_backup.js synchronized successfully.")
