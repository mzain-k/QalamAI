import fitz
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import time

# ─── CHANGE THESE ───────────────────────────────────────────
INPUT_PDF  = "qalamai/documents/computer_science/computer_textbook.pdf"
OUTPUT_TXT = "qalamai/documents/computer_science/computer_textbook.txt"
# ────────────────────────────────────────────────────────────

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT = """Extract ALL content from this page including:
1. All text exactly as written, preserving headings and structure
2. For every diagram, figure, or illustration: describe what it shows, all labels, arrows, and spatial relationships in detail. Do not summarize — be exhaustive and literal.
3. For every formula or equation: write in plain text notation (use ^ for powers, / for fractions, spell out Greek letters)
4. For every table: extract with rows and columns preserved
This text will be used to power an AI study assistant, so accuracy and completeness matter more than brevity."""

def extract_pdf(pdf_path, output_path):
    doc = fitz.open(pdf_path)
    total_pages = len(doc)
    all_text = []

    print(f"Starting extraction: {total_pages} pages found\n")

    for page_num in range(total_pages):
        try:
            page = doc[page_num]
            pix = page.get_pixmap(dpi=200)
            img_bytes = pix.tobytes("png")

            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[
                    types.Part.from_bytes(data=img_bytes, mime_type="image/png"),
                    PROMPT
                ]
            )

            page_text = response.text
            all_text.append(f"--- Page {page_num + 1} ---\n{page_text}")
            print(f"Extracted page {page_num + 1}/{total_pages}")

        except Exception as e:
            print(f"Error on page {page_num + 1}: {e} — skipping")
            all_text.append(f"--- Page {page_num + 1} ---\n[EXTRACTION FAILED]")

        if page_num < total_pages - 1:
            time.sleep(12)

    doc.close()

    final_text = "\n\n".join(all_text)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(final_text)

    print(f"\nDone. Saved to {output_path}")

if __name__ == "__main__":
    extract_pdf(INPUT_PDF, OUTPUT_TXT)