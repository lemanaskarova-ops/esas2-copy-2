const fs = require('fs');
const path = require('path');

const rootDir = '/Users/konul/Documents/esas2 copy 2';
const styleCssPath = path.join(rootDir, 'style.css');
const scriptJsPath = path.join(rootDir, 'script.js');
const backupJsPath = path.join(rootDir, 'scratch/script_working_backup.js');

// 1. ADD GALLERY CSS TO style.css
let css = fs.readFileSync(styleCssPath, 'utf8');

const galleryCss = `
/* Honor Student Media Gallery */
.honor-gallery-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 14px;
}

.honor-gallery-item {
  position: relative;
  border-radius: 14px;
  overflow: hidden;
  border: 1.5px solid rgba(207, 169, 94, 0.35);
  background: #061326;
  aspect-ratio: 4 / 3;
  cursor: pointer;
  transition: all 0.28s ease;
}

.honor-gallery-item:hover {
  transform: translateY(-3px);
  border-color: #cfa95e;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5), 0 0 20px rgba(207, 169, 94, 0.3);
}

.honor-gallery-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.45s ease;
}

.honor-gallery-item:hover .honor-gallery-img {
  transform: scale(1.06);
}

.honor-gallery-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.honor-gallery-video-badge {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(220, 38, 38, 0.85);
  color: #fff;
  font-size: 0.72rem;
  font-weight: 800;
  display: flex;
  align-items: center;
  gap: 5px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  z-index: 2;
}

.honor-gallery-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 12px;
  background: linear-gradient(0deg, rgba(6, 19, 38, 0.95) 0%, rgba(6, 19, 38, 0.7) 60%, transparent 100%);
  color: #f8fafc;
  font-size: 0.78rem;
  font-weight: 600;
  line-height: 1.35;
  z-index: 2;
}

.honor-gallery-preview-strip {
  display: flex;
  gap: 8px;
  margin-top: 12px;
  overflow-x: auto;
  padding-bottom: 6px;
  width: 100%;
  max-width: 270px;
}

.honor-preview-thumb {
  width: 44px;
  height: 44px;
  border-radius: 8px;
  object-fit: cover;
  border: 1px solid rgba(207, 169, 94, 0.4);
  flex-shrink: 0;
  cursor: pointer;
  transition: transform 0.2s ease, border-color 0.2s ease;
}

.honor-preview-thumb:hover {
  transform: scale(1.1);
  border-color: #cfa95e;
}

@media (max-width: 768px) {
  .honor-gallery-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .honor-gallery-grid {
    grid-template-columns: 1fr;
  }
}
`;

if (!css.includes('.honor-gallery-grid')) {
  css += '\n' + galleryCss;
  fs.writeFileSync(styleCssPath, css, 'utf8');
  console.log('style.css updated with gallery styles!');
}

// 2. UPDATE script.js WITH GALLERY DATA & MODAL TAB
let js = fs.readFileSync(scriptJsPath, 'utf8');

// Replace the initHonorStudentsModule with the enhanced version that includes the gallery
const oldModuleStart = '/* ═══════════════ HONORARY STUDENTS / FƏXRİ TƏLƏBƏLƏR MODULE ═══════════════ */';
const oldModuleIndex = js.indexOf(oldModuleStart);

