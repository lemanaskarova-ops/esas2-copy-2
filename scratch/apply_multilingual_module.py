import os, sys

base_dir = "/Users/konul/Documents/esas2 copy 2"

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

pos_mod = js_src.find('CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)')
pos_mod = js_src.rfind('/**', 0, pos_mod)
assert pos_mod != -1, "Module start not found"

base_js = js_src[:pos_mod].rstrip()

multilingual_module = r'''/**
 * ═══════════════════════════════════════════════════════════
 * CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)
 * İnteraktiv Rəqəmsal Kampus Bələdçisi və Ağıllı Otaq Naviqatoru
 * 100% Çoxdilli (AZ, EN, RU) Dəstəkli Mühərrik
 * ═══════════════════════════════════════════════════════════
 */
(function initCampusNavigatorModule() {
  const CAMPUS_ROOMS = [
    // ═════════════ I MƏRTƏBƏ (12 Otaq) ═════════════
    {
      id: "f1_107",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 107",
      name_az: "Qiyabi şöbə", name_en: "Distance Learning Department", name_ru: "Заочное отделение",
      cat: "admin",
      catLabel_az: "İnzibati Şöbə", catLabel_en: "Administrative Dept", catLabel_ru: "Административный отдел",
      icon: "📋",
      desc_az: "Qiyabi təhsil alan tələbələrin sənədləşməsi, tədris cədvəli və sessiya imtahanlarının təşkili mərkəzi.",
      desc_en: "Coordination of documentation, academic schedules, and examination sessions for distance learning students.",
      desc_ru: "Организация документации, учебных графиков и экзаменационных сессий для студентов заочного отделения.",
      features_az: ["Qiyabi təhsil kabineti", "Tələbə sənədlər fondu", "İmtahan qeydiyyatı"],
      features_en: ["Distance learning office", "Student archives", "Exam registration"],
      features_ru: ["Кабинет заочного обучения", "Студенческий архив", "Экзаменационный учет"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f1_106a",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 106A",
      name_az: "Hərbi otağı", name_en: "Military Training Room", name_ru: "Военный кабинет",
      cat: "sport",
      catLabel_az: "Hərbi Hazırlıq", catLabel_en: "Military Training", catLabel_ru: "Военная подготовка",
      icon: "🎖️",
      desc_az: "Gənclərin çağırışaqədərki hazırlığı və hərbi vətənpərvərlik tədrisi kabineti.",
      desc_en: "Classroom for pre-conscription military training and civil defense education.",
      desc_ru: "Кабинет допризывной подготовки молодежи и военно-патриотического воспитания.",
      features_az: ["Tədris stendləri", "Hərbi hazırlıq vəsaitləri", "Mülki müdafiə bazası"],
      features_en: ["Training stands", "Military visual aids", "Civil defense aids"],
      features_ru: ["Учебные стенды", "Военные пособия", "База гражданской обороны"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f1_106",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 106",
      name_az: "Kimya laboratoriyası №1", name_en: "Chemistry Laboratory No. 1", name_ru: "Химическая лаборатория №1",
      cat: "lab",
      catLabel_az: "Laboratoriya", catLabel_en: "Laboratory", catLabel_ru: "Лаборатория",
      icon: "🧪",
      desc_az: "Kimyəvi tədqiqatlar, reaktivlər və tələbələrin laboratoriya təcrübələri üçün xüsusi avadanlıqlar.",
      desc_en: "Specialized equipment for chemical synthesis, reactions, and practical student experiments.",
      desc_ru: "Специализированное оборудование для химических исследований, реактивов и практических опытов.",
      features_az: ["Dartıcı şkaf", "Reaktivlər guşəsi", "Təhlükəsizlik avadanlıqları", "Təcrübə masaları"],
      features_en: ["Fume hood", "Reagent corner", "Safety gear", "Experiment benches"],
      features_ru: ["Вытяжной шкаф", "Уголок реактивов", "Средства защиты", "Лабораторные столы"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f1_113",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 113",
      name_az: "Mühasibat şöbəsi (2 otaq daxilində)", name_en: "Accounting Department (2 rooms)", name_ru: "Бухгалтерия (2 кабинета)",
      cat: "admin",
      catLabel_az: "Maliyyə & Uçot", catLabel_en: "Finance & Accounting", catLabel_ru: "Финансы и Учет",
      icon: "💰",
      desc_az: "Kollecin maliyyə-təsərrüfat fəaliyyəti, təqaüd və əməkhaqqı əməliyyatları mərkəzi (2 otaq daxilində).",
      desc_en: "Financial operations, payroll management, and student scholarship processing (within 2 rooms).",
      desc_ru: "Финансово-хозяйственный центр колледжа, начисление зарплат и стипендий (в 2 кабинетах).",
      features_az: ["2 otaq daxilində", "Maliyyə arxivi", "Mühasibat uçotu sistemi"],
      features_en: ["Within 2 rooms", "Financial archive", "Accounting software"],
      features_ru: ["В пределах 2 комнат", "Финансовый архив", "Бухгалтерская система"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f1_114",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 114",
      name_az: "Təsərrüfat işləri üzrə direktor müavini", name_en: "Deputy Director for Economic Affairs", name_ru: "Замдиректора по хозяйственной части",
      cat: "admin",
      catLabel_az: "Rəhbərlik & İnzibati", catLabel_en: "Leadership & Admin", catLabel_ru: "Руководство и Администрация",
      icon: "🛠️",
      desc_az: "Kollecin maddi-texniki təminatı, abadlıq, təhlükəsizlik və infrastruktur idarəetməsi.",
      desc_en: "Logistical management, facility safety, infrastructure maintenance, and supply services.",
      desc_ru: "Материально-техническое обеспечение, безопасность помещений, снабжение и эксплуатация здания.",
      features_az: ["İnzibati kabinet", "Təsərrüfat təchizatı", "Texniki nəzarət"],
      features_en: ["Executive office", "Facility supplies", "Technical supervision"],
      features_ru: ["Административный кабинет", "Хозяйственный инвентарь", "Технадзор"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f1_115",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 115",
      name_az: "İstehsalat təcrübə rəhbəri", name_en: "Industrial Internship Coordinator", name_ru: "Руководитель производственной практики",
      cat: "admin",
      catLabel_az: "Təcrübə Şöbəsi", catLabel_en: "Internship Dept", catLabel_ru: "Отдел практики",
      icon: "🤝",
      desc_az: "Tələbələrin müəssisələrdə istehsalat və diplomqabağı təcrübələrinin təşkili, karyera mərkəzi.",
      desc_en: "Organization of internships, career development, and industrial partner relationships.",
      desc_ru: "Организация производственной и преддипломной практики на предприятиях, карьерный центр.",
      features_az: ["Təcrübə müqavilələri bazası", "İstehsalat koordinasiyası", "Müəssisələrlə əməkdaşlıq"],
      features_en: ["Internship database", "Industrial coordination", "Corporate partnerships"],
      features_ru: ["База договоров о практике", "Координация стажировок", "Связь с предприятиями"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f1_116",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 116",
      name_az: "Tərbiyə işləri üzrə direktor müavini", name_en: "Deputy Director for Student Affairs", name_ru: "Замдиректора по воспитательной работе",
      cat: "admin",
      catLabel_az: "Rəhbərlik & İnzibati", catLabel_en: "Leadership & Admin", catLabel_ru: "Руководство и Администрация",
      icon: "🎗️",
      desc_az: "Tələbələrin sosial-mədəni fəallığı, tədbirlər və vətənpərvərlik layihələrinin koordinasiyası.",
      desc_en: "Student life leadership, cultural initiatives, youth clubs, and civic projects coordination.",
      desc_ru: "Координация культурных инициатив, студенческих клубов и молодежных патриотических проектов.",
      features_az: ["İnzibati kabinet", "Gənclər təşkilatı ilə əlaqə", "Tələbə tədbirləri mərkəzi"],
      features_en: ["Administrative office", "Youth organizations liaison", "Student events center"],
      features_ru: ["Административный кабинет", "Связь с молодежными союзами", "Центр студенческих мероприятий"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f1_107a",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 107A",
      name_az: "Telekommunikasiya laboratoriyası", name_en: "Telecommunications Laboratory", name_ru: "Телекоммуникационная лаборатория",
      cat: "lab",
      catLabel_az: "Laboratoriya", catLabel_en: "Laboratory", catLabel_ru: "Лаборатория",
      icon: "📡",
      desc_az: "Simli və simsiz rabitə, optik lifli rabitə xətləri və kommutasiya stendləri ilə təchiz olunmuş laboratoriya.",
      desc_en: "Modern lab equipped with optical fiber lines, telecom switching units, and signal analyzers.",
      desc_ru: "Современная лаборатория оптоволоконных линий, телекоммутационных стендов и анализаторов сигналов.",
      features_az: ["Optik lif stendləri", "Siqnal generatorları", "Şəbəkə analizatorları", "Ölçmə cihazları"],
      features_en: ["Fiber optics stands", "Signal generators", "Network analyzers", "Testing devices"],
      features_ru: ["Оптоволоконные стенды", "Генераторы сигналов", "Сетевые анализаторы", "Измерительные приборы"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f1_103",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "№ 103",
      name_az: "Kimya laboratoriyası №2", name_en: "Chemistry Laboratory No. 2", name_ru: "Химическая лаборатория №2",
      cat: "lab",
      catLabel_az: "Laboratoriya", catLabel_en: "Laboratory", catLabel_ru: "Лаборатория",
      icon: "⚗️",
      desc_az: "Qeyri-üzvi və analitik kimya fənləri üzrə tələbələrin praktiki dərsləri və kimyəvi sınaqlar.",
      desc_en: "Analytical and inorganic chemistry research facility for experimental student courseworks.",
      desc_ru: "Исследовательский кабинет аналитической и неорганической химии для лабораторных работ.",
      features_az: ["Mikroskoplar", "Analitik tərəzilər", "Kimyəvi reaktivlər fondu"],
      features_en: ["Microscopes", "Analytical balances", "Chemical reagents stock"],
      features_ru: ["Микроскопы", "Аналитические весы", "Фонд химических реактивов"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f1_kadrlar",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "Kadrlar",
      name_az: "Kadrlar şöbəsi", name_en: "Human Resources Department", name_ru: "Отдел кадров",
      cat: "admin",
      catLabel_az: "İnzibati Şöbə", catLabel_en: "Administrative Dept", catLabel_ru: "Административный отдел",
      icon: "👥",
      desc_az: "Kollec əməkdaşlarının, professor-müəllim heyətinin şəxsi işləri, əmr layihələri və kadr qeydiyyatı.",
      desc_en: "Faculty and personnel records management, official staff decrees, and employment registry.",
      desc_ru: "Учет личных дел преподавателей и сотрудников, проекты кадровых приказов и трудовой реестр.",
      features_az: ["Şəxsi işlər arxivi", "Kadr kargüzarlığı", "Müqavilələr fondu"],
      features_en: ["Personal files archive", "HR paperwork", "Contracts fund"],
      features_ru: ["Архив личных дел", "Кадровое делопроизводство", "Фонд договоров"],
      wing_az: "Mərkəzi korpus", wing_en: "Central Wing", wing_ru: "Центральный корпус"
    },
    {
      id: "f1_comp_lab",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "Komp. Lab",
      name_az: "Kompüter laboratoriyası", name_en: "Computer Laboratory", name_ru: "Компьютерная лаборатория",
      cat: "it",
      catLabel_az: "Kompüter & İKT", catLabel_en: "Computer & IT", catLabel_ru: "Компьютеры и ИКТ",
      icon: "🖥️",
      desc_az: "Yüksək sürətli lokal şəbəkə, proqramlaşdırma və rəqəmsal bacarıqlar üçün kompüter laboratoriyası.",
      desc_en: "Equipped with high-speed LAN, IDE environments, and digital development tools.",
      desc_ru: "Оснащена высокоскоростной локальной сетью, средами программирования и ПК.",
      features_az: ["Lokal şəbəkə", "Yüksəksürətli internet", "Proqramlaşdırma mühiti", "Kondisioner"],
      features_en: ["Local LAN network", "High-speed Internet", "Programming tools", "Climate control"],
      features_ru: ["Локальная сеть", "Высокоскоростной интернет", "Среды разработки", "Кондиционер"],
      wing_az: "Mərkəzi korpus", wing_en: "Central Wing", wing_ru: "Центральный корпус"
    },
    {
      id: "f1_sport",
      floor: 1,
      floorText_az: "I Mərtəbə", floorText_en: "1st Floor", floorText_ru: "1-й Этаж",
      no: "ZAL",
      name_az: "İdman zalı (daxilində geyinmə otağı)", name_en: "Sports Complex & Gym (with locker rooms)", name_ru: "Спортивный зал (с раздевалками)",
      cat: "sport",
      catLabel_az: "İdman Kompleksi", catLabel_en: "Sports Complex", catLabel_ru: "Спорткомплекс",
      icon: "⚽",
      desc_az: "Basketbol, voleybol, mini-futbol, stolüstü tennis və gimnastika üçün geniş müasir idman kompleksi.",
      desc_en: "Spacious gymnasium for basketball, volleyball, futsal, table tennis, and athletics.",
      desc_ru: "Просторный спортзал для баскетбола, волейбола, мини-футбола, настольного тенниса и атлетики.",
      features_az: ["Daxilində geyinmə otaqları", "Duş və sanitar qovşaq", "Basketbol və voleybol meydançası", "İdman inventarı"],
      features_en: ["Locker rooms inside", "Showers and facilities", "Basketball & volleyball courts", "Sports equipment"],
      features_ru: ["Раздевалки внутри", "Душевые и санузел", "Баскетбольная площадка", "Спортивный инвентарь"],
      wing_az: "İdman korpusu", wing_en: "Sports Wing", wing_ru: "Спортивное крыло"
    },

    // ═════════════ II MƏRTƏBƏ (11 Otaq) ═════════════
    {
      id: "f2_director",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "Direktor",
      name_az: "Direktor otağı (Səbuhi Qurbanov)", name_en: "Director's Office (Assoc. Prof. Sebuhi Gurbanov)", name_ru: "Кабинет директора (доц. Сабухи Гурбанов)",
      cat: "admin",
      catLabel_az: "Rəhbərlik", catLabel_en: "Leadership", catLabel_ru: "Руководство",
      icon: "🏛️",
      desc_az: "BDRNK direktoru dos. Səbuhi Qurbanovun iş və qəbul otağı, kollecin strateji idarəetmə mərkəzi.",
      desc_en: "Executive office of BDRNK Director Assoc. Prof. Sebuhi Gurbanov, college leadership and reception.",
      desc_ru: "Рабочий кабинет директора колледжа доц. Сабухи Гурбанова, центр стратегического руководства.",
      features_az: ["Rəhbərlik kabineti", "Qəbul otağı", "Müşavirə və iclas masası"],
      features_en: ["Executive office", "Reception room", "Conference meeting table"],
      features_ru: ["Кабинет директора", "Приемная комната", "Стол для совещаний"],
      wing_az: "Mərkəzi qanad", wing_en: "Central Wing", wing_ru: "Центральное крыло",
      action: "director_bio"
    },
    {
      id: "f2_engineer",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "Mühəndis",
      name_az: "Mühəndis otağı (daxilində FBK otağı 2 otaq)", name_en: "Engineering & Subject Commission (2 rooms)", name_ru: "Инженерный кабинет (включая ПЦК, 2 комнаты)",
      cat: "admin",
      catLabel_az: "Mühəndislik & FBK", catLabel_en: "Engineering & Commission", catLabel_ru: "Инженерия и ПЦК",
      icon: "⚙️",
      desc_az: "Fənn Birləşmə Komissiyası (FBK) və baş mühəndisin texniki xidmət otaqları (2 otaq daxilində).",
      desc_en: "Offices for subject commission coordinators and chief engineering technical maintenance.",
      desc_ru: "Кабинеты предметных цикловых комиссий (ПЦК) и службы главного инженера (2 совмещенные комнаты).",
      features_az: ["2 otaq daxilində", "FBK mərkəzi", "Texniki mühəndislik sənədləri"],
      features_en: ["Within 2 rooms", "Subject commission hub", "Engineering documentation"],
      features_ru: ["В составе 2 комнат", "Центр ПЦК", "Инженерная документация"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_214",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 214",
      name_az: "Qeydiyyat, qiymətləndirmə və monitorinq şöbəsi", name_en: "Registration, Assessment & Monitoring", name_ru: "Отдел регистрации, оценивания и мониторинга",
      cat: "admin",
      catLabel_az: "Akademik Qeydiyyat", catLabel_en: "Academic Registry", catLabel_ru: "Академический реестр",
      icon: "📊",
      desc_az: "Tələbələrin akademik göstəriciləri, imtahan nəticələri, transkriptlər və monitorinq sistemi.",
      desc_en: "Academic grading records, exam results administration, transcript services, and monitoring.",
      desc_ru: "Учет успеваемости студентов, результаты экзаменов, оформление транскриптов и мониторинг.",
      features_az: ["Elektron qiymətləndirmə bazası", "İmtahan qeydiyyatı", "Akademik monitorinq"],
      features_en: ["Electronic gradebook", "Exam registrar", "Academic monitoring"],
      features_ru: ["Электронный журнал", "Реестр экзаменов", "Академический мониторинг"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f2_217",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 217",
      name_az: "Metodiki kabinet", name_en: "Methodological Cabinet", name_ru: "Методический кабинет",
      cat: "classroom",
      catLabel_az: "Metodika Kabineti", catLabel_en: "Methodology Cabinet", catLabel_ru: "Методический кабинет",
      icon: "📑",
      desc_az: "Tədris proqramları, sillabuslar, metodik vəsaitlər və müəllimlərin ixtisasartırma mərkəzi.",
      desc_en: "Curriculum plans, teaching guidelines, syllabi archives, and pedagogical training.",
      desc_ru: "Учебные планы, методические пособия, фонд силлабусов и повышение квалификации преподавателей.",
      features_az: ["Metodik vəsaitlər fondu", "Tədris planları", "Sillabus arxivi"],
      features_en: ["Methodology collection", "Curriculum plans", "Syllabi archive"],
      features_ru: ["Методический фонд", "Учебные планы", "Архив силлабусов"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f2_205",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 205",
      name_az: "Tədris işləri üzrə direktor müavini", name_en: "Deputy Director for Academic Affairs", name_ru: "Замдиректора по учебной работе",
      cat: "admin",
      catLabel_az: "Rəhbərlik", catLabel_en: "Leadership", catLabel_ru: "Руководство",
      icon: "🎓",
      desc_az: "Tədris prosesinin təşkili, akademik cədvəllər və tədris keyfiyyətinin təminatı rəhbərliyi.",
      desc_en: "Overall management of the academic process, curriculum scheduling, and pedagogical standards.",
      desc_ru: "Организация учебного процесса, академические расписания и обеспечение качества преподавания.",
      features_az: ["İnzibati kabinet", "Tədris idarəetməsi", "Qəbul masası"],
      features_en: ["Executive office", "Academic management", "Advisory desk"],
      features_ru: ["Административный кабинет", "Учебное управление", "Приемная зона"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_hemkar",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "Həmkar",
      name_az: "Həmkarlar İttifaqı Komitəsi (Həmkar otağı)", name_en: "Trade Union Committee Office", name_ru: "Профсоюзный комитет",
      cat: "admin",
      catLabel_az: "Həmkarlar Təşkilatı", catLabel_en: "Trade Union", catLabel_ru: "Профсоюз",
      icon: "🤝",
      desc_az: "Əməkdaşların və müəllimlərin əmək hüquqlarının və sosial rifahının təminatı otağı.",
      desc_en: "Representation of labor rights, social benefits, and collective contracts for staff and teachers.",
      desc_ru: "Защита трудовых прав сотрудников, социальное обеспечение и профсоюзная деятельность.",
      features_az: ["Həmkarlar təşkilatı", "Sosial dəstək", "Kollektiv müqavilələr"],
      features_en: ["Union committee", "Social support", "Collective agreements"],
      features_ru: ["Профсоюзная организация", "Социальная поддержка", "Коллективные договоры"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_203",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 203",
      name_az: "Kompüter otağı №1", name_en: "Computer Room No. 1", name_ru: "Компьютерный класс №1",
      cat: "it",
      catLabel_az: "Kompüter & İKT", catLabel_en: "Computer & IT", catLabel_ru: "Компьютеры и ИКТ",
      icon: "💻",
      desc_az: "İKT və kompüter texnologiyaları ixtisası tələbələri üçün praktiki dərslər otağı.",
      desc_en: "Hands-on computing lab for students in information systems and digital technology programs.",
      desc_ru: "Практический класс для студентов специальностей ИКТ и компьютерных технологий.",
      features_az: ["Fərdi kompüterlər", "Lokal şəbəkə", "İnternet təminatı"],
      features_en: ["Personal workstations", "Local LAN", "Internet access"],
      features_ru: ["Рабочие станции", "Локальная сеть", "Доступ в интернет"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_202",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 202",
      name_az: "Müəllim kabineti (Ceyhun m.)", name_en: "Faculty Office (Instructor Jeyhun)", name_ru: "Кабинет преподавателя (Джейхун м.)",
      cat: "classroom",
      catLabel_az: "Müəllim Kabineti", catLabel_en: "Faculty Office", catLabel_ru: "Кабинет преподавателя",
      icon: "👨‍🏫",
      desc_az: "İxtisas fənni müəlliminin fərdi iş və tələbələrə fərdi məsləhət kabineti.",
      desc_en: "Private office for specialized discipline instructor consultations and student advising.",
      desc_ru: "Рабочий кабинет преподавателя специальных дисциплин и индивидуальных консультаций.",
      features_az: ["Müəllim iş yeri", "Məsləhət guşəsi", "Metodik vəsaitlər"],
      features_en: ["Teacher workspace", "Advising corner", "Teaching guides"],
      features_ru: ["Рабочее место преподавателя", "Зона консультаций", "Методические материалы"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_211",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 211",
      name_az: "Kompüter otağı №2", name_en: "Computer Room No. 2", name_ru: "Компьютерный класс №2",
      cat: "it",
      catLabel_az: "Kompüter & İKT", catLabel_en: "Computer & IT", catLabel_ru: "Компьютеры и ИКТ",
      icon: "🖥️",
      desc_az: "Kompüter qrafikası, şəbəkə inzibatçılığı və proqramlaşdırma dərsləri üçün sinif.",
      desc_en: "Dedicated classroom for computer graphics, network administration, and coding.",
      desc_ru: "Аудитория компьютерной графики, сетевого администрирования и программирования.",
      features_az: ["Qrafik kompüterlər", "Proyektor", "Tədris proqramları"],
      features_en: ["Graphics workstations", "Projector", "Educational software"],
      features_ru: ["Графические ПК", "Проектор", "Учебные программы"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f2_201",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 201",
      name_az: "Kompüter otağı №3", name_en: "Computer Room No. 3", name_ru: "Компьютерный класс №3",
      cat: "it",
      catLabel_az: "Kompüter & İKT", catLabel_en: "Computer & IT", catLabel_ru: "Компьютеры и ИКТ",
      icon: "💻",
      desc_az: "İnformasiya texnologiyaları və verilənlər bazası fənlərinin tədrisi üçün müasir kompüter otağı.",
      desc_en: "Modern computing lab for databases, algorithms, and practical software design.",
      desc_ru: "Современный компьютерный класс для баз данных, алгоритмов и практического ПО.",
      features_az: ["İKT avadanlıqları", "Lokal şəbəkə", "İnteraktiv tədris mühiti"],
      features_en: ["IT equipment", "Local network", "Interactive learning environment"],
      features_ru: ["ИКТ оборудование", "Локальная сеть", "Интерактивная среда"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f2_206",
      floor: 2,
      floorText_az: "II Mərtəbə", floorText_en: "2nd Floor", floorText_ru: "2-й Этаж",
      no: "№ 206",
      name_az: "Kollec Kitabxanası və Oxu Zalı (2 otaq)", name_en: "College Library & Reading Hall (2 rooms)", name_ru: "Библиотека колледжа и Читальный зал (2 комнаты)",
      cat: "library",
      catLabel_az: "Kitabxana & Oxu Zalı", catLabel_en: "Library & Reading Hall", catLabel_ru: "Библиотека и Читальный зал",
      icon: "📚",
      desc_az: "22 000-dən çox ümumi kitab fondu, 10 000-dən artıq dərslik və işıqlı oxu zalı (oxu zalı ilə bir yerdə 2 otaq).",
      desc_en: "Rich collection exceeding 22,000 books, 10,000+ textbooks, and a serene reading hall (within 2 rooms).",
      desc_ru: "Богатый фонд из более 22 000 книг, свыше 10 000 учебников и светлый читальный зал (в составе 2 комнат).",
      features_az: ["2 otaq daxilində", "Geniş oxu zalı", "22 000+ kitab fondu", "Prezident sərəncamı ilə dərsliklər"],
      features_en: ["Within 2 rooms", "Spacious reading hall", "22,000+ book fund", "Presidential decree textbooks"],
      features_ru: ["В пределах 2 комнат", "Просторный читальный зал", "Фонд 22 000+ книг", "Учебники по президентскому указу"],
      wing_az: "Mərkəzi / Şərq", wing_en: "Central / East Wing", wing_ru: "Центральное / Восточное крыло",
      action: "library_fund"
    },

    // ═════════════ III MƏRTƏBƏ (Cəmi 16 Otaq) ═════════════
    {
      id: "f3_307",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 307",
      name_az: "Telekommunikasiya şöbəsi", name_en: "Telecommunications Department", name_ru: "Отделение телекоммуникаций",
      cat: "admin",
      catLabel_az: "Tədris Şöbəsi", catLabel_en: "Academic Dept", catLabel_ru: "Учебное отделение",
      icon: "📡",
      desc_az: "Telekommunikasiya sistemləri və rabitə ixtisaslarının tədris və təşkilati idarəetmə mərkəzi.",
      desc_en: "Academic management and curriculum coordination for telecommunication systems majors.",
      desc_ru: "Центр организации учебного процесса для специальностей телекоммуникаций и связи.",
      features_az: ["Şöbə rəhbərliyi", "Tələbə sənədləşməsi", "İxtisas koordinasiyası"],
      features_en: ["Department chair", "Student records", "Curriculum coordination"],
      features_ru: ["Заведующий отделением", "Студенческая документация", "Координация специальности"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f3_309",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 309",
      name_az: "Mühəndis otağı", name_en: "Engineering Office", name_ru: "Инженерный кабинет",
      cat: "admin",
      catLabel_az: "Mühəndislik", catLabel_en: "Engineering", catLabel_ru: "Инженерия",
      icon: "📐",
      desc_az: "Kollecin mühəndis-texniki heyətinin iş və texniki layihələndirmə kabineti.",
      desc_en: "Technical team office for engineering design, campus wiring, and infrastructure blueprints.",
      desc_ru: "Рабочий кабинет инженерно-технического персонала по проектированию и обслуживанию.",
      features_az: ["Texniki avadanlıqlar", "Çertyoj və planlar", "Mühəndis masaları"],
      features_en: ["Technical equipment", "Blueprints & layouts", "Engineering workstations"],
      features_ru: ["Техническое оснащение", "Чертежи и схемы", "Инженерные столы"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f3_301",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 301",
      name_az: "Fizika laboratoriyası", name_en: "Physics Laboratory", name_ru: "Физическая лаборатория",
      cat: "lab",
      catLabel_az: "Laboratoriya", catLabel_en: "Laboratory", catLabel_ru: "Лаборатория",
      icon: "🔬",
      desc_az: "Mexanika, optika, elektromaqnetizm və dalğa fizikası üzrə praktiki təcrübə stendləri.",
      desc_en: "Practical experimental stands covering mechanics, optics, electromagnetism, and wave physics.",
      desc_ru: "Практические стенды по механике, оптике, электромагнетизму и волновой физике.",
      features_az: ["Optika qurğuları", "Elektrik ölçmə cihazları", "Laboratoriya stendləri", "Təcrübə masaları"],
      features_en: ["Optics apparatus", "Electrical meters", "Lab benches", "Experiment tables"],
      features_ru: ["Оптические установки", "Электроизмерители", "Лабораторные стенды", "Экспериментальные столы"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f3_306",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 306",
      name_az: "Elektron lövhə otağı", name_en: "Smart Board Interactive Classroom", name_ru: "Интерактивная аудитория со смарт-доской",
      cat: "it",
      catLabel_az: "İnteraktiv Tədris", catLabel_en: "Interactive Classroom", catLabel_ru: "Интерактивное обучение",
      icon: "🖥️",
      desc_az: "Ağıllı lövhə (Smart Board) və interaktiv multimedia dərs vəsaitləri ilə təchiz olunmuş qabaqcıl auditoriya.",
      desc_en: "Equipped with interactive Smart Board touchscreens and multimedia visual teaching software.",
      desc_ru: "Оснащена интерактивной смарт-доской и мультимедийными учебными программами.",
      features_az: ["Smart Board elektron lövhə", "Proyektor", "Multimedia tədris proqramları"],
      features_en: ["Smart Board touchscreen", "HD projector", "Multimedia lesson aids"],
      features_ru: ["Электронная смарт-доска", "HD проектор", "Мультимедийные пособия"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f3_302",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 302",
      name_az: "Tədris şöbəsi", name_en: "Academic Affairs Division", name_ru: "Учебный отдел",
      cat: "admin",
      catLabel_az: "Tədris Şöbəsi", catLabel_en: "Academic Division", catLabel_ru: "Учебный отдел",
      icon: "📚",
      desc_az: "Dərs cədvəllərinin tərtibi, pedaqoji yükün bölüşdürülməsi və auditoriya fondu idarəçiliyi.",
      desc_en: "Timetable scheduling, faculty teaching load allocation, and classroom allocation management.",
      desc_ru: "Составление расписания занятий, распределение педагогической нагрузки и аудиторного фонда.",
      features_az: ["Dərs cədvəli monitoru", "Auditoriya fondu uçotu", "Akademik qrafik"],
      features_en: ["Timetable monitor", "Classroom allocation", "Academic timeline"],
      features_ru: ["Монитор расписания", "Учет аудиторного фонда", "Академический график"],
      wing_az: "Mərkəzi korpus", wing_en: "Central Wing", wing_ru: "Центральный корпус"
    },
    {
      id: "f3_303",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "№ 303",
      name_az: "Müəllimlər otağı", name_en: "Faculty Lounge & Teachers' Room", name_ru: "Учительская комната",
      cat: "classroom",
      catLabel_az: "Müəllimlər Otağı", catLabel_en: "Faculty Lounge", catLabel_ru: "Учительская",
      icon: "☕",
      desc_az: "Pedaqoji heyətin dərslərarası istirahəti, metodiki müzakirələr və hazırlıq mərkəzi.",
      desc_en: "Comfortable faculty lounge for inter-lecture rest, lesson preparation, and peer collaboration.",
      desc_ru: "Комната отдыха преподавателей между парами, методические дискуссии и подготовка к занятиям.",
      features_az: ["Müəllimlər üçün istirahət guşəsi", "Metodik ədəbiyyat", "İş masaları"],
      features_en: ["Rest lounge area", "Methodological literature", "Workstations"],
      features_ru: ["Зона отдыха преподавателей", "Методическая литература", "Рабочие столы"],
      wing_az: "Mərkəzi korpus", wing_en: "Central Wing", wing_ru: "Центральный корпус"
    },
    {
      id: "f3_auditoriyalar",
      floor: 3,
      floorText_az: "III Mərtəbə", floorText_en: "3rd Floor", floorText_ru: "3-й Этаж",
      no: "Auditoriyalar",
      name_az: "10 Mühazirə və Seminar Auditoriyası (Cəmi 16 otaq)", name_en: "10 Lecture & Seminar Classrooms (Total 16 rooms)", name_ru: "10 лекционных и семинарских аудиторий (Всего 16 комнат)",
      cat: "classroom",
      catLabel_az: "Tədris Fondu", catLabel_en: "Classrooms Fund", catLabel_ru: "Учебный фонд",
      icon: "🏛️",
      desc_az: "III mərtəbə üzrə ümumilikdə 16 otaq mövcuddur; 10 müasir tədris auditoriyası burada yerləşir.",
      desc_en: "3rd floor houses 16 rooms in total; 10 modern lecture and seminar classrooms are located here.",
      desc_ru: "На 3-м этаже всего 16 кабинетов; здесь расположено 10 современных лекционных и семинарских аудиторий.",
      features_az: ["Cəmi 16 otaq fondu", "İşıqlı və geniş mühazirə otaqları", "Müasir partalar və yazı lövhələri"],
      features_en: ["Total 16 room capacity", "Bright and spacious halls", "Modern desks and whiteboards"],
      features_ru: ["Всего 16 помещений", "Светлые и просторные залы", "Современные парты и доски"],
      classrooms: ["304", "305", "308", "310", "311", "312", "313", "314", "315", "316"],
      wing_az: "Bütün mərtəbə boyu", wing_en: "Across the Floor", wing_ru: "По всему этажу"
    },

    // ═════════════ IV MƏRTƏBƏ (Cəmi 17 Otaq) ═════════════
    {
      id: "f4_410",
      floor: 4,
      floorText_az: "IV Mərtəbə", floorText_en: "4th Floor", floorText_ru: "4-й Этаж",
      no: "№ 410",
      name_az: "Poçt laboratoriyası", name_en: "Postal & Logistics Laboratory", name_ru: "Почтовая лаборатория",
      cat: "lab",
      catLabel_az: "Laboratoriya", catLabel_en: "Laboratory", catLabel_ru: "Лаборатория",
      icon: "📮",
      desc_az: "Poçt əməliyyatları, bank xidmətləri simulyatorları və logistika qeydiyyatı təlim laboratoriyası.",
      desc_en: "Training laboratory equipped for postal operations, banking services simulation, and shipment sorting.",
      desc_ru: "Учебно-практическая лаборатория почтовых операций, банковских услуг и сортировки отправлений.",
      features_az: ["Poçt əməliyyat stendi", "Barkod və qeydiyyat terminalları", "Tədris kassa simulyatoru"],
      features_en: ["Postal operations stand", "Barcode and registration terminals", "Cashier simulation"],
      features_ru: ["Стенд почтовых операций", "Терминалы штрихкодов и учета", "Учебная кассовая зона"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f4_409",
      floor: 4,
      floorText_az: "IV Mərtəbə", floorText_en: "4th Floor", floorText_ru: "4-й Этаж",
      no: "№ 409",
      name_az: "İKT şöbəsi", name_en: "Information Technologies Department", name_ru: "Отделение ИКТ",
      cat: "admin",
      catLabel_az: "İKT Şöbəsi", catLabel_en: "IT Department", catLabel_ru: "Отделение ИКТ",
      icon: "💻",
      desc_az: "İnformasiya-Kommunikasiya Texnologiyaları ixtisaslarının tədris prosesi və şöbə rəhbərliyi.",
      desc_en: "Academic administration and development oversight for ICT and communication majors.",
      desc_ru: "Учебно-методическое руководство и координация специальностей сферы ИКТ и связи.",
      features_az: ["İKT rəhbərliyi", "Tələbə layihələri arxivi", "Server bağlantısı"],
      features_en: ["IT department chair", "Student projects archive", "Server infrastructure"],
      features_ru: ["Руководство ИКТ", "Архив проектов студентов", "Серверное подключение"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f4_413",
      floor: 4,
      floorText_az: "IV Mərtəbə", floorText_en: "4th Floor", floorText_ru: "4-й Этаж",
      no: "№ 413",
      name_az: "Poçt rabitəsi və mühasibat uçotu şöbəsi", name_en: "Postal Communications & Accounting Dept", name_ru: "Отделение почтовой связи и бухучета",
      cat: "admin",
      catLabel_az: "Tədris Şöbəsi", catLabel_en: "Academic Dept", catLabel_ru: "Учебное отделение",
      icon: "📊",
      desc_az: "Poçt rabitəsi və mühasibat uçotu ixtisasları üzrə akademik koordinasiya və tələbə qeydiyyatı.",
      desc_en: "Academic leadership and student registrar for postal communications and accounting tracks.",
      desc_ru: "Академическая координация и учет студентов специальностей почтовой связи и бухгалтерии.",
      features_az: ["Şöbə müdirliyi", "İxtisas qeydiyyatı", "Tələbə sənədləşməsi"],
      features_en: ["Department office", "Majors registry", "Student records"],
      features_ru: ["Заведующий отделением", "Реестр специальностей", "Студенческая документация"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f4_408",
      floor: 4,
      floorText_az: "IV Mərtəbə", floorText_en: "4th Floor", floorText_ru: "4-й Этаж",
      no: "№ 408",
      name_az: "Proyektor otağı", name_en: "Multimedia Projector Classroom", name_ru: "Мультимедийная аудитория с проектором",
      cat: "it",
      catLabel_az: "Multimedia Auditoriyası", catLabel_en: "Multimedia Classroom", catLabel_ru: "Мультимедийная аудитория",
      icon: "📽️",
      desc_az: "Mühazirələrin proyektor və audio sistem vasitəsilə vizual təqdimatı üçün multimedia auditoriyası.",
      desc_en: "Visual presentation classroom with high-definition digital projection and acoustics.",
      desc_ru: "Мультимедийная аудитория для визуальных презентаций лекций с проектором и акустикой.",
      features_az: ["Yüksək dəqiqlikli proyektor", "Böyük proyeksiya ekranı", "Audio akustika sistemi"],
      features_en: ["High-res projector", "Large projection screen", "Audio acoustics system"],
      features_ru: ["HD проектор", "Большой проекционный экран", "Акустическая система"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f4_auditoriyalar",
      floor: 4,
      floorText_az: "IV Mərtəbə", floorText_en: "4th Floor", floorText_ru: "4-й Этаж",
      no: "Auditoriyalar",
      name_az: "13 Tədris və Mühazirə Auditoriyası (Cəmi 17 otaq)", name_en: "13 Teaching & Lecture Classrooms (Total 17 rooms)", name_ru: "13 учебных и лекционных аудиторий (Всего 17 комнат)",
      cat: "classroom",
      catLabel_az: "Tədris Fondu", catLabel_en: "Classrooms Fund", catLabel_ru: "Учебный фонд",
      icon: "🏛️",
      desc_az: "IV mərtəbə üzrə ümumilikdə 17 otaq mövcuddur; 13 tədris və mühazirə auditoriyası burada fəaliyyət göstərir.",
      desc_en: "4th floor has 17 total rooms; 13 classrooms and lecture halls provide comfortable study environments.",
      desc_ru: "На 4-м этаже 17 помещений; 13 учебных аудиторий создают комфортную академическую среду.",
      features_az: ["Cəmi 17 otaq fondu", "Təbii havalandırma və işıqlanma", "Akademik mühit"],
      features_en: ["17 room capacity", "Natural daylight & ventilation", "Academic environment"],
      features_ru: ["17 помещений всего", "Естественная вентиляция и свет", "Академическая среда"],
      classrooms: ["401", "402", "403", "404", "405", "406", "407", "411", "412", "414", "415", "416", "417"],
      wing_az: "Bütün mərtəbə boyu", wing_en: "Across the Floor", wing_ru: "По всему этажу"
    },

    // ═════════════ V MƏRTƏBƏ (Cəmi 18 Otaq) ═════════════
    {
      id: "f5_508",
      floor: 5,
      floorText_az: "V Mərtəbə", floorText_en: "5th Floor", floorText_ru: "5-й Этаж",
      no: "№ 508",
      name_az: "Proyektor otağı", name_en: "Conference & Projector Auditorium", name_ru: "Конференц-аудитория с проектором",
      cat: "it",
      catLabel_az: "Multimedia Auditoriyası", catLabel_en: "Multimedia Classroom", catLabel_ru: "Мультимедийная аудитория",
      icon: "📽️",
      desc_az: "Multimedia təqdimatları, açıq dərslər və seminar mühazirələri üçün proyektorlu auditoriya.",
      desc_en: "Multimedia presentations, open lectures, and defense seminars hall with digital projection.",
      desc_ru: "Мультимедийные презентации, открытые уроки и семинары в аудитории с проектором.",
      features_az: ["HD Proyektor", "Mühazirə tribunası", "Motorlu proyeksiya pərdəsi"],
      features_en: ["HD Projector", "Lecture rostrum", "Motorized screen"],
      features_ru: ["HD Проектор", "Лекционная трибуна", "Моторизованный экран"],
      wing_az: "Qərb qanadı", wing_en: "West Wing", wing_ru: "Западное крыло"
    },
    {
      id: "f5_512",
      floor: 5,
      floorText_az: "V Mərtəbə", floorText_en: "5th Floor", floorText_ru: "5-й Этаж",
      no: "№ 512",
      name_az: "Kompüter texnologiyası şöbəsi", name_en: "Computer Technologies Department", name_ru: "Отделение компьютерных технологий",
      cat: "admin",
      catLabel_az: "İxtisas Şöbəsi", catLabel_en: "Specialty Dept", catLabel_ru: "Специальное отделение",
      icon: "💻",
      desc_az: "Kompüter sistemləri, şəbəkə inzibatçılığı və proqram təminatı ixtisaslarının akademik rəhbərliyi.",
      desc_en: "Academic administration for software engineering, network systems, and computing specialties.",
      desc_ru: "Руководство специальностями программного обеспечения, компьютерных систем и сетей.",
      features_az: ["Şöbə müdirliyi", "İxtisas komissiyası", "Tələbə layihələri laboratoriyası"],
      features_en: ["Department office", "Specialty committee", "Student projects hub"],
      features_ru: ["Заведующий отделением", "Профильная комиссия", "Лаборатория проектов студентов"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f5_514",
      floor: 5,
      floorText_az: "V Mərtəbə", floorText_en: "5th Floor", floorText_ru: "5-й Этаж",
      no: "№ 514",
      name_az: "Təhsildə keyfiyyətə nəzarət və monitorinq şöbəsi", name_en: "Quality Assurance & Academic Monitoring Dept", name_ru: "Отдел контроля качества образования и мониторинга",
      cat: "admin",
      catLabel_az: "Keyfiyyət & Monitorinq", catLabel_en: "Quality & Monitoring", catLabel_ru: "Качество и Мониторинг",
      icon: "🎯",
      desc_az: "Tədrisin keyfiyyət standartlarına uyğunluğunun qiymətləndirilməsi, daxili audit və akkreditasiya mərkəzi.",
      desc_en: "Evaluation of academic standards compliance, internal audit, and educational accreditation center.",
      desc_ru: "Оценка стандартов качества преподавания, внутренний аудит и аккредитация учебных программ.",
      features_az: ["Keyfiyyət təminatı", "Monitorinq və daxili audit", "Tədris statistikası bazası"],
      features_en: ["Quality assurance", "Monitoring & internal audit", "Academic statistics database"],
      features_ru: ["Обеспечение качества", "Мониторинг и внутренний аудит", "База академической статистики"],
      wing_az: "Şərq qanadı", wing_en: "East Wing", wing_ru: "Восточное крыло"
    },
    {
      id: "f5_auditoriyalar",
      floor: 5,
      floorText_az: "V Mərtəbə", floorText_en: "5th Floor", floorText_ru: "5-й Этаж",
      no: "Auditoriyalar",
      name_az: "15 Tədris və İxtisas Auditoriyası (Cəmi 18 otaq)", name_en: "15 Teaching & Specialized Classrooms (Total 18 rooms)", name_ru: "15 учебных и профильных аудиторий (Всего 18 комнат)",
      cat: "classroom",
      catLabel_az: "Tədris Fondu", catLabel_en: "Classrooms Fund", catLabel_ru: "Учебный фонд",
      icon: "🏛️",
      desc_az: "V mərtəbə üzrə ümumilikdə 18 otaq mövcuddur; 15 mühazirə və qrup seminar otağı fəaliyyət göstərir.",
      desc_en: "5th floor comprises 18 total rooms; 15 quiet and focused lecture rooms provide an elevated study atmosphere.",
      desc_ru: "На 5-м этаже расположено 18 помещений; 15 лекционных и аудиторных залов обеспечивают спокойную атмосферу.",
      features_az: ["Cəmi 18 otaq fondu", "Sakit və konsentrasiyalı mühit", "Geniş mühazirə otaqları"],
      features_en: ["Total 18 rooms", "Quiet & focused atmosphere", "Spacious study halls"],
      features_ru: ["Всего 18 помещений", "Тихая сосредоточенная атмосфера", "Просторные аудитории"],
      classrooms: ["501", "502", "503", "504", "505", "506", "507", "509", "510", "511", "513", "515", "516", "517", "518"],
      wing_az: "Bütün mərtəbə boyu", wing_en: "Across the Floor", wing_ru: "По всему этажу"
    }
  ];

  const FLOOR_CONFIGS = {
    "1": {
      icon: "🏢",
      title_az: "I MƏRTƏBƏ — İdman Kompleksi, Kimya & Rabitə Laboratoriyaları",
      title_en: "1ST FLOOR — Sports Complex, Chemistry & Telecom Laboratories",
      title_ru: "1-Й ЭТАЖ — Спорткомплекс, Лаборатории Химии и Связи",
      desc_az: "Kollecin 1-ci mərtəbəsində tələbələrin fiziki hazırlığı üçün idman zalı, 2 kimya laboratoriyası, telekommunikasiya laboratoriyası və inzibati şöbələr yerləşir.",
      desc_en: "The 1st floor houses the gymnasium complex, 2 chemistry laboratories, a telecommunications lab, and administrative departments.",
      desc_ru: "На 1-м этаже расположен спортзал, 2 химические лаборатории, телекоммуникационная лаборатория и административные отделы.",
      countBadge_az: "12 Əsas Otaq və Məkan", countBadge_en: "12 Main Rooms & Spaces", countBadge_ru: "12 Основных Кабинетов",
      wings_az: [
        { label: "Qərb Qanadı", text: "107 (Qiyabi), 106A (Hərbi), 106 (Kimya-1), 107A (Telekom), 103 (Kimya-2)", icon: "⬅️" },
        { label: "Mərkəzi", text: "Kadrlar şöbəsi, Kompüter laboratoriyası", icon: "🏛️" },
        { label: "Şərq Qanadı", text: "113 (Mühasibat - 2 otaq), 114 (Təsərrüfat), 115 (Təcrübə), 116 (Tərbiyə)", icon: "➡️" },
        { label: "İdman", text: "İdman zalı (geyinmə otağı ilə)", icon: "⚽" }
      ],
      wings_en: [
        { label: "West Wing", text: "107 (Distance), 106A (Military), 106 (Chem-1), 107A (Telecom), 103 (Chem-2)", icon: "⬅️" },
        { label: "Central", text: "Human Resources, Computer Laboratory", icon: "🏛️" },
        { label: "East Wing", text: "113 (Accounting - 2 rooms), 114 (Economic), 115 (Internship), 116 (Student Affairs)", icon: "➡️" },
        { label: "Sports", text: "Sports gym (with locker rooms)", icon: "⚽" }
      ],
      wings_ru: [
        { label: "Западное крыло", text: "107 (Заочное), 106A (Военный), 106 (Химия-1), 107A (Связь), 103 (Химия-2)", icon: "⬅️" },
        { label: "Центральное", text: "Отдел кадров, Компьютерная лаборатория", icon: "🏛️" },
        { label: "Восточное крыло", text: "113 (Бухгалтерия - 2 комнаты), 114 (Хозчасть), 115 (Практика), 116 (Воспитание)", icon: "➡️" },
        { label: "Спорткомплекс", text: "Спортивный зал (с раздевалками)", icon: "⚽" }
      ]
    },
    "2": {
      icon: "🏛️",
      title_az: "II MƏRTƏBƏ — Kollec Rəhbərliyi, Əsas Kitabxana & Kompüter Mərkəzləri",
      title_en: "2ND FLOOR — College Leadership, Central Library & IT Hubs",
      title_ru: "2-Й ЭТАЖ — Руководство Колледжа, Библиотека и Центры ИКТ",
      desc_az: "2-ci mərtəbədə direktorluq, müavinliklər, 3 kompüter otağı, metodiki kabinet və 22 000-dən çox kitab fondu olan zəngin Kitabxana & Oxu Zalı (206) fəaliyyət göstərir.",
      desc_en: "The 2nd floor hosts the Director's suite, deputies, 3 computer labs, methodic office, and the Central Library & Reading Hall (Room 206).",
      desc_ru: "На 2-м этаже находятся кабинет директора, заместители, 3 компьютерных класса, методический кабинет и Библиотека (каб. 206).",
      countBadge_az: "11 Əsas Otaq və Mərkəz", countBadge_en: "11 Main Rooms & Hubs", countBadge_ru: "11 Основных Помещений",
      wings_az: [
        { label: "Mərkəzi Qanad", text: "Direktor otağı (dos. Səbuhi Qurbanov)", icon: "🏛️" },
        { label: "Qərb Qanadı", text: "205 (Tədris müavini), Həmkar otağı, Mühəndis (FBK 2 otaq), 201, 203 (Kompüter), 202 (Ceyhun m.)", icon: "⬅️" },
        { label: "Şərq Qanadı", text: "214 (Qeydiyyat & Monitorinq), 217 (Metodiki kabinet), 211 (Kompüter otağı)", icon: "➡️" },
        { label: "Kitabxana", text: "206 - Kitabxana və Oxu Zalı (2 otaq daxilində)", icon: "📚" }
      ],
      wings_en: [
        { label: "Central Wing", text: "Director's office (Assoc. Prof. Sebuhi Gurbanov)", icon: "🏛️" },
        { label: "West Wing", text: "205 (Academic Deputy), Trade Union, Engineering (FBK), 201, 203 (Computer), 202 (Faculty)", icon: "⬅️" },
        { label: "East Wing", text: "214 (Registration & Monitoring), 217 (Methodic office), 211 (Computer)", icon: "➡️" },
        { label: "Library", text: "206 - Library and Reading Hall (2 rooms)", icon: "📚" }
      ],
      wings_ru: [
        { label: "Центральное", text: "Кабинет директора (доц. Сабухи Гурбанов)", icon: "🏛️" },
        { label: "Западное крыло", text: "205 (Зам по учебной части), Профком, Инженерия (ПЦК), 201, 203 (ПК), 202 (Кабинет)", icon: "⬅️" },
        { label: "Восточное крыло", text: "214 (Регистрация и Мониторинг), 217 (Методический кабинет), 211 (ПК)", icon: "➡️" },
        { label: "Библиотека", text: "206 - Библиотека и Читальный зал (2 комнаты)", icon: "📚" }
      ]
    },
    "3": {
      icon: "🔬",
      title_az: "III MƏRTƏBƏ — Fizika Laboratoriyası, Tədris Şöbəsi & 16 Auditoriya",
      title_en: "3RD FLOOR — Physics Laboratory, Academic Division & 16 Classrooms",
      title_ru: "3-Й ЭТАЖ — Лаборатория Физики, Учебный Отдел и 16 Аудиторий",
      desc_az: "3-cü mərtəbə tələbələrin əsas mühazirə və təcrübə məkanlarındandır. Burada müasir fizika laboratoriyası, elektron smart-lövhə otağı və cəmi 16 otaq fondu yerləşir.",
      desc_en: "Key lecture and experimental zone with modern physics lab, smart interactive board room, and 16 classrooms in total.",
      desc_ru: "Ключевая лекционная зона: современная лаборатория физики, интерактивная аудитория со смарт-доской и всего 16 комнат.",
      countBadge_az: "Cəmi 16 Otaq Fondu", countBadge_en: "Total 16 Rooms Capacity", countBadge_ru: "Всего 16 Кабинетов",
      wings_az: [
        { label: "Qərb Qanadı", text: "301 (Fizika lab), 306 (Elektron lövhə), 307 (Telekom şöbəsi), 309 (Mühəndis)", icon: "⬅️" },
        { label: "Mərkəzi Korpus", text: "302 (Tədris şöbəsi), 303 (Müəllimlər otağı)", icon: "🏛️" },
        { label: "Tədris Fondu", text: "10 Mühazirə və Seminar Auditoriyası (Cəmi 16 otaq)", icon: "🎓" }
      ],
      wings_en: [
        { label: "West Wing", text: "301 (Physics lab), 306 (Smart board), 307 (Telecom dept), 309 (Engineering)", icon: "⬅️" },
        { label: "Central Wing", text: "302 (Academic division), 303 (Teachers' room)", icon: "🏛️" },
        { label: "Study Rooms", text: "10 Lecture and Seminar Classrooms (Total 16 rooms)", icon: "🎓" }
      ],
      wings_ru: [
        { label: "Западное крыло", text: "301 (Лаб физики), 306 (Смарт-доска), 307 (Отдел связи), 309 (Инженерия)", icon: "⬅️" },
        { label: "Центральное", text: "302 (Учебный отдел), 303 (Учительская комната)", icon: "🏛️" },
        { label: "Учебный фонд", text: "10 лекционных и семинарских аудиторий (Всего 16 комнат)", icon: "🎓" }
      ]
    },
    "4": {
      icon: "📮",
      title_az: "IV MƏRTƏBƏ — İKT və Poçt Rabitəsi Şöbələri, Poçt Laboratoriyası & 17 Auditoriya",
      title_en: "4TH FLOOR — IT & Postal Departments, Postal Lab & 17 Classrooms",
      title_ru: "4-Й ЭТАЖ — Отделения ИКТ и Почтовой Связи, Почтовая Лаборатория и 17 Аудиторий",
      desc_az: "4-cü mərtəbədə rabitə və informasiya texnologiyaları ixtisaslarının tədris mərkəzi, poçt laboratoriyası, multimedia proyektor otağı və 17 auditoriya yerləşir.",
      desc_en: "Academic hub for postal communication and information technology majors, postal lab, multimedia room, and 17 classrooms.",
      desc_ru: "Учебный центр специальностей связи и информационных технологий, почтовая лаборатория, мультимедиа и 17 аудиторий.",
      countBadge_az: "Cəmi 17 Otaq Fondu", countBadge_en: "Total 17 Rooms Capacity", countBadge_ru: "Всего 17 Кабинетов",
      wings_az: [
        { label: "Şərq Qanadı", text: "410 (Poçt laboratoriyası), 409 (İKT şöbəsi), 413 (Poçt rabitəsi və mühasibat)", icon: "➡️" },
        { label: "Qərb Qanadı", text: "408 (Proyektor multimedia auditoriyası)", icon: "⬅️" },
        { label: "Tədris Fondu", text: "13 Tədris və Mühazirə Auditoriyası (Cəmi 17 otaq)", icon: "🎓" }
      ],
      wings_en: [
        { label: "East Wing", text: "410 (Postal lab), 409 (IT dept), 413 (Postal & Accounting)", icon: "➡️" },
        { label: "West Wing", text: "408 (Multimedia projector auditorium)", icon: "⬅️" },
        { label: "Study Rooms", text: "13 Lecture and Teaching Classrooms (Total 17 rooms)", icon: "🎓" }
      ],
      wings_ru: [
        { label: "Восточное крыло", text: "410 (Почтовая лаб), 409 (Отделение ИКТ), 413 (Почта и бухучет)", icon: "➡️" },
        { label: "Западное крыло", text: "408 (Мультимедийная аудитория с проектором)", icon: "⬅️" },
        { label: "Учебный фонд", text: "13 учебных и лекционных аудиторий (Всего 17 комнат)", icon: "🎓" }
      ]
    },
    "5": {
      icon: "🎯",
      title_az: "V MƏRTƏBƏ — Kompüter Texnologiyaları Şöbəsi, Keyfiyyət Təminatı & 18 Auditoriya",
      title_en: "5TH FLOOR — Computer Technologies Department, Quality Assurance & 18 Classrooms",
      title_ru: "5-Й ЭТАЖ — Отделение Компьютерных Технологий, Контроль Качества и 18 Аудиторий",
      desc_az: "5-ci mərtəbə proqramlaşdırma və kompüter ixtisasları, təhsildə keyfiyyətə nəzarət və monitorinq şöbəsi və 18 geniş auditoriyadan ibarətdir.",
      desc_en: "Programming and software engineering department, educational quality control office, and 18 spacious lecture rooms.",
      desc_ru: "Отделение компьютерных наук и программирования, отдел контроля качества образования и 18 аудиторий.",
      countBadge_az: "Cəmi 18 Otaq Fondu", countBadge_en: "Total 18 Rooms Capacity", countBadge_ru: "Всего 18 Кабинетов",
      wings_az: [
        { label: "Şərq Qanadı", text: "512 (Kompüter texnologiyası şöbəsi), 514 (Keyfiyyətə nəzarət və monitorinq)", icon: "➡️" },
        { label: "Qərb Qanadı", text: "508 (Proyektorlu konfrans və tədris auditoriyası)", icon: "⬅️" },
        { label: "Tədris Fondu", text: "15 Tədris və İxtisas Seminar Otağı (Cəmi 18 otaq)", icon: "🎓" }
      ],
      wings_en: [
        { label: "East Wing", text: "512 (Computer technologies dept), 514 (Quality assurance & monitoring)", icon: "➡️" },
        { label: "West Wing", text: "508 (Projector conference & lecture hall)", icon: "⬅️" },
        { label: "Study Rooms", text: "15 Specialized and Seminar Classrooms (Total 18 rooms)", icon: "🎓" }
      ],
      wings_ru: [
        { label: "Восточное крыло", text: "512 (Отделение компьютерных технологий), 514 (Контроль качества)", icon: "➡️" },
        { label: "Западное крыло", text: "508 (Конференц-аудитория с проектором)", icon: "⬅️" },
        { label: "Учебный фонд", text: "15 профильных и семинарских аудиторий (Всего 18 комнат)", icon: "🎓" }
      ]
    },
    "all": {
      icon: "🏢",
      title_az: "BÜTÜN MƏRTƏBƏLƏR — Əsas Tədris Korpusu Üzrə Tam Rəqəmsal Xəritə",
      title_en: "ALL FLOORS — Complete Digital Map of the Academic Campus",
      title_ru: "ВСЕ ЭТАЖИ — Полная Цифровая Карта Учебного Корпуса",
      desc_az: "I mərtəbədən V mərtəbəyədək bütün 80+ auditoriya, ixtisas laboratoriyaları, rəhbərlik otaqları və kitabxana kompleksinin vahid bələdçisi.",
      desc_en: "Unified guide across all 80+ classrooms, specialized labs, faculty offices, and library from Floor 1 to Floor 5.",
      desc_ru: "Единый навигатор по всем 80+ аудиториям, специализированным лабораториям, руководству и библиотеке с 1 по 5 этаж.",
      countBadge_az: "5 Mərtəbə · 80+ Otaq", countBadge_en: "5 Floors · 80+ Rooms", countBadge_ru: "5 Этажей · 80+ Комнат",
      wings_az: [
        { label: "I Mərtəbə", text: "İdman kompleksi, Kimya və Telekommunikasiya laboratoriyaları", icon: "1️⃣" },
        { label: "II Mərtəbə", text: "Direktorluq, Kitabxana və Oxu Zalı (206), Kompüter otaqları", icon: "2️⃣" },
        { label: "III Mərtəbə", text: "Fizika laboratoriyası (301), Elektron lövhə (306), 16 otaq", icon: "3️⃣" },
        { label: "IV Mərtəbə", text: "Poçt laboratoriyası (410), İKT şöbəsi (409), 17 otaq", icon: "4️⃣" },
        { label: "V Mərtəbə", text: "Kompüter texnologiyası (512), Keyfiyyət (514), 18 otaq", icon: "5️⃣" }
      ],
      wings_en: [
        { label: "1st Floor", text: "Sports gym, Chemistry & Telecommunications laboratories", icon: "1️⃣" },
        { label: "2nd Floor", text: "Leadership, Central Library & Reading Hall (206), Computer labs", icon: "2️⃣" },
        { label: "3rd Floor", text: "Physics laboratory (301), Smart board (306), 16 classrooms", icon: "3️⃣" },
        { label: "4th Floor", text: "Postal lab (410), IT department (409), 17 classrooms", icon: "4️⃣" },
        { label: "5th Floor", text: "Computer tech (512), Quality assurance (514), 18 classrooms", icon: "5️⃣" }
      ],
      wings_ru: [
        { label: "1-й Этаж", text: "Спорткомплекс, Лаборатории химии и телекоммуникаций", icon: "1️⃣" },
        { label: "2-й Этаж", text: "Руководство, Библиотека и Читальный зал (206), Компьютерные классы", icon: "2️⃣" },
        { label: "3-й Этаж", text: "Лаборатория физики (301), Смарт-доска (306), 16 комнат", icon: "3️⃣" },
        { label: "4-й Этаж", text: "Почтовая лаб (410), Отделение ИКТ (409), 17 комнат", icon: "4️⃣" },
        { label: "5-й Этаж", text: "Компьютерные технологии (512), Контроль качества (514), 18 комнат", icon: "5️⃣" }
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

  function getLang() {
    return (typeof currentLang !== "undefined" && currentLang) ? currentLang : "az";
  }

  function getField(obj, key) {
    if (!obj) return "";
    const l = getLang();
    return obj[key + "_" + l] || obj[key + "_az"] || obj[key] || "";
  }

  function getArrayField(obj, key) {
    if (!obj) return [];
    const l = getLang();
    return obj[key + "_" + l] || obj[key + "_az"] || obj[key] || [];
  }

  function updateFloorBanner() {
    if (!floorBanner) return;
    const l = getLang();
    const cfg = FLOOR_CONFIGS[activeFloor] || FLOOR_CONFIGS["all"];
    const title = cfg["title_" + l] || cfg.title_az;
    const desc = cfg["desc_" + l] || cfg.desc_az;
    const countBadge = cfg["countBadge_" + l] || cfg.countBadge_az;
    const wings = cfg["wings_" + l] || cfg.wings_az || [];

    let wingsHtml = "";
    if (wings && wings.length) {
      wingsHtml = wings.map(w =>
        `<span class="cfb-wing-chip">${w.icon} <strong>${w.label}:</strong> ${w.text}</span>`
      ).join("");
    }
    floorBanner.innerHTML = `
      <div class="cfb-header">
        <div class="cfb-title-wrap">
          <span class="cfb-floor-icon">${cfg.icon}</span>
          <div>
            <h3 class="cfb-title">${title}</h3>
            <p class="cfb-desc">${desc}</p>
          </div>
        </div>
        <span class="cfb-badge-count">${countBadge}</span>
      </div>
      <div class="cfb-wings">${wingsHtml}</div>
    `;
  }

  function renderRooms() {
    if (!roomsGrid) return;
    const l = getLang();
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

      // 3. Search query match across all languages
      if (q) {
        const matchNo = (room.no || "").toLowerCase().includes(q);
        const matchName = (room.name_az || "").toLowerCase().includes(q) ||
                          (room.name_en || "").toLowerCase().includes(q) ||
                          (room.name_ru || "").toLowerCase().includes(q);
        const matchDesc = (room.desc_az || "").toLowerCase().includes(q) ||
                          (room.desc_en || "").toLowerCase().includes(q) ||
                          (room.desc_ru || "").toLowerCase().includes(q);
        const matchWing = (room.wing_az || "").toLowerCase().includes(q) ||
                          (room.wing_en || "").toLowerCase().includes(q) ||
                          (room.wing_ru || "").toLowerCase().includes(q);
        const matchFeatures = (room.features_az || []).some(f => f.toLowerCase().includes(q)) ||
                              (room.features_en || []).some(f => f.toLowerCase().includes(q)) ||
                              (room.features_ru || []).some(f => f.toLowerCase().includes(q));
        const matchClassrooms = (room.classrooms || []).some(c => c.toLowerCase().includes(q));
        if (!matchNo && !matchName && !matchDesc && !matchWing && !matchFeatures && !matchClassrooms) {
          return false;
        }
      }

      return true;
    });

    if (countText) {
      const dict = (typeof i18n !== "undefined" && i18n[l]) ? i18n[l] : {};
      if (q) {
        const foundPrefix = dict.campus_search_found || "Axtarış nəticəsi:";
        const foundSuffix = dict.campus_search_rooms_suffix || "otaq tapıldı";
        countText.innerHTML = `${foundPrefix} <strong>${targetRooms.length}</strong> ${foundSuffix}`;
      } else {
        let floorLabel = "";
        if (activeFloor === "all") {
          floorLabel = dict.campus_fbtn_all_title || "Bütün mərtəbələr";
        } else {
          const key = "campus_fbtn_" + activeFloor + "_title";
          floorLabel = dict[key] || (activeFloor + "-ci Mərtəbə");
        }
        const shownLabel = dict.campus_count_shown || "göstərilən otaqlar:";
        countText.innerHTML = `${floorLabel} ${shownLabel} <strong>${targetRooms.length}</strong>`;
      }
    }

    if (targetRooms.length === 0) {
      const dict = (typeof i18n !== "undefined" && i18n[l]) ? i18n[l] : {};
      const notFoundTitle = dict.campus_not_found_title || "Axtarış üzrə otaq tapılmadı";
      const notFoundDesc = dict.campus_not_found_desc || "Daxil etdiyiniz meyar üzrə heç bir otaq və ya laboratoriya aşkar edilmədi.";
      const resetBtnText = dict.campus_reset_btn || "Bütün Otaqları Göstər";

      roomsGrid.innerHTML = `
        <div style="grid-column: 1/-1; text-align: center; padding: 50px 20px; background: var(--surface); border: 1px dashed var(--border); border-radius: 14px;">
          <div style="font-size: 2.5rem; margin-bottom: 12px;">🔍</div>
          <h4 style="font-size: 1.15rem; font-weight: 800; color: var(--text); margin-bottom: 6px;">${notFoundTitle}</h4>
          <p style="font-size: 0.88rem; color: var(--text-dim); max-width: 450px; margin: 0 auto 16px;">
            ${notFoundDesc}
          </p>
          <button type="button" class="btn btn-secondary" id="campus-reset-filters-btn">${resetBtnText}</button>
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

    const dict = (typeof i18n !== "undefined" && i18n[l]) ? i18n[l] : {};
    const audTitle = dict.campus_aud_list_title || "Auditoriya nömrələri";
    const btnLibText = dict.campus_btn_lib || "📖 Kitabxana Fondu və Tarixi";
    const btnBioText = dict.campus_btn_bio || "👤 Səbuhi Qurbanov Bioqrafiyası";

    roomsGrid.innerHTML = targetRooms.map(room => {
      const name = getField(room, "name");
      const desc = getField(room, "desc");
      const wing = getField(room, "wing");
      const catLabel = getField(room, "catLabel");
      const floorText = getField(room, "floorText");
      const features = getArrayField(room, "features");

      const featTags = features.map(f => `<span class="room-feature-tag">${escapeHTML ? escapeHTML(f) : f}</span>`).join("");
      let audPills = "";
      if (room.classrooms && room.classrooms.length) {
        const audBadges = room.classrooms.map(c => `<span class="room-aud-num">№ ${c}</span>`).join("");
        audPills = `
          <div class="room-aud-pills-wrap">
            <span class="room-aud-pills-title">${audTitle} (${room.classrooms.length}):</span>
            <div class="room-aud-pills-grid">${audBadges}</div>
          </div>
        `;
      }

      let actionsHtml = "";
      if (room.action === "library_fund") {
        actionsHtml = `
          <div class="room-card-actions">
            <button type="button" class="room-card-btn room-card-btn-action" data-action="library_fund">
              ${btnLibText}
            </button>
          </div>
        `;
      } else if (room.action === "director_bio") {
        actionsHtml = `
          <div class="room-card-actions">
            <button type="button" class="room-card-btn room-card-btn-action" data-action="director_bio">
              ${btnBioText}
            </button>
          </div>
        `;
      }

      return `
        <article class="campus-room-card" data-room-id="${room.id}">
          <div class="room-card-top">
            <div class="room-badge-group">
              <span class="room-num-pill">${room.no}</span>
              <span class="room-cat-tag cat-${room.cat}">${catLabel}</span>
            </div>
            <span class="room-floor-tag">${floorText}</span>
          </div>

          <div class="room-title-row">
            <div class="room-icon-box">${room.icon}</div>
            <div>
              <h3 class="room-title">${escapeHTML ? escapeHTML(name) : name}</h3>
              <p class="room-desc">${escapeHTML ? escapeHTML(desc) : desc}</p>
            </div>
          </div>

          <div class="room-tags-wrap">${featTags}</div>
          ${audPills}

          <div class="room-wing-hint">
            <span>📍</span>
            <span>${escapeHTML ? escapeHTML(wing) : wing}</span>
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

  function switchFloor(floor) {
    if (!floor) return;
    activeFloor = String(floor);
    floorBtns.forEach(b => {
      const isCurrent = b.getAttribute("data-floor") === activeFloor;
      b.classList.toggle("active", isCurrent);
      b.setAttribute("aria-selected", isCurrent ? "true" : "false");
    });
    updateFloorBanner();
    renderRooms();
  }
  window.switchCampusFloor = switchFloor;

  // Bind Header Dropdown & Mobile Nav Floor links
  document.querySelectorAll("[data-campus-floor]").forEach(item => {
    item.addEventListener("click", () => {
      const fl = item.getAttribute("data-campus-floor");
      switchFloor(fl);

      // Close mobile drawer if open
      const mobileNav = document.getElementById("mobile-nav");
      if (mobileNav && mobileNav.classList.contains("active")) {
        mobileNav.classList.remove("active");
        document.body.classList.remove("nav-open");
      }

      // Smooth scroll to campus section
      const sec = document.getElementById("campus-navigator");
      if (sec) {
        sec.scrollIntoView({ behavior: "smooth" });
      }
    });
  });

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

full_js = base_js + "\n\n" + multilingual_module

with open(os.path.join(base_dir, "script.js"), "w", encoding="utf-8") as f:
    f.write(full_js)

with open(os.path.join(base_dir, "scratch/script_working_backup.js"), "w", encoding="utf-8") as f:
    f.write(full_js)

print("script.js updated and synced with backup!")
