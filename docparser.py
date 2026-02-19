import os
import asyncio
import re
from pathlib import Path
import httpx
from PyPDF2 import PdfReader
from llama_cloud import AsyncLlamaCloud
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("LLAMA_CLOUD_API_KEY")

DATA_DIR = Path(__file__).parent / "temp"
PARSED_DIR = Path(__file__).parent / "parsed"

def get_pdf_page_count(file_path):
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        return len(reader.pages)

async def download_image(url, out_path):
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(url)
        response.raise_for_status()
        with open(out_path, "wb") as img_file:
            img_file.write(response.content)

async def process_pdf(pdf_path):
    client = AsyncLlamaCloud(api_key=api_key)

    file_obj = await client.files.create(file=str(pdf_path), purpose="parse")

    input_options = {}  # <-- No crop_box, no page_ranges

    result = await client.parsing.parse(
        file_id=file_obj.id,
        tier="cost_effective",
        version="latest",
        input_options=input_options,
        output_options={
            "markdown": {
                "tables": {
                    "output_tables_as_markdown": False,
                    "markdown_table_multiline_separator": " | "
                },
            },
            "images_to_save": ["screenshot", "embedded"],
        },
        processing_options={
            "ignore": {
                "ignore_diagonal_text": True,
            },
            "specialized_chart_parsing": "efficient",
            "ocr_parameters": {
                "languages": ["en"]
            }
        },
        expand=["text", "markdown", "items", "images_content_metadata"],
    )

    out_dir = PARSED_DIR / pdf_path.stem
    out_dir.mkdir(exist_ok=True)

    # Save markdown
    md_pages = getattr(getattr(result, "markdown", None), "pages", [])
    combined_md = "\n\n---\n\n".join(getattr(p, "markdown", "") or "" for p in md_pages)
    (out_dir / f"{pdf_path.stem}.md").write_text(combined_md, encoding="utf-8")

    # Save plain text
    text_pages = getattr(getattr(result, "text", None), "pages", [])
    combined_text = "\n\n".join(getattr(p, "text", "") or "" for p in text_pages)
    (out_dir / f"{pdf_path.stem}.txt").write_text(combined_text, encoding="utf-8")

    # Download screenshots and embedded images
    images_meta = getattr(result, "images_content_metadata", None)
    if images_meta and getattr(images_meta, "images", None):
        for image in images_meta.images:
            fname = getattr(image, "filename", None)
            url = getattr(image, "presigned_url", None)
            if not fname or not url:
                continue
            # Download all images (screenshots and embedded)
            await download_image(url, out_dir / fname)

async def main():
    pdf_files = sorted(DATA_DIR.glob("*.pdf"))
    if not pdf_files:
        print("No PDF files found in data/ to process.")
        return
    for pdf in pdf_files:
        try:
            await process_pdf(pdf)
            print(f"Parsed {pdf.name} -> {PARSED_DIR / pdf.stem}")
        except Exception as e:
            print(f"Error processing {pdf.name}: {e}")

if __name__ == "__main__":
    asyncio.run(main())