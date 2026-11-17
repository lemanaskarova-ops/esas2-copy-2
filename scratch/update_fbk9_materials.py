import re

with open('script.js', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. Add chips for FBK-09 in grid cards
old_chip_grid = '''        if (fbk.id === "fbk-9" && (d.includes("ƏMM") || d.includes("Ətraf Mühit") || d.includes("Ekologiya"))) {'''
new_chip_grid = '''        if (fbk.id === "fbk-9" && (d === "Riyaziyyat" || d.includes("Riyaziyyat"))) {
          return `<button type="button" class="fbk-chip fbk-chip-has-doc" title="${d} — Oxu Zalında Aç" onclick="event.stopPropagation(); window.openDocumentReader('1 ci semestr riyaziyyat.pdf', '${d} (I Semestr Mühazirələri)', 'Dəqiq Elmlər FBK');"><span class="chip-doc-icon">📐</span> <span>${d}</span> <span class="fbk-chip-doc-badge">📖 Oxu Zalı</span></button>`;
        }
        if (fbk.id === "fbk-9" && d.includes("Biologiya")) {
          return `<button type="button" class="fbk-chip fbk-chip-has-doc" title="${d} — Oxu Zalında Aç" onclick="event.stopPropagation(); window.openDocumentReader('Biologiya mövzular.pdf', '${d}', 'Dəqiq Elmlər FBK');"><span class="chip-doc-icon">🔬</span> <span>${d}</span> <span class="fbk-chip-doc-badge">📖 Oxu Zalı</span></button>`;
        }
        if (fbk.id === "fbk-9" && (d.includes("ƏMM") || d.includes("Ətraf Mühit") || d.includes("Ekologiya"))) {'''

if old_chip_grid in s:
    s = s.replace(old_chip_grid, new_chip_grid, 1)
    print("Added chips to FBK-09 grid")

# 2. Add chips for FBK-09 in drawer/modal
old_chip_modal = '''            if (fbk.id === "fbk-9" && (d.includes("ƏMM") || d.includes("Ətraf Mühit") || d.includes("Ekologiya"))) {'''
new_chip_modal = '''            if (fbk.id === "fbk-9" && (d === "Riyaziyyat" || d.includes("Riyaziyyat"))) {
              return `<button type="button" class="fbk-chip fbk-chip-has-doc" style="display:inline-flex; align-items:center; gap:6px; background:rgba(184,147,74,0.18); border:1px solid var(--gold); color:var(--text); text-decoration:none; padding:6px 14px; border-radius:12px; font-weight:700; cursor:pointer;" onclick="event.stopPropagation(); window.openDocumentReader('1 ci semestr riyaziyyat.pdf', '📐 ${d} (I Semestr)', 'FBK Tədris Vəsaiti');"><span>📐 ${d}</span><span style="font-size:0.75rem; background:var(--gold); color:#111; padding:2px 6px; border-radius:6px; font-weight:800;">📖 Oxu Zalı</span></button>`;
            }
            if (fbk.id === "fbk-9" && d.includes("Biologiya")) {
              return `<button type="button" class="fbk-chip fbk-chip-has-doc" style="display:inline-flex; align-items:center; gap:6px; background:rgba(184,147,74,0.18); border:1px solid var(--gold); color:var(--text); text-decoration:none; padding:6px 14px; border-radius:12px; font-weight:700; cursor:pointer;" onclick="event.stopPropagation(); window.openDocumentReader('Biologiya mövzular.pdf', '🔬 ${d}', 'FBK Tədris Vəsaiti');"><span>🔬 ${d}</span><span style="font-size:0.75rem; background:var(--gold); color:#111; padding:2px 6px; border-radius:6px; font-weight:800;">📖 Oxu Zalı</span></button>`;
            }
            if (fbk.id === "fbk-9" && (d.includes("ƏMM") || d.includes("Ətraf Mühit") || d.includes("Ekologiya"))) {'''

if old_chip_modal in s:
    s = s.replace(old_chip_modal, new_chip_modal, 1)
    print("Added chips to FBK-09 modal")

# 3. Add materials inside FBK-09 drawer
fbk9_math_materials = '''                  <!-- Material 3: Riyaziyyat I Semestr (Mühazirə) -->
                  <div style="display:flex; flex-direction:column; gap:10px; padding-top:14px; border-top:1px dashed rgba(184,147,74,0.3);">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                      <div style="font-size:2.2rem; line-height:1;">📐</div>
                      <div style="flex:1;">
                        <div style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; background:rgba(184,147,74,0.15); padding:2px 8px; border-radius:4px; margin-bottom:6px;">
                          <span>Rəsmi Mühazirə Vəsaiti</span> • <span>PDF</span> • <span>I Semestr</span> • <span>866 KB</span>
                        </div>
                        <h4 style="margin:0 0 6px; font-size:1.1rem; font-weight:800; color:var(--text);">Riyaziyyat Fənnindən Mühazirələr Toplusu (I Semestr)</h4>
                        <p style="margin:0; font-size:0.86rem; color:var(--text-dim); line-height:1.55;">Dəqiq Elmlər FBK (FBK-09). Ədədi funksiyanın tərifi, təyin oblastı, qiymətlər çoxluğu, funksiyaların qrafikləri və analizi üzrə rəsmi I semestr mühazirə vəsaiti.</p>
                      </div>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding-top:6px;">
                      <button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('1 ci semestr riyaziyyat.pdf', 'Riyaziyyat (I Semestr Mühazirələri)', 'Dəqiq Elmlər FBK');">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        <span>Oxu Zalında Aç</span>
                      </button>
                    </div>
                  </div>

                  <!-- Material 4: Riyaziyyat II Semestr (Mühazirə) -->
                  <div style="display:flex; flex-direction:column; gap:10px; padding-top:14px; border-top:1px dashed rgba(184,147,74,0.3);">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                      <div style="font-size:2.2rem; line-height:1;">📐</div>
                      <div style="flex:1;">
                        <div style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; background:rgba(184,147,74,0.15); padding:2px 8px; border-radius:4px; margin-bottom:6px;">
                          <span>Rəsmi Mühazirə Vəsaiti</span> • <span>PDF</span> • <span>II Semestr</span> • <span>706 KB</span>
                        </div>
                        <h4 style="margin:0 0 6px; font-size:1.1rem; font-weight:800; color:var(--text);">Riyaziyyat Fənnindən Mühazirələr Toplusu (II Semestr)</h4>
                        <p style="margin:0; font-size:0.86rem; color:var(--text-dim); line-height:1.55;">Dəqiq Elmlər FBK (FBK-09). Kompleks ədədin tərifi, qoşma kompleks ədədlər, cəbri əməllər və riyazi analiz üzrə rəsmi II semestr mühazirə vəsaiti.</p>
                      </div>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding-top:6px;">
                      <button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('2 ci semestr riyaziyyat.pdf', 'Riyaziyyat (II Semestr Mühazirələri)', 'Dəqiq Elmlər FBK');">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        <span>Oxu Zalında Aç</span>
                      </button>
                    </div>
                  </div>

                  <!-- Material 5: Ali Riyaziyyatın Əsasları (2025) -->
                  <div style="display:flex; flex-direction:column; gap:10px; padding-top:14px; border-top:1px dashed rgba(184,147,74,0.3);">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                      <div style="font-size:2.2rem; line-height:1;">📊</div>
                      <div style="flex:1;">
                        <div style="display:inline-flex; align-items:center; gap:6px; font-family:var(--font-mono); font-size:0.75rem; color:var(--gold-light); font-weight:700; text-transform:uppercase; letter-spacing:0.05em; background:rgba(184,147,74,0.15); padding:2px 8px; border-radius:4px; margin-bottom:6px;">
                          <span>Rəsmi Dərs Vəsaiti</span> • <span>PDF</span> • <span>6.5 MB</span>
                        </div>
                        <h4 style="margin:0 0 6px; font-size:1.1rem; font-weight:800; color:var(--text);">Ali Riyaziyyatın Əsasları — Mühazirələr Toplusu</h4>
                        <p style="margin:0; font-size:0.86rem; color:var(--text-dim); line-height:1.55;">Dəqiq Elmlər FBK (FBK-09). Matrislər və determinantlar, Kramer və Qauss üsulları, ikitərtibli əyrilər, limit, müəyyən inteqral və diferensial tənliklər üzrə 15 mövzuluq rəsmi mühazirələr toplusu.</p>
                      </div>
                    </div>
                    <div style="display:flex; flex-wrap:wrap; gap:10px; align-items:center; padding-top:6px;">
                      <button type="button" class="fbk-mat-download-btn" style="display:inline-flex; align-items:center; gap:8px; background:var(--gold); color:#111; padding:9px 18px; border-radius:10px; font-weight:700; font-size:0.88rem; border:none; cursor:pointer; box-shadow:0 4px 12px rgba(184,147,74,0.3); transition:all 0.2s ease;" onclick="window.openDocumentReader('ALI RIY muhazire (1).pdf', 'Ali Riyaziyyatın Əsasları', 'Dəqiq Elmlər FBK');">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
                        <span>Oxu Zalında Aç</span>
                      </button>
                    </div>
                  </div>'''

target_anchor = '''onclick="window.openDocumentReader('Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf', 'Həyat fəaliyyətinin təhlükəsizliyi. Alidə Mahmudova, Azadə Quliyeva.pdf', 'FBK Mühazirələr Fondu');">
  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
  <span>Oxu Zalında Aç</span>
</button>
                    </div>
                  </div>'''

if target_anchor in s and '1 ci semestr riyaziyyat.pdf\', \'Riyaziyyat (I Semestr Mühazirələri)' not in s:
    s = s.replace(target_anchor, target_anchor + '\n\n' + fbk9_math_materials, 1)
    print("Added math materials to FBK-09 drawer")

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(s)

print('Updated script.js with 1 ci semestr riyaziyyat and FBK-09 materials.')
