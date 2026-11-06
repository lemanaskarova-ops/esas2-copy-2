// Lists unique, valid news photos as "file label" pairs (one per line) for the montage tool
const fs = require("fs");
const crypto = require("crypto");
const path = require("path");
const ROOT = "/Users/konul/Documents/esas2 copy 2";
const src = fs.readFileSync(path.join(ROOT, "script.js"), "utf8");
const s = src.indexOf("const newsData = [");
const e = src.indexOf("\n];", s);
const arr = eval(src.slice(s + "const newsData = ".length, e + 3));
const seen = new Set();
const out = [];
for (const n of arr) {
  const f = path.join(ROOT, n.image);
  if (!fs.existsSync(f)) continue;
  const buf = fs.readFileSync(f);
  if (buf.length < 20000) continue;
  const h = crypto.createHash("md5").update(buf).digest("hex");
  if (seen.has(h)) continue;
  seen.add(h);
  out.push({ id: n.id, f });
}
if (process.argv[2] === "json") {
  console.log(JSON.stringify(out.map((o) => o.id)));
} else {
  out.forEach((o) => console.log(o.f + "\t" + o.id));
}
