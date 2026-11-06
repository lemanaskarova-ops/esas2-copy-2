import os, sys, re, json

base_dir = "/Users/konul/Documents/esas2 copy 2"

# 1. READ FILES
with open(os.path.join(base_dir, "index.html"), "r", encoding="utf-8") as f:
    html_src = f.read()

with open(os.path.join(base_dir, "script.js"), "r", encoding="utf-8") as f:
    js_src = f.read()

print("Files read successfully.")
