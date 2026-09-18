#!/usr/bin/env python3
import itertools
import json
import re
from pathlib import Path

HTML = Path("app/src/main/assets/index.html")
text = HTML.read_text(encoding="utf-8")
match = re.search(r'<script id="game-data" type="application/json">(.*?)</script>', text, re.S)
if not match:
    raise SystemExit("game-data JSON bulunamadı")

data = json.loads(match.group(1))
scenes = data.get("scenes", [])
assert len(scenes) == 9, f"Beklenen 9 sahne, bulunan {len(scenes)}"
assert all(len(scene.get("choices", [])) == 3 for scene in scenes), "Her sahnede 3 seçim olmalı"

def clamp(v):
    return max(0, min(100, v))

def ending(h, s, i, flags, action):
    if h <= 60 or s <= 20:
        return "lost_signal"
    if action == "publish" and i >= 75:
        return "daylight"
    if action == "hide" and s >= 60:
        return "ghost"
    if action == "deliver" and ("trace_employers" in flags or i >= 70):
        return "double_agent"
    return "gray"

counts = {}
for path in itertools.product(range(3), repeat=len(scenes)):
    h, s, i = 100, 100, 0
    flags = set()
    action = ""
    for scene_index, choice_index in enumerate(path):
        choice = scenes[scene_index]["choices"][choice_index]
        effects = choice.get("effects", {})
        h = clamp(h + effects.get("h", 0))
        s = clamp(s + effects.get("s", 0))
        i = clamp(i + effects.get("i", 0))
        if choice.get("flag"):
            flags.add(choice["flag"])
        if choice.get("finalAction"):
            action = choice["finalAction"]
    key = ending(h, s, i, flags, action)
    counts[key] = counts.get(key, 0) + 1

expected = {"lost_signal", "daylight", "ghost", "double_agent", "gray"}
assert set(counts) == expected, f"Erişilemeyen veya beklenmeyen final: {counts}"
assert sum(counts.values()) == 3 ** 9

print("Karar yolları:", sum(counts.values()))
for key in sorted(counts):
    print(f"{key}: {counts[key]}")
print("Doğrulama başarılı.")
