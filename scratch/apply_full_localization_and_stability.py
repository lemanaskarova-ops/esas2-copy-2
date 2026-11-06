# -*- coding: utf-8 -*-
import os
import re
import sys

BASE_DIR = '/Users/konul/Documents/esas2 copy 2'
HTML_FILE = os.path.join(BASE_DIR, 'index.html')
CSS_FILE = os.path.join(BASE_DIR, 'style.css')
JS_FILE = os.path.join(BASE_DIR, 'script.js')
BACKUP_JS = os.path.join(BASE_DIR, 'scratch/script_working_backup.js')

# 1. DICTIONARIES FOR THE 147 KEYS
KEYS_AZ = {
    # Page Title & Hero
    "page_title": "BDRNK — Bakı Dövlət Rabitə və Nəqliyyat Kolleci Publik Hüquqi Şəxsi",
    "hero_aura_tagline": "Dövlət Standartı ilə Rəqəmsal Gələcəyə Doğru",
    "about_director_bio_btn": "Rəsmi Bioqrafiya",

    # Honor Students / Hall of Fame
    "honors_sub_badge": "Qlobal Nailiyyətlər & Beynəlxalq Təmsilçilik",
    "fame_tab_all": "Hamısı",
    "fame_tab_it": "İKT & Robototexnika",
    "fame_tab_champ": "Beynəlxalq Çempionatlar",
    "fame_tab_youth": "İlin Gənci & Sosial İnklüzivlik",

    # Qarabağ Zəfər Salnaməsi
    "qarabag_video_title_1": "Zəfər Xronikası · 8 Noyabr",
    "qarabag_video_badge_1": "QARABAĞ AZƏRBAYCANDIR!",
    "qarabag_cinema_btn_1": "Zəfər Xronikası (Tam Ekran)",
    "qarabag_video_title_2": "Qarabağ Gəzintisi · Ağdam - Xankəndi - Şuşa",
    "qarabag_video_badge_2": "QARABAĞ GƏZİNTİSİ",
    "qarabag_cinema_btn_2": "Qarabağ Gəzintisi (Tam Ekran)",
    "qarabag_eyebrow": "🇦🇿 ZƏFƏR SALNAMƏSİ · 8 NOYABR",
    "qarabag_heading": "ZƏFƏR YOLUNDA BİRLİK, HƏMRƏYLİK VƏ VƏTƏN SEVGİSİ",
    "qarabag_pill_agdam": "📍 Ağdam",
    "qarabag_pill_khankendi": "📍 Xankəndi",
    "qarabag_pill_shusha": "📍 Şuşa",
    "qarabag_lead": "8 Noyabr – Zəfər Günü münasibətilə Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecinin kollektivinin Ağdam, Xankəndi və Şuşaya təşkil olunan səfəri həm tarixi yaddaşımıza, milli-mənəvi dəyərlərimizə və Vətən sevgimizə bağlılığın, həm də kollektiv birliyinin və həmrəyliyinin parlaq təzahürü oldu.",
    "qarabag_p1": "Səfərin əsas dəyəri yalnız tarixi və mədəni məkanları ziyarət etməklə məhdudlaşmırdı. Müxtəlif vəzifə və fəaliyyət istiqamətlərində çalışan əməkdaşlarımızın vahid məqsəd, ortaq dəyərlər və eyni Vətən sevgisi ətrafında bir araya gəlməsi bu səfərə xüsusi məna və mənəvi dəyər qazandırdı. Birlikdə qət etdiyimiz yollar, səmimi ünsiyyətimiz, xoş təəssüratlarımız və bölüşdüyümüz qürur hissi kollektivimizin həm peşəkar, həm də insani münasibətlər baxımından möhkəm birliyini bir daha nümayiş etdirdi.",
    "qarabag_p2": "Belə səfərlər kollektiv üzvləri arasında qarşılıqlı hörmət və etimadı gücləndirir, işgüzar münasibətləri daha səmimi əməkdaşlığa çevirir, dostluq və həmrəylik bağlarını möhkəmləndirir. Çünki sağlam kollektiv mühiti yalnız birgə əmək fəaliyyəti ilə deyil, həm də ortaq dəyərlərin, sevincin, qürurun və məsuliyyətin bölüşülməsi ilə formalaşır.",
    "qarabag_quote": "“Ağdamın dirçəlişi və yenidən qurulan siması, Xankəndinin doğma yurda qovuşmasının yaratdığı qürur, Şuşanın tarixi və mədəni əzəməti hər birimizdə unudulmaz təəssüratlar yaratdı. Bu torpaqlarda olmaq bizə bir daha xatırlatdı ki, Zəfərimiz yalnız hərbi-siyasi qələbə deyil, həm də xalqımızın milli birliyinin, sarsılmaz iradəsinin, dövlətçilik əzminin və Vətən sevgisinin təntənəsidir.”",
    "qarabag_p3": "Bu səfər, eyni zamanda, torpaqlarımızın azadlığı uğrunda canlarından keçmiş şəhidlərimizin əziz xatirəsinə ehtiramımızın, qəhrəman qazilərimizə minnətdarlığımızın ifadəsi idi. Azad Qarabağın havasını udmaq, bu müqəddəs torpaqlarda Zəfər tariximizin izlərini görmək hər birimiz üçün böyük şərəf və qürur mənbəyinə çevrildi.",
    "qarabag_p4": "İnanırıq ki, belə mənəvi əhəmiyyət daşıyan tədbirlər kollektivimizin birliyini daha da gücləndirir, əməkdaşlarımız arasında dostluq və həmrəylik münasibətlərini inkişaf etdirir, gələcək fəaliyyətimizdə ortaq məqsədlər ətrafında daha sıx birləşməyimizə stimul verir.",
    "qarabag_p5": "Çünki güclü kollektiv yalnız birlikdə çalışan insanlar deyil, həm də eyni dəyərləri bölüşən, uğura birlikdə sevinən, çətinlikləri birgə aşan, məsuliyyəti və qüruru paylaşan insanlardan formalaşır.",
    "qarabag_p6": "Bu səfər bizə bir daha göstərdi ki, birliyimiz mənəvi gücümüz, həmrəyliyimiz uğurlarımızın təməli, Vətən sevgimiz isə bizi birləşdirən ən ali dəyərdir.",
    "qarabag_p7": "Şəhidlərimizin əziz xatirəsi daim qəlbimizdə yaşayacaq, onların bizə əmanət etdiyi Zəfər və azadlıq ruhu gələcək nəsillərə ötürüləcək!",
    "qarabag_p8": "Zəfər tariximizlə fəxr edir, azad Qarabağımızın dirçəlişinə sevinir və milli birliyimizi, kollektiv həmrəyliyimizi daim yaşatmağı özümüzə mənəvi borc bilirik.",
    "qarabag_credo_title": "🇦🇿 Birliyimiz gücümüz, həmrəyliyimiz qürurumuz, Vətən sevgimiz ən böyük dəyərimizdir!",
    "qarabag_credo_sub": "Zəfərimiz əbədi, Azərbaycanımız daim var olsun! Qarabağ Azərbaycandır!",

    # Structure & Campus Navigator
    "struct_badge_count": "9 FBK",
    "struct_commissions_view_title": "🎓 TƏDRİS-METODİK APARAT",
    "campus_rooms_count_text": "Göstərilən otaqlar:",
    "lib_total_counter": "44 Rəsmi Dərs Vəsaiti",
    "lib_fund_about_btn": "🏛️ Kitabxana Fondu və Tarixi",
    "science_director_bio_btn": "Direktor Səbuhi Qurbanovun Bioqrafiyası",

    # Video Lectures Department Metas
    "dept_meta_all": "23 Videodərs · Bütün fənlər",
    "dept_meta_it": "2 Videodərs · Kompüter sistemləri",
    "dept_meta_transport": "1 Videodərs · Nəqliyyat Sistemləri",
    "dept_meta_geography": "2 Videodərs · Yer Elmləri və Coğrafiya",
    "dept_meta_physics": "1 Videodərs · Təbiət və Fizika",
    "dept_meta_history": "9 Videodərs · Tarix və Zəfər",
    "dept_meta_az_lang": "1 Videodərs · Qrammatika və Nitq",
    "dept_meta_law": "6 Videodərs · Hüquq sistemi",
    "dept_meta_biology": "1 Videodərs · Təbiət elmləri",

    # Gallery Portals
    "gal_headline_exam": "Şəffaf və Rəqəmsal İmtahan Sessiyaları",
    "gal_summary_exam": "Kollecimizdə tələbələrin biliyinin obyektiv qiymətləndirilməsi üçün müasir monitorinq və kompüterləşdirilmiş imtahan mərkəzi fəaliyyət göstərir.",
    "gal_headline_events": "Təntənəli Toplantılar və Tarixi Günlər",
    "gal_summary_events": "Dövlət bayramları, məzun buraxılışları, anım tədbirləri və beynəlxalq konfranslardan yaddaqalan rəsmi kadrlar toplusu.",
    "gal_headline_rooms": "Müasir Tədris Zalları və İnfrastruktur",
    "gal_summary_rooms": "Geniş amfiteatr zalları, multimedia lövhələri ilə təchiz olunmuş siniflər və texnoloji laboratoriyalarımız.",
    "gal_headline_study": "Canlı Dərs Mühiti və Tələbə Praktikası",
    "gal_summary_study": "Tələbələrimizin komanda işləri, interaktiv seminarlar, elektron kitabxana fəaliyyəti və laborator təcrübə saatları.",

    # Director Bio Modal
    "bio_brand_title": "BDRNK · RƏSMİ DİREKTOR PORTALI",
    "bio_brand_sub": "Səbuhi Qurbanov Yusif oğlu — Tərcümeyi-hal və Təəssüratlar",
    "bio_pill_medal": "🎖️ «TƏRƏQQİ» MEDALLI",
    "bio_pill_entity": "KOLLEC DİREKTORLUĞU",
    "bio_hero_name": "SƏBUHİ QURBANOV YUSİF OĞLU",
    "bio_hero_title": "Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi, Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru",
    "bio_fact_birth": "🎂 4 avqust 1980 · Şəki",
    "bio_fact_edu": "🎓 BDU Riyaziyyat & UNEC MBA",
    "bio_fact_author": "📐 ETN Qrifli Dərslik Müəllifi",
    "bio_nav_tab_edu": "🎓 Təhsil və Həyatı",
    "bio_nav_tab_career": "💼 Əmək Fəaliyyəti",
    "bio_nav_tab_pedagogy": "📚 Elmi Əsərləri",
    "bio_nav_tab_international": "🌐 Beynəlxalq Fəaliyyət",
    "bio_nav_tab_awards": "🏅 Dövlət Təltifləri",
    "bio_nav_tab_reflections": "✍️ Kollec Haqqında Təəssüratlarım",
    "bio_sec_i_kicker": "BÖLMƏ I · DOĞUMU VƏ AKADEMİK TƏHSİLİ",
    "bio_sec_i_title": "Həyatı və Təhsil İlləri",
    "bio_sec_i_lead": "<strong>Səbuhi Qurbanov Yusif oğlu</strong> 4 avqust 1980-ci ildə Şəki rayonu Qayabaşı kəndində anadan olmuş, 1986-cı ildə Qayabaşı kənd tam orta məktəbinin 1-ci sinifinə qəbul olmuş, 1997-ci ildə məktəbi fərqlənmə ilə bitirmişdir.",
    "bio_sec_i_p2": "1997–2001-ci illərdə <strong>Bakı Dövlət Universitetinin Riyaziyyat fakültəsində</strong> bakalavr təhsili almışdır. 2001–2002-ci illərdə Azərbaycan Respublikası Silahlı Qüvvələrinin N saylı hərbi hissəsində hərbi xidmətdə olmuşdur. Daha sonra <strong>Azərbaycan Dövlət İqtisad Universitetində (UNEC)</strong> «Biznesin təşkili və idarə edilməsi» ixtisası üzrə magistratura təhsili almışdır.",
    "bio_sec_ii_kicker": "BÖLMƏ II · ƏMƏK FƏALİYYƏTİNİN RƏSMİ XRONOLOGİYASI",
    "bio_sec_ii_title": "Peşəkar İdarəçilik və Pedaqoji Yolu",
    "bio_sec_ii_lead": "Səbuhi Qurbanov əmək fəaliyyətinə 2002-ci ildə başlamış və 24 ildən artıq zəngin təhsil idarəçiliyi təcrübəsinə malikdir:",
    "bio_tl_1_title": "Şəki şəhər 11 nömrəli tam orta məktəb",
    "bio_tl_1_desc": "Riyaziyyat müəllimi, eyni zamanda Təlim-tərbiyə işləri üzrə direktor müavini vəzifəsində çalışmışdır.",
    "bio_tl_2_title": "Şəki şəhər 20 nömrəli tam orta məktəb",
    "bio_tl_2_desc": "10 il ərzində məktəbin direktoru vəzifəsində səmərəli idarəçilik fəaliyyəti göstərmişdir.",
    "bio_tl_3_title": "Şəki-Zaqatala Regional Təhsil İdarəsi",
    "bio_tl_3_desc": "Tədrisin Keyfiyyəti sektorunda baş məsləhətçi vəzifəsində çalışmışdır.",
    "bio_tl_4_title": "Bakı Dövlət Rabitə və Nəqliyyat Kolleci",
    "bio_tl_4_desc": "Tədris işləri üzrə direktor müavini vəzifəsinə təyin olunmuşdur.",
    "bio_tl_5_year": "2026-cı ildən",
    "bio_tl_5_title": "Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru",
    "bio_tl_5_desc": "Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi tərəfindən Kollecin direktoru vəzifəsinə təyin olunmuşdur.",
    "bio_sec_iii_kicker": "BÖLMƏ III · ELMİ-METODİKİ VƏ PEDAQOJİ FƏALİYYƏT",
    "bio_sec_iii_title": "Dərsliklər və Elmi Vəsaitlər",
    "bio_sec_iii_lead": "Səbuhi Qurbanov pedaqoji fəaliyyəti ilə yanaşı, riyaziyyat elminin tədrisi və ali təhsil metodikasının inkişafına mühüm töhfələr vermişdir:",
    "bio_sec_iii_b1_year": "2019 · ADPU Şurasının Qərarı",
    "bio_sec_iii_b1_title": "«Riyaziyyat – 11»",
    "bio_sec_iii_b1_desc": "Azərbaycan Dövlət Pedaqoji Universitetinin Tədris-Metodiki Şurasının qərarı ilə nəşrə tövsiyə edilmiş dərs vəsaiti.",
    "bio_sec_iii_b2_year": "3 iyun 2026 · ETN Rəsmi Qrifi",
    "bio_sec_iii_b2_title": "«Xətti cəbr və riyazi analiz»",
    "bio_sec_iii_b2_desc": "Azərbaycan Respublikası Elm və Təhsil Nazirliyinin müvafiq əmri əsasında nəşr edilmiş və rəsmi qrif verilmiş fundamental dərslik.",
    "bio_sec_iv_kicker": "BÖLMƏ IV · BEYNƏLXALQ ELMİ FORUMLAR VƏ SERTİFİKATLAR",
    "bio_sec_iv_title": "Beynəlxalq Təcrübə və İxtisasartırma",
    "bio_feat_1_badge": "🇷🇺 Moskva · 2018",
    "bio_feat_1_title": "«Современные технологии в образовании»",
    "bio_feat_1_desc": "26 iyun 2018-ci il tarixində Moskva şəhərində keçirilən beynəlxalq elmi-praktiki konfransda iştirak etmiş və məruzə ilə çıxış etmişdir.",
    "bio_feat_2_badge": "🌍 Qlobal Forum · 2021",
    "bio_feat_2_title": "«Second International Forum on New Challenges in Education»",
    "bio_feat_2_desc": "1 oktyabr 2021-ci il tarixində keçirilən beynəlxalq təhsil forumunda iştirak edərək müvafiq beynəlxalq sertifikatlar əldə etmişdir.",
    "bio_feat_3_badge": "🛡️ Dövlət Qulluğu · AC3",
    "bio_feat_3_title": "Liderlik və Dövlət İdarəçiliyi",
    "bio_feat_3_desc": "«Gənc liderlərin yay məktəbi» proqramında, Təhsil Nazirliyinin Təhsil Proqramları İnstitutu və «Mədəd Azərbaycan» MMC təlimlərində iştirak etmiş, Dövlət qulluğuna qəbul üzrə <strong>AC3 sertifikatı</strong> əldə etmişdir.",
    "bio_sec_v_kicker": "BÖLMƏ V · DÖVLƏT VƏ NAZİRLİK TƏLTİFLƏRİ",
    "bio_sec_v_title": "Milli Təhsilə Fədakar Xidmət və Mükafatlar",
    "bio_sec_v_lead": "Təhsil sahəsində uzunillik səmərəli fəaliyyəti və gənc nəslin vətənpərvər ruhda yetişməsindəki xidmətləri dövlət səviyyəsində yüksək qiymətləndirilmişdir:",
    "bio_aw_1_year": "3 oktyabr 2017",
    "bio_aw_1_title": "«Tərəqqi» Medalı",
    "bio_aw_1_desc": "Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin müvafiq Sərəncamı ilə Azərbaycan təhsilinin inkişafındakı xidmətlərinə görə <strong>«Tərəqqi» medalı</strong> ilə təltif edilmişdir.",
    "bio_aw_2_year": "5 oktyabr 2010",
    "bio_aw_2_title": "«Qabaqcıl Təhsil İşçisi» Döş Nişanı",
    "bio_aw_2_desc": "Azərbaycan Respublikası Təhsil Nazirinin müvafiq Əmri ilə gənc nəslin təlim-tərbiyəsində qazandığı uğurlara görə <strong>«Azərbaycan Respublikası qabaqcıl təhsil işçisi»</strong> döş nişanı ilə təltif olunmuşdur.",
    "bio_sec_vi_kicker": "BÖLMƏ VI · RƏHBƏRİN ŞƏXSİ BAXIŞI VƏ GƏLƏCƏK HƏDƏFLƏRİ",
    "bio_sec_vi_title": "Kollec Haqqında Təəssüratlarım və Strateji Vizyon",
    "bio_sec_vi_lead": "Direktor Səbuhi Qurbanovun Bakı Dövlət Rabitə və Nəqliyyat Kollecinin hazırkı inkişaf dinamikası və strateji hədəfləri haqqında rəsmi essesi:",
    "bio_essay_p1": "Azərbaycan Respublikası Elm və Təhsil Nazirliyinin, Elm və Ali Təhsil üzrə Dövlət Agentliyinin qərarı ilə Bakı Dövlət Rabitə və Nəqliyyat Kollecinə rəhbər təyin olunmağım mənim üçün böyük şərəf olmaqla yanaşı, həm də yüksək məsuliyyətdir.",
    "bio_essay_p2": "Kollecin fəaliyyətinə qoşulduğum ilk gündən burada formalaşmış pedaqoji ənənələr, əməkdaşların peşəkarlığı, təhsilalanların potensialı və müəssisənin zəngin tarixi məndə xoş təəssürat yaratdı. Bu təhsil müəssisəsinin illər ərzində rabitə və nəqliyyat sahələri üçün ixtisaslı kadrların hazırlanmasında oynadığı rolu xüsusi qeyd etmək istərdim.",
    "bio_essay_p3": "Kollecin fəaliyyəti ilə yaxından tanış olduqca gördüm ki, burada yalnız tədris prosesi deyil, həm də kollektivin birgə fəaliyyəti, qarşılıqlı hörmət, məsuliyyət və peşəkar yanaşma mühüm yer tutur. Mənim üçün rəhbər vəzifədə əsas məqsədlərdən biri mövcud müsbət ənənələri qorumaqla yanaşı, onların müasir dövrün tələblərinə uyğun inkişaf etdirilməsidir.",
    "bio_essay_p4": "Fəaliyyətim dövründə diqqət yetirdiyim əsas istiqamətlərdən biri təhsilin keyfiyyətinin yüksəldilməsi, tədris prosesinin müasir tələblərə uyğun təşkili, qiymətləndirmə və monitorinq mexanizmlərinin təkmilləşdirilməsi, innovativ texnologiyaların tədrisə tətbiqi və tələbələrin praktiki bilik və bacarıqlarının inkişafıdır.",
    "bio_essay_p5": "Xüsusilə kollecdə müəllim-tələbə münasibətlərinin sağlam əsaslar üzərində qurulmasını, tələbələrin təşəbbüskarlığının dəstəklənməsini, onların müxtəlif elmi, intellektual, idman və yaradıcılıq tədbirlərində iştirakını vacib hesab edirəm. Çünki müasir təhsil müəssisəsi yalnız bilik verən deyil, eyni zamanda şəxsiyyət yetişdirən, gənclərin dünyagörüşünü və vətəndaşlıq mövqeyini formalaşdıran bir məkandır.",
    "bio_essay_p6": "Kollecin əməkdaşlarının təşəbbüskarlığı, müxtəlif tədbirlərin təşkili, şagird və tələbələrlə maarifləndirici görüşlərin keçirilməsi, digər təhsil müəssisələri ilə əməkdaşlıq əlaqələrinin genişləndirilməsi istiqamətində görülən işlər də məndə müsbət təəssürat yaradır. Bakı Avropa Liseyinin müəllim və şagird heyətinin kollecdə qonaq olması, robototexnika və süni intellekt sahəsində fikir mübadiləsinin aparılması kimi görüşlər təhsil müəssisələri arasında əməkdaşlığın əhəmiyyətini bir daha nümayiş etdirir.",
    "bio_essay_p7": "Kollecin ictimai həyatında milli-mənəvi dəyərlərin, vətənpərvərlik ruhunun və dövlətçilik ənənələrinin qorunmasına da xüsusi önəm verirəm. Zəfər Günü münasibətilə kollektivimizin Ağdam, Xankəndi və Şuşaya səfəri, tələbələrin və əməkdaşların müxtəlif vətənpərvərlik tədbirlərində iştirakı bu baxımdan əlamətdar olmuşdur. İnanıram ki, gənclərimiz tariximizi dərindən öyrənməklə yanaşı, Vətənimizin bugünkü inkişafına da öz töhfələrini verməlidirlər.",
    "bio_essay_p8": "Rəhbərlik etdiyim müddətdə kollecin kollektivində müşahidə etdiyim əməkdaşlıq, qarşılıqlı dəstək və ümumi məqsəd ətrafında birləşmək istəyi gələcək fəaliyyətimiz üçün mühüm zəmin yaradır. Mən hesab edirəm ki, hər bir təhsil müəssisəsinin uğuru onun maddi-texniki imkanları ilə yanaşı, insan kapitalından, kollektivin birliyindən və yeniliklərə açıq olmasından asılıdır. Bakı Dövlət Rabitə və Nəqliyyat Kollecini daha müasir, rəqabətqabiliyyətli, innovativ və əmək bazarının tələblərinə cavab verən təhsil müəssisəsi kimi inkişaf etdirmək əsas hədəflərimizdəndir. İnanıram ki, birgə fəaliyyətimiz sayəsində yeni uğurlara imza atacağıq.",
    "bio_sig_name": "Səbuhi Qurbanov",
    "bio_sig_title": "Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru",

    # Library Fund Modal
    "lib_fund_stat_val_3": "57 Adda",
    "lib_fund_p1": "Kitabxanada kitab fondu ilkin mərhələdə təxminən <strong>22.000 nüsxədən</strong> ibarət olmuşdur. Sonralar köhnəlmiş, indiki tələbatlara cavab verməyən ədəbiyyatların silinməsi nəticəsində hal-hazırda fondumuz <strong>10.000 nüsxə ədəbiyyat</strong> təşkil edir. Kitabxanamızda müxtəlif istiqamətlər üzrə zəngin ədəbiyyat fondu formalaşmışdır.",
    "lib_fund_p2": "Eyni zamanda bu dövrdə fondun müasir tələblərə uyğunlaşdırılması, ədəbiyyatın yenidən nəzərdən keçirilməsi və kitabxana resurslarından səmərəli istifadə istiqamətində vacib təşkilati işlər həyata keçirilmişdir.",
    "lib_fund_p3": "<strong>Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin</strong> “Azərbaycan dilində latın qrafikası ilə kütləvi nəşrlərin həyata keçirilməsi haqqında” <strong>12 yanvar 2004-cü il tarixli Sərəncamına</strong> əsasən bütün bədii ədəbiyyatlar yeni nəşrlərlə əvəz olunaraq, kitabxanamıza hədiyyə olunmuşdur.",
    "lib_fund_p4": "Tədris fondunun zənginləşdirilməsi istiqamətində kollecimizin müəllim heyəti tərəfindən tədris planına uyğun olaraq kitabxana fondu mütəmadi olaraq artırılır. Bu nəşrlərin olması tələbələrə ixtisaslarına uyğun olaraq informasiya təminatının yaxşılaşdırılmasına xidmət edir.",
    "lib_fund_p5": "Hal-hazırda kitabxanamızda <strong>57 adda dərslik</strong> fondumuza daxil edilmişdir. 2026-cı ildə nəşr olunmuş yeni dərsliklərimizi xüsusi vurğulamaq istərdik:",
    "lib_tb_1_title": "Xətti cəbr və riyazi analiz",
    "lib_tb_1_meta": "Direktor Səbuhi Qurbanov · 2026",
    "lib_tb_2_title": "Ekoloji Monitorinq",
    "lib_tb_2_meta": "Kollec Pedaqoji Heyəti · 2026",
    "lib_tb_3_title": "Dərslik Sxematexnika-1",
    "lib_tb_3_meta": "Texniki Fənlər Kafedrası · 2026",
    "lib_tb_4_title": "İnformasiya-Şəbəkə Texnologiyaları",
    "lib_tb_4_meta": "İKT və Telekommunikasiya · 2026",

    # Certificates & Sports extra
    "trophy_silver_4x": "4x II Yer",
    "science_scope_both": "🇦🇿 Yerli / Xarici",
    "science_scope_foreign": "Beynəlxalq",
    "science_scope_local": "🇦🇿 Yerli"
}

