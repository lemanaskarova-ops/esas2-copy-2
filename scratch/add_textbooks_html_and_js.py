import re

# ========================================================
# 2. UPDATE index.html
# ========================================================
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Insert textbooks section right below science-ceremony-banner
tb_html_markup = '''                    <!-- ═══════════════ RƏSMİ DƏRSLİK VƏ DƏRS VƏSAİTLƏRİ REYESTRİ (2025/2026 - 2026/2027) ═══════════════ -->
                    <div class="science-textbooks-registry p-6 sm:p-8 rounded-3xl bg-white/85 dark:bg-[#112038]/85 border border-slate-900/[0.08] dark:border-white/[0.08] shadow-apple space-y-6" id="science-textbooks-section">
                        <!-- Header with official accreditation badge -->
                        <div class="science-tb-header-wrap">
                            <div class="flex flex-wrap items-center justify-between gap-3">
                                <span class="science-tb-kicker" data-i18n="science_tb_kicker">
                                    🏛️ RƏSMİ QEYDİYYAT REYESTRİ · 2025/2026 – 2026/2027
                                </span>
                                <div class="science-tb-view-switchers flex items-center gap-1.5 p-1 rounded-xl bg-slate-100 dark:bg-slate-900/60 border border-slate-200 dark:border-white/10" role="radiogroup" aria-label="Reyestr görünüşü">
                                    <button type="button" class="science-tb-view-btn active px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 bg-white dark:bg-[#0a2240] text-slate-900 dark:text-white shadow-xs" data-tb-view="cards">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>
                                        <span data-i18n="science_tb_view_cards">Kartlar</span>
                                    </button>
                                    <button type="button" class="science-tb-view-btn px-3 py-1.5 rounded-lg text-xs font-bold transition flex items-center gap-1.5 text-slate-600 dark:text-slate-400 hover:text-slate-900 dark:hover:text-white" data-tb-view="table">
                                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M3 3h18v18H3zM3 9h18M3 15h18M9 3v18M15 3v18"></path></svg>
                                        <span data-i18n="science_tb_view_table">Rəsmi Cədvəl</span>
                                    </button>
                                </div>
                            </div>
                            <h3 class="science-tb-title" data-i18n="science_tb_title">
                                Kollec Əməkdaşlarının Nəşr Olunan Dərslik və Dərs Vəsaitləri
                            </h3>
                            <p class="science-tb-desc" data-i18n="science_tb_desc">
                                Azərbaycan Respublikası Elm və Təhsil Nazirliyinin müvafiq qrifləri ilə təsdiq olunmuş və Bakı Dövlət Rabitə və Nəqliyyat Kolleci əməkdaşları tərəfindən 2025/2026 və 2026/2027-ci tədris illərində nəşr edilmiş rəsmi dərsliklər və tədris vəsaitlərinin tam dövlət reyestri.
                            </p>
                        </div>

                        <!-- Stat strip -->
                        <div class="science-tb-stat-strip">
                            <div class="science-tb-stat-item">
                                <span class="science-tb-stat-icon">📘</span>
                                <div>
                                    <div class="science-tb-stat-val">4 Dərslik</div>
                                    <div class="science-tb-stat-lbl" data-i18n="science_tb_stat1">Nazirlik Qrifi İlə</div>
                                </div>
                            </div>
                            <div class="science-tb-stat-item">
                                <span class="science-tb-stat-icon">📗</span>
                                <div>
                                    <div class="science-tb-stat-val">4 Dərs Vəsaiti</div>
                                    <div class="science-tb-stat-lbl" data-i18n="science_tb_stat2">Tədris-Metodik Vəsait</div>
                                </div>
                            </div>
                            <div class="science-tb-stat-item">
                                <span class="science-tb-stat-icon">👥</span>
                                <div>
                                    <div class="science-tb-stat-val">11 Müəllif</div>
                                    <div class="science-tb-stat-lbl" data-i18n="science_tb_stat3">Rəhbərlik & Müəllimlər</div>
                                </div>
                            </div>
                            <div class="science-tb-stat-item">
                                <span class="science-tb-stat-icon">📅</span>
                                <div>
                                    <div class="science-tb-stat-val">2025 – 2027</div>
                                    <div class="science-tb-stat-lbl" data-i18n="science_tb_stat4">Tədris İlləri Nəşri</div>
                                </div>
                            </div>
                        </div>

                        <!-- Filter row -->
                        <div class="science-tb-controls">
                            <div class="science-tb-filters" role="tablist">
                                <button type="button" class="science-tb-filter-btn active" data-tb-filter="all">
                                    <span>🌟</span>
                                    <span data-i18n="filter_all">Hamısı</span>
                                    <span class="science-tab-count">8</span>
                                </button>
                                <button type="button" class="science-tb-filter-btn" data-tb-filter="derslik">
                                    <span>📘</span>
                                    <span data-i18n="science_tb_filter_derslik">Qrifli Dərsliklər</span>
                                    <span class="science-tab-count">4</span>
                                </button>
                                <button type="button" class="science-tb-filter-btn" data-tb-filter="vesait">
                                    <span>📗</span>
                                    <span data-i18n="science_tb_filter_vesait">Dərs Vəsaitləri</span>
                                    <span class="science-tab-count">4</span>
                                </button>
                            </div>
                            <div class="text-xs font-semibold text-slate-500 dark:text-slate-400">
                                <span>🏛️ BDRNK Publik Hüquqi Şəxs</span>
                            </div>
                        </div>

                        <!-- Cards Grid View -->
                        <div class="science-tb-cards-grid" id="science-tb-cards-grid">
                            <!-- Populated dynamically via script.js -->
                        </div>

                        <!-- Official Table View -->
                        <div class="science-tb-table-wrap" id="science-tb-table-wrap" style="display: none; overflow-x: auto;">
                            <!-- Populated dynamically via script.js -->
                        </div>
                    </div>'''

