import os, sys, re

base_dir = "/Users/konul/Documents/esas2 copy 2"

# 1. UPDATE INDEX.HTML
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

# Remove campus-filter-hint
hint_old = '<span class="campus-filter-hint">Otaq kartına basaraq ətraflı bələdçi məlumatını əldə edin</span>'
if hint_old in html_src:
    html_src = html_src.replace(hint_old, '')
    print("Removed campus-filter-hint from index.html")

# Remove campus-room-modal block
pos_modal = html_src.find('id="campus-room-modal"')
if pos_modal != -1:
    pos_start = html_src.rfind('<!-- ═══ CAMPUS ROOM DETAIL', 0, pos_modal)
    pos_end = html_src.find('</div>\n    </div>', pos_modal) + len('</div>\n    </div>')
    html_src = html_src[:pos_start] + html_src[pos_end:].lstrip()
    print("Removed #campus-room-modal markup from index.html")

# Bump cache version to v=20261106_32
html_src = re.sub(r'style\.css\?v=[a-zA-Z0-9_]+', 'style.css?v=20261106_32', html_src)
html_src = re.sub(r'script\.js\?v=[a-zA-Z0-9_]+', 'script.js?v=20261106_32', html_src)

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_src)
print("index.html saved successfully.")

# 2. UPDATE SCRIPT.JS
with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

# Let's locate the campus navigator module in script.js
pos_mod = js_src.find('CAMPUS & ROOM NAVIGATOR CONTROLLER (OTAQLAR.docx)')
if pos_mod != -1:
    print("Found Campus Navigator in script.js")
    # Replace the module with the refined streamlined version with no useless buttons