if (oldModuleIndex !== -1) {
  const baseJs = js.substring(0, oldModuleIndex);

  const newModule = `/* ═══════════════ HONORARY STUDENTS / FƏXRİ TƏLƏBƏLƏR MODULE ═══════════════ */
(function initHonorStudentsModule() {
  const honorStudentsData = [
    {
      id: "senan-mirzezade",
      fullName: "Mirzəzadə Sənan Azər oğlu",
      photo: "senan1.jpeg",
      fallbackPhoto: "logo.jpg",
      titleBadge: "“İlin Gənci” Mükafatçısı",
      role: "İnformasiya Texnologiyaları, Kibertəhlükəsizlik və Robototexnika Mütəxəssisi",
      categories: ["all", "it-robotics", "international", "youth"],
      statusText: "Beynəlxalq Çempion & Tədqiqatçı",
      quote: "Sənan əldə etdiyi bilik və təcrübəni yalnız şəxsi inkişafı üçün deyil, həmçinin yarışlara hazırlaşan uşaqların və gənclərin hazırlanmasına dəstək olmaq, öz təcrübəsini bölüşmək və texnologiya sahəsində sosial inklüzivliyin inkişafına töhfə vermək məqsədilə də istifadə edir.",
      flags: [
        { emoji: "🇦🇿", name: "Azərbaycan", note: "Respublika Çempionu" },
        { emoji: "🇺🇸", name: "ABŞ", note: "FIRST Robotics / NASA Layihəsi" },
        { emoji: "🇯🇵", name: "Yaponiya", note: "Beynəlxalq Robototexnika 2026" },
        { emoji: "🇫🇮", name: "Finlandiya", note: "Beynəlxalq Abilimpiya 2027" },
        { emoji: "🇹🇷", name: "Türkiyə", note: "16-cı Beynəlxalq MEB Robot" }
      ],
      stats: [
        { icon: "🥇", val: "I YER", label: "Milli Abilimpiya 2026", sub: "İT istiqaməti üzrə Qızıl Medal" },
        { icon: "🤖", val: "ÇEMPİON", label: "Mini Sumo Robototexnika", sub: "Azərbaycan Beynəlxalq Olimpiada" },
        { icon: "🛡️", val: "LEVEL 1 & 2", label: "Ethical Hacker", sub: "Beynəlxalq kiber sertifikatlar" },
        { icon: "🌟", val: "İLİN GƏNCİ", label: "Fəxri Dövlət Mükafatı", sub: "İctimai fəallıq və nailiyyətlər" }
      ],
      highlights: [
        {
          year: "2027",
          flag: "🇫🇮",
          country: "Finlandiya",
          title: "Beynəlxalq Abilimpiya Çempionatı",
          text: "Azərbaycan Milli Komandasının tərkibində ölkəmizi təmsil etmək vəsiqəsi qazanmışdır."
        },
        {
          year: "2026",
          flag: "🇯🇵",
          country: "Yaponiya",
          title: "Beynəlxalq Robototexnika Yarışı",
          text: "Azərbaycan Mini Sumo çempionu kimi Yaponiyada keçiriləcək beynəlxalq yarışda Azərbaycanı təmsil edəcək."
        },
        {
          year: "2024",
          flag: "🇺🇸",
          country: "ABŞ",
          title: "FIRST Robotics Competition & NASA Layihəsi",
          text: "Amerika Birləşmiş Ştatlarında NASA layihəsi ilə əlaqəli FRC yarışında Azərbaycanı təmsil etmişdir."
        }
      ],
      tags: [
        "#İnformasiyaTexnologiyaları",
        "#Kibertəhlükəsizlik",
        "#EthicalHacker_L1_L2",
        "#Robototexnika",
        "#MiniSumo_Çempionu",
        "#FIRST_Robotics_NASA",
        "#MilliAbilimpiya_I_Yer",
        "#Finlandiya2027",
        "#Yaponiya2026",
        "#İlinGənci"
      ],
      timeline: [
        {
          year: "2027",
          badge: "🇫🇮 Finlandiya · Qlobal Vəsiqə",
          title: "Beynəlxalq Abilimpiya Çempionatı (Finlandiya)",
          desc: "2026-cı il Milli Abilimpiya Çempionatında İnformasiya Texnologiyaları istiqaməti üzrə qazanılmış I yer (qızıl medal) nəticəsinə əsasən, 2027-ci ildə Finlandiyada keçiriləcək Beynəlxalq Abilimpiya Çempionatında iştirak edəcək Azərbaycan milli komandasının tərkibində ölkəmizi təmsil etmək hüququ qazanmışdır."
        },
        {
          year: "2026",
          badge: "🇯🇵 Yaponiya · Qlobal Vəsiqə & Çempionluq",
          title: "Azərbaycan Beynəlxalq Robot Olimpiadası — Mini Sumo Çempionu",
          desc: "Azərbaycan Beynəlxalq Robot Olimpiadasında yüksək nəticə göstərərək Mini Sumo robototexnika kateqoriyasında Respublika Çempionu olmuşdur. Əldə etdiyi nəticələr əsasında Yaponiyada keçiriləcək beynəlxalq robototexnika yarışında Azərbaycanı təmsil etmək hüququ qazanmışdır."
        },
        {
          year: "2026",
          badge: "🥇 Qızıl Medal & Diplom",
          title: "Milli Abilimpiya Çempionatı — I Yer Qalibi",
          desc: "İnformasiya Texnologiyaları istiqaməti üzrə bütün rəqiblərini qabaqlayaraq fəxri I yerin qalibi olmuş, qızıl medal və xüsusi diplomla təltif edilmişdir."
        },
        {
          year: "2025",
          badge: "🤝 Könüllü Mentorluq & İnklüziv Dəstək",
          title: "FIRST Robotics Komandasına Texniki Mentorluq və Sosial Maarifləndirmə",
          desc: "FIRST Robotics Competition yarışında iştirak etmək üçün xaricə gedən komandaya könüllü olaraq öz bilik və təcrübəsi ilə dəstək olmuş, komanda üzvlərinin hazırlanmasına və onların texniki biliklərinin inkişafına töhfə vermişdir. Eyni zamanda müxtəlif texnologiya ilə bağlı sosial inklüziv layihələrdə iştirak etmiş, əldə etdiyi bilik və bacarıqlarını digər uşaqlar və gənclərlə bölüşmüşdür."
        },
        {
          year: "2024",
          badge: "🇺🇸 ABŞ & 🇹🇷 Türkiyə",
          title: "FIRST Robotics Competition (NASA Layihəsi) & 16-cı MEB Robot",
          desc: "Amerika Birləşmiş Ştatlarında keçirilən və NASA layihəsi ilə əlaqəli FIRST Robotics Competition yarışında Azərbaycanı təmsil etmiş, beynəlxalq robototexnika mühitində zəngin praktiki təcrübə qazanmışdır. Həmin il Türkiyədə keçirilən 16-cı Beynəlxalq MEB Robot Yarışında iştirak etmişdir."
        },
        {
          year: "2023",
          badge: "🥉 Respublika Mükafatı & Kiber Məktəb",
          title: "Milli Abilimpiya Çempionatı III Yer & AKTA Cyber Summer School 2023",
          desc: "Milli Abilimpiya Çempionatında İnformasiya Texnologiyaları istiqaməti üzrə III yerin qalibi olmuş, medal və diplomla təltif edilmişdir. Həmin il AKTA Cyber Summer School 2023 proqramında iştirak edərək kibertəhlükəsizlik sahəsində bilik və praktiki bacarıqlarını inkişaf etdirmişdir."
        },
        {
          year: "2019–2022",
          badge: "💻 Fundamental Təhsil",
          title: "STEP IT Kids Academy — İT və Rəqəmsal Texnologiyalar",
          desc: "STEP IT Kids Academy-də informasiya texnologiyaları və rəqəmsal texnologiyalar istiqamətində dördillik peşəkar təhsil almışdır."
        }
      ],
      fullBio: [
        "Mirzəzadə Sənan Azər oğlu informasiya texnologiyaları, kibertəhlükəsizlik və robototexnika sahələrində özünü inkişaf etdirən, müxtəlif yerli və beynəlxalq yarışlarda iştirak edərək yüksək nəticələr əldə edən gəncdir.",
        "2019–2022-ci illərdə STEP IT Kids Academy-də informasiya texnologiyaları və rəqəmsal texnologiyalar istiqamətində təhsil almışdır.",
        "2023-cü ildə Milli Abilimpiya Çempionatında İnformasiya Texnologiyaları istiqaməti üzrə III yerin qalibi olmuş, medal və diplomla təltif edilmişdir. Həmin il AKTA Cyber Summer School 2023 proqramında iştirak edərək kibertəhlükəsizlik sahəsində bilik və praktiki bacarıqlarını inkişaf etdirmişdir.",
        "2024-cü ildə Türkiyədə keçirilən 16-cı Beynəlxalq MEB Robot Yarışında iştirak etmişdir. Həmin il Amerika Birləşmiş Ştatlarında keçirilən və NASA layihəsi ilə əlaqəli FIRST Robotics Competition yarışında Azərbaycanı təmsil etmişdir. Bu yarış çərçivəsində beynəlxalq robototexnika mühitində praktiki təcrübə qazanmışdır.",
        "2025-ci ildə FIRST Robotics Competition yarışında iştirak etmək üçün xaricə gedən komandaya könüllü olaraq öz bilik və təcrübəsi ilə dəstək olmuş, komanda üzvlərinin hazırlanmasına və onların texniki biliklərinin inkişafına töhfə vermişdir. Eyni zamanda müxtəlif texnologiya ilə bağlı sosial inklüziv layihələrdə iştirak etmiş, əldə etdiyi bilik və bacarıqlarını digər uşaqlar və gənclərlə bölüşmüşdür.",
        "2026-cı ildə Milli Abilimpiya Çempionatında İnformasiya Texnologiyaları istiqaməti üzrə I yerin qalibi olmuşdur. Bu nəticəyə əsasən, 2027-ci ildə Finlandiyada keçiriləcək Beynəlxalq Abilimpiya Çempionatında iştirak edəcək Azərbaycan milli komandasının tərkibində ölkəmizi təmsil etmək hüququ qazanmışdır.",
        "2026-cı ildə Azərbaycan Beynəlxalq Robot Olimpiadasında iştirak edərək yüksək nəticə göstərmiş, Mini Sumo robototexnika kateqoriyasında çempion olmuşdur. Əldə etdiyi nəticələr əsasında Yaponiyada keçiriləcək beynəlxalq robototexnika yarışında Azərbaycanı təmsil etmək hüququ qazanmışdır.",
        "Kibertəhlükəsizlik sahəsində Ethical Hacker Level 1 və Ethical Hacker Level 2 proqramlarını uğurla tamamlamışdır. İnformasiya texnologiyaları, kompüter şəbəkələri, kibertəhlükəsizlik və robototexnika üzrə müxtəlif seminar, təlim və praktiki proqramlarda iştirak edərək peşəkar bilik və bacarıqlarını davamlı şəkildə inkişaf etdirir.",
        "Sənan əldə etdiyi bilik və təcrübəni yalnız şəxsi inkişafı üçün deyil, həmçinin yarışlara hazırlaşan uşaqların və gənclərin hazırlanmasına dəstək olmaq, öz təcrübəsini bölüşmək və texnologiya sahəsində sosial inklüzivliyin inkişafına töhfə vermək məqsədilə də istifadə edir.",
        "Gənclər və texnologiya sahəsində göstərdiyi fəallıq, əldə etdiyi nailiyyətlər və ictimai fəaliyyəti nəzərə alınaraq “İlin Gənci” mükafatına layiq görülmüşdür.",
        "Sənanın əldə etdiyi nəticələr onun informasiya texnologiyaları, kibertəhlükəsizlik və robototexnika sahələrində ardıcıl inkişaf etdiyini, beynəlxalq səviyyədə Azərbaycanı təmsil etdiyini və öz bilik və təcrübəsini digər gənclərlə bölüşərək sosial fayda yaratdığını göstərir."
      ],
      certificates: [
        { icon: "🛡️", title: "Ethical Hacker Level 1", sub: "Kibertəhlükəsizlik & Şəbəkə Müdafiəsi" },
        { icon: "🔐", title: "Ethical Hacker Level 2", sub: "Təkmil Penetrasiya & Təhlükə Analizi" },
        { icon: "🌐", title: "AKTA Cyber Summer School 2023", sub: "Azərbaycan Kibertəhlükəsizlik Təşkilatları Assosiasiyası" },
        { icon: "🥇", title: "Milli Abilimpiya Qızıl Medal (2026)", sub: "İnformasiya Texnologiyaları üzrə I Yer" },
        { icon: "🤖", title: "Mini Sumo Robototexnika Çempionu", sub: "Azərbaycan Beynəlxalq Robot Olimpiadası (2026)" },
        { icon: "🚀", title: "FIRST Robotics & NASA Layihəsi", sub: "Beynəlxalq Mühəndislik və Robototexnika (ABŞ)" },
        { icon: "💻", title: "STEP IT Kids Academy Məzunu", sub: "İKT və Rəqəmsal Texnologiyalar (2019-2022)" },
        { icon: "🌟", title: "“İlin Gənci” Fəxri Dövlət Mükafatı", sub: "İctimai Fəallıq və İnklüziv Layihələrə Töhfə" }
      ],
      gallery: [
        { type: "image", src: "senan1.jpeg", caption: "Mirzəzadə Sənan — Fəxri Tələbə Portreti" },
        { type: "image", src: "senan2.jpeg", caption: "Milli Abilimpiya Mükafatlandırma Mərasimi" },
        { type: "image", src: "senan3.jpeg", caption: "Mini Sumo Robototexnika Çempionluğu" },
        { type: "image", src: "senan4.jpeg", caption: "FIRST Robotics (NASA) Beynəlxalq Yarışı" },
        { type: "image", src: "senan5.jpeg", caption: "Kibertəhlükəsizlik & Ethical Hacker Proqramı" },
        { type: "image", src: "senan6.jpeg", caption: "AKTA Cyber Summer School Praktiki Təlimi" },
        { type: "image", src: "senan7.jpeg", caption: "16-cı Beynəlxalq MEB Robot Yarışı (Türkiyə)" },
        { type: "image", src: "senan8.jpeg", caption: "Sosial İnklüziv Layihələr & Könüllü Dəstək" },
        { type: "image", src: "senan9.jpeg", caption: "“İlin Gənci” Mükafat Təqdimatı" },
        { type: "video", src: "senan10.mp4", caption: "Robototexnika və Canlı Çıxış Video Xronikası" },
        { type: "image", src: "senan11.jpeg", caption: "Beynəlxalq Robot Arena və Hazırlıq" },
        { type: "image", src: "senan12.jpeg", caption: "Diplomlar, Qızıl Medallar və Təltiflər" }
      ]
    }
  ];

  function renderHonorCard(student) {
    const flagsHtml = student.flags
      .map(
        (f) =>
          '<span class="honor-flag-tag" title="' + f.note + '">' +
            '<span class="flag-emoji">' + f.emoji + '</span> ' +
            '<span>' + f.name + '</span>' +
          '</span>'
      )
      .join("");

    const statsHtml = student.stats
      .map(
        (s) =>
          '<div class="honor-stat-card">' +
            '<div class="honor-stat-top">' +
              '<span class="honor-stat-icon">' + s.icon + '</span>' +
              '<span class="honor-stat-val">' + s.val + '</span>' +
            '</div>' +
            '<div class="honor-stat-label">' + s.label + '</div>' +
            '<div class="honor-stat-sub">' + s.sub + '</div>' +
          '</div>'
      )
      .join("");

    const highlightsHtml = student.highlights
      .map(
        (h) =>
          '<div class="honor-highlight-row">' +
            '<span class="honor-highlight-bullet">✦</span>' +
            '<div>' +
              '<strong>' + h.flag + ' ' + h.year + ' (' + h.country + ') — ' + h.title + ':</strong> ' +
              '<span>' + h.text + '</span>' +
            '</div>' +
          '</div>'
      )
      .join("");

    const tagsHtml = student.tags
      .map((t) => '<span class="honor-tag-pill">' + t + '</span>')
      .join("");

    // Mini thumbnails
    const thumbsHtml = student.gallery
      .slice(0, 5)
      .map(
        (g) =>
          '<img src="' +
          (g.type === "video" ? "logo.jpg" : g.src) +
          '" class="honor-preview-thumb" alt="' +
          g.caption +
          '" title="' +
          g.caption +
          '" data-open-modal="' +
          student.id +
          '" data-tab="gallery" />'
      )
      .join("");

    return (
      '<article class="honor-student-card" id="student-' + student.id + '">' +
        '<div class="honor-card-ambient" aria-hidden="true"></div>' +

        '<!-- Left Column: Avatar & Actions -->' +
        '<div class="honor-card-aside">' +
          '<div class="honor-avatar-wrap">' +
            '<img ' +
              'src="' + student.photo + '" ' +
              'alt="' + student.fullName + '" ' +
              'class="honor-avatar-img" ' +
              'loading="lazy" ' +
              'onerror="this.onerror=null;this.src=\\'' + student.fallbackPhoto + '\\';" ' +
            '/>' +
            '<div class="honor-avatar-overlay">' +
              '<span class="honor-verified-pill">⭐ FƏXRİ TƏLƏBƏ</span>' +
            '</div>' +
          '</div>' +

          '<div class="honor-status-pill">' +
            '<span class="honor-status-dot"></span>' +
            '<span>' + student.statusText + '</span>' +
          '</div>' +

          '<div class="honor-flags-box">' +
            '<div class="honor-flags-heading">' +
              '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>' +
              '<span>TƏMSİL OLUNAN ÖLKƏLƏR</span>' +
            '</div>' +
            '<div class="honor-flags-list">' +
              flagsHtml +
            '</div>' +
          '</div>' +

          '<div class="honor-aside-actions">' +
            '<button type="button" class="honor-btn-primary" data-open-modal="' + student.id + '" data-tab="bio">' +
              '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>' +
              '<span>Ətraflı Dosye</span>' +
            '</button>' +
            '<button type="button" class="honor-btn-secondary" data-open-modal="' + student.id + '" data-tab="timeline">' +
              '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>' +
              '<span>Nailiyyət Xronologiyası</span>' +
            '</button>' +
            '<button type="button" class="honor-btn-secondary" data-open-modal="' + student.id + '" data-tab="gallery" style="border-color: rgba(0, 210, 255, 0.4); color: #7fe4ff;">' +
              '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>' +
              '<span>Foto & Video Arxivi (12 Media)</span>' +
            '</button>' +
            '<div class="honor-gallery-preview-strip">' +
              thumbsHtml +
            '</div>' +
          '</div>' +
        '</div>' +

        '<!-- Right Column: Details & Stats -->' +
        '<div class="honor-card-main">' +
          '<div class="honor-main-topbar">' +
            '<div class="honor-kicker-tag">' +
              '<span>🤖</span> ' +
              '<span>İKT, Kibertəhlükəsizlik & Robototexnika</span>' +
            '</div>' +
            '<div class="honor-badge-shimmer">' +
              '<span>🌟</span> ' +
              '<span>' + student.titleBadge + '</span>' +
            '</div>' +
          '</div>' +

          '<div>' +
            '<h4 class="honor-student-name">' + student.fullName + '</h4>' +
            '<div class="honor-student-role">' + student.role + '</div>' +
          '</div>' +

          '<!-- 4 Stats Grid -->' +
          '<div class="honor-stats-grid">' +
            statsHtml +
          '</div>' +

          '<!-- Recent Milestones Box -->' +
          '<div class="honor-highlights-box">' +
            '<div class="honor-highlights-heading">' +
              '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>' +
              '<span>ƏSAS BEYNƏLXALQ TƏMSİLÇİLİKLƏR VƏ HƏDƏFLƏR</span>' +
            '</div>' +
            '<div class="honor-highlights-list">' +
              highlightsHtml +
            '</div>' +
          '</div>' +

          '<!-- Quote Block -->' +
          '<div class="honor-quote-box">' +
            '<span class="honor-quote-icon" aria-hidden="true">“</span>' +
            '<p class="honor-quote-text">' + student.quote + '</p>' +
          '</div>' +

          '<!-- Tags -->' +
          '<div class="honor-tags-row">' +
            tagsHtml +
          '</div>' +
        '</div>' +
      '</article>'
    );
  }

  function renderHonorList(filter) {
    if (!filter) filter = "all";
    const grid = document.getElementById("honor-students-grid");
    if (!grid) return;

    const filtered = honorStudentsData.filter((student) => {
      if (filter === "all") return true;
      return student.categories.indexOf(filter) !== -1;
    });

    if (filtered.length === 0) {
      grid.innerHTML = '<div style="text-align: center; padding: 40px; color: rgba(248, 250, 252, 0.6);">Bu kateqoriya üzrə məlumat hazırlanır.</div>';
      return;
    }

    grid.innerHTML = filtered.map(renderHonorCard).join("");
    attachCardListeners();
  }

  function openHonorModal(studentId, initialTab) {
    if (!initialTab) initialTab = "bio";
    const student = honorStudentsData.find((s) => s.id === studentId);
    if (!student) return;

    const modal = document.getElementById("honor-student-modal");
    const modalBody = document.getElementById("honor-modal-body");
    if (!modal || !modalBody) return;

    // Timeline HTML
    const timelineHtml = student.timeline
      .map(
        (t) =>
          '<div class="honor-timeline-node">' +
            '<div class="honor-timeline-marker">✦</div>' +
            '<div class="honor-timeline-content">' +
              '<div class="honor-timeline-header">' +
                '<span class="honor-timeline-year">' + t.year + '</span>' +
                '<span class="honor-timeline-badge">' + t.badge + '</span>' +
              '</div>' +
              '<h5 class="honor-timeline-title">' + t.title + '</h5>' +
              '<p class="honor-timeline-desc">' + t.desc + '</p>' +
            '</div>' +
          '</div>'
      )
      .join("");

    // Bio HTML
    const bioHtml = student.fullBio
      .map((p) => '<p class="honor-modal-bio-p">' + p + '</p>')
      .join("");

    // Certificates HTML
    const certsHtml = student.certificates
      .map(
        (c) =>
          '<div class="honor-cert-item">' +
            '<div class="honor-cert-icon">' + c.icon + '</div>' +
            '<div>' +
              '<h5 class="honor-cert-name">' + c.title + '</h5>' +
              '<p class="honor-cert-org">' + c.sub + '</p>' +
            '</div>' +
          '</div>'
      )
      .join("");

    // Gallery HTML
    const galleryHtml = student.gallery
      .map((g) => {
        if (g.type === "video") {
          return (
            '<div class="honor-gallery-item">' +
              '<span class="honor-gallery-video-badge">▶ Video</span>' +
              '<video src="' + g.src + '" class="honor-gallery-video" controls playsinline preload="metadata"></video>' +
              '<div class="honor-gallery-caption">' + g.caption + '</div>' +
            '</div>'
          );
        } else {
          return (
            '<div class="honor-gallery-item">' +
              '<img src="' + g.src + '" class="honor-gallery-img" alt="' + g.caption + '" loading="lazy" />' +
              '<div class="honor-gallery-caption">' + g.caption + '</div>' +
            '</div>'
          );
        }
      })
      .join("");

    modalBody.innerHTML =
      '<!-- Modal Hero -->' +
      '<div class="honor-modal-hero">' +
        '<img ' +
          'src="' + student.photo + '" ' +
          'alt="' + student.fullName + '" ' +
          'class="honor-modal-avatar" ' +
          'onerror="this.onerror=null;this.src=\\'' + student.fallbackPhoto + '\\';" ' +
        '/>' +
        '<div class="honor-modal-hero-info">' +
          '<h3>' + student.fullName + '</h3>' +
          '<p>' + student.role + '</p>' +
          '<div class="honor-modal-hero-badges">' +
            '<span class="honor-badge-shimmer">🌟 ' + student.titleBadge + '</span> ' +
            '<span class="honor-verified-pill">🏆 Fəxri Tələbə</span>' +
          '</div>' +
        '</div>' +
      '</div>' +

      '<!-- Tab Navigation inside Modal -->' +
      '<div class="honor-modal-tab-nav" role="tablist">' +
        '<button type="button" class="honor-modal-tab ' + (initialTab === 'bio' ? 'active' : '') + '" data-modal-target="pane-bio">' +
          '📖 Tam Bioqrafiya və İctimai Fəaliyyət' +
        '</button>' +
        '<button type="button" class="honor-modal-tab ' + (initialTab === 'timeline' ? 'active' : '') + '" data-modal-target="pane-timeline">' +
          '⏳ 2019–2027 Uğur Xronologiyası' +
        '</button>' +
        '<button type="button" class="honor-modal-tab ' + (initialTab === 'certs' ? 'active' : '') + '" data-modal-target="pane-certs">' +
          '🎖️ Sertifikatlar & Qələbələr' +
        '</button>' +
        '<button type="button" class="honor-modal-tab ' + (initialTab === 'gallery' ? 'active' : '') + '" data-modal-target="pane-gallery">' +
          '📸 Foto & Video Arxivi (' + student.gallery.length + ')' +
        '</button>' +
      '</div>' +

      '<!-- Tab Panes -->' +
      '<div class="honor-modal-panes">' +
        '<div class="honor-modal-tab-pane ' + (initialTab === 'bio' ? 'active' : '') + '" id="pane-bio">' +
          bioHtml +
        '</div>' +
        '<div class="honor-modal-tab-pane ' + (initialTab === 'timeline' ? 'active' : '') + '" id="pane-timeline">' +
          '<div class="honor-modal-timeline">' +
            timelineHtml +
          '</div>' +
        '</div>' +
        '<div class="honor-modal-tab-pane ' + (initialTab === 'certs' ? 'active' : '') + '" id="pane-certs">' +
          '<div class="honor-certs-grid">' +
            certsHtml +
          '</div>' +
        '</div>' +
        '<div class="honor-modal-tab-pane ' + (initialTab === 'gallery' ? 'active' : '') + '" id="pane-gallery">' +
          '<div class="honor-gallery-grid">' +
            galleryHtml +
          '</div>' +
        '</div>' +
      '</div>';

    // Tab switching inside modal
    modalBody.querySelectorAll(".honor-modal-tab").forEach((tabBtn) => {
      tabBtn.addEventListener("click", () => {
        const targetId = tabBtn.getAttribute("data-modal-target");
        modalBody.querySelectorAll(".honor-modal-tab").forEach((b) => b.classList.remove("active"));
        modalBody.querySelectorAll(".honor-modal-tab-pane").forEach((p) => p.classList.remove("active"));

        tabBtn.classList.add("active");
        const targetPane = modalBody.querySelector("#" + targetId);
        if (targetPane) targetPane.classList.add("active");
      });
    });

    modal.classList.add("open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
  }

  function closeHonorModal() {
    const modal = document.getElementById("honor-student-modal");
    if (!modal) return;
    modal.classList.remove("open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    // Pause any playing videos
    modal.querySelectorAll("video").forEach((v) => v.pause());
  }

  function attachCardListeners() {
    document.querySelectorAll("[data-open-modal]").forEach((btn) => {
      btn.addEventListener("click", () => {
        const sId = btn.getAttribute("data-open-modal");
        const tab = btn.getAttribute("data-tab") || "bio";
        openHonorModal(sId, tab);
      });
    });
  }

  function init() {
    // 1. Initial Render
    renderHonorList("all");

    // 2. Tab filtering listeners
    const filterBtns = document.querySelectorAll(".honor-tab-btn[data-honor-filter]");
    filterBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        const filter = btn.getAttribute("data-honor-filter");
        filterBtns.forEach((b) => {
          b.classList.remove("active");
          b.setAttribute("aria-selected", "false");
        });
        btn.classList.add("active");
        btn.setAttribute("aria-selected", "true");
        renderHonorList(filter);
      });
    });

    // 3. Modal close events
    const closeBtn = document.getElementById("honor-modal-close");
    if (closeBtn) {
      closeBtn.addEventListener("click", closeHonorModal);
    }

    const modal = document.getElementById("honor-student-modal");
    if (modal) {
      modal.addEventListener("click", (e) => {
        if (e.target === modal) {
          closeHonorModal();
        }
      });
    }

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape") {
        closeHonorModal();
      }
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
`;

  const updatedJs = baseJs + newModule;
  fs.writeFileSync(scriptJsPath, updatedJs, 'utf8');
  fs.writeFileSync(backupJsPath, updatedJs, 'utf8');
  console.log('script.js and script_working_backup.js updated with gallery support!');
} else {
  console.error('Could not find oldModuleStart in script.js');
}

