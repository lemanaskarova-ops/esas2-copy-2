import re

with open('script.js', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Update book actions in renderBooks
old_book_actions = """              <div class="book-actions">
                <button type="button" class="book-btn book-btn-preview">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                  <span>${readingRoomBtnText}</span>
                </button>
                <a href="${book.url || "#"}" target="_blank" rel="noopener noreferrer" class="book-btn-ext" title="${extBtnTitle}">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                </a>
              </div>"""

new_book_actions = """              <div class="book-actions">
                <button type="button" class="book-btn book-btn-preview" style="width:100%; justify-content:center;">
                  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
                  <span>${readingRoomBtnText}</span>
                </button>
              </div>"""

if old_book_actions in s:
    s = s.replace(old_book_actions, new_book_actions)
    print("Replaced book actions in renderBooks")
elif '<button type="button" class="book-btn book-btn-preview" style="width:100%;' in s:
    print("Book actions already updated")

# 2. Update lecture actions in renderLibraryLectures
old_lec_actions = """            <div class="lib-lec-actions">
              <button type="button" class="lib-lec-btn-read" data-open-lec="${lec.id}">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                <span>${isPdf ? "Oxu Zalında Aç" : "Məlumat və Yüklə"}</span>
              </button>
              <a href="${safeUrl}" download class="lib-lec-btn-dl" title="${lec.url} — Birbaşa Yüklə">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                <span>Yüklə</span>
              </a>
              ${lec.extraDocUrl ? `
                <a href="${encodeURI(lec.extraDocUrl)}" download class="lib-lec-btn-dl-alt" title="Alternativ DOCX Konspekti Yüklə">DOCX</a>
              ` : ""}
            </div>"""

new_lec_actions = """            <div class="lib-lec-actions">
              <button type="button" class="lib-lec-btn-read" data-open-lec="${lec.id}" style="width:100%; justify-content:center;">
                <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                <span>Oxu Zalında Aç</span>
              </button>
            </div>"""

if old_lec_actions in s:
    s = s.replace(old_lec_actions, new_lec_actions)
    print("Replaced lecture actions in renderLibraryLectures")
elif '<button type="button" class="lib-lec-btn-read" data-open-lec="${lec.id}" style="width:100%;' in s:
    print("Lecture actions already updated")

# 3. Add window.openDocumentReader and update openBookReader
reader_anchor = 'function openBookReader(book) {'
reader_replacement = """  window.openDocumentReader = function(url, title, author, cat) {
    if (typeof openBookReader === "function") {
      openBookReader({
        title_az: title || "Tədris Vəsaiti",
        author_az: author || "BDRNK Fənn Birləşməsi",
        category: cat || "Rəqəmsal Kitabxana",
        icon: "📖",
        url: url
      });
    }
  };

  function openBookReader(book) {"""

if 'window.openDocumentReader =' not in s:
    s = s.replace(reader_anchor, reader_replacement, 1)
    print("Added window.openDocumentReader")

# In openBookReader: add #toolbar=0&navpanes=0 to iframe url and hide readerOpenExt
s = s.replace(
    'readerViewport.innerHTML = `<iframe class="book-reader-iframe" src="${encodeURI(url)}" title="${title}"></iframe>`;',
    'readerViewport.innerHTML = `<iframe class="book-reader-iframe" src="${encodeURI(url)}#toolbar=0&navpanes=0" title="${title}"></iframe>`;'
)
s = s.replace(
    'if (readerOpenExt) readerOpenExt.href = url;',
    'if (readerOpenExt) readerOpenExt.style.display = "none";'
)

# 4. Update FBK chips (lines 8320-8480)
# Replace <a href="..." target="_blank" download="..." class="fbk-chip ..."> with button calling window.openDocumentReader
def replace_fbk_chip_a(m):
    url = m.group(1)
    icon = m.group(2)
    label = m.group(3)
    return f'<button type="button" class="fbk-chip fbk-chip-has-doc" title="{label} — Oxu Zalında Aç" onclick="event.stopPropagation(); window.openDocumentReader(\'{url}\', \'{label}\', \'FBK Tədris Vəsaiti\');"><span class="chip-doc-icon">{icon}</span> <span>{label}</span> <span class="fbk-chip-doc-badge">📖 Oxu Zalı</span></button>'

# Pattern for return `<a href="FILE" ... class="fbk-chip ..."><span class="chip-doc-icon">ICON</span> <span>${d}</span> <span class="fbk-chip-doc-badge">...</span></a>`;
s = re.sub(
    r'<a\s+href="([^"]+)"(?:\s+target="_blank")?\s+download="[^"]*"\s+class="fbk-chip fbk-chip-has-doc"[^>]*><span class="chip-doc-icon">([^<]*)<\/span>\s*<span>([^<]*)<\/span>\s*<span class="fbk-chip-doc-badge">[^<]*<\/span><\/a>',
    replace_fbk_chip_a,
    s
)

# 5. Update FBK drawer material download buttons (lines 8490-8895)
def replace_fbk_drawer_btn(m):
    url = m.group(1)
    return f'''<button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('{url}', '{url}', 'FBK Mühazirələr Fondu');">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
  <span>Oxu Zalında Aç</span>
</button>'''

s = re.sub(
    r'<a\s+href="([^"]+)"(?:\s+target="_blank")?\s+download="[^"]*"\s+class="fbk-mat-download-btn"[\s\S]*?<\/a>',
    replace_fbk_drawer_btn,
    s
)

# 6. Update quick search catalog actions:
catalog_replacements = [
    (
        'link.href = "azdilifb.pdf";\n        link.download = "azdilifb.pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("azdilifb.pdf", "Azərbaycan Dili Fənnindən Mühazirələr Toplusu", "Müəllimə: Məmmədova Vüsalə (FBK-06)", "azer_dili");'
    ),
    (
        'link.href = "edebiyyatfb.pdf";\n        link.download = "edebiyyatfb.pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("edebiyyatfb.pdf", "Ədəbiyyat Fənnindən Mühazirələr Toplusu", "Azərbaycan dili və ədəbiyyat FBK (Ziba Səfərova)", "azer_dili");'
    ),
    (
        'link.href = "aztarixifb.pdf";\n        link.download = "aztarixifb.pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("aztarixifb.pdf", "Azərbaycan Tarixi Fənnindən Mühazirələr Toplusu", "Humanitar və İctimai Elmlər FBK (Səidə Quliyeva)", "tarix");'
    ),
    (
        'link.href = "umtarixfb.pdf";\n        link.download = "umtarixfb.pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("umtarixfb.pdf", "Ümumi Tarix Fənnindən Mühazirələr Toplusu", "Humanitar və İctimai Elmlər FBK (Səidə Quliyeva)", "tarix");'
    ),
    (
        'link.href = "yeni mühazirələr.pdf";\n        link.download = "yeni mühazirələr.pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("yeni mühazirələr.pdf", "Hüququn Əsasları Fənnindən Mühazirələr Toplusu", "Humanitar və İctimai Elmlər FBK", "tarix");'
    ),
    (
        'link.href = "KOMMUNİKASİYA DF 2 (1).pdf";\n        link.download = "KOMMUNİKASİYA DF 2 (1).pdf";\n        document.body.appendChild(link);\n        link.click();\n        document.body.removeChild(link);',
        'window.openDocumentReader("KOMMUNİKASİYA DF 2 (1).pdf", "İşgüzar və Akademik Kommunikasiya", "Natəvan Hüseynova", "azer_dili");'
    )
]

for old_block, new_block in catalog_replacements:
    if old_block in s:
        s = s.replace(old_block, new_block)
        print("Replaced catalog action block")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated script.js successfully.')
