#!/usr/bin/env python3
import glob

def update_domains():
    # 1. Update index.html
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Replace domain strings
    html = html.replace("www.rabitakolleci.edu.az", "www.rabitankolleci.edu.az")
    html = html.replace("https://rabitakolleci.edu.az", "https://www.rabitankolleci.edu.az")
    html = html.replace(">rabitakolleci.edu.az<", ">www.rabitankolleci.edu.az<")
    html = html.replace("rabitakolleci.edu.az", "www.rabitankolleci.edu.az")

    # Bump cache buster
    html = html.replace("v=20261106_39", "v=20261106_40")

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html domain references")

    # 2. Update script.js and backup
    with open("script.js", "r", encoding="utf-8") as f:
        js = f.read()

    js = js.replace("https://rabitakolleci.edu.az", "https://www.rabitankolleci.edu.az")
    js = js.replace("http://rabitakolleci.edu.az", "https://www.rabitankolleci.edu.az")
    js = js.replace("rabitakolleci.edu.az", "www.rabitankolleci.edu.az")

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js)
    with open("scratch/script_working_backup.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Updated script.js domain references")

    # 3. Update json files if any
    for jf in glob.glob("*.json"):
        try:
            with open(jf, "r", encoding="utf-8") as f:
                content = f.read()
            if "rabitakolleci.edu.az" in content:
                content = content.replace("https://rabitakolleci.edu.az", "https://www.rabitankolleci.edu.az")
                content = content.replace("rabitakolleci.edu.az", "www.rabitankolleci.edu.az")
                with open(jf, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"Updated {jf}")
        except Exception as e:
            print(f"Skipping {jf}: {e}")

update_domains()

