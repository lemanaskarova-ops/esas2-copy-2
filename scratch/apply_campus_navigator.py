import os, sys, re, json

base = "/Users/konul/Documents/esas2 copy 2"

# 1. READ FILES
with open(os.path.join(base, "index.html"), "r", encoding="utf-8") as f:
    html_content = f.read()

with open(os.path.join(base, "style.css"), "r", encoding="utf-8") as f:
    css_content = f.read()

with open(os.path.join(base, "script.js"), "r", encoding="utf-8") as f:
    js_content = f.read()

print("Files read successfully.")
