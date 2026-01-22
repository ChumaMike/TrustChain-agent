# src/skills/ingest.py
import logging
from docling.document_converter import DocumentConverter

# Mute the noisy logs from Docling's internal PDF parser
logging.getLogger("docling").setLevel(logging.WARNING)

def ingest_document(file_path: str) -> str:
    """
    The 'Prep Cook'. Takes a file path (PDF/DOCX/Image), 
    washes it, and returns clean Markdown text.
    """
    print(f"📂 Opening file: {file_path}...")
    
    try:
        converter = DocumentConverter()
        result = converter.convert(file_path)
        
        # We export to Markdown because LLMs understand it best (tables, headers, etc.)
        clean_text = result.document.export_to_markdown()
        
        print(f"✅ Docling finished. Extracted {len(clean_text)} characters.")
        return clean_text
        
    except Exception as e:
        print(f"❌ Docling Error: {e}")
        return ""