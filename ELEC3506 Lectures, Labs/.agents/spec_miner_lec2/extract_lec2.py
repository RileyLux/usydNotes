import pypdf
import json

pdf_path = r"c:\Users\R4iley\Downloads\Lecture2.pdf"
reader = pypdf.PdfReader(pdf_path)

print(f"Total pages: {len(reader.pages)}")

slides = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    slides.append({
        "page_num": idx + 1,
        "text": text.strip()
    })

output_path = r"c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs\.agents\spec_miner_lec2\extracted_slides.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(slides, f, indent=2, ensure_ascii=False)

txt_output_path = r"c:\Users\R4iley\OneDrive\Documents\UUUuusyd\Usyd\ELEC3506 Lectures, Labs\.agents\spec_miner_lec2\extracted_slides.txt"
with open(txt_output_path, "w", encoding="utf-8") as f:
    for s in slides:
        f.write(f"=== SLIDE {s['page_num']} ===\n")
        f.write(s['text'] + "\n\n")

print(f"Extraction complete. Saved {len(slides)} slides.")