KEYS_EN = {
    # Page Title & Hero
    "page_title": "BDRNK — Baku State Communications and Transport College Public Legal Entity",
    "hero_aura_tagline": "Towards a Digital Future with State Educational Standards",
    "about_director_bio_btn": "Official Biography",

    # Honor Students / Hall of Fame
    "honors_sub_badge": "Global Achievements & International Representation",
    "fame_tab_all": "All",
    "fame_tab_it": "ICT & Robotics",
    "fame_tab_champ": "International Championships",
    "fame_tab_youth": "Youth of the Year & Social Inclusion",

    # Qarabağ Zəfər Salnaməsi
    "qarabag_video_title_1": "Victory Chronicle · November 8",
    "qarabag_video_badge_1": "KARABAKH IS AZERBAIJAN!",
    "qarabag_cinema_btn_1": "Victory Chronicle (Full Screen)",
    "qarabag_video_title_2": "Karabakh Tour · Aghdam - Khankendi - Shusha",
    "qarabag_video_badge_2": "KARABAKH TOUR",
    "qarabag_cinema_btn_2": "Karabakh Tour (Full Screen)",
    "qarabag_eyebrow": "🇦🇿 VICTORY CHRONICLE · NOVEMBER 8",
    "qarabag_heading": "UNITY, SOLIDARITY AND PATRIOTISM ON THE PATH OF VICTORY",
    "qarabag_pill_agdam": "📍 Aghdam",
    "qarabag_pill_khankendi": "📍 Khankendi",
    "qarabag_pill_shusha": "📍 Shusha",
    "qarabag_lead": "On the occasion of November 8 – Victory Day, the educational journey of Baku State Communications and Transport College under Azerbaijan Technical University to Aghdam, Khankendi, and Shusha became a vivid manifestation of fidelity to our historical memory, national-moral values, patriotism, as well as institutional unity and solidarity.",
    "qarabag_p1": "The essential value of this visit was not merely limited to exploring historical and cultural destinations. Uniting colleagues working across diverse educational functions around a singular goal, shared values, and profound patriotism imparted deep spiritual resonance to this journey. The roads traveled together, genuine interactions, and shared pride demonstrated once again the unshakeable unity of our faculty and staff.",
    "qarabag_p2": "Such journeys strengthen mutual trust and respect among team members, turning professional relations into heartfelt collaboration while cementing bonds of solidarity. A thriving academic environment is built not merely by routine work, but by sharing common values, joy, honor, and institutional responsibility.",
    "qarabag_quote": "“The renaissance of Aghdam, the immense pride in Khankendi's return to our motherland, and the historic cultural grandeur of Shusha left indelible impressions on each of us. Standing on these sacred lands reminded us once again that our Victory is not merely a military triumph, but a celebration of our nation's unbreakable will and love for the Fatherland.”",
    "qarabag_p3": "This visit was simultaneously an expression of our deepest reverence for the blessed memory of martyrs who sacrificed their lives for territorial integrity, and profound gratitude to our heroic veterans. Inhaling the air of liberated Karabakh and witnessing the footsteps of victory became a supreme source of pride for everyone.",
    "qarabag_p4": "We firmly believe that initiatives of such spiritual significance consolidate our team spirit, nurture lifelong friendship among educators, and provide powerful impetus toward common goals in shaping the future of education.",
    "qarabag_p5": "For a truly strong collective is formed by individuals who embrace the same core values, rejoice in shared achievements, overcome challenges arm-in-arm, and bear responsibility with collective pride.",
    "qarabag_p6": "This visit proved once more that unity is our moral power, solidarity the bedrock of our success, and patriotism the highest virtue binding us together.",
    "qarabag_p7": "The memory of our martyrs will forever live in our hearts, and the spirit of Victory and liberty they entrusted to us will be proudly passed on to future generations!",
    "qarabag_p8": "We take boundless pride in our history of Victory, rejoice in the revival of free Karabakh, and consider it our sacred moral duty to uphold our national unity and collective solidarity always.",
    "qarabag_credo_title": "🇦🇿 Our unity is our strength, our solidarity our pride, our patriotism our greatest value!",
    "qarabag_credo_sub": "May our Victory endure forever and our Azerbaijan flourish eternally! Karabakh is Azerbaijan!",

    # Structure & Campus Navigator
    "struct_badge_count": "9 PDC",
    "struct_commissions_view_title": "🎓 TEACHING & METHODOLOGICAL APPARATUS",
    "campus_rooms_count_text": "Rooms shown:",
    "lib_total_counter": "44 Official Textbooks",
    "lib_fund_about_btn": "🏛️ Library Fund & History",
    "science_director_bio_btn": "Director Sabuhi Gurbanov's Biography",

    # Video Lectures Department Metas
    "dept_meta_all": "23 Video Lectures · All subjects",
    "dept_meta_it": "2 Video Lectures · Computer Systems",
    "dept_meta_transport": "1 Video Lecture · Transport Systems",
    "dept_meta_geography": "2 Video Lectures · Earth Sciences & Geography",
    "dept_meta_physics": "1 Video Lecture · Nature & Physics",
    "dept_meta_history": "9 Video Lectures · History & Victory",
    "dept_meta_az_lang": "1 Video Lecture · Grammar & Speech",
    "dept_meta_law": "6 Video Lectures · Legal System",
    "dept_meta_biology": "1 Video Lecture · Life Sciences",

    # Gallery Portals
    "gal_headline_exam": "Transparent & Digital Exam Sessions",
    "gal_summary_exam": "Our college operates a modern computerized examination center equipped for objective monitoring and student assessment.",
    "gal_headline_events": "Solemn Ceremonies & Historic Days",
    "gal_summary_events": "Memorable collection of official footage from national holidays, graduation ceremonies, commemorative events, and international conferences.",
    "gal_headline_rooms": "Modern Lecture Halls & Infrastructure",
    "gal_summary_rooms": "Spacious lecture amphitheaters, interactive classrooms equipped with multimedia systems, and tech laboratories.",
    "gal_headline_study": "Active Academic Life & Student Practice",
    "gal_summary_study": "Team projects, interactive seminars, digital library studies, and hands-on laboratory sessions of our students.",

    # Director Bio Modal
    "bio_brand_title": "BDRNK · OFFICIAL DIRECTOR PORTAL",
    "bio_brand_sub": "Sabuhi Gurbanov Yusif oglu — Curriculum Vitae & Reflections",
    "bio_pill_medal": "🎖️ «TARAQQI» MEDALIST",
    "bio_pill_entity": "COLLEGE PRINCIPAL'S OFFICE",
    "bio_hero_name": "SABUHI GURBANOV YUSIF OGLU",
    "bio_hero_title": "Director of Baku State Communications and Transport College under Azerbaijan Technical University, State Agency for Science and Higher Education, Ministry of Science and Education of the Republic of Azerbaijan",
    "bio_fact_birth": "🎂 August 4, 1980 · Sheki",
    "bio_fact_edu": "🎓 BSU Mathematics & UNEC MBA",
    "bio_fact_author": "📐 MSE-Approved Textbook Author",
    "bio_nav_tab_edu": "🎓 Education & Early Life",
    "bio_nav_tab_career": "💼 Professional Career",
    "bio_nav_tab_pedagogy": "📚 Academic Works",
    "bio_nav_tab_international": "🌐 International Activity",
    "bio_nav_tab_awards": "🏅 State Honors & Awards",
    "bio_nav_tab_reflections": "✍️ Reflections on the College",
    "bio_sec_i_kicker": "SECTION I · BIRTH & ACADEMIC EDUCATION",
    "bio_sec_i_title": "Life & Education Years",
    "bio_sec_i_lead": "<strong>Sabuhi Gurbanov Yusif oglu</strong> was born on August 4, 1980 in Gayabashi village, Sheki district. In 1986, he enrolled in Gayabashi Secondary School and graduated with honors in 1997.",
    "bio_sec_i_p2": "From 1997 to 2001, he completed his bachelor's degree at the <strong>Faculty of Mathematics, Baku State University</strong>. In 2001–2002, he performed military service in the Armed Forces of Azerbaijan. Later, he earned a master's degree in 'Business Organization and Management' at <strong>Azerbaijan State University of Economics (UNEC)</strong>.",
    "bio_sec_ii_kicker": "SECTION II · PROFESSIONAL CAREER CHRONOLOGY",
    "bio_sec_ii_title": "Professional Leadership & Pedagogical Path",
    "bio_sec_ii_lead": "Sabuhi Gurbanov commenced his career in 2002 and commands over 24 years of extensive educational leadership and management experience:",
    "bio_tl_1_title": "Sheki City Secondary School No. 11",
    "bio_tl_1_desc": "Served as a mathematics teacher and Deputy Director for Educational & Academic Affairs.",
    "bio_tl_2_title": "Sheki City Secondary School No. 20",
    "bio_tl_2_desc": "Led the school as Principal for 10 years with distinguished management excellence.",
    "bio_tl_3_title": "Sheki-Zaqatala Regional Education Department",
    "bio_tl_3_desc": "Served as Senior Advisor in the Quality of Education Sector.",
    "bio_tl_4_title": "Baku State Communications and Transport College",
    "bio_tl_4_desc": "Appointed Deputy Director for Academic Affairs.",
    "bio_tl_5_year": "From 2026",
    "bio_tl_5_title": "Director of Baku State Communications and Transport College",
    "bio_tl_5_desc": "Appointed College Director by the Ministry of Science and Education of the Republic of Azerbaijan and the State Agency for Science and Higher Education.",
    "bio_sec_iii_kicker": "SECTION III · METHODOLOGICAL & PEDAGOGICAL WORK",
    "bio_sec_iii_title": "Textbooks and Scientific Publications",
    "bio_sec_iii_lead": "Alongside pedagogical practice, Sabuhi Gurbanov has made fundamental contributions to mathematical education and vocational curriculum standards:",
    "bio_sec_iii_b1_year": "2019 · ASPU Academic Council Resolution",
    "bio_sec_iii_b1_title": "«Mathematics – 11»",
    "bio_sec_iii_b1_desc": "Textbook recommended for publication by the Teaching and Methodological Council of Azerbaijan State Pedagogical University.",
    "bio_sec_iii_b2_year": "June 3, 2026 · Official Ministry Seal",
    "bio_sec_iii_b2_title": "«Linear Algebra and Mathematical Analysis»",
    "bio_sec_iii_b2_desc": "Fundamental textbook approved and granted official ministerial seal by the Ministry of Science and Education of the Republic of Azerbaijan.",
    "bio_sec_iv_kicker": "SECTION IV · INTERNATIONAL FORUMS & CERTIFICATIONS",
    "bio_sec_iv_title": "International Experience & Professional Development",
    "bio_feat_1_badge": "🇷🇺 Moscow · 2018",
    "bio_feat_1_title": "«Modern Technologies in Education»",
    "bio_feat_1_desc": "Participated as keynote speaker in the international scientific-practical conference held in Moscow on June 26, 2018.",
    "bio_feat_2_badge": "🌍 Global Forum · 2021",
    "bio_feat_2_title": "«Second International Forum on New Challenges in Education»",
    "bio_feat_2_desc": "Earned international credentials and certifications during the global education leadership forum on October 1, 2021.",
    "bio_feat_3_badge": "🛡️ Civil Service · AC3",
    "bio_feat_3_title": "Leadership & State Governance",
    "bio_feat_3_desc": "Completed leadership institutes and received the prestigious <strong>AC3 Civil Service Certification</strong> for public administration.",
    "bio_sec_v_kicker": "SECTION V · STATE & MINISTERIAL HONORS",
    "bio_sec_v_title": "Dedicated Service to National Education and Accolades",
    "bio_sec_v_lead": "Decades of dedicated public service and commitment to cultivating patriotic, highly qualified youths have been recognized at the highest state level:",
    "bio_aw_1_year": "October 3, 2017",
    "bio_aw_1_title": "«Taraqqi» (Progress) Medal",
    "bio_aw_1_desc": "Awarded the <strong>«Taraqqi» Medal</strong> by Decree of President of the Republic of Azerbaijan Ilham Aliyev for distinguished contributions to the development of national education.",
    "bio_aw_2_year": "October 5, 2010",
    "bio_aw_2_title": "«Advanced Education Worker» Badge of Honor",
    "bio_aw_2_desc": "Conferred the honorary badge <strong>«Advanced Education Worker of the Republic of Azerbaijan»</strong> by the Minister of Education for remarkable achievements in educating the youth.",
    "bio_sec_vi_kicker": "SECTION VI · DIRECTOR'S PERSONAL ESSAY & STRATEGIC VISION",
    "bio_sec_vi_title": "My Impressions and Strategic Vision for the College",
    "bio_sec_vi_lead": "Official essay by Director Sabuhi Gurbanov on the institutional dynamism and long-term strategic transformation of Baku State Communications and Transport College:",
    "bio_essay_p1": "Being appointed Director of Baku State Communications and Transport College by decision of the Ministry of Science and Education and the State Agency for Science and Higher Education is an immense honor and a profound civic responsibility.",
    "bio_essay_p2": "From my very first day leading this institution, the established pedagogical traditions, faculty professionalism, student potential, and rich history left a deep positive impression upon me. I must underscore the historical role this college has fulfilled in training elite specialists for communications and transport sectors.",
    "bio_essay_p3": "Engaging closely with college operations revealed that academic rigor is accompanied by genuine collegiality, mutual respect, and high professional standards. As director, my foremost aim is safeguarding these traditions while adapting our programs to modern technological demands.",
    "bio_essay_p4": "My strategic focus centers on elevating educational quality, modernizing teaching delivery, reforming evaluation and assessment mechanisms, integrating innovative technology, and cultivating real-world practical competencies for our students.",
    "bio_essay_p5": "I place paramount emphasis on fostering healthy mentor-student relationships, championing student initiatives, and encouraging participation in scientific, intellectual, athletic, and creative arenas. A modern college does not merely dispense knowledge; it builds character, worldview, and active civic responsibility.",
    "bio_essay_p6": "The creative initiative displayed by our staff, the hosting of distinguished academic events, informative forums with high school and vocational students, and expanding institutional partnerships bring me great pride. Notable engagements such as hosting European Lyceum delegations and exchanging insights in AI and robotics demonstrate the vitality of inter-institutional collaboration.",
    "bio_essay_p7": "Preserving national moral values, patriotic spirit, and statehood traditions across our collegiate life remains a personal priority. Our team visit to Aghdam, Khankendi, and Shusha on Victory Day exemplifies this dedication. I believe our youth must know their history intimately while actively contributing to modern Azerbaijan's ascent.",
    "bio_essay_p8": "The camaraderie, mutual support, and unified purpose I observe daily across our faculty form an inspiring bedrock for our future. Transforming Baku State Communications and Transport College into a cutting-edge, competitive, and innovative educational center matching market demands is our prime objective. United in purpose, we shall achieve new horizons.",
    "bio_sig_name": "Sabuhi Gurbanov",
    "bio_sig_title": "Director of Baku State Communications and Transport College",

    # Library Fund Modal
    "lib_fund_stat_val_3": "57 Titles",
    "lib_fund_p1": "The college library fund initially comprised approximately <strong>22,000 volumes</strong>. Following systematic de-accessioning of obsolete literature to align with modern standards, our collection currently comprises <strong>10,000 volumes</strong> of rich, specialized academic works.",
    "lib_fund_p2": "During this period, vital organizational reforms were undertaken to update the collection in accordance with curriculum requirements and ensure optimal access to digital and physical resources.",
    "lib_fund_p3": "In accordance with the <strong>Decree of President of the Republic of Azerbaijan Ilham Aliyev</strong> dated January 12, 2004 'On the implementation of mass publications in Azerbaijani language in Latin script', all classic and fiction literature was replaced with brand-new publications and gifted to our library.",
    "lib_fund_p4": "Our teaching staff continuously enriches the library fund with tailored specialized textbooks adhering to national curriculum standards. These publications ensure optimal informational and pedagogical support for all student majors.",
    "lib_fund_p5": "Currently, our collection features <strong>57 official textbook titles</strong>. We highlight key new textbooks published in 2026:",
    "lib_tb_1_title": "Linear Algebra and Mathematical Analysis",
    "lib_tb_1_meta": "Director Sabuhi Gurbanov · 2026",
    "lib_tb_2_title": "Ecological Monitoring",
    "lib_tb_2_meta": "College Pedagogical Faculty · 2026",
    "lib_tb_3_title": "Textbook Circuitry-1",
    "lib_tb_3_meta": "Department of Technical Disciplines · 2026",
    "lib_tb_4_title": "Information & Network Technologies",
    "lib_tb_4_meta": "ICT and Telecommunications Department · 2026",

    # Certificates & Sports extra
    "trophy_silver_4x": "4x 2nd Place",
    "science_scope_both": "Local / International",
    "science_scope_foreign": "International",
    "science_scope_local": "Local"
}

