import os, sys

base_dir = "/Users/konul/Documents/esas2 copy 2"

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

pos_mod = js_src.find('/**\n * ═══════════════════════════════════════════════════════════\n * CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)')
if pos_mod == -1:
    pos_mod = js_src.find('CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)')
    pos_mod = js_src.rfind('/**', 0, pos_mod)

assert pos_mod != -1, "Could not find Campus Navigator Controller start"

base_js = js_src[:pos_mod].rstrip()

new_module = r'''/**
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Mərkəzi korpus"
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
      wing: "Mərkəzi korpus"
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
      desc: "Basketbol, voleybol, mini-futbol, stolüstü tennis və gimnastika üçün geniş müasir idman kompleksi (daxilində geyinmə otağı ilə).",
      features: ["Daxilində geyinmə otaqları", "Duş və sanitar qovşaq", "Basketbol və voleybol meydançası", "İdman inventarı"],
      wing: "İdman korpusu"
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
      wing: "Qərb qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Mərkəzi korpus"
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
      wing: "Mərkəzi korpus"
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
      wing: "Bütün mərtəbə boyu"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Qərb qanadı"
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
      wing: "Bütün mərtəbə boyu"
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
      wing: "Qərb qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Şərq qanadı"
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
      wing: "Bütün mərtəbə boyu"
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

    let targetRooms = CAMPUS_ROOMS.filter(room => {
      // 1. Floor match
      if (activeFloor !== "all" && String(room.floor) !== String(activeFloor)) {
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
        const audBadges = room.classrooms.map(c => `<span class="room-aud-num">№ ${c}</span>`).join("");
        audPills = `
          <div class="room-aud-pills-wrap">
            <span class="room-aud-pills-title">Auditoriya nömrələri (${room.classrooms.length} otaq):</span>
            <div class="room-aud-pills-grid">${audBadges}</div>
          </div>
        `;
      }

      // Only render special action button when there is actual dedicated content
      let actionsHtml = "";
      if (room.action === "library_fund") {
        actionsHtml = `
          <div class="room-card-actions">
            <button type="button" class="room-card-btn room-card-btn-action" data-action="library_fund">
              📖 Kitabxana Fondu və Tarixi
            </button>
          </div>
        `;
      } else if (room.action === "director_bio") {
        actionsHtml = `
          <div class="room-card-actions">
            <button type="button" class="room-card-btn room-card-btn-action" data-action="director_bio">
              👤 Səbuhi Qurbanov Bioqrafiyası
            </button>
          </div>
        `;
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

          ${actionsHtml}
        </article>
      `;
    }).join("");

    // Attach event listeners strictly to actionable buttons
    roomsGrid.querySelectorAll(".campus-room-card").forEach(card => {
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

full_js = base_js + "\n\n" + new_module

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(full_js)

with open(os.path.join(base_dir, "scratch/script_working_backup.js"), "w", encoding="utf-8") as f:
    f.write(full_js)

print("script.js updated and synchronized with backup.")
