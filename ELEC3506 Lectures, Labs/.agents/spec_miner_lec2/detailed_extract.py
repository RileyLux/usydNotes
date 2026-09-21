import pymupdf
import json

doc = pymupdf.open(r"c:\Users\R4iley\Downloads\Lecture2.pdf")

print(f"Total pages: {len(doc)}")

slides_detail = []
for page_idx in range(len(doc)):
    page = doc[page_idx]
    # Get all text blocks
    blocks = page.get_text("blocks")
    # Get text as layout
    layout_text = page.get_text("text")
    
    # Store clean blocks
    cleaned_blocks = []
    for b in blocks:
        # b is (x0, y0, x1, y1, text, block_no, block_type)
        if b[6] == 0: # text block
            txt = b[4].strip()
            if txt:
                cleaned_blocks.append({
                    "bbox": [round(x, 1) for x in b[:4]],
                    "text": txt
                })
    
    slides_detail.append({
        "slide_num": page_idx + 1,
        "raw_text": layout_text.strip(),
        "blocks": cleaned_blocks
    })

output_path = r"c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs\.agents\spec_miner_lec2\slides_detail.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(slides_detail, f, indent=2, ensure_ascii=False)

txt_out = r"c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs\.agents\spec_miner_lec2\slides_detail.txt"
with open(txt_out, "w", encoding="utf-8") as f:
    for s in slides_detail:
        f.write(f"==================================================\n")
        f.write(f"SLIDE {s['slide_num']}\n")
        f.write(f"==================================================\n")
        for b in s['blocks']:
            f.write(f"[{b['bbox']}]: {b['text']}\n")
        f.write("\n")

print("Saved slides_detail.json and slides_detail.txt")