KEYS_RU = {
    # Page Title & Hero
    "page_title": "БГКСТ — Бакинский Государственный Колледж Связи и Транспорта",
    "hero_aura_tagline": "К цифровому будущему по государственным образовательным стандартам",
    "about_director_bio_btn": "Официальная биография",

    # Honor Students / Hall of Fame
    "honors_sub_badge": "Глобальные достижения и международное представительство",
    "fame_tab_all": "Все",
    "fame_tab_it": "ИКТ и Робототехника",
    "fame_tab_champ": "Международные чемпионаты",
    "fame_tab_youth": "Молодежь года и социальная инклюзия",

    # Qarabağ Zəfər Salnaməsi
    "qarabag_video_title_1": "Летопись Победы · 8 Ноября",
    "qarabag_video_badge_1": "КАРАБАХ — ЭТО АЗЕРБАЙДЖАН!",
    "qarabag_cinema_btn_1": "Летопись Победы (Полный экран)",
    "qarabag_video_title_2": "Поездка в Карабах · Агдам - Ханкенди - Шуша",
    "qarabag_video_badge_2": "ПОЕЗДКА В КАРАБАХ",
    "qarabag_cinema_btn_2": "Поездка в Карабах (Полный экран)",
    "qarabag_eyebrow": "🇦🇿 ЛЕТОПИСЬ ПОБЕДЫ · 8 НОЯБРЯ",
    "qarabag_heading": "ЕДИНСТВО, СОЛИДАРНОСТЬ И ПАТРИОТИЗМ НА ПУТИ ПОБЕДЫ",
    "qarabag_pill_agdam": "📍 Агдам",
    "qarabag_pill_khankendi": "📍 Ханкенди",
    "qarabag_pill_shusha": "📍 Шуша",
    "qarabag_lead": "По случаю 8 Ноября — Дня Победы визит коллектива Бакинского государственного колледжа связи и транспорта при Азербайджанском техническом университете в Агдам, Ханкенди и Шушу стал ярким выражением преданности исторической памяти, национально-духовным ценностям, а также символом сплоченности и единства нашего коллектива.",
    "qarabag_p1": "Главная ценность визита не ограничивалась лишь посещением исторических памятников. Объединение сотрудников различных направлений вокруг единой цели, общих ценностей и преданности Родине придало этой поездке особый смысл и духовную силу. Пройденный вместе путь, искреннее общение и общее чувство гордости вновь продемонстрировали нерушимое единство нашего коллектива как в профессиональном, так и в человеческом плане.",
    "qarabag_p2": "Подобные поездки укрепляют взаимное уважение и доверие среди коллег, превращают служебные отношения в искреннее сотрудничество и скрепляют узы дружбы и солидарности. Здоровая атмосфера формируется не только совместным трудом, но и разделением общих ценностей, радости, гордости и ответственности.",
    "qarabag_quote": "«Возрождение и преображение Агдама, гордость воссоединения Ханкенди с родным краем, историческое и культурное величие Шуши оставили неизгладимые впечатления в сердце каждого из нас. Пребывание на этой земле вновь напомнило, что наша Победа — это не просто военно-политический триумф, а торжество национального единства, несгибаемой воли и сыновней любви к Родине.»",
    "qarabag_p3": "Эта поездка стала данью глубокого уважения светлой памяти шехидов, отдавших жизни за свободу наших земель, и выражением безмерной благодарности героям-ветеранам. Вдыхать воздух освобожденного Карабаха и видеть следы истории Победы на этой священной земле — великая честь и гордость для каждого из нас.",
    "qarabag_p4": "Мы верим, что мероприятия столь высокой духовной значимости укрепляют сплоченность коллектива, развивают дружбу и солидарность среди сотрудников, давая мощный стимул к еще более тесному объединению вокруг общих созидательных целей.",
    "qarabag_p5": "Ведь сильный коллектив — это не просто коллеги по работе, а люди, разделяющие общие ценности, вместе радующиеся успеху, плечом к плечу преодолевающие трудности и разделяющие общую гордость и ответственность.",
    "qarabag_p6": "Эта поездка вновь показала нам, что единство — наша духовная сила, солидарность — основа достижений, а любовь к Родине — высшая ценность, связывающая нас воедино.",
    "qarabag_p7": "Светлая память о шехидах вечно пребудет в наших сердцах, а дух Победы и свободы, завещанный ими, будет передаваться будущим поколениям!",
    "qarabag_p8": "Мы гордимся историей Победы, радуемся возрождению свободного Карабаха и считаем своим священным моральным долгом вечно беречь национальное единство и солидарность.",
    "qarabag_credo_title": "🇦🇿 Наше единство — наша сила, наша солидарность — наша гордость, любовь к Родине — высшая ценность!",
    "qarabag_credo_sub": "Да пребудет наша Победа вечной, а Азербайджан процветающим! Карабах — это Азербайджан!",

    # Structure & Campus Navigator
    "struct_badge_count": "9 ПЦК",
    "struct_commissions_view_title": "🎓 УЧЕБНО-МЕТОДИЧЕСКИЙ АППАРАТ",
    "campus_rooms_count_text": "Показано комнат:",
    "lib_total_counter": "44 Официальных учебных пособия",
    "lib_fund_about_btn": "🏛️ Библиотечный фонд и история",
    "science_director_bio_btn": "Биография директора Сабухи Гурбанова",

    # Video Lectures Department Metas
    "dept_meta_all": "23 Видеоурока · Все предметы",
    "dept_meta_it": "2 Видеоурока · Компьютерные системы",
    "dept_meta_transport": "1 Видеоурок · Транспортные системы",
    "dept_meta_geography": "2 Видеоурока · Науки о Земле и география",
    "dept_meta_physics": "1 Видеоурок · Естествознание и физика",
    "dept_meta_history": "9 Видеоуроков · История и Победа",
    "dept_meta_az_lang": "1 Видеоурок · Грамматика и речь",
    "dept_meta_law": "6 Видеоуроков · Правовая система",
    "dept_meta_biology": "1 Видеоурок · Естественные науки",

    # Gallery Portals
    "gal_headline_exam": "Прозрачные и цифровые экзаменационные сессии",
    "gal_summary_exam": "В нашем колледже действует современный компьютеризированный экзаменационный центр с объективным мониторингом оценки знаний студентов.",
    "gal_headline_events": "Торжественные собрания и исторические даты",
    "gal_summary_events": "Памятная коллекция официальных кадров с государственных праздников, выпускных церемоний, памятных дат и международных конференций.",
    "gal_headline_rooms": "Современные аудитории и инфраструктура",
    "gal_summary_rooms": "Просторные амфитеатры, аудитории с интерактивными мультимедийными досками и передовые технологические лаборатории.",
    "gal_headline_study": "Живая учебная среда и студенческая практика",
    "gal_summary_study": "Командная работа студентов, интерактивные семинары, занятия в электронной библиотеке и практические лабораторные часы.",

    # Director Bio Modal
    "bio_brand_title": "БГКСТ · ОФИЦИАЛЬНЫЙ ПОРТАЛ ДИРЕКТОРА",
    "bio_brand_sub": "Сабухи Гурбанов Юсиф оглы — Биография и впечатления",
    "bio_pill_medal": "🎖️ МЕДАЛИСТ «ТЭРЭГГИ»",
    "bio_pill_entity": "ДИРЕКТОРАТ КОЛЛЕДЖА",
    "bio_hero_name": "САБУХИ ГУРБАНОВ ЮСИФ ОГЛЫ",
    "bio_hero_title": "Директор Бакинского государственного колледжа связи и транспорта при Азербайджанском техническом университете, Государственное агентство по науке и высшему образованию Министерства науки и образования Азербайджанской Республики",
    "bio_fact_birth": "🎂 4 августа 1980 · Шеки",
    "bio_fact_edu": "🎓 БГУ Математика & UNEC MBA",
    "bio_fact_author": "📐 Автор учебников с грифом МНО",
    "bio_nav_tab_edu": "🎓 Образование и жизнь",
    "bio_nav_tab_career": "💼 Трудовая деятельность",
    "bio_nav_tab_pedagogy": "📚 Научные труды",
    "bio_nav_tab_international": "🌐 Международная деятельность",
    "bio_nav_tab_awards": "🏅 Государственные награды",
    "bio_nav_tab_reflections": "✍️ Мои впечатления о колледже",
    "bio_sec_i_kicker": "РАЗДЕЛ I · РОЖДЕНИЕ И АКАДЕМИЧЕСКОЕ ОБРАЗОВАНИЕ",
    "bio_sec_i_title": "Жизнь и годы учебы",
    "bio_sec_i_lead": "<strong>Сабухи Гурбанов Юсиф оглы</strong> родился 4 августа 1980 года в селе Гаябаши Шекинского района, в 1986 году пошел в 1-й класс Гаябашинской средней школы и окончил её с отличием в 1997 году.",
    "bio_sec_i_p2": "В 1997–2001 годах получил степень бакалавра на <strong>механико-математическом факультете Бакинского государственного университета</strong>. В 2001–2002 годах проходил действительную военную службу в Вооруженных Силах Азербайджанской Республики. Позже окончил магистратуру в <strong>Азербайджанском государственном экономическом университете (UNEC)</strong> по специальности «Организация и управление бизнесом».",
    "bio_sec_ii_kicker": "РАЗДЕЛ II · ХРОНОЛОГИЯ ТРУДОВОЙ ДЕЯТЕЛЬНОСТИ",
    "bio_sec_ii_title": "Путь профессионального управления и педагогики",
    "bio_sec_ii_lead": "Сабухи Гурбанов начал трудовую деятельность в 2002 году и обладает более чем 24-летним богатым опытом управления в сфере образования:",
    "bio_tl_1_title": "Шекинская городская средняя школа № 11",
    "bio_tl_1_desc": "Работал учителем математики, а также заместителем директора по учебно-воспитательной работе.",
    "bio_tl_2_title": "Шекинская городская средняя школа № 20",
    "bio_tl_2_desc": "В течение 10 лет успешно руководил школой в должности директора.",
    "bio_tl_3_title": "Шеки-Загатальское региональное управление образования",
    "bio_tl_3_desc": "Работал главным консультантом сектора качества образования.",
    "bio_tl_4_title": "Бакинский государственный колледж связи и транспорта",
    "bio_tl_4_desc": "Был назначен заместителем директора по учебной работе.",
    "bio_tl_5_year": "С 2026 года",
    "bio_tl_5_title": "Директор Бакинского государственного колледжа связи и транспорта",
    "bio_tl_5_desc": "Назначен директором Колледжа Министерством науки и образования Азербайджанской Республики и Государственным агентством по науке и высшему образованию.",
    "bio_sec_iii_kicker": "РАЗДЕЛ III · НАУЧНО-МЕТОДИЧЕСКАЯ И ПЕДАГОГИЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ",
    "bio_sec_iii_title": "Учебники и научные пособия",
    "bio_sec_iii_lead": "Наряду с педагогической деятельностью, Сабухи Гурбанов внес весомый вклад в преподавание математических дисциплин и развитие стандартов профессионального образования:",
    "bio_sec_iii_b1_year": "2019 · Решение Совета АГПУ",
    "bio_sec_iii_b1_title": "«Математика – 11»",
    "bio_sec_iii_b1_desc": "Учебное пособие, рекомендованное к изданию Учебно-методическим советом Азербайджанского государственного педагогического университета.",
    "bio_sec_iii_b2_year": "3 июня 2026 · Официальный гриф МНО",
    "bio_sec_iii_b2_title": "«Линейная алгебра и математический анализ»",
    "bio_sec_iii_b2_desc": "Фундаментальный учебник, изданный и получивший официальный гриф Министерства науки и образования Азербайджанской Республики.",
    "bio_sec_iv_kicker": "РАЗДЕЛ IV · МЕЖДУНАРОДНЫЕ НАУЧНЫЕ ФОРУМЫ И СЕРТИФИКАТЫ",
    "bio_sec_iv_title": "Международный опыт и повышение квалификации",
    "bio_feat_1_badge": "🇷🇺 Москва · 2018",
    "bio_feat_1_title": "«Современные технологии в образовании»",
    "bio_feat_1_desc": "26 июня 2018 года принял участие и выступил с докладом на международной научно-практической конференции в Москве.",
    "bio_feat_2_badge": "🌍 Глобальный форум · 2021",
    "bio_feat_2_title": "«Second International Forum on New Challenges in Education»",
    "bio_feat_2_desc": "Принял участие в международном образовательном форуме 1 октября 2021 года и получил соответствующие международные сертификаты.",
    "bio_feat_3_badge": "🛡️ Госгражданслужба · AC3",
    "bio_feat_3_title": "Лидерство и государственное управление",
    "bio_feat_3_desc": "Прошел обучение по программам Института программ образования и получил престижный <strong>сертификат AC3</strong> по государственной службе.",
    "bio_sec_v_kicker": "РАЗДЕЛ V · ГОСУДАРСТВЕННЫЕ И МИНИСТЕРСКИЕ НАГРАДЫ",
    "bio_sec_v_title": "Самоотверженное служение национальному образованию и награды",
    "bio_sec_v_lead": "Многолетний плодотворный труд в сфере образования и заслуги в патриотическом воспитании молодежи высоко оценены на государственном уровне:",
    "bio_aw_1_year": "3 октября 2017",
    "bio_aw_1_title": "Медаль «Тэрэгги» (Прогресс)",
    "bio_aw_1_desc": "Распоряжением Президента Азербайджанской Республики Ильхама Алиева награжден <strong>медалью «Тэрэгги»</strong> за заслуги в развитии образования в Азербайджане.",
    "bio_aw_2_year": "5 октября 2010",
    "bio_aw_2_title": "Нагрудный знак «Передовой работник образования»",
    "bio_aw_2_desc": "Приказом Министра образования Азербайджанской Республики награжден нагрудным знаком <strong>«Передовой работник образования Азербайджанской Республики»</strong> за успехи в обучении и воспитании подрастающего поколения.",
    "bio_sec_vi_kicker": "РАЗДЕЛ VI · ЛИЧНЫЙ ВЗГЛЯД РУКОВОДИТЕЛЯ И СТРАТЕГИЧЕСКИЕ ЦЕЛИ",
    "bio_sec_vi_title": "Мои впечатления о колледже и стратегическое видение",
    "bio_sec_vi_lead": "Официальное эссе директора Сабухи Гурбанова о текущей динамике развития и стратегических горизонтах Бакинского государственного колледжа связи и транспорта:",
    "bio_essay_p1": "Назначение директором Бакинского государственного колледжа связи и транспорта решением Министерства науки и образования и Государственного агентства по науке и высшему образованию — для меня не только высокая честь, но и колоссальная ответственность.",
    "bio_essay_p2": "С первых же дней руководства сложившиеся здесь академические традиции, профессионализм преподавателей, потенциал студентов и богатая история заведения произвели на меня самое благоприятное впечатление. Особо хочу отметить историческую роль колледжа в подготовке высококлассных специалистов для сфер связи и транспорта.",
    "bio_essay_p3": "Ближе знакомясь с деятельностью колледжа, я увидел, что здесь наряду с учебным процессом важнейшее место занимают взаимное уважение, солидарность и профессионализм. Моя главная цель как руководителя — бережно сохранять эти традиции и развивать их в соответствии с высокими стандартами современности.",
    "bio_essay_p4": "Главные приоритеты нашей работы — повышение качества образования, модернизация учебного процесса, совершенствование мониторинга и механизмов оценивания, внедрение инновационных технологий и развитие практических навыков учащихся.",
    "bio_essay_p5": "Особое значение я придаю здоровым доверительным отношениям между преподавателями и студентами, поддержке инициатив молодежи, их участию в научных, интеллектуальных, спортивных и творческих проектах. Современный колледж не просто обучает, но и воспитывает личность с широким кругозором и активной гражданской позицией.",
    "bio_essay_p6": "Инициативность наших сотрудников, организация просветительских встреч и расширение сотрудничества с другими учебными заведениями заслуживают высокой оценки. Визиты делегаций Бакинского Европейского лицея и совместный обмен идеями в области робототехники и ИИ ярко подтверждают важность академического партнерства.",
    "bio_essay_p7": "Сохранению национально-духовных ценностей, патриотического духа и традиций государственности мы уделяем приоритетное внимание. Наша поездка в Агдам, Ханкенди и Шушу по случаю Дня Победы стала тому ярким подтверждением. Наша молодежь должна глубоко знать историю и вносить достойный вклад в процветание Отчизны.",
    "bio_essay_p8": "Сплоченность, взаимная поддержка и единство целей, которые я наблюдаю в коллективе, служат прочным фундаментом нашего будущего. Развитие Бакинского государственного колледжа связи и транспорта как современного, инновационного и востребованного на рынке труда центра — наша общая цель. Верю, что совместным трудом мы добьемся новых ярких побед.",
    "bio_sig_name": "Сабухи Гурбанов",
    "bio_sig_title": "Директор Бакинского государственного колледжа связи и транспорта",

    # Library Fund Modal
    "lib_fund_stat_val_3": "57 Названий",
    "lib_fund_p1": "На начальном этапе библиотечный фонд насчитывал около <strong>22 000 экземпляров</strong>. Впоследствии, после списания устаревшей литературы, наш фонд в настоящее время насчитывает <strong>10 000 экземпляров</strong> богатой профильной литературы.",
    "lib_fund_p2": "В этот период была проделана важная организационная работа по модернизации фонда, пересмотру литературы и эффективному использованию библиотечных ресурсов в соответствии с современными требованиями.",
    "lib_fund_p3": "В соответствии с <strong>Распоряжением Президента Азербайджанской Республики господина Ильхама Алиева</strong> от 12 января 2004 года «Об осуществлении массовых изданий на азербайджанском языке на латинской графике» вся художественная литература была заменена новыми изданиями и передана в дар библиотеке.",
    "lib_fund_p4": "Преподавательский состав колледжа регулярно пополняет фонд профильными учебниками в соответствии с учебным планом. Наличие этих изданий служит повышению качества информационного обеспечения студентов по всем специальностям.",
    "lib_fund_p5": "В настоящее время в наш фонд включено <strong>57 наименований учебников</strong>. Особо хотим подчеркнуть новые учебные пособия, изданные в 2026 году:",
    "lib_tb_1_title": "Линейная алгебра и математический анализ",
    "lib_tb_1_meta": "Директор Сабухи Гурбанов · 2026",
    "lib_tb_2_title": "Экологический мониторинг",
    "lib_tb_2_meta": "Педагогический коллектив колледжа · 2026",
    "lib_tb_3_title": "Учебник Схемотехника-1",
    "lib_tb_3_meta": "Кафедра технических дисциплин · 2026",
    "lib_tb_4_title": "Информационно-сетевые технологии",
    "lib_tb_4_meta": "Отделение ИКТ и телекоммуникаций · 2026",

    # Certificates & Sports extra
    "trophy_silver_4x": "4x II Место",
    "science_scope_both": "Местный / Международный",
    "science_scope_foreign": "Международный",
    "science_scope_local": "Местный"
}

