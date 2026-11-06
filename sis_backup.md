
## 1. HTML Qismi (index.html üçün)
\`\`\`html
<!-- ═══════════════ STUDENT PORTAL (SIS) ═══════════════ -->
<section class="section" id="sis">
    <div class="section-inner reveal">
        <span class="section-badge" data-i18n="sis_badge">Portal</span>
        <h2 class="section-title" data-i18n="sis_title">
            Tələbə Məlumat Sistemi
        </h2>
        <p class="section-desc" data-i18n="sis_desc">
            İmtahan nəticələri, davamiyyət və performans göstəricilərini izləyin.
        </p>

        <!-- LOGIN -->
        <div class="sis-login-card" id="sis-login">
            <div class="sis-float-icon sis-float-1" style="--rot: -15deg">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="1.5">
                    <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                    <path d="M6 12v5c3 3 9 3 12 0v-5" />
                </svg>
            </div>
            <div class="sis-float-icon sis-float-2" style="--rot: 15deg">
                <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                    stroke-width="1.5">
                    <path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20" />
                    <path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z" />
                </svg>
            </div>
            <div class="sis-login-inner">
                <div class="sis-login-icon">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                        stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
                        <path d="M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4" />
                        <polyline points="10 17 15 12 10 7" />
                        <line x1="15" y1="12" x2="3" y2="12" />
                    </svg>
                </div>
                <h3 data-i18n="sis_login_title">Daxil olun</h3>
                <p class="sis-login-hint" data-i18n="sis_login_hint">
                    Tələbə ID nömrənizi daxil edin
                </p>
                <form id="sis-form" autocomplete="off">
                    <div class="sis-input-group">
                        <input type="text" id="sis-id" class="sis-input" placeholder="STU01" required />
                        <button type="submit" class="btn btn-primary btn-sis" data-i18n="sis_login_btn">
                            Daxil ol
                        </button>
                    </div>
                    <p class="sis-error" id="sis-error"></p>
                    <p class="sis-demo-hint">
                        Demo: STU01 (Qrup 1313A), STU002 (Qrup 1313B)
                    </p>
                </form>
            </div>
        </div>

        <!-- DASHBOARD (Group List) -->
        <div class="sis-dashboard" id="sis-dashboard" style="display: none">
            <div class="dash-header">
                <div class="dash-student-info">
                    <div class="dash-avatar" id="dash-avatar">
                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                            stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
                            <circle cx="9" cy="7" r="4"></circle>
                            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
                            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
                        </svg>
                    </div>
                    <div>
                        <p class="dash-greeting" id="dash-greeting" data-i18n="dash_greeting">
                            Tədris Hesabatı
                        </p>
                        <h3 class="dash-name" id="dash-group-name"></h3>
                    </div>
                </div>
                <div>
                    <button class="btn btn-outline btn-sm" id="sis-logout" data-i18n="sis_logout">
                        Çıxış
                    </button>
                </div>
            </div>

            <div class="semester-tabs">
                <button class="semester-tab active" data-semester="semester1" data-i18n="sem1">
                    1-ci Semestr
                </button>
                <button class="semester-tab" data-semester="semester2" data-i18n="sem2">
                    2-ci Semestr
                </button>
            </div>

            <div class="subject-filters" id="subject-filters">
                <!-- Subject buttons injected by JS -->
            </div>

            <div class="group-table-wrap">
                <table class="group-table" id="group-table">
                    <thead>
                        <tr>
                            <th data-i18n="th_n">N</th>
                            <th data-i18n="th_name">Ad və Soyad</th>
                            <th data-i18n="th_attendance">Davamiyyət</th>
                            <th data-i18n="th_exam">İmtahan</th>
                            <th data-i18n="th_final">Yekun</th>
                            <th data-i18n="th_grade">Qiymət</th>
                        </tr>
                    </thead>
                    <tbody id="group-table-body">
                        <!-- Injected by JS -->
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</section>
\`\`\`

## 2. JavaScript Məntiqi (script.js üçün)
\`\`\`javascript
/** STUDENT INFORMATION SYSTEM MOCK DATA (Group Mode — Semester Logic) */
const groupDb = {
  // BURA SİZİN ƏVVƏLKİ 1313A VƏ 1313B TƏLƏBƏ MƏLUMATLARINIZ DAXIL OLACAQ (script.js faylından sildiyimiz siyahı)
};

let currentGroup = null;

function initSISEngine() {
  const form = document.getElementById("sis-form");
  const input = document.getElementById("sis-id");
  const error = document.getElementById("sis-error");
  const loginCard = document.getElementById("sis-login");
  const dashboard = document.getElementById("sis-dashboard");
  const logoutBtn = document.getElementById("sis-logout");

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const id = input.value.trim().toUpperCase();

    let groupId = id;
    if (id === "STU01" || id === "STU001") groupId = "1313A";
    if (id === "STU02" || id === "STU002") groupId = "1313B";

    if (groupDb[groupId]) {
      error.textContent = "";
      currentGroup = groupDb[groupId];
      loginCard.style.display = "none";
      dashboard.style.display = "block";
      renderGroupDashboard(currentGroup);
    } else {
      error.textContent = "Qrup və ya Tələbə ID tapılmadı.";
    }
  });

  logoutBtn.addEventListener("click", () => {
    currentGroup = null;
    input.value = "";
    dashboard.style.display = "none";
    loginCard.style.display = "block";
  });
}

function renderGroupDashboard(group, semesterKey, subjectName) {
  /* Dashboard render funksiyası (script.js-dən silindi) */
}

function getGradeFromTotal(total) {
  if (total >= 90) return { letter: "Əla", cls: "grade-a" };
  if (total >= 70) return { letter: "Yaxşı", cls: "grade-b" };
  if (total >= 50) return { letter: "Kafi", cls: "grade-c" };
  return { letter: "Qeyri-kafi", cls: "grade-d" };
}
\`\`\`
