import json

with open(r'.agents\spec_miner_lec2\slides_detail.json', encoding='utf-8') as f:
    slides = json.load(f)

sparse_ids = [3, 10, 16, 17, 19, 21, 24, 27, 28, 29, 30, 31, 34, 36, 37, 38, 45, 46, 47, 50, 52, 53, 56, 58, 59, 61, 63, 64]

with open(r'.agents\spec_miner_lec2\sparse_slides_inspect.txt', 'w', encoding='utf-8') as out:
    for s in slides:
        if s['slide_num'] in sparse_ids:
            out.write(f"=== SLIDE {s['slide_num']} ===\n")
            for b in s['blocks']:
                out.write(f"  {b['text'].replace('\n', ' ')}\n")
            out.write("\n")

print("Saved sparse_slides_inspect.txt")
