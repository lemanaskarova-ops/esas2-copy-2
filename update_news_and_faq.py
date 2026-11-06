import json, re

# New comprehensive news data
new_news_data = [
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
]

# New comprehensive FAQ data (Məlumat / Tez-tez verilən suallar)
new_faq_data = [
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
      "az": "İmtahan nəticələrimi və davamiyyətimi necə öyrənə bilərəm?",
      "ru": "Как проверить результаты экзаменов и посещаемость?",
      "en": "How can I check my exam grades and attendance?"
    },
    "a": {
      "az": "Saytımızın 'Tələbə Portalı' (SIS) bölməsinə daxil olub tələbə biletinizin ID kodunu yazmaqla cari semestr üzrə fənn ballarınızı, imtahan nəticələrinizi, GPA göstəricinizi və aylıq davamiyyət statistikanızı canlı izləyə bilərsiniz.",
      "ru": "Войдя в раздел 'Студенческий Портал' (SIS) на сайте и введя свой студенческий ID, вы сможете в режиме реального времени отслеживать баллы за предметы, результаты экзаменов, текущий GPA и ежемесячную посещаемость.",
      "en": "By signing in to the 'Student Portal' (SIS) with your Student ID number, you can instantly review real-time course grades, exam results, cumulative GPA, and monthly attendance tracking."
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
]

# Read script.js
with open("/Users/konul/Documents/kollec 2 copy 6/script.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# 1. Update i18n object to include missing context menu keys
az_cm = """    cm_theme: "Açıq / Tünd Rejim",
    cm_portal: "Tələbə Portalı",
    cm_totop: "Yuxarı Qayıt",
    footer_copyright:"""

en_cm = """    cm_theme: "Light / Dark Mode",
    cm_portal: "Student Portal",
    cm_totop: "Back to Top",
    footer_copyright:"""

ru_cm = """    cm_theme: "Светлая / Темная Тема",
    cm_portal: "Студенческий Портал",
    cm_totop: "Наверх",
    footer_copyright:"""

if "cm_theme:" not in js_content:
    js_content = js_content.replace('footer_copyright:\n      "© 2026 BDRNK - Müəllif hüquqları qorunur. Hazırlayan: Ləman Əskərova",', az_cm + '\n      "© 2026 BDRNK - Müəllif hüquqları qorunur. Hazırlayan: Ləman Əskərova",', 1)
    js_content = js_content.replace('footer_copyright: "© 2026 BDRNK - All rights reserved. Created by: Ləman Əskərova",', en_cm + ' "© 2026 BDRNK - All rights reserved. Created by: Ləman Əskərova",', 1)
    js_content = js_content.replace('footer_copyright: "© 2026 BDRNK - Все права защищены. Разработчик: Ləman Əskərova",', ru_cm + ' "© 2026 BDRNK - Все права защищены. Разработчик: Ləman Əskərova",', 1)

# 2. Replace newsData
news_json_str = json.dumps(new_news_data, ensure_ascii=False, indent=2)
# Replace newsData array
pattern_news = r"const newsData = \[.*?\];"
replacement_news = f"const newsData = {news_json_str};"
js_content, n_count = re.subn(pattern_news, replacement_news, js_content, flags=re.DOTALL)
print(f"newsData replaced: {n_count}")

# 3. Replace faqData
faq_json_str = json.dumps(new_faq_data, ensure_ascii=False, indent=2)
pattern_faq = r"const faqData = \[.*?\];"
replacement_faq = f"const faqData = {faq_json_str};"
js_content, f_count = re.subn(pattern_faq, replacement_faq, js_content, flags=re.DOTALL)
print(f"faqData replaced: {f_count}")

# 4. Check renderFAQ language reactivity
# Verify how FAQ is rendered when language changes
with open("/Users/konul/Documents/kollec 2 copy 6/script.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print("Update completed successfully!")