ceremony_end_marker = '''                            <p class="science-ceremony-text" data-i18n="science_ceremony_p">
                                Direktor Səbuhi Qurbanovun təşəbbüsü ilə pedaqoji heyətin xarici arenada təmsil
                                olunması, impakt faktorlu və Index Copernicus, ERIH PLUS indeksli nəşrlərdə dərc olunan
                                araşdırmaları yüksək qiymətləndirilmişdir.
                            </p>
                        </div>
                    </div>'''

assert ceremony_end_marker in html, "ceremony_end_marker not found in index.html"
html = html.replace(ceremony_end_marker, ceremony_end_marker + "\n\n" + tb_html_markup, 1)

# Add "Dərslik və Dərs Vəsaitləri (8)" tab in science-tabs
old_science_tabs = '''                        <div class="science-tabs flex flex-wrap gap-2" role="tablist">
                            <button class="science-tab-btn active" data-filter="all" role="tab">
                                <span data-i18n="science_tab_all">Bütün Nəşrlər (23)</span>
                            </button>'''

new_science_tabs = '''                        <div class="science-tabs flex flex-wrap gap-2" role="tablist">
                            <button class="science-tab-btn active" data-filter="all" role="tab">
                                <span data-i18n="science_tab_all">Bütün Nəşrlər (23)</span>
                            </button>
                            <button class="science-tab-btn" data-filter="textbooks" role="tab" id="science-tab-tb-btn">
                                <span data-i18n="science_tab_textbooks">📚 Dərslik və Dərs Vəsaitləri (8)</span>
                            </button>'''

assert old_science_tabs in html, "old_science_tabs not found in index.html"
html = html.replace(old_science_tabs, new_science_tabs, 1)

# Bump script tag version
html = re.sub(r'script\.js\?v=[0-9_]+', 'script.js?v=20261119_1115', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html updated successfully with textbooks section!")
