import re

with open("index.html", "r", encoding="utf-8") as f:
    index_html = f.read()

# 1. Update honor student filter tabs
old_honor_tabs = '''                        <!-- Filter Tabs -->
                        <div class="grad-honors-tabs flex flex-wrap gap-2" role="tablist"
                            aria-label="Fəxri tələbə kateqoriyaları">
                            <button type="button"
                                class="honor-tab-btn active px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="all" role="tab" aria-selected="true">
                                <span class="tab-emoji">🌟</span>
                                <span data-i18n="fame_tab_all">Hamısı</span>
                                <span class="honor-tab-count" id="honor-count-all">1</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="it-robotics" role="tab" aria-selected="false">
                                <span class="tab-emoji">🤖</span>
                                <span data-i18n="fame_tab_it">İKT & Robototexnika</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="international" role="tab" aria-selected="false">
                                <span class="tab-emoji">🌍</span>
                                <span data-i18n="fame_tab_champ">Beynəlxalq Çempionatlar</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="youth" role="tab" aria-selected="false">
                                <span class="tab-emoji">🎖️</span>
                                <span data-i18n="fame_tab_youth">İlin Gənci & Sosial İnklüzivlik</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                        </div>'''

new_honor_tabs = '''                        <!-- Filter Tabs -->
                        <div class="grad-honors-tabs flex flex-wrap gap-2" role="tablist"
                            aria-label="Fəxri tələbə kateqoriyaları">
                            <button type="button"
                                class="honor-tab-btn active px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="all" role="tab" aria-selected="true">
                                <span class="tab-emoji">🌟</span>
                                <span data-i18n="fame_tab_all">Hamısı</span>
                                <span class="honor-tab-count" id="honor-count-all">4</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="it-robotics" role="tab" aria-selected="false">
                                <span class="tab-emoji">🤖</span>
                                <span data-i18n="fame_tab_it">İKT & Robototexnika</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="sports" role="tab" aria-selected="false">
                                <span class="tab-emoji">🥋</span>
                                <span data-i18n="fame_tab_sports">İdman & Döyüş Növləri</span>
                                <span class="honor-tab-count">2</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="arts" role="tab" aria-selected="false">
                                <span class="tab-emoji">💃</span>
                                <span data-i18n="fame_tab_arts">İncəsənət & Rəqs</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                            <button type="button"
                                class="honor-tab-btn px-4 py-2 rounded-full text-xs sm:text-sm font-semibold border border-slate-900/10 dark:border-white/10 bg-white dark:bg-[#112038] hover:border-[#0a2240] dark:hover:border-[#c8a45d] transition cursor-pointer"
                                data-honor-filter="youth" role="tab" aria-selected="false">
                                <span class="tab-emoji">🎖️</span>
                                <span data-i18n="fame_tab_youth">İlin Gənci & Sosial İnklüzivlik</span>
                                <span class="honor-tab-count">1</span>
                            </button>
                        </div>'''

assert old_honor_tabs in index_html, "old_honor_tabs not found in index.html"
index_html = index_html.replace(old_honor_tabs, new_honor_tabs, 1)

# 2. Update cert stats cards
index_html = index_html.replace(
    '<div class="cert-stat-val" data-i18n="cert_stat_gold_val">1 Qızıl</div>',
    '<div class="cert-stat-val" data-i18n="cert_stat_gold_val">10 Qızıl</div>',
    1
)
index_html = index_html.replace(
    '<div class="cert-stat-val" data-i18n="cert_stat_silver_val">6 Gümüş</div>',
    '<div class="cert-stat-val" data-i18n="cert_stat_silver_val">7 Gümüş</div>',
    1
)
index_html = index_html.replace(
    '<div class="cert-stat-val" data-i18n="cert_stat_total_val">13 Sənəd</div>',
    '<div class="cert-stat-val" data-i18n="cert_stat_total_val">24 Sənəd</div>',
    1
)

# 3. Update cert filters group
old_cert_filters_group = '''                        <div class="cert-filters-group">
                            <button type="button" class="cert-filter-btn active" data-cert-cat="all">
                                <span data-i18n="cert_filter_all">Hamısı</span>
                                <span class="cert-btn-count">13</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="respublika">
                                <span data-i18n="cert_filter_respublika">Respublika Birinciliyi</span>
                                <span class="cert-btn-count">4</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="turnir">
                                <span data-i18n="cert_filter_turnir">Rayon Turnirləri</span>
                                <span class="cert-btn-count">8</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="fexri">
                                <span data-i18n="cert_filter_fexri">Fəxri Fərman</span>
                                <span class="cert-btn-count">1</span>
                            </button>
                        </div>'''

new_cert_filters_group = '''                        <div class="cert-filters-group">
                            <button type="button" class="cert-filter-btn active" data-cert-cat="all">
                                <span data-i18n="cert_filter_all">Hamısı</span>
                                <span class="cert-btn-count">24</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="respublika">
                                <span data-i18n="cert_filter_respublika">Respublika Birinciliyi</span>
                                <span class="cert-btn-count">10</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="turnir">
                                <span data-i18n="cert_filter_turnir">Turnirlər & Çempionatlar</span>
                                <span class="cert-btn-count">13</span>
                            </button>
                            <button type="button" class="cert-filter-btn" data-cert-cat="fexri">
                                <span data-i18n="cert_filter_fexri">Fəxri Fərman</span>
                                <span class="cert-btn-count">1</span>
                            </button>
                        </div>'''

assert old_cert_filters_group in index_html, "old_cert_filters_group not found in index.html"
index_html = index_html.replace(old_cert_filters_group, new_cert_filters_group, 1)

# 4. Update year chips
old_year_chips = '''                            <div class="cert-year-chips">
                                <button type="button" class="cert-year-chip active" data-cert-year="all"
                                    data-i18n="cert_year_all">Bütün İllər</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2024">2024</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2023">2023</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2022">2022</button>
                            </div>'''

new_year_chips = '''                            <div class="cert-year-chips">
                                <button type="button" class="cert-year-chip active" data-cert-year="all"
                                    data-i18n="cert_year_all">Bütün İllər</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2026">2026</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2025">2025</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2024">2024</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2023">2023</button>
                                <button type="button" class="cert-year-chip" data-cert-year="2022">2022</button>
                            </div>'''

assert old_year_chips in index_html, "old_year_chips not found in index.html"
index_html = index_html.replace(old_year_chips, new_year_chips, 1)

# 5. Update script tag version
index_html = re.sub(r'script\.js\?v=[0-9_]+', 'script.js?v=20261119_1055', index_html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(index_html)

print("index.html updated successfully!")
