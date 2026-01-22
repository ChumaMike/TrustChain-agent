import sys
import os
from src.skills.ingest import ingest_document
from src.skills.extract import analyze_document

def run_agent(file_path):
    # 1. Check if file exists
    if not os.path.exists(file_path):
        print(f"❌ Error: File not found at {file_path}")
        return

    # 2. Ingest (Docling)
    print("--- STEP 1: INGESTION (Docling) ---")
    markdown_text = ingest_document(file_path)
    
    if not markdown_text:
        print("System Halted: Empty document.")
        return

    # 3. Think & Validate (Granite + ALTK)
    print("\n--- STEP 2: REASONING (Granite + ALTK) ---")
    result = analyze_document(markdown_text)

    # 4. Final Report
    if result:
        print("\n🏆 TRUSTCHAIN VERIFIED REPORT 🏆")
        print(f"🏢 Company:   {result.company_name}")
        print(f"📅 Year:      {result.report_year}")
        print(f"🏭 Emissions: {result.carbon_emissions_mt} tonnes")
        print(f"📜 Certified: {result.certifications}")
        
        # Simple Logic for Trust Score
        score = 100
        if not result.has_child_labor_policy: score -= 50
        if result.carbon_emissions_mt > 1000: score -= 20
        
        print(f"⭐️ Trust Score: {score}/100")
    else:
        print("\n❌ AGENT FAILED: Could not verify document.")

if __name__ == "__main__":
    # Allow running from command line: python main.py my_invoice.pdf
    if len(sys.argv) > 1:
        run_agent(sys.argv[1])
    else:
        print("Usage: python main.py <path_to_pdf>")