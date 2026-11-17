import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

rule = """
/* ══════════════════════════════════════════════════════════════
   DIGITAL READING ROOM ENFORCEMENT — NO DOWNLOADS
══════════════════════════════════════════════════════════════ */
.book-btn-ext,
.lib-lec-btn-dl,
.lib-lec-btn-dl-alt,
.btn-reader-ext,
#reader-open-ext {
  display: none !important;
}

.book-btn {
  width: 100% !important;
  flex: 1 1 100% !important;
  justify-content: center !important;
}

.lib-lec-btn-read {
  width: 100% !important;
  flex: 1 1 100% !important;
  justify-content: center !important;
}
"""

if 'DIGITAL READING ROOM ENFORCEMENT — NO DOWNLOADS' not in css:
    css += '\n' + rule

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('Updated style.css')

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update subtitle in library section
html = html.replace('Dərs vəsaitləri və metodik materiallar — baxış və yükləmə imkanı ilə.', 'Dərs vəsaitləri və metodik materiallar — rəqəmsal oxu zalında interaktiv baxış.')
html = html.replace('İstər daxili oxu zalında vərəqləyin, istərsə də orijinal formatda (PDF / DOCX) birbaşa yükləyin.', 'Bütün materiallar daxili rəqəmsal oxu zalında oxunaqlı şəkildə təqdim olunur.')

# Update stat card from Birbaşa Yükləmə to Rəqəmsal Oxu Zalı
old_stat = """                        <div class="lib-lec-stat-card p-4 rounded-2xl bg-slate-50 dark:bg-slate-950/60 border border-slate-900/[0.08] dark:border-white/[0.08] flex items-center gap-3">
                            <div class="lib-stat-icon">📄</div>
                            <div class="lib-stat-data">
                                <span class="lib-stat-number">DOCX</span>
                                <span class="lib-stat-label">Birbaşa Yükləmə</span>
                            </div>
                        </div>"""

new_stat = """                        <div class="lib-lec-stat-card p-4 rounded-2xl bg-slate-50 dark:bg-slate-950/60 border border-slate-900/[0.08] dark:border-white/[0.08] flex items-center gap-3">
                            <div class="lib-stat-icon">🛡️</div>
                            <div class="lib-stat-data">
                                <span class="lib-stat-number">100%</span>
                                <span class="lib-stat-label">Rəqəmsal Oxu Zalı</span>
                            </div>
                        </div>"""

html = html.replace(old_stat, new_stat)

# Hide format switcher docx button in lectures section if present
old_format_group = """                    <div class="lib-lec-format-group" id="lib-lec-format-group">
                        <button type="button" class="lib-format-btn active" data-format="all">
                            <span>Hamısı</span>
                            <span class="format-num">24</span>
                        </button>
                        <button type="button" class="lib-format-btn" data-format="pdf">
                            <span class="format-dot dot-pdf"></span>
                            <span>📕 PDF (Oxu Zalı)</span>
                            <span class="format-num">14</span>
                        </button>
                        <button type="button" class="lib-format-btn" data-format="docx">
                            <span class="format-dot dot-docx"></span>
                            <span>📘 DOCX (Word)</span>
                            <span class="format-num">10</span>
                        </button>
                    </div>"""

new_format_group = """                    <div class="lib-lec-format-group" id="lib-lec-format-group" style="display:none;">
                        <button type="button" class="lib-format-btn active" data-format="all">
                            <span>Hamısı</span>
                            <span class="format-num">24</span>
                        </button>
                    </div>"""

html = html.replace(old_format_group, new_format_group)

# Remove reader-open-ext from reader header
old_reader_act = """                <div class="book-reader-actions">
                    <a href="#" target="_blank" rel="noopener noreferrer" class="btn-reader-ext" id="reader-open-ext">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" aria-hidden="true">
                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
                            <polyline points="15 3 21 3 21 9" />
                            <line x1="10" y1="14" x2="21" y2="3" />
                        </svg>
                        <span data-i18n="reader_fullscreen_download">Tam Ekranda / Yüklə</span>
                    </a>
                    <button type="button" class="book-reader-close" id="book-reader-close" aria-label="Close">"""

new_reader_act = """                <div class="book-reader-actions">
                    <button type="button" class="book-reader-close" id="book-reader-close" aria-label="Close">"""

html = html.replace(old_reader_act, new_reader_act)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html')
