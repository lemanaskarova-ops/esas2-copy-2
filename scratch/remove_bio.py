# -*- coding: utf-8 -*-
import os, re

base_dir = '/Users/konul/Documents/esas2 copy 2'
html_path = os.path.join(base_dir, 'index.html')
js_path = os.path.join(base_dir, 'script.js')
backup_js_path = os.path.join(base_dir, 'scratch/script_working_backup.js')

# 1. UPDATE index.html
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# a) Remove about-director-bio-btn
btn_about_pattern = r'\s*<button type="button" class="quote-bio-btn" id="about-director-bio-btn"[\s\S]*?</button>'
html, n1 = re.subn(btn_about_pattern, '', html)
print(f'Removed about-director-bio-btn: {n1}')

# b) Remove science-director-bio-btn
btn_science_pattern = r'\s*<button type="button" class="science-btn-bio" id="science-director-bio-btn"[\s\S]*?</button>'
html, n2 = re.subn(btn_science_pattern, '', html)
print(f'Removed science-director-bio-btn: {n2}')

# c) Remove #director-bio-modal
start_idx = html.find('id="director-bio-modal"')
if start_idx != -1:
    comment_idx = html.rfind('<!-- ═══ DIRECTOR SƏBUHİ QURBANOV', 0, start_idx)
    start_pos = comment_idx if comment_idx != -1 else html.rfind('<div class="bio-modal-backdrop"', 0, start_idx)
    
    next_modal_idx = html.find('id="library-fund-modal"', start_idx)
    end_comment = html.rfind('<!-- ═══ OFFICIAL LIBRARY FUND', start_idx, next_modal_idx)
    end_pos = end_comment if end_comment != -1 else html.rfind('<div class="lib-fund-backdrop"', start_idx, next_modal_idx)
    
    removed_chunk = html[start_pos:end_pos]
    print(f'Modal chunk length to remove: {len(removed_chunk)}')
    html = html[:start_pos] + '\n\n    ' + html[end_pos:]
    print('Removed #director-bio-modal markup successfully.')

# Bump cache version in index.html
html = re.sub(r'script\.js\?v=[^\"]+', 'script.js?v=20261106_37', html)
html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=20261106_37', html)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. UPDATE script.js
with open(js_path, 'r', encoding='utf-8') as f:
    js = f.read()

# a) Remove action: "director_bio" from f2_director
old_f2 = '''      features_ru: ["Кабинет директора", "Приемная комната", "Стол для совещаний"],
      wing_az: "Mərkəzi qanad", wing_en: "Central Wing", wing_ru: "Центральное крыло",
      action: "director_bio"
    }'''
new_f2 = '''      features_ru: ["Кабинет директора", "Приемная комната", "Стол для совещаний"],
      wing_az: "Mərkəzi qanad", wing_en: "Central Wing", wing_ru: "Центральное крыло"
    }'''
if old_f2 in js:
    js = js.replace(old_f2, new_f2)
    print('Removed action: director_bio from f2_director.')

# b) In renderRooms: remove else if (room.action === "director_bio")
room_bio_action = '''      } else if (room.action === "director_bio") {
        actionsHtml = `
          <div class="room-card-actions">
            <button type="button" class="room-card-btn room-card-btn-action" data-action="director_bio">
              ${btnBioText}
            </button>
          </div>
        `;'''
if room_bio_action in js:
    js = js.replace(room_bio_action, '')
    print('Removed director_bio action button template from renderRooms.')

# c) In renderRooms: remove bioBtn click listener
room_bio_listener = '''      const bioBtn = card.querySelector('[data-action="director_bio"]');
      if (bioBtn) {
        bioBtn.addEventListener("click", (e) => {
          e.stopPropagation();
          if (typeof window.openDirectorBioModal === "function") {
            window.openDirectorBioModal();
          }
        });
      }'''
if room_bio_listener in js:
    js = js.replace(room_bio_listener, '')
    print('Removed director_bio click listener from renderRooms.')

# d) In tree render: remove tree-director-bio-btn
tree_btn = '''            <button type="button" class="tree-director-bio-pill-btn" id="tree-director-bio-btn" title="Rəsmi Bioqrafiyanı Oxu">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              <span>Rəsmi Bioqrafiya və Qeydlər</span>
            </button>'''
if tree_btn in js:
    js = js.replace(tree_btn, '')
    print('Removed tree-director-bio-btn from structure tree.')

# e) In person modal: remove person-director-bio-btn
person_btn = '''          ${person.id === "1" ? `
            <button type="button" class="person-director-bio-btn" id="person-director-bio-btn">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>
              <span>Rəsmi Bioqrafiya və Təəssüratlar (Tam Oxu Rejimi)</span>
            </button>
          ` : ""}'''
if person_btn in js:
    js = js.replace(person_btn, '')
    print('Removed person-director-bio-btn from person modal.')

# f) Remove initDirectorBioModule IIFE
init_bio_start = js.find('DIRECTOR SƏBUHİ QURBANOV BIOGRAPHY READING MODULE')
if init_bio_start != -1:
    comment_start = js.rfind('/**', 0, init_bio_start)
    next_module = js.find('LIBRARY FUND & HISTORY READING MODAL CONTROLLER', init_bio_start)
    next_comment = js.rfind('/**', init_bio_start, next_module)
    removed_bio_js = js[comment_start:next_comment]
    print(f'Removed initDirectorBioModule from script.js (length: {len(removed_bio_js)})')
    js = js[:comment_start] + js[next_comment:]

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js)
with open(backup_js_path, 'w', encoding='utf-8') as f:
    f.write(js)

print('Updated script.js and synced with backup.')