def format_js_entries(d):
    lines = []
    for k, v in d.items():
        v_escaped = v.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
        lines.append(f'    {k}: "{v_escaped}",')
    return '\n'.join(lines)

def update_script_js():
    with open(JS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject into az: { ... }
    def inject_keys(lang_name, keys_dict, code):
        pattern = r'(' + lang_name + r':\s*\{[\s\S]*?)(\n  \},|\n  \})'
        match = re.search(pattern, code)
        if not match:
            print(f"Error finding language block: {lang_name}")
            return code
        prefix = match.group(1)
        suffix = match.group(2)
        new_block = format_js_entries(keys_dict)
        return code[:match.start()] + prefix + '\n' + new_block + suffix + code[match.end():]

    content = inject_keys('az', KEYS_AZ, content)
    content = inject_keys('en', KEYS_EN, content)
    content = inject_keys('ru', KEYS_RU, content)

    # Update document.title in initLanguageEngine()
    old_init_lang = '''function initLanguageEngine() {
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
}'''

    new_init_lang = '''function initLanguageEngine() {
  const btns = document.querySelectorAll(".lang-btn");
  btns.forEach((btn) => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      // UI Toggle
      btns.forEach((b) => b.classList.remove("active"));
      const target = e.currentTarget || e.target;
      target.classList.add("active");

      // Set state & update DOM
      currentLang = target.getAttribute("data-lang");
      document.documentElement.lang = currentLang;
      if (i18n[currentLang] && i18n[currentLang].page_title) {
        document.title = i18n[currentLang].page_title;
      }
      updateDOMTexts();
      document.dispatchEvent(new CustomEvent("languageChanged"));
    });
  });
}'''

    if old_init_lang in content:
        content = content.replace(old_init_lang, new_init_lang)
        print("Updated initLanguageEngine with title synchronization and event prevention.")

    # Remove duplicate delayed lang-btn listeners that caused visual flickering/jumping
    dup_news = '''    const langBtns = document.querySelectorAll(".lang-btn");
    langBtns.forEach((btn) => {
      btn.addEventListener("click", () => {
        setTimeout(renderNews, 50);
      });
    });'''
    if dup_news in content:
        content = content.replace(dup_news, '    // News listener handled cleanly by languageChanged')
        print("Removed duplicate delayed renderNews click listener.")

    dup_lib = '''  // Re-render when language changes
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      setTimeout(applyFilter, 50);
    });
  });'''
    if dup_lib in content:
        content = content.replace(dup_lib, '  document.addEventListener("languageChanged", applyFilter);')
        print("Replaced delayed library click listener with unified languageChanged listener.")

    dup_calc = '''    // Re-populate on language change
    document.querySelectorAll(".lang-btn").forEach(btn => {
      btn.addEventListener("click", () => setTimeout(populateMajors, 100));
    });'''
    if dup_calc in content:
        content = content.replace(dup_calc, '    document.addEventListener("languageChanged", populateMajors);')
        print("Replaced delayed admission click listener with unified languageChanged listener.")

    # Localize badgesHtml in renderCards for Science module
    old_badges = """        author.scope_type === 'both' ? `<span class="science-badge-scope local">🇦🇿 Yerli / Xarici</span>` :
        author.scope_type === 'xarici' ? `<span class="science-badge-scope foreign">Beynəlxalq</span>` :
        `<span class="science-badge-scope local">🇦🇿 Yerli</span>`"""

    new_badges = """        author.scope_type === 'both' ? `<span class="science-badge-scope local">${typeof gT === 'function' ? gT('science_scope_both') : 'Yerli / Xarici'}</span>` :
        author.scope_type === 'xarici' ? `<span class="science-badge-scope foreign">${typeof gT === 'function' ? gT('science_scope_foreign') : 'Beynəlxalq'}</span>` :
        `<span class="science-badge-scope local">${typeof gT === 'function' ? gT('science_scope_local') : 'Yerli'}</span>`"""

    if old_badges in content:
        content = content.replace(old_badges, new_badges)
        print("Localized science card badgesHtml.")

    with open(JS_FILE, 'w', encoding='utf-8') as f:
        f.write(content)
    with open(BACKUP_JS, 'w', encoding='utf-8') as f:
        f.write(content)
    print("script.js updated and synced with working backup.")

def update_style_css():
    with open(CSS_FILE, 'r', encoding='utf-8') as f:
        css = f.read()

    # 1. Ensure viewport text size stabilization
    if '-webkit-text-size-adjust: 100%;' not in css:
        css = """html, body {
  -webkit-text-size-adjust: 100%;
  text-size-adjust: 100%;
}
""" + css

    # 2. Fix .site-header transition to prevent elastic resizing animation
    old_header = """  box-shadow: 0 2px 16px rgba(10, 34, 64, 0.06);
  transition: all var(--transition);
}"""
    new_header = """  box-shadow: 0 2px 16px rgba(10, 34, 64, 0.06);
  transition: background-color var(--transition), box-shadow var(--transition);
}"""
    if old_header in css:
        css = css.replace(old_header, new_header)
        print("Fixed .site-header transition.")

    # 3. Ensure header-nav and nav-link never wrap or shift vertically
    old_nav = """.header-nav {
  display: flex;
  align-items: center;
  gap: 2px;
}"""
    new_nav = """.header-nav {
  display: flex;
  align-items: center;
  gap: 2px;
  flex-wrap: nowrap;
  white-space: nowrap;
  flex-shrink: 0;
}"""
    if old_nav in css:
        css = css.replace(old_nav, new_nav)
        print("Added nowrap and shrink control to .header-nav.")

    # 4. Add nowrap to nav-link
    if '.nav-link {' in css and 'white-space: nowrap;' not in css[:css.find('.nav-link {') + 200]:
        css = css.replace('.nav-link {\n  position: relative;', '.nav-link {\n  position: relative;\n  white-space: nowrap;\n  flex-shrink: 0;')
        print("Added nowrap to .nav-link.")

    # 5. Fix .lang-switcher and .lang-btn
    old_switcher = """.lang-switcher {
  display: flex;
  gap: 2px;
  background: var(--bg-alt);
  border-radius: var(--radius-sm);
  padding: 3px;
  border: 1px solid var(--border);
}"""
    new_switcher = """.lang-switcher {
  display: flex;
  gap: 2px;
  background: var(--bg-alt);
  border-radius: var(--radius-sm);
  padding: 3px;
  border: 1px solid var(--border);
  flex-shrink: 0;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
}"""
    if old_switcher in css:
        css = css.replace(old_switcher, new_switcher)
        print("Updated .lang-switcher with anti-zoom touch properties.")

    old_btn = """.lang-btn {
  padding: 6px 10px;
  border-radius: var(--radius-xs);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-dim);
  transition: all var(--transition);
  letter-spacing: 0.05em;
}"""
    new_btn = """.lang-btn {
  padding: 6px 10px;
  border-radius: var(--radius-xs);
  font-size: 0.72rem;
  font-weight: 700;
  color: var(--text-dim);
  transition: background-color 0.18s ease, color 0.18s ease, border-color 0.18s ease;
  letter-spacing: 0.05em;
  touch-action: manipulation;
  user-select: none;
  -webkit-user-select: none;
}"""
    if old_btn in css:
        css = css.replace(old_btn, new_btn)
        print("Updated .lang-btn with discrete color transitions.")

    with open(CSS_FILE, 'w', encoding='utf-8') as f:
        f.write(css)
    print("style.css updated successfully.")

def update_index_html():
    with open(HTML_FILE, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Title tag
    html = re.sub(r'<title>[^<]*</title>', '<title data-i18n="page_title">BDRNK — Bakı Dövlət Rabitə və Nəqliyyat Kolleci Publik Hüquqi Şəxsi</title>', html)

    # 2. Hero Aura tagline
    html = re.sub(
        r'<p class="aura-tagline">([^<]*)</p>',
        r'<p class="aura-tagline" data-i18n="hero_aura_tagline">Dövlət Standartı ilə Rəqəmsal Gələcəyə Doğru</p>',
        html
    )

    # 3. Director Bio button in About
    html = re.sub(
        r'<a href="#director-bio-modal" id="about-director-bio-btn"([^>]*)>([\s\S]*?)<span>Rəsmi Bioqrafiya</span>([\s\S]*?)</a>',
        r'<a href="#director-bio-modal" id="about-director-bio-btn"\1>\2<span data-i18n="about_director_bio_btn">Rəsmi Bioqrafiya</span>\3</a>',
        html
    )

    # 4. Honor students / Hall of fame tabs and sub-badge
    html = re.sub(
        r'<span class="honors-sub-badge">Qlobal Nailiyyətlər & Beynəlxalq Təmsilçilik</span>',
        r'<span class="honors-sub-badge" data-i18n="honors_sub_badge">Qlobal Nailiyyətlər & Beynəlxalq Təmsilçilik</span>',
        html
    )
    html = html.replace('data-fame-cat="all"><span>Hamısı</span>', 'data-fame-cat="all"><span data-i18n="fame_tab_all">Hamısı</span>')
    html = html.replace('data-fame-cat="ikt"><span>İKT & Robototexnika</span>', 'data-fame-cat="ikt"><span data-i18n="fame_tab_it">İKT & Robototexnika</span>')
    html = html.replace('data-fame-cat="champ"><span>Beynəlxalq Çempionatlar</span>', 'data-fame-cat="champ"><span data-i18n="fame_tab_champ">Beynəlxalq Çempionatlar</span>')
    html = html.replace('data-fame-cat="youth"><span>İlin Gənci & Sosial İnklüzivlik</span>', 'data-fame-cat="youth"><span data-i18n="fame_tab_youth">İlin Gənci & Sosial İnklüzivlik</span>')

    # 5. Qarabağ section
    html = html.replace('<span class="qarabag-video-tag-title">Zəfər Xronikası · 8 Noyabr</span>', '<span class="qarabag-video-tag-title" data-i18n="qarabag_video_title_1">Zəfər Xronikası · 8 Noyabr</span>')
    html = html.replace('<strong>QARABAĞ AZƏRBAYCANDIR!</strong>', '<strong data-i18n="qarabag_video_badge_1">QARABAĞ AZƏRBAYCANDIR!</strong>')
    html = html.replace('<span>Zəfər Xronikası (Tam Ekran)</span>', '<span data-i18n="qarabag_cinema_btn_1">Zəfər Xronikası (Tam Ekran)</span>')
    html = html.replace('<span class="qarabag-video-tag-title">Qarabağ Gəzintisi · Ağdam - Xankəndi - Şuşa</span>', '<span class="qarabag-video-tag-title" data-i18n="qarabag_video_title_2">Qarabağ Gəzintisi · Ağdam - Xankəndi - Şuşa</span>')
    html = html.replace('<strong>QARABAĞ GƏZİNTİSİ</strong>', '<strong data-i18n="qarabag_video_badge_2">QARABAĞ GƏZİNTİSİ</strong>')
    html = html.replace('<span>Qarabağ Gəzintisi (Tam Ekran)</span>', '<span data-i18n="qarabag_cinema_btn_2">Qarabağ Gəzintisi (Tam Ekran)</span>')
    html = html.replace('<span class="qarabag-eyebrow">🇦🇿 ZƏFƏR SALNAMƏSİ · 8 NOYABR</span>', '<span class="qarabag-eyebrow" data-i18n="qarabag_eyebrow">🇦🇿 ZƏFƏR SALNAMƏSİ · 8 NOYABR</span>')
    html = html.replace('<h2 class="qarabag-heading">\n                        ZƏFƏR YOLUNDA BİRLİK, HƏMRƏYLİK VƏ VƏTƏN SEVGİSİ\n                    </h2>', '<h2 class="qarabag-heading" data-i18n="qarabag_heading">ZƏFƏR YOLUNDA BİRLİK, HƏMRƏYLİK VƏ VƏTƏN SEVGİSİ</h2>')
    html = html.replace('<span class="qarabag-pill">📍 Ağdam</span>', '<span class="qarabag-pill" data-i18n="qarabag_pill_agdam">📍 Ağdam</span>')
    html = html.replace('<span class="qarabag-pill">📍 Xankəndi</span>', '<span class="qarabag-pill" data-i18n="qarabag_pill_khankendi">📍 Xankəndi</span>')
    html = html.replace('<span class="qarabag-pill">📍 Şuşa</span>', '<span class="qarabag-pill" data-i18n="qarabag_pill_shusha">📍 Şuşa</span>')

    # Qarabağ paragraphs
    html = re.sub(
        r'<p class="qarabag-lead">[\s\S]*?8 Noyabr – Zəfər Günü[\s\S]*?</p>',
        '<p class="qarabag-lead" data-i18n="qarabag_lead">8 Noyabr – Zəfər Günü münasibətilə Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecinin kollektivinin Ağdam, Xankəndi və Şuşaya təşkil olunan səfəri həm tarixi yaddaşımıza, milli-mənəvi dəyərlərimizə və Vətən sevgimizə bağlılığın, həm də kollektiv birliyinin və həmrəyliyinin parlaq təzahürü oldu.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Səfərin əsas dəyəri yalnız tarixi və mədəni məkanları[\s\S]*?</p>',
        '<p data-i18n="qarabag_p1">Səfərin əsas dəyəri yalnız tarixi və mədəni məkanları ziyarət etməklə məhdudlaşmırdı. Müxtəlif vəzifə və fəaliyyət istiqamətlərində çalışan əməkdaşlarımızın vahid məqsəd, ortaq dəyərlər və eyni Vətən sevgisi ətrafında bir araya gəlməsi bu səfərə xüsusi məna və mənəvi dəyər qazandırdı. Birlikdə qət etdiyimiz yollar, səmimi ünsiyyətimiz, xoş təəssüratlarımız və bölüşdüyümüz qürur hissi kollektivimizin həm peşəkar, həm də insani münasibətlər baxımından möhkəm birliyini bir daha nümayiş etdirdi.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Belə səfərlər kollektiv üzvləri arasında qarşılıqlı hörmət[\s\S]*?</p>',
        '<p data-i18n="qarabag_p2">Belə səfərlər kollektiv üzvləri arasında qarşılıqlı hörmət və etimadı gücləndirir, işgüzar münasibətləri daha səmimi əməkdaşlığa çevirir, dostluq və həmrəylik bağlarını möhkəmləndirir. Çünki sağlam kollektiv mühiti yalnız birgə əmək fəaliyyəti ilə deyil, həm də ortaq dəyərlərin, sevincin, qürurun və məsuliyyətin bölüşülməsi ilə formalaşır.</p>',
        html
    )
    html = re.sub(
        r'<blockquote class="qarabag-quote">[\s\S]*?“Ağdamın dirçəlişi[\s\S]*?</blockquote>',
        '<blockquote class="qarabag-quote" data-i18n="qarabag_quote">“Ağdamın dirçəlişi və yenidən qurulan siması, Xankəndinin doğma yurda qovuşmasının yaratdığı qürur, Şuşanın tarixi və mədəni əzəməti hər birimizdə unudulmaz təəssüratlar yaratdı. Bu torpaqlarda olmaq bizə bir daha xatırlatdı ki, Zəfərimiz yalnız hərbi-siyasi qələbə deyil, həm də xalqımızın milli birliyinin, sarsılmaz iradəsinin, dövlətçilik əzminin və Vətən sevgisinin təntənəsidir.”</blockquote>',
        html
    )
    html = re.sub(
        r'<p>\s*Bu səfər, eyni zamanda, torpaqlarımızın azadlığı uğrunda[\s\S]*?</p>',
        '<p data-i18n="qarabag_p3">Bu səfər, eyni zamanda, torpaqlarımızın azadlığı uğrunda canlarından keçmiş şəhidlərimizin əziz xatirəsinə ehtiramımızın, qəhrəman qazilərimizə minnətdarlığımızın ifadəsi idi. Azad Qarabağın havasını udmaq, bu müqəddəs torpaqlarda Zəfər tariximizin izlərini görmək hər birimiz üçün böyük şərəf və qürur mənbəyinə çevrildi.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*İnanırıq ki, belə mənəvi əhəmiyyət daşıyan tədbirlər[\s\S]*?</p>',
        '<p data-i18n="qarabag_p4">İnanırıq ki, belə mənəvi əhəmiyyət daşıyan tədbirlər kollektivimizin birliyini daha da gücləndirir, əməkdaşlarımız arasında dostluq və həmrəylik münasibətlərini inkişaf etdirir, gələcək fəaliyyətimizdə ortaq məqsədlər ətrafında daha sıx birləşməyimizə stimul verir.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Çünki güclü kollektiv yalnız birlikdə çalışan insanlar deyil[\s\S]*?</p>',
        '<p data-i18n="qarabag_p5">Çünki güclü kollektiv yalnız birlikdə çalışan insanlar deyil, həm də eyni dəyərləri bölüşən, uğura birlikdə sevinən, çətinlikləri birgə aşan, məsuliyyəti və qüruru paylaşan insanlardan formalaşır.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Bu səfər bizə bir daha göstərdi ki, birliyimiz mənəvi gücümüz[\s\S]*?</p>',
        '<p data-i18n="qarabag_p6">Bu səfər bizə bir daha göstərdi ki, birliyimiz mənəvi gücümüz, həmrəyliyimiz uğurlarımızın təməli, Vətən sevgimiz isə bizi birləşdirən ən ali dəyərdir.</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Şəhidlərimizin əziz xatirəsi daim qəlbimizdə yaşayacaq[\s\S]*?</p>',
        '<p data-i18n="qarabag_p7">Şəhidlərimizin əziz xatirəsi daim qəlbimizdə yaşayacaq, onların bizə əmanət etdiyi Zəfər və azadlıq ruhu gələcək nəsillərə ötürüləcək!</p>',
        html
    )
    html = re.sub(
        r'<p>\s*Zəfər tariximizlə fəxr edir, azad Qarabağımızın dirçəlişinə sevinir[\s\S]*?</p>',
        '<p data-i18n="qarabag_p8">Zəfər tariximizlə fəxr edir, azad Qarabağımızın dirçəlişinə sevinir və milli birliyimizi, kollektiv həmrəyliyimizi daim yaşatmağı özümüzə mənəvi borc bilirik.</p>',
        html
    )
    html = html.replace('<strong class="qarabag-credo-title">🇦🇿 Birliyimiz gücümüz, həmrəyliyimiz qürurumuz, Vətən sevgimiz ən böyük dəyərimizdir!</strong>', '<strong class="qarabag-credo-title" data-i18n="qarabag_credo_title">🇦🇿 Birliyimiz gücümüz, həmrəyliyimiz qürurumuz, Vətən sevgimiz ən böyük dəyərimizdir!</strong>')
    html = html.replace('<span class="qarabag-credo-sub">Zəfərimiz əbədi, Azərbaycanımız daim var olsun! Qarabağ Azərbaycandır!</span>', '<span class="qarabag-credo-sub" data-i18n="qarabag_credo_sub">Zəfərimiz əbədi, Azərbaycanımız daim var olsun! Qarabağ Azərbaycandır!</span>')

    # 6. Structure badges
    html = html.replace('<span class="struct-badge-count">9 FBK</span>', '<span class="struct-badge-count" data-i18n="struct_badge_count">9 FBK</span>')
    html = html.replace('<span>🎓 TƏDRİS-METODİK APARAT</span>', '<span data-i18n="struct_commissions_view_title">🎓 TƏDRİS-METODİK APARAT</span>')

    # 7. Campus rooms count text & library fund button in campus/library
    html = html.replace('<span id="campus-rooms-count-text">Göstərilən otaqlar:</span>', '<span id="campus-rooms-count-text" data-i18n="campus_rooms_count_text">Göstərilən otaqlar:</span>')
    html = html.replace('<span id="lib-total-counter" class="lib-bar-count">44 Rəsmi Dərs Vəsaiti</span>', '<span id="lib-total-counter" class="lib-bar-count" data-i18n="lib_total_counter">44 Rəsmi Dərs Vəsaiti</span>')
    html = html.replace('id="lib-fund-about-btn">\n                    <span>🏛️ Kitabxana Fondu və Tarixi</span>', 'id="lib-fund-about-btn">\n                    <span data-i18n="lib_fund_about_btn">🏛️ Kitabxana Fondu və Tarixi</span>')
    html = html.replace('id="science-director-bio-btn">\n                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>\n                            <span>Direktor Səbuhi Qurbanovun Bioqrafiyası</span>', 'id="science-director-bio-btn">\n                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>\n                            <span data-i18n="science_director_bio_btn">Direktor Səbuhi Qurbanovun Bioqrafiyası</span>')

    # 8. Video Lecture Department meta labels
    html = html.replace('<span id="dept-meta-all" class="lecture-dept-meta">23 Videodərs · Bütün fənlər</span>', '<span id="dept-meta-all" class="lecture-dept-meta" data-i18n="dept_meta_all">23 Videodərs · Bütün fənlər</span>')
    html = html.replace('<span id="dept-meta-informatika" class="lecture-dept-meta">2 Videodərs · Kompüter sistemləri</span>', '<span id="dept-meta-informatika" class="lecture-dept-meta" data-i18n="dept_meta_it">2 Videodərs · Kompüter sistemləri</span>')
    html = html.replace('<span id="dept-meta-neqliyyat" class="lecture-dept-meta">1 Videodərs · Nəqliyyat Sistemləri</span>', '<span id="dept-meta-neqliyyat" class="lecture-dept-meta" data-i18n="dept_meta_transport">1 Videodərs · Nəqliyyat Sistemləri</span>')
    html = html.replace('<span id="dept-meta-cografiya" class="lecture-dept-meta">2 Videodərs · Yer Elmləri və Coğrafiya</span>', '<span id="dept-meta-cografiya" class="lecture-dept-meta" data-i18n="dept_meta_geography">2 Videodərs · Yer Elmləri və Coğrafiya</span>')
    html = html.replace('<span id="dept-meta-fizika" class="lecture-dept-meta">1 Videodərs · Təbiət və Fizika</span>', '<span id="dept-meta-fizika" class="lecture-dept-meta" data-i18n="dept_meta_physics">1 Videodərs · Təbiət və Fizika</span>')
    html = html.replace('<span id="dept-meta-tarix" class="lecture-dept-meta">9 Videodərs · Tarix və Zəfər</span>', '<span id="dept-meta-tarix" class="lecture-dept-meta" data-i18n="dept_meta_history">9 Videodərs · Tarix və Zəfər</span>')
    html = html.replace('<span id="dept-meta-az-dili" class="lecture-dept-meta">1 Videodərs · Qrammatika və Nitq</span>', '<span id="dept-meta-az-dili" class="lecture-dept-meta" data-i18n="dept_meta_az_lang">1 Videodərs · Qrammatika və Nitq</span>')
    html = html.replace('<span id="dept-meta-huquq" class="lecture-dept-meta">6 Videodərs · Hüquq sistemi</span>', '<span id="dept-meta-huquq" class="lecture-dept-meta" data-i18n="dept_meta_law">6 Videodərs · Hüquq sistemi</span>')
    html = html.replace('<span id="dept-meta-biologiya" class="lecture-dept-meta">1 Videodərs · Təbiət elmləri</span>', '<span id="dept-meta-biologiya" class="lecture-dept-meta" data-i18n="dept_meta_biology">1 Videodərs · Təbiət elmləri</span>')

    # 9. Certificates 4x II Yer
    html = html.replace('<span class="trophy-tab-medal medal-silver">4x II Yer</span>', '<span class="trophy-tab-medal medal-silver" data-i18n="trophy_silver_4x">4x II Yer</span>')

    # 10. Gallery cards
    html = html.replace('<h3 class="gal-portal-headline">Şəffaf və Rəqəmsal İmtahan Sessiyaları</h3>', '<h3 class="gal-portal-headline" data-i18n="gal_headline_exam">Şəffaf və Rəqəmsal İmtahan Sessiyaları</h3>')
    html = html.replace('<p class="gal-portal-summary">Kollecimizdə tələbələrin biliyinin obyektiv qiymətləndirilməsi üçün müasir monitorinq və kompüterləşdirilmiş imtahan mərkəzi fəaliyyət göstərir.</p>', '<p class="gal-portal-summary" data-i18n="gal_summary_exam">Kollecimizdə tələbələrin biliyinin obyektiv qiymətləndirilməsi üçün müasir monitorinq və kompüterləşdirilmiş imtahan mərkəzi fəaliyyət göstərir.</p>')
    html = html.replace('<h3 class="gal-portal-headline">Təntənəli Toplantılar və Tarixi Günlər</h3>', '<h3 class="gal-portal-headline" data-i18n="gal_headline_events">Təntənəli Toplantılar və Tarixi Günlər</h3>')
    html = html.replace('<p class="gal-portal-summary">Dövlət bayramları, məzun buraxılışları, anım tədbirləri və beynəlxalq konfranslardan yaddaqalan rəsmi kadrlar toplusu.</p>', '<p class="gal-portal-summary" data-i18n="gal_summary_events">Dövlət bayramları, məzun buraxılışları, anım tədbirləri və beynəlxalq konfranslardan yaddaqalan rəsmi kadrlar toplusu.</p>')
    html = html.replace('<h3 class="gal-portal-headline">Müasir Tədris Zalları və İnfrastruktur</h3>', '<h3 class="gal-portal-headline" data-i18n="gal_headline_rooms">Müasir Tədris Zalları və İnfrastruktur</h3>')
    html = html.replace('<p class="gal-portal-summary">Geniş amfiteatr zalları, multimedia lövhələri ilə təchiz olunmuş siniflər və texnoloji laboratoriyalarımız.</p>', '<p class="gal-portal-summary" data-i18n="gal_summary_rooms">Geniş amfiteatr zalları, multimedia lövhələri ilə təchiz olunmuş siniflər və texnoloji laboratoriyalarımız.</p>')
    html = html.replace('<h3 class="gal-portal-headline">Canlı Dərs Mühiti və Tələbə Praktikası</h3>', '<h3 class="gal-portal-headline" data-i18n="gal_headline_study">Canlı Dərs Mühiti və Tələbə Praktikası</h3>')
    html = html.replace('<p class="gal-portal-summary">Tələbələrimizin komanda işləri, interaktiv seminarlar, elektron kitabxana fəaliyyəti və laborator təcrübə saatları.</p>', '<p class="gal-portal-summary" data-i18n="gal_summary_study">Tələbələrimizin komanda işləri, interaktiv seminarlar, elektron kitabxana fəaliyyəti və laborator təcrübə saatları.</p>')

    # 11. Director Bio Modal Complete Elements
    html = html.replace('<span class="bio-brand-title">BDRNK · RƏSMİ DİREKTOR PORTALI</span>', '<span class="bio-brand-title" data-i18n="bio_brand_title">BDRNK · RƏSMİ DİREKTOR PORTALI</span>')
    html = html.replace('<span class="bio-brand-sub">Səbuhi Qurbanov Yusif oğlu — Tərcümeyi-hal və Təəssüratlar</span>', '<span class="bio-brand-sub" data-i18n="bio_brand_sub">Səbuhi Qurbanov Yusif oğlu — Tərcümeyi-hal və Təəssüratlar</span>')
    html = html.replace('<span class="bio-pill-medal">🎖️ «TƏRƏQQİ» MEDALLI</span>', '<span class="bio-pill-medal" data-i18n="bio_pill_medal">🎖️ «TƏRƏQQİ» MEDALLI</span>')
    html = html.replace('<span class="bio-pill-entity">KOLLEC DİREKTORLUĞU</span>', '<span class="bio-pill-entity" data-i18n="bio_pill_entity">KOLLEC DİREKTORLUĞU</span>')
    html = html.replace('<h2 class="bio-hero-name">SƏBUHİ QURBANOV YUSİF OĞLU</h2>', '<h2 class="bio-hero-name" data-i18n="bio_hero_name">SƏBUHİ QURBANOV YUSİF OĞLU</h2>')
    html = html.replace('<p class="bio-hero-title">Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi, Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</p>', '<p class="bio-hero-title" data-i18n="bio_hero_title">Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi, Azərbaycan Texniki Universitetinin nəzdində Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</p>')
    html = html.replace('<span class="bio-fact-item">🎂 4 avqust 1980 · Şəki</span>', '<span class="bio-fact-item" data-i18n="bio_fact_birth">🎂 4 avqust 1980 · Şəki</span>')
    html = html.replace('<span class="bio-fact-item">🎓 BDU Riyaziyyat & UNEC MBA</span>', '<span class="bio-fact-item" data-i18n="bio_fact_edu">🎓 BDU Riyaziyyat & UNEC MBA</span>')
    html = html.replace('<span class="bio-fact-item">📐 ETN Qrifli Dərslik Müəllifi</span>', '<span class="bio-fact-item" data-i18n="bio_fact_author">📐 ETN Qrifli Dərslik Müəllifi</span>')

    # Bio Chapter Strip
    html = html.replace('<a href="#bio-sec-personal" class="bio-nav-chip active">🎓 Təhsil və Həyatı</a>', '<a href="#bio-sec-personal" class="bio-nav-chip active" data-i18n="bio_nav_tab_edu">🎓 Təhsil və Həyatı</a>')
    html = html.replace('<a href="#bio-sec-career" class="bio-nav-chip">💼 Əmək Fəaliyyəti</a>', '<a href="#bio-sec-career" class="bio-nav-chip" data-i18n="bio_nav_tab_career">💼 Əmək Fəaliyyəti</a>')
    html = html.replace('<a href="#bio-sec-pedagogy" class="bio-nav-chip">📚 Elmi Əsərləri</a>', '<a href="#bio-sec-pedagogy" class="bio-nav-chip" data-i18n="bio_nav_tab_pedagogy">📚 Elmi Əsərləri</a>')
    html = html.replace('<a href="#bio-sec-international" class="bio-nav-chip">🌐 Beynəlxalq Fəaliyyət</a>', '<a href="#bio-sec-international" class="bio-nav-chip" data-i18n="bio_nav_tab_international">🌐 Beynəlxalq Fəaliyyət</a>')
    html = html.replace('<a href="#bio-sec-awards" class="bio-nav-chip">🏅 Dövlət Təltifləri</a>', '<a href="#bio-sec-awards" class="bio-nav-chip" data-i18n="bio_nav_tab_awards">🏅 Dövlət Təltifləri</a>')
    html = html.replace('<a href="#bio-sec-reflections" class="bio-nav-chip highlight">✍️ Kollec Haqqında Təəssüratlarım</a>', '<a href="#bio-sec-reflections" class="bio-nav-chip highlight" data-i18n="bio_nav_tab_reflections">✍️ Kollec Haqqında Təəssüratlarım</a>')

    # Bio Section 1
    html = html.replace('<span>BÖLMƏ I · DOĞUMU VƏ AKADEMİK TƏHSİLİ</span>', '<span data-i18n="bio_sec_i_kicker">BÖLMƏ I · DOĞUMU VƏ AKADEMİK TƏHSİLİ</span>')
    html = html.replace('<h3 class="bio-card-title">Həyatı və Təhsil İlləri</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_i_title">Həyatı və Təhsil İlləri</h3>')
    html = re.sub(
        r'<p class="bio-p bio-lead">[\s\S]*?4 avqust 1980-ci ildə Şəki rayonu[\s\S]*?</p>',
        '<p class="bio-p bio-lead" data-i18n="bio_sec_i_lead"><strong>Səbuhi Qurbanov Yusif oğlu</strong> 4 avqust 1980-ci ildə Şəki rayonu Qayabaşı kəndində anadan olmuş, 1986-cı ildə Qayabaşı kənd tam orta məktəbinin 1-ci sinifinə qəbul olmuş, 1997-ci ildə məktəbi fərqlənmə ilə bitirmişdir.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-p">\s*1997–2001-ci illərdə <strong>Bakı Dövlət Universitetinin Riyaziyyat fakültəsində</strong>[\s\S]*?</p>',
        '<p class="bio-p" data-i18n="bio_sec_i_p2">1997–2001-ci illərdə <strong>Bakı Dövlət Universitetinin Riyaziyyat fakültəsində</strong> bakalavr təhsili almışdır. 2001–2002-ci illərdə Azərbaycan Respublikası Silahlı Qüvvələrinin N saylı hərbi hissəsində hərbi xidmətdə olmuşdur. Daha sonra <strong>Azərbaycan Dövlət İqtisad Universitetində (UNEC)</strong> «Biznesin təşkili və idarə edilməsi» ixtisası üzrə magistratura təhsili almışdır.</p>',
        html
    )

    # Bio Section 2
    html = html.replace('<span>BÖLMƏ II · ƏMƏK FƏALİYYƏTİNİN RƏSMİ XRONOLOGİYASI</span>', '<span data-i18n="bio_sec_ii_kicker">BÖLMƏ II · ƏMƏK FƏALİYYƏTİNİN RƏSMİ XRONOLOGİYASI</span>')
    html = html.replace('<h3 class="bio-card-title">Peşəkar İdarəçilik və Pedaqoji Yolu</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_ii_title">Peşəkar İdarəçilik və Pedaqoji Yolu</h3>')
    html = re.sub(
        r'<p class="bio-p">\s*Səbuhi Qurbanov əmək fəaliyyətinə 2002-ci ildə başlamış[\s\S]*?</p>',
        '<p class="bio-p" data-i18n="bio_sec_ii_lead">Səbuhi Qurbanov əmək fəaliyyətinə 2002-ci ildə başlamış və 24 ildən artıq zəngin təhsil idarəçiliyi təcrübəsinə malikdir:</p>',
        html
    )
    html = html.replace('<h4 class="bio-tl-title">Şəki şəhər 11 nömrəli tam orta məktəb</h4>', '<h4 class="bio-tl-title" data-i18n="bio_tl_1_title">Şəki şəhər 11 nömrəli tam orta məktəb</h4>')
    html = html.replace('<p class="bio-tl-desc">Riyaziyyat müəllimi, eyni zamanda Təlim-tərbiyə işləri üzrə direktor müavini vəzifəsində çalışmışdır.</p>', '<p class="bio-tl-desc" data-i18n="bio_tl_1_desc">Riyaziyyat müəllimi, eyni zamanda Təlim-tərbiyə işləri üzrə direktor müavini vəzifəsində çalışmışdır.</p>')
    html = html.replace('<h4 class="bio-tl-title">Şəki şəhər 20 nömrəli tam orta məktəb</h4>', '<h4 class="bio-tl-title" data-i18n="bio_tl_2_title">Şəki şəhər 20 nömrəli tam orta məktəb</h4>')
    html = html.replace('<p class="bio-tl-desc">10 il ərzində məktəbin direktoru vəzifəsində səmərəli idarəçilik fəaliyyəti göstərmişdir.</p>', '<p class="bio-tl-desc" data-i18n="bio_tl_2_desc">10 il ərzində məktəbin direktoru vəzifəsində səmərəli idarəçilik fəaliyyəti göstərmişdir.</p>')
    html = html.replace('<h4 class="bio-tl-title">Şəki-Zaqatala Regional Təhsil İdarəsi</h4>', '<h4 class="bio-tl-title" data-i18n="bio_tl_3_title">Şəki-Zaqatala Regional Təhsil İdarəsi</h4>')
    html = html.replace('<p class="bio-tl-desc">Tədrisin Keyfiyyəti sektorunda baş məsləhətçi vəzifəsində çalışmışdır.</p>', '<p class="bio-tl-desc" data-i18n="bio_tl_3_desc">Tədrisin Keyfiyyəti sektorunda baş məsləhətçi vəzifəsində çalışmışdır.</p>')
    html = html.replace('<h4 class="bio-tl-title">Bakı Dövlət Rabitə və Nəqliyyat Kolleci</h4>', '<h4 class="bio-tl-title" data-i18n="bio_tl_4_title">Bakı Dövlət Rabitə və Nəqliyyat Kolleci</h4>')
    html = html.replace('<p class="bio-tl-desc">Tədris işləri üzrə direktor müavini vəzifəsinə təyin olunmuşdur.</p>', '<p class="bio-tl-desc" data-i18n="bio_tl_4_desc">Tədris işləri üzrə direktor müavini vəzifəsinə təyin olunmuşdur.</p>')
    html = html.replace('<div class="bio-tl-year gold">2026-cı ildən</div>', '<div class="bio-tl-year gold" data-i18n="bio_tl_5_year">2026-cı ildən</div>')
    html = html.replace('<h4 class="bio-tl-title gold">Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</h4>', '<h4 class="bio-tl-title gold" data-i18n="bio_tl_5_title">Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</h4>')
    html = html.replace('<p class="bio-tl-desc">Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi tərəfindən Kollecin direktoru vəzifəsinə təyin olunmuşdur.</p>', '<p class="bio-tl-desc" data-i18n="bio_tl_5_desc">Azərbaycan Respublikası Elm və Təhsil Nazirliyi, Elm və Ali Təhsil üzrə Dövlət Agentliyi tərəfindən Kollecin direktoru vəzifəsinə təyin olunmuşdur.</p>')

    # Bio Section 3
    html = html.replace('<span>BÖLMƏ III · ELMİ-METODİKİ VƏ PEDAQOJİ FƏALİYYƏT</span>', '<span data-i18n="bio_sec_iii_kicker">BÖLMƏ III · ELMİ-METODİKİ VƏ PEDAQOJİ FƏALİYYƏT</span>')
    html = html.replace('<h3 class="bio-card-title">Dərsliklər və Elmi Vəsaitlər</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_iii_title">Dərsliklər və Elmi Vəsaitlər</h3>')
    html = re.sub(
        r'<p class="bio-p">\s*Səbuhi Qurbanov pedaqoji fəaliyyəti ilə yanaşı, riyaziyyat elminin tədrisi[\s\S]*?</p>',
        '<p class="bio-p" data-i18n="bio_sec_iii_lead">Səbuhi Qurbanov pedaqoji fəaliyyəti ilə yanaşı, riyaziyyat elminin tədrisi və ali təhsil metodikasının inkişafına mühüm töhfələr vermişdir:</p>',
        html
    )
    html = html.replace('<span class="bio-book-year">2019 · ADPU Şurasının Qərarı</span>', '<span class="bio-book-year" data-i18n="bio_sec_iii_b1_year">2019 · ADPU Şurasının Qərarı</span>')
    html = html.replace('<h4 class="bio-book-title">«Riyaziyyat – 11»</h4>', '<h4 class="bio-book-title" data-i18n="bio_sec_iii_b1_title">«Riyaziyyat – 11»</h4>')
    html = html.replace('<p class="bio-book-desc">Azərbaycan Dövlət Pedaqoji Universitetinin Tədris-Metodiki Şurasının qərarı ilə nəşrə tövsiyə edilmiş dərs vəsaiti.</p>', '<p class="bio-book-desc" data-i18n="bio_sec_iii_b1_desc">Azərbaycan Dövlət Pedaqoji Universitetinin Tədris-Metodiki Şurasının qərarı ilə nəşrə tövsiyə edilmiş dərs vəsaiti.</p>')
    html = html.replace('<span class="bio-book-year gold">3 iyun 2026 · ETN Rəsmi Qrifi</span>', '<span class="bio-book-year gold" data-i18n="bio_sec_iii_b2_year">3 iyun 2026 · ETN Rəsmi Qrifi</span>')
    html = html.replace('<h4 class="bio-book-title">«Xətti cəbr və riyazi analiz»</h4>', '<h4 class="bio-book-title" data-i18n="bio_sec_iii_b2_title">«Xətti cəbr və riyazi analiz»</h4>')
    html = html.replace('<p class="bio-book-desc">Azərbaycan Respublikası Elm və Təhsil Nazirliyinin müvafiq əmri əsasında nəşr edilmiş və rəsmi qrif verilmiş fundamental dərslik.</p>', '<p class="bio-book-desc" data-i18n="bio_sec_iii_b2_desc">Azərbaycan Respublikası Elm və Təhsil Nazirliyinin müvafiq əmri əsasında nəşr edilmiş və rəsmi qrif verilmiş fundamental dərslik.</p>')

    # Bio Section 4
    html = html.replace('<span>BÖLMƏ IV · BEYNƏLXALQ ELMİ FORUMLAR VƏ SERTİFİKATLAR</span>', '<span data-i18n="bio_sec_iv_kicker">BÖLMƏ IV · BEYNƏLXALQ ELMİ FORUMLAR VƏ SERTİFİKATLAR</span>')
    html = html.replace('<h3 class="bio-card-title">Beynəlxalq Təcrübə və İxtisasartırma</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_iv_title">Beynəlxalq Təcrübə və İxtisasartırma</h3>')
    html = html.replace('<div class="bio-feat-badge">🇷🇺 Moskva · 2018</div>', '<div class="bio-feat-badge" data-i18n="bio_feat_1_badge">🇷🇺 Moskva · 2018</div>')
    html = html.replace('<strong>«Современные технологии в образовании»</strong>', '<strong data-i18n="bio_feat_1_title">«Современные технологии в образовании»</strong>')
    html = html.replace('<p>26 iyun 2018-ci il tarixində Moskva şəhərində keçirilən beynəlxalq elmi-praktiki konfransda iştirak etmiş və məruzə ilə çıxış etmişdir.</p>', '<p data-i18n="bio_feat_1_desc">26 iyun 2018-ci il tarixində Moskva şəhərində keçirilən beynəlxalq elmi-praktiki konfransda iştirak etmiş və məruzə ilə çıxış etmişdir.</p>')
    html = html.replace('<div class="bio-feat-badge">🌍 Qlobal Forum · 2021</div>', '<div class="bio-feat-badge" data-i18n="bio_feat_2_badge">🌍 Qlobal Forum · 2021</div>')
    html = html.replace('<strong>«Second International Forum on New Challenges in Education»</strong>', '<strong data-i18n="bio_feat_2_title">«Second International Forum on New Challenges in Education»</strong>')
    html = html.replace('<p>1 oktyabr 2021-ci il tarixində keçirilən beynəlxalq təhsil forumunda iştirak edərək müvafiq beynəlxalq sertifikatlar əldə etmişdir.</p>', '<p data-i18n="bio_feat_2_desc">1 oktyabr 2021-ci il tarixində keçirilən beynəlxalq təhsil forumunda iştirak edərək müvafiq beynəlxalq sertifikatlar əldə etmişdir.</p>')
    html = html.replace('<div class="bio-feat-badge">🛡️ Dövlət Qulluğu · AC3</div>', '<div class="bio-feat-badge" data-i18n="bio_feat_3_badge">🛡️ Dövlət Qulluğu · AC3</div>')
    html = html.replace('<strong>Liderlik və Dövlət İdarəçiliyi</strong>', '<strong data-i18n="bio_feat_3_title">Liderlik və Dövlət İdarəçiliyi</strong>')
    html = html.replace('<p>«Gənc liderlərin yay məktəbi» proqramında, Təhsil Nazirliyinin Təhsil Proqramları İnstitutu və «Mədəd Azərbaycan» MMC təlimlərində iştirak etmiş, Dövlət qulluğuna qəbul üzrə <strong>AC3 sertifikatı</strong> əldə etmişdir.</p>', '<p data-i18n="bio_feat_3_desc">«Gənc liderlərin yay məktəbi» proqramında, Təhsil Nazirliyinin Təhsil Proqramları İnstitutu və «Mədəd Azərbaycan» MMC təlimlərində iştirak etmiş, Dövlət qulluğuna qəbul üzrə <strong>AC3 sertifikatı</strong> əldə etmişdir.</p>')

    # Bio Section 5
    html = html.replace('<span>BÖLMƏ V · DÖVLƏT VƏ NAZİRLİK TƏLTİFLƏRİ</span>', '<span data-i18n="bio_sec_v_kicker">BÖLMƏ V · DÖVLƏT VƏ NAZİRLİK TƏLTİFLƏRİ</span>')
    html = html.replace('<h3 class="bio-card-title">Milli Təhsilə Fədakar Xidmət və Mükafatlar</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_v_title">Milli Təhsilə Fədakar Xidmət və Mükafatlar</h3>')
    html = re.sub(
        r'<p class="bio-p">\s*Təhsil sahəsində uzunillik səmərəli fəaliyyəti və gənc nəslin vətənpərvər ruhda yetişməsindəki[\s\S]*?</p>',
        '<p class="bio-p" data-i18n="bio_sec_v_lead">Təhsil sahəsində uzunillik səmərəli fəaliyyəti və gənc nəslin vətənpərvər ruhda yetişməsindəki xidmətləri dövlət səviyyəsində yüksək qiymətləndirilmişdir:</p>',
        html
    )
    html = html.replace('<div class="bio-aw-date">3 oktyabr 2017</div>', '<div class="bio-aw-date" data-i18n="bio_aw_1_year">3 oktyabr 2017</div>')
    html = html.replace('<h4 class="bio-aw-name">«Tərəqqi» Medalı</h4>', '<h4 class="bio-aw-name" data-i18n="bio_aw_1_title">«Tərəqqi» Medalı</h4>')
    html = re.sub(
        r'<p class="bio-aw-desc">\s*Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin müvafiq Sərəncamı ilə[\s\S]*?«Tərəqqi» medalı[\s\S]*?</p>',
        '<p class="bio-aw-desc" data-i18n="bio_aw_1_desc">Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin müvafiq Sərəncamı ilə Azərbaycan təhsilinin inkişafındakı xidmətlərinə görə <strong>«Tərəqqi» medalı</strong> ilə təltif edilmişdir.</p>',
        html
    )
    html = html.replace('<div class="bio-aw-date">5 oktyabr 2010</div>', '<div class="bio-aw-date" data-i18n="bio_aw_2_year">5 oktyabr 2010</div>')
    html = html.replace('<h4 class="bio-aw-name">«Qabaqcıl Təhsil İşçisi» Döş Nişanı</h4>', '<h4 class="bio-aw-name" data-i18n="bio_aw_2_title">«Qabaqcıl Təhsil İşçisi» Döş Nişanı</h4>')
    html = re.sub(
        r'<p class="bio-aw-desc">\s*Azərbaycan Respublikası Təhsil Nazirinin müvafiq Əmri ilə gənc nəslin təlim-tərbiyəsində[\s\S]*?«Azərbaycan Respublikası qabaqcıl təhsil işçisi»[\s\S]*?</p>',
        '<p class="bio-aw-desc" data-i18n="bio_aw_2_desc">Azərbaycan Respublikası Təhsil Nazirinin müvafiq Əmri ilə gənc nəslin təlim-tərbiyəsində qazandığı uğurlara görə <strong>«Azərbaycan Respublikası qabaqcıl təhsil işçisi»</strong> döş nişanı ilə təltif olunmuşdur.</p>',
        html
    )

    # Bio Section 6
    html = html.replace('<span>BÖLMƏ VI · RƏHBƏRİN ŞƏXSİ BAXIŞI VƏ GƏLƏCƏK HƏDƏFLƏRİ</span>', '<span data-i18n="bio_sec_vi_kicker">BÖLMƏ VI · RƏHBƏRİN ŞƏXSİ BAXIŞI VƏ GƏLƏCƏK HƏDƏFLƏRİ</span>')
    html = html.replace('<h3 class="bio-card-title">Kollec Haqqında Təəssüratlarım və Strateji Vizyon</h3>', '<h3 class="bio-card-title" data-i18n="bio_sec_vi_title">Kollec Haqqında Təəssüratlarım və Strateji Vizyon</h3>')
    html = re.sub(
        r'<p class="bio-p bio-lead">\s*Direktor Səbuhi Qurbanovun Bakı Dövlət Rabitə və Nəqliyyat Kollecinin hazırkı[\s\S]*?</p>',
        '<p class="bio-p bio-lead" data-i18n="bio_sec_vi_lead">Direktor Səbuhi Qurbanovun Bakı Dövlət Rabitə və Nəqliyyat Kollecinin hazırkı inkişaf dinamikası və strateji hədəfləri haqqında rəsmi essesi:</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Azərbaycan Respublikası Elm və Təhsil Nazirliyinin[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p1">Azərbaycan Respublikası Elm və Təhsil Nazirliyinin, Elm və Ali Təhsil üzrə Dövlət Agentliyinin qərarı ilə Bakı Dövlət Rabitə və Nəqliyyat Kollecinə rəhbər təyin olunmağım mənim üçün böyük şərəf olmaqla yanaşı, həm də yüksək məsuliyyətdir.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Kollecin fəaliyyətinə qoşulduğum ilk gündən[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p2">Kollecin fəaliyyətinə qoşulduğum ilk gündən burada formalaşmış pedaqoji ənənələr, əməkdaşların peşəkarlığı, təhsilalanların potensialı və müəssisənin zəngin tarixi məndə xoş təəssürat yaratdı. Bu təhsil müəssisəsinin illər ərzində rabitə və nəqliyyat sahələri üçün ixtisaslı kadrların hazırlanmasında oynadığı rolu xüsusi qeyd etmək istərdim.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Kollecin fəaliyyəti ilə yaxından tanış olduqca[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p3">Kollecin fəaliyyəti ilə yaxından tanış olduqca gördüm ki, burada yalnız tədris prosesi deyil, həm də kollektivin birgə fəaliyyəti, qarşılıqlı hörmət, məsuliyyət və peşəkar yanaşma mühüm yer tutur. Mənim üçün rəhbər vəzifədə əsas məqsədlərdən biri mövcud müsbət ənənələri qorumaqla yanaşı, onların müasir dövrün tələblərinə uyğun inkişaf etdirilməsidir.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Fəaliyyətim dövründə diqqət yetirdiyim əsas istiqamətlərdən[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p4">Fəaliyyətim dövründə diqqət yetirdiyim əsas istiqamətlərdən biri təhsilin keyfiyyətinin yüksəldilməsi, tədris prosesinin müasir tələblərə uyğun təşkili, qiymətləndirmə və monitorinq mexanizmlərinin təkmilləşdirilməsi, innovativ texnologiyaların tədrisə tətbiqi və tələbələrin praktiki bilik və bacarıqlarının inkişafıdır.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Xüsusilə kollecdə müəllim-tələbə münasibətlərinin[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p5">Xüsusilə kollecdə müəllim-tələbə münasibətlərinin sağlam əsaslar üzərində qurulmasını, tələbələrin təşəbbüskarlığının dəstəklənməsini, onların müxtəlif elmi, intellektual, idman və yaradıcılıq tədbirlərində iştirakını vacib hesab edirəm. Çünki müasir təhsil müəssisəsi yalnız bilik verən deyil, eyni zamanda şəxsiyyət yetişdirən, gənclərin dünyagörüşünü və vətəndaşlıq mövqeyini formalaşdıran bir məkandır.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Kollecin əməkdaşlarının təşəbbüskarlığı, müxtəlif tədbirlərin təşkili[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p6">Kollecin əməkdaşlarının təşəbbüskarlığı, müxtəlif tədbirlərin təşkili, şagird və tələbələrlə maarifləndirici görüşlərin keçirilməsi, digər təhsil müəssisələri ilə əməkdaşlıq əlaqələrinin genişləndirilməsi istiqamətində görülən işlər də məndə müsbət təəssürat yaradır. Bakı Avropa Liseyinin müəllim və şagird heyətinin kollecdə qonaq olması, robototexnika və süni intellekt sahəsində fikir mübadiləsinin aparılması kimi görüşlər təhsil müəssisələri arasında əməkdaşlığın əhəmiyyətini bir daha nümayiş etdirir.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Kollecin ictimai həyatında milli-mənəvi dəyərlərin[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p7">Kollecin ictimai həyatında milli-mənəvi dəyərlərin, vətənpərvərlik ruhunun və dövlətçilik ənənələrinin qorunmasına da xüsusi önəm verirəm. Zəfər Günü münasibətilə kollektivimizin Ağdam, Xankəndi və Şuşaya səfəri, tələbələrin və əməkdaşların müxtəlif vətənpərvərlik tədbirlərində iştirakı bu baxımdan əlamətdar olmuşdur. İnanıram ki, gənclərimiz tariximizi dərindən öyrənməklə yanaşı, Vətənimizin bugünkü inkişafına da öz töhfələrini verməlidirlər.</p>',
        html
    )
    html = re.sub(
        r'<p class="bio-essay-p">\s*Rəhbərlik etdiyim müddətdə kollecin kollektivində müşahidə etdiyim əməkdaşlıq[\s\S]*?</p>',
        '<p class="bio-essay-p" data-i18n="bio_essay_p8">Rəhbərlik etdiyim müddətdə kollecin kollektivində müşahidə etdiyim əməkdaşlıq, qarşılıqlı dəstək və ümumi məqsəd ətrafında birləşmək istəyi gələcək fəaliyyətimiz üçün mühüm zəmin yaradır. Mən hesab edirəm ki, hər bir təhsil müəssisəsinin uğuru onun maddi-texniki imkanları ilə yanaşı, insan kapitalından, kollektivin birliyindən və yeniliklərə açıq olmasından asılıdır. Bakı Dövlət Rabitə və Nəqliyyat Kollecini daha müasir, rəqabətqabiliyyətli, innovativ və əmək bazarının tələblərinə cavab verən təhsil müəssisəsi kimi inkişaf etdirmək əsas hədəflərimizdəndir. İnanıram ki, birgə fəaliyyətimiz sayəsində yeni uğurlara imza atacağıq.</p>',
        html
    )
    # Highlight conclusion if present
    html = re.sub(
        r'<p class="bio-essay-p highlight-conclusion">[\s\S]*?</p>',
        '',
        html
    )
    html = html.replace('<strong>Səbuhi Qurbanov</strong>\n                                    <span>Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</span>', '<strong data-i18n="bio_sig_name">Səbuhi Qurbanov</strong>\n                                    <span data-i18n="bio_sig_title">Bakı Dövlət Rabitə və Nəqliyyat Kollecinin Direktoru</span>')

    # 12. Library Fund Modal
    html = html.replace('<div class="lib-fund-stat-val">57 Adda</div>', '<div class="lib-fund-stat-val" data-i18n="lib_fund_stat_val_3">57 Adda</div>')
    html = re.sub(
        r'<p class="lib-card-p">\s*Kitabxanada kitab fondu ilkin mərhələdə təxminən[\s\S]*?</p>',
        '<p class="lib-card-p" data-i18n="lib_fund_p1">Kitabxanada kitab fondu ilkin mərhələdə təxminən <strong>22.000 nüsxədən</strong> ibarət olmuşdur. Sonralar köhnəlmiş, indiki tələbatlara cavab verməyən ədəbiyyatların silinməsi nəticəsində hal-hazırda fondumuz <strong>10.000 nüsxə ədəbiyyat</strong> təşkil edir. Kitabxanamızda müxtəlif istiqamətlər üzrə zəngin ədəbiyyat fondu formalaşmışdır.</p>',
        html
    )
    html = re.sub(
        r'<p class="lib-card-p">\s*Eyni zamanda bu dövrdə fondun müasir tələblərə uyğunlaşdırılması[\s\S]*?</p>',
        '<p class="lib-card-p" data-i18n="lib_fund_p2">Eyni zamanda bu dövrdə fondun müasir tələblərə uyğunlaşdırılması, ədəbiyyatın yenidən nəzərdən keçirilməsi və kitabxana resurslarından səmərəli istifadə istiqamətində vacib təşkilati işlər həyata keçirilmişdir.</p>',
        html
    )
    html = re.sub(
        r'<p class="lib-card-p">\s*<strong>Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin</strong> “Azərbaycan dilində latın qrafikası[\s\S]*?</p>',
        '<p class="lib-card-p" data-i18n="lib_fund_p3"><strong>Azərbaycan Respublikasının Prezidenti cənab İlham Əliyevin</strong> “Azərbaycan dilində latın qrafikası ilə kütləvi nəşrlərin həyata keçirilməsi haqqında” <strong>12 yanvar 2004-cü il tarixli Sərəncamına</strong> əsasən bütün bədii ədəbiyyatlar yeni nəşrlərlə əvəz olunaraq, kitabxanamıza hədiyyə olunmuşdur.</p>',
        html
    )
    html = re.sub(
        r'<p class="lib-card-p">\s*Tədris fondunun zənginləşdirilməsi istiqamətində kollecimizin müəllim heyəti[\s\S]*?</p>',
        '<p class="lib-card-p" data-i18n="lib_fund_p4">Tədris fondunun zənginləşdirilməsi istiqamətində kollecimizin müəllim heyəti tərəfindən tədris planına uyğun olaraq kitabxana fondu mütəmadi olaraq artırılır. Bu nəşrlərin olması tələbələrə ixtisaslarına uyğun olaraq informasiya təminatının yaxşılaşdırılmasına xidmət edir.</p>',
        html
    )
    html = re.sub(
        r'<p class="lib-card-p">\s*Hal-hazırda kitabxanamızda <strong>57 adda dərslik</strong>[\s\S]*?</p>',
        '<p class="lib-card-p" data-i18n="lib_fund_p5">Hal-hazırda kitabxanamızda <strong>57 adda dərslik</strong> fondumuza daxil edilmişdir. 2026-cı ildə nəşr olunmuş yeni dərsliklərimizi xüsusi vurğulamaq istərdik:</p>',
        html
    )

    # Textbook badges in Library fund modal
    html = html.replace('<strong>Xətti cəbr və riyazi analiz</strong>\n                                <span>Direktor Səbuhi Qurbanov · 2026</span>', '<strong data-i18n="lib_tb_1_title">Xətti cəbr və riyazi analiz</strong>\n                                <span data-i18n="lib_tb_1_meta">Direktor Səbuhi Qurbanov · 2026</span>')
    html = html.replace('<strong>Ekoloji Monitorinq</strong>\n                                <span>Kollec Pedaqoji Heyəti · 2026</span>', '<strong data-i18n="lib_tb_2_title">Ekoloji Monitorinq</strong>\n                                <span data-i18n="lib_tb_2_meta">Kollec Pedaqoji Heyəti · 2026</span>')
    html = html.replace('<strong>Dərslik Sxematexnika-1</strong>\n                                <span>Texniki Fənlər Kafedrası · 2026</span>', '<strong data-i18n="lib_tb_3_title">Dərslik Sxematexnika-1</strong>\n                                <span data-i18n="lib_tb_3_meta">Texniki Fənlər Kafedrası · 2026</span>')
    html = html.replace('<strong>İnformasiya-Şəbəkə Texnologiyaları</strong>\n                                <span>İKT və Telekommunikasiya · 2026</span>', '<strong data-i18n="lib_tb_4_title">İnformasiya-Şəbəkə Texnologiyaları</strong>\n                                <span data-i18n="lib_tb_4_meta">İKT və Telekommunikasiya · 2026</span>')

    # Bump cache version
    html = re.sub(r'script\.js\?v=[^\"]+', 'script.js?v=20261106_36', html)
    html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=20261106_36', html)

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html)
    print("index.html updated successfully with complete data-i18n attributes.")

if __name__ == '__main__':
    update_script_js()
    update_style_css()
    update_index_html()
    print("ALL UPDATES APPLIED!")
