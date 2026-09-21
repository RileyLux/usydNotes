import json

with open(r'.agents\spec_miner_lec2\extracted_slides.json', encoding='utf-8') as f:
    slides = json.load(f)

for s in slides:
    print(f"==================== SLIDE {s['page_num']} ====================")
    print(s['text'])
    print("\n")
