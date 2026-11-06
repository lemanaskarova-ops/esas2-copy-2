import os, sys, re

base_dir = "/Users/konul/Documents/esas2 copy 2"

with open(os.path.join(base_dir, "scratch/script_backup_pre_campus.js"), "r", encoding="utf-8") as f:
    orig_js = f.read()

pos_az = orig_js.find('const i18n = {')
pos_en = orig_js.find('\n  en: {')
pos_ru = orig_js.find('\n  ru: {')
pos_end = orig_js.find('\nlet currentLang =')

orig_az = orig_js[pos_az:pos_en]
orig_en = orig_js[pos_en:pos_ru]
orig_ru = orig_js[pos_ru:pos_end]

print("Found original blocks:")
print("orig_az length:", len(orig_az))
print("orig_en length:", len(orig_en))
print("orig_ru length:", len(orig_ru))
