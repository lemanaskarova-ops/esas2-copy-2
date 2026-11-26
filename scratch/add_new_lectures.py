import re

with open('script.js', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Add new items to libraryData
new_library_items = '''  {
    id: 84,
    title_az: "Riyaziyyat (II Semestr Mühazirələri)",
    title_en: "Mathematics (Semester II Lectures)",
    title_ru: "Математика (Лекции II семестра)",
    author_az: "Dəqiq Elmlər FBK",
    author_en: "Exact Sciences Department",
    author_ru: "ФБК Точных наук",
    category: "riyaziyyat",
    icon: "📐",
    url: "2 ci semestr riyaziyyat.pdf",
  },
  {
    id: 85,
    title_az: "Riyaziyyat (I Semestr Mühazirələri)",
    title_en: "Mathematics (Semester I Lectures)",
    title_ru: "Математика (Лекции I семестра)",
    author_az: "Dəqiq Elmlər FBK",
    author_en: "Exact Sciences Department",
    author_ru: "ФБК Точных наук",
    category: "riyaziyyat",
    icon: "📐",
    url: "1 ci semestr riyaziyyat.pdf",
  },
  {
    id: 86,
    title_az: "Ali Riyaziyyat (Mühazirələr Toplusu)",
    title_en: "Higher Mathematics (Lecture Notes)",
    title_ru: "Высшая математика (Сборник лекций)",
    author_az: "Dəqiq Elmlər FBK",
    author_en: "Exact Sciences Department",
    author_ru: "ФБК Точных наук",
    category: "riyaziyyat",
    icon: "📊",
    url: "ALI RIY muhazire (1).pdf",
  },
  {
    id: 87,
    title_az: "Biologiya (Mövzular və Mühazirələr)",
    title_en: "Biology (Topics & Lectures)",
    title_ru: "Биология (Темы и лекции)",
    author_az: "Dəqiq Elmlər FBK (İlahə Qaraxanova)",
    author_en: "Exact Sciences Department",
    author_ru: "ФБК Точных наук",
    category: "ekologiya",
    icon: "🔬",
    url: "Biologiya mövzular.pdf",
  },'''

if 'id: 84,' not in s:
    target_lib_end = 'url: "kitab.ƏSLİ-İSTEHLAKÇI DAVRANIŞLARI-1 (1).pdf",\n  },'
    replacement_lib_end = target_lib_end + '\n' + new_library_items
    s = s.replace(target_lib_end, replacement_lib_end, 1)
    print("Added new books to libraryData")

# 2. Add new lectures to fbkLecturesArchive
new_lecture_items = ''',
    // --- Riyaziyyat və Dəqiq Elmlər (Yeni Mühazirələr) ---
    {
      id: "fbk-lec-riyaziyyat-2",
      fbkId: "fbk-9",
      fieldBadge: "RİYAZİYYAT",
      fieldName_az: "Dəqiq Elmlər, FT və ÇHQ",
      subject_az: "Riyaziyyat (II Semestr)",
      title_az: "Riyaziyyat Fənnindən Mühazirələr Toplusu (II Semestr)",
      author_az: "Dəqiq Elmlər FBK",
      format: "pdf",
      icon: "📐",
      volume: "Mühazirələr Toplusu · PDF",
      fileSize: "706 KB",
      desc_az: "Kompleks ədədin tərifi, qoşma kompleks ədədlər, kompleks ədədlər üzərində cəbri əməllər, funksiyalar və riyazi analiz üzrə II semestr rəsmi mühazirə vəsaiti.",
      topics_az: ["Kompleks Ədədlər", "Cəbri Əməllər", "Qoşma Ədədlər", "II Semestr Mövzuları"],
      url: "2 ci semestr riyaziyyat.pdf"
    },
    {
      id: "fbk-lec-riyaziyyat-1",
      fbkId: "fbk-9",
      fieldBadge: "RİYAZİYYAT",
      fieldName_az: "Dəqiq Elmlər, FT və ÇHQ",
      subject_az: "Riyaziyyat (I Semestr)",
      title_az: "Riyaziyyat Fənnindən Mühazirələr Toplusu (I Semestr)",
      author_az: "Dəqiq Elmlər FBK",
      format: "pdf",
      icon: "📐",
      volume: "Mühazirələr Toplusu · PDF",
      fileSize: "866 KB",
      desc_az: "Ədədi funksiyanın tərifi, təyin oblastı, qiymətlər çoxluğu və qrafiki, təyin oblastının tapılması üsulları və funksional asılılıqlar üzrə I semestr mühazirə vəsaiti.",
      topics_az: ["Ədədi Funksiyalar", "Təyin Oblastı", "Qiymətlər Çoxluğu", "Funksiya Qrafikləri"],
      url: "1 ci semestr riyaziyyat.pdf"
    },
    {
      id: "fbk-lec-ali-riy",
      fbkId: "fbk-9",
      fieldBadge: "ALİ RİYAZİYYAT",
      fieldName_az: "Dəqiq Elmlər, FT və ÇHQ",
      subject_az: "Ali Riyaziyyat",
      title_az: "Ali Riyaziyyat Fənnindən Fundamental Mühazirələr Toplusu",
      author_az: "Dəqiq Elmlər FBK",
      format: "pdf",
      icon: "📊",
      volume: "Fundamental Mühazirə · PDF",
      fileSize: "6.5 MB",
      desc_az: "Xətti cəbr, matrislər və determinantlar, xətti tənliklər sistemi, vektorlar cəbri, analitik həndəsə, limit, diferensial və inteqral hesabı üzrə ali riyaziyyat mühazirələri.",
      topics_az: ["Xətti Cəbr", "Matris və Determinant", "Analitik Həndəsə", "Riyazi Analiz"],
      url: "ALI RIY muhazire (1).pdf"
    },
    {
      id: "fbk-lec-biologiya",
      fbkId: "fbk-9",
      fieldBadge: "BİOLOGİYA",
      fieldName_az: "Dəqiq Elmlər, FT və ÇHQ",
      subject_az: "Biologiya",
      title_az: "Biologiya Fənni Üzrə Mövzular və Mühazirələr Toplusu",
      author_az: "Dəqiq Elmlər FBK (Qaraxanova İlahə)",
      format: "pdf",
      icon: "🔬",
      volume: "Mövzular Toplusu · PDF",
      fileSize: "2.0 MB",
      desc_az: "Canlılarda qidalanma, tənəffüs, ifrazat, çoxalma və qıcıqlanma, avtotrof və heterotrof canlılar, hüceyrə biologiyası və orqanizmlərin həyat fəaliyyəti üzrə mühazirə vəsaiti.",
      topics_az: ["Canlıların Xüsusiyyətləri", "Qidalanma və Tənəffüs", "Çoxalma və İfrazat", "Hüceyrə Nəzəriyyəsi"],
      url: "Biologiya mövzular.pdf"
    }'''

if 'fbk-lec-riyaziyyat-2' not in s:
    target_lec_end = 'url: "Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf"\n    }\n  ];'
    replacement_lec_end = 'url: "Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf"\n    }' + new_lecture_items + '\n  ];'
    s = s.replace(target_lec_end, replacement_lec_end, 1)
    print("Added new lectures to fbkLecturesArchive")

# 3. Add material cards inside FBK-09 drawer in script.js
fbk9_materials = '''                  <!-- Material 3: Riyaziyyat II Semestr (Mühazirə) -->
                  <div style="display:flex; flex-direction:column; gap:10px; padding-top:14px; border-top:1px dashed rgba(184,147,74,0.3);">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                      <div style="font-size:2.2rem; line-height:1;">📐</div>
                      <div style="flex:1;">
                        <div style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; background:rgba(184,147,74,0.15); padding:2px 8px; border-radius:4px; margin-bottom:6px;">
                          <span>Rəsmi Mühazirə Vəsaiti</span> • <span>PDF</span> • <span>II Semestr</span>
                        </div>
                        <h4 style="margin:0 0 6px; font-size:1.1rem; font-weight:800; color:var(--text);">Riyaziyyat Fənnindən Mühazirələr Toplusu (II Semestr)</h4>
                        <p style="margin:0; font-size:0.86rem; color:var(--text-dim); line-height:1.55;">Dəqiq Elmlər FBK (FBK-09). Kompleks ədədin tərifi, qoşma kompleks ədədlər, cəbri əməllər, funksiyalar və riyazi analiz üzrə II semestr mühazirə vəsaiti.</p>
                      </div>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding-top:6px;">
                      <button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('2 ci semestr riyaziyyat.pdf', 'Riyaziyyat (II Semestr)', 'Dəqiq Elmlər FBK');">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        <span>Oxu Zalında Aç</span>
                      </button>
                    </div>
                  </div>

                  <!-- Material 4: Biologiya Mövzular (Mühazirə) -->
                  <div style="display:flex; flex-direction:column; gap:10px; padding-top:14px; border-top:1px dashed rgba(184,147,74,0.3);">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                      <div style="font-size:2.2rem; line-height:1;">🔬</div>
                      <div style="flex:1;">
                        <div style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; background:rgba(184,147,74,0.15); padding:2px 8px; border-radius:4px; margin-bottom:6px;">
                          <span>Rəsmi Mühazirə Vəsaiti</span> • <span>PDF</span>
                        </div>
                        <h4 style="margin:0 0 6px; font-size:1.1rem; font-weight:800; color:var(--text);">Biologiya Fənni Üzrə Mövzular və Mühazirələr Toplusu</h4>
                        <p style="margin:0; font-size:0.86rem; color:var(--text-dim); line-height:1.55;">Dəqiq Elmlər FBK (FBK-09, İlahə Qaraxanova). Canlılarda qidalanma, tənəffüs, ifrazat, çoxalma və hüceyrə biologiyası üzrə rəsmi mühazirə toplusu.</p>
                      </div>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding-top:6px;">
                      <button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('Biologiya mövzular.pdf', 'Biologiya Mövzular', 'Dəqiq Elmlər FBK');">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        <span>Oxu Zalında Aç</span>
                      </button>
                    </div>
                  </div>'''

if '2 ci semestr riyaziyyat.pdf' not in s:
    target_drawer_end = 'onclick="window.openDocumentReader(\'Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf\', \'Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf\', \'FBK Mühazirələr Fondu\');">\n  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>\n  <span>Oxu Zalında Aç</span>\n</button>\n                    </div>\n                  </div>'
    replacement_drawer_end = target_drawer_end + '\n\n' + fbk9_materials
    s = s.replace(target_drawer_end, replacement_drawer_end, 1)
    print("Added material cards to FBK-09 drawer")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated script.js successfully with all new items.')
