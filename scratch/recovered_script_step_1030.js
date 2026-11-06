const fs = require("fs");
const ROOT = "/Users/konul/Documents/esas2 copy 2";
const src = fs.readFileSync(ROOT + "/script.js", "utf8");
const s = src.indexOf("const newsData = [");
const e = src.indexOf("\n];", s);
const arr = eval(src.slice(s + "const newsData = ".length, e + 3));

const photoPool = [
  // Exam & Sports (11 items)
  { id: 6, cat: "exam", custom_az: "Stolüstü tennis üzrə qalib tələbə komandamız", custom_en: "Our student table tennis champions", custom_ru: "Студенческая команда-победитель по настольному теннису" },
  { id: 9, cat: "exam", custom_az: "Respublika turnirində qalib müəllimimiz", custom_en: "Our award-winning instructor at national tournament", custom_ru: "Преподаватель-победитель республиканского турнира" },
  { id: 13, cat: "exam", custom_az: "10 km marafon və atletika qaçışında uğur", custom_en: "Success in 10k marathon and athletic race", custom_ru: "Успех в 10-километровом марафоне" },
  { id: 14, cat: "exam", custom_az: "«Parlaq Gələcək Naminə Qaç» turniri mükafatlandırma", custom_en: "Award ceremony for Bright Future Run", custom_ru: "Церемония награждения турнира Бег во имя будущего" },
  { id: 15, cat: "exam", custom_az: "Türkiyədə Beynəlxalq Marafon təmsilçiliyi", custom_en: "Representation at the International Marathon in Turkey", custom_ru: "Участие в международном марафоне в Турции" },
  { id: 25, cat: "exam", custom_az: "«Qızıl payız» qaçış festivalı qalibləri", custom_en: "Winners of the Golden Autumn running festival", custom_ru: "Победители бегового фестиваля Золотая осень" },
  { id: 40, cat: "exam", custom_az: "Tələbələr arasında ənənəvi idman spartakiadası", custom_en: "Traditional student sports tournament", custom_ru: "Традиционная студенческая спартакиада" },
  { id: 59, cat: "exam", custom_az: "Kollec tələbələrinin Şahmat və Dama çempionatı", custom_en: "College student Chess and Checkers championship", custom_ru: "Чемпионат колледжа по шахматам и шашкам" },
  { id: 76, cat: "exam", custom_az: "Basketbol üzrə Respublika çempionluğu kuboku", custom_en: "National championship trophy in basketball", custom_ru: "Кубок чемпионов по баскетболу" },
  { id: 88, cat: "exam", custom_az: "Kollec Basketbol komandasının uğurlu çıxışı", custom_en: "Victorious performance of College basketball team", custom_ru: "Успешное выступление баскетбольной команды колледжа" },
  { id: 93, cat: "exam", custom_az: "Tələbələrimizin rəsmi idman nailiyyətləri diplomu", custom_en: "Official sports achievement diploma", custom_ru: "Официальный спортивный диплом наших студентов" },

  // Events (14 items)
  { id: 7, cat: "events", custom_az: "Kollecin yeni rəhbərliyinin kollektivə təqdimatı", custom_en: "Presentation of new leadership to college staff", custom_ru: "Представление нового руководства коллективу" },
  { id: 10, cat: "events", custom_az: "BMT Ümumdünya Şəhərsalma Forumu XIII sessiyası", custom_en: "UN World Urban Forum XIII session celebration", custom_ru: "Мероприятие к XIII сессии Всемирного форума ООН" },
  { id: 11, cat: "events", custom_az: "Kollec əməkdaşlarının Fəxri Fərmanla təltifi", custom_en: "Honoring college employees with Certificates of Merit", custom_ru: "Награждение сотрудников почетными грамотами" },
  { id: 12, cat: "events", custom_az: "Ümummilli Lider Heydər Əliyevin Anım Tədbiri", custom_en: "Commemorative assembly for National Leader Heydar Aliyev", custom_ru: "Мероприятие памяти Общенационального Лидера Гейдара Алиева" },
  { id: 19, cat: "events", custom_az: "Xalq şairi Bəxtiyar Vahabzadənin 100 illik yubileyi", custom_en: "100th anniversary of national poet Bakhtiyar Vahabzade", custom_ru: "100-летний юбилей народного поэта Бахтияра Вахабзаде" },
  { id: 20, cat: "events", custom_az: "8 Noyabr — Zəfər Gününə həsr olunmuş təntənəli toplantı", custom_en: "Solemn assembly celebrating November 8 Victory Day", custom_ru: "Торжественное собрание ко Дню Победы 8 Ноября" },
  { id: 26, cat: "events", custom_az: "5 Oktyabr — Beynəlxalq Müəllimlər Günü qeyd edilməsi", custom_en: "Celebration of World Teachers Day on October 5", custom_ru: "Празднование Международного дня учителя 5 Октября" },
  { id: 30, cat: "events", custom_az: "Kollecdə Şeir və Mahnı Müsabiqəsinin qala tədbiri", custom_en: "Gala event of College Poetry and Song Competition", custom_ru: "Гала-мероприятие конкурса стихов и песен" },
  { id: 39, cat: "events", custom_az: "Tarixi anım və dövlətçilik tədbiri", custom_en: "Historical commemoration and statehood event", custom_ru: "Историческое и государственное памятное мероприятие" },
  { id: 43, cat: "events", custom_az: "20 Yanvar — Xalqımızın Qürur və Anım Günü", custom_en: "January 20 National Pride and Commemoration Day", custom_ru: "20 Января — День всенародной скорби и гордости" },
  { id: 57, cat: "events", custom_az: "Dövlət Bayrağı Günü və Zəfər Bayramı tədbiri", custom_en: "State Flag Day and Victory Day celebration", custom_ru: "Празднование Дня Государственного Флага и Победы" },
  { id: 58, cat: "events", custom_az: "Dahi dramaturq Hüseyn Cavidin anım toplantısı", custom_en: "Commemoration assembly for dramatist Huseyn Javid", custom_ru: "Мероприятие памяти великого драматурга Гусейна Джавида" },
  { id: 66, cat: "events", custom_az: "Fədakar pedaqoqlarımızın təltifetmə mərasimi", custom_en: "Award ceremony honoring dedicated educators", custom_ru: "Церемония чествования выдающихся педагогов" },
  { id: 91, cat: "events", custom_az: "Xocalı Soyqırımı qurbanlarının xatirəsinə tədbir", custom_en: "Commemoration of the Khojaly genocide victims", custom_ru: "Мероприятие памяти жертв Ходжалинского геноцида" },

  // Rooms & Infrastructure (12 items)
  { id: 16, cat: "rooms", custom_az: "Rəhbərlik və Həmkarlar İttifaqı iclas zalı", custom_en: "Leadership & Trade Union council conference room", custom_ru: "Зал заседаний руководства и профсоюза" },
  { id: 29, cat: "rooms", custom_az: "Kollecin geniş Mərkəzi Akt Zalı", custom_en: "Central Grand Auditorium of the College", custom_ru: "Центральный актовый зал колледжа" },
  { id: 31, cat: "rooms", custom_az: "Böyük amfiteatr auditoriyası və mühazirə zalı", custom_en: "Large amphitheater lecture hall", custom_ru: "Большая лекционная аудитория-амфитеатр" },
  { id: 44, cat: "rooms", custom_az: "Tələbə konfrans zalı və panel müzakirə otağı", custom_en: "Student conference hall and panel room", custom_ru: "Студенческий конференц-зал и комната панелей" },
  { id: 55, cat: "rooms", custom_az: "Dəyirmi masa və seminar zalı", custom_en: "Roundtable discussion and seminar hall", custom_ru: "Круглый стол и зал семинаров" },
  { id: 63, cat: "rooms", custom_az: "Müasir interaktiv tədris zalı", custom_en: "Modern interactive academic hall", custom_ru: "Современный интерактивный учебный зал" },
  { id: 64, cat: "rooms", custom_az: "Elmi Şura və Rəyasət Heyəti otağı", custom_en: "Academic Council and presidium conference room", custom_ru: "Зал Ученого совета и президиума" },
  { id: 70, cat: "rooms", custom_az: "İnteraktiv mühazirə auditoriyası", custom_en: "Interactive lecture auditorium", custom_ru: "Интерактивная лекционная аудитория" },
  { id: 74, cat: "rooms", custom_az: "Akademik seminar və layihə müzakirə otağı", custom_en: "Academic seminar & project discussion room", custom_ru: "Зал академических семинаров и проектов" },
  { id: 85, cat: "rooms", custom_az: "Kollecin təqdimat və görüş auditoriyası", custom_en: "College presentation & meeting hall", custom_ru: "Презентационный и встречный зал колледжа" },
  { id: 96, cat: "rooms", custom_az: "Tələbə ekskursiyası və mərkəz foye kompleksi", custom_en: "Student study visit and center foyer complex", custom_ru: "Фойе и выставочный комплекс колледжа" },
  { id: 97, cat: "rooms", custom_az: "Dövlət təhsil standartları dəyirmi masa zalı", custom_en: "State educational standards conference room", custom_ru: "Зал круглого стола государственных стандартов" },

  // Study & Classes (13 items)
  { id: 1, cat: "study", custom_az: "«Narkomaniyaya qarşı mübarizə» maarifləndirici dərsi", custom_en: "Awareness lecture on healthy student lifestyle", custom_ru: "Просветительский урок о здоровом образе жизни" },
  { id: 2, cat: "study", custom_az: "Açıq maarifləndirici seminar və tələbə diskussiyası", custom_en: "Open educational seminar and student discussion", custom_ru: "Открытый просветительский семинар и дискуссия" },
  { id: 3, cat: "study", custom_az: "Şəffaflıq və hüquq maarifləndirmə dərsi", custom_en: "Transparency and legal awareness class", custom_ru: "Урок правового просвещения и прозрачности" },
  { id: 4, cat: "study", custom_az: "«Azərbaycan dilinin saflığı» interaktiv auditoriya dərsi", custom_en: "Interactive lecture on native language purity", custom_ru: "Интерактивный урок чистоты родного языка" },
  { id: 18, cat: "study", custom_az: "Dövlət dili və nitq mədəniyyəti seminarı", custom_en: "State language and speech culture seminar", custom_ru: "Семинар культуры речи и государственного языка" },
  { id: 22, cat: "study", custom_az: "Tələbələrlə interaktiv qrup işi və təqdimat dərsi", custom_en: "Interactive student teamwork and presentation lesson", custom_ru: "Интерактивная групповая работа студентов" },
  { id: 23, cat: "study", custom_az: "Hüquq və vətəndaşlıq aylığı çərçivəsində dərs", custom_en: "Civics and legal awareness class", custom_ru: "Урок в рамках месячника правовых знаний" },
  { id: 32, cat: "study", custom_az: "Şəffaflıq və korrupsiyaya qarşı birgə mübarizə dərsi", custom_en: "Integrity and ethics seminar for youth", custom_ru: "Урок этики и прозрачности для молодежи" },
  { id: 33, cat: "study", custom_az: "Tələbələrin fərdi və qrup təqdimat çıxışları", custom_en: "Student individual and group presentations", custom_ru: "Индивидуальные и групповые выступления студентов" },
  { id: 48, cat: "study", custom_az: "Mərkəzləşdirilmiş Elektron İnformasiya Sistemi təlimi", custom_en: "Centralized Electronic Info System training", custom_ru: "Обучение централизованной информационной системе" },
  { id: 51, cat: "study", custom_az: "Gənclərin hüquqi məsuliyyəti seminarı", custom_en: "Legal responsibility seminar for students", custom_ru: "Семинар юридической ответственности студентов" },
  { id: 60, cat: "study", custom_az: "Təbii sərvətlər və ekoloji məsuliyyət dərsi", custom_en: "Environmental awareness & sustainability lesson", custom_ru: "Урок экологической ответственности" },
  { id: 84, cat: "study", custom_az: "Tələbə auditoriyasında praktiki məşğələ prosesi", custom_en: "Practical training in college lecture hall", custom_ru: "Практическое занятие в учебной аудитории" }
];

const enriched = photoPool.map(item => {
  const n = arr.find(x => x.id === item.id);
  return {
    id: item.id,
    cat: item.cat,
    src: n ? n.image : "",
    title_az: item.custom_az,
    title_en: item.custom_en,
    title_ru: item.custom_ru,
    date_az: n ? n.date_az : "",
    date_en: n ? n.date_en : "",
    date_ru: n ? n.date_ru : "",
    tag_az: n ? n.tag_az : "",
    tag_en: n ? n.tag_en : "",
    tag_ru: n ? n.tag_ru : ""
  };
});

fs.writeFileSync("/tmp/enriched_gallery.json", JSON.stringify(enriched, null, 2));
console.log("Enriched gallery pool count:", enriched.length);
