import json
import sys

with open(r'.agents\spec_miner_lec2\extracted_slides.json', encoding='utf-8') as f:
    slides = json.load(f)

with open(r'.agents\spec_miner_lec2\slide_titles.txt', 'w', encoding='utf-8') as out:
    for s in slides:
        lines = [l.strip() for l in s['text'].split('\n') if l.strip()]
        title = lines[0] if lines else '[EMPTY]'
        sub = lines[1] if len(lines) > 1 else ''
        out.write(f"Slide {s['page_num']:2d}: {title} || {sub[:80]}\n")

print("Saved slide_titles.txt successfully.")
