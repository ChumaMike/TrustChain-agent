from src.skills.extract import analyze_document

# A fake messy supplier email/document
fake_doc = """
REPORT FOR: ACME SUSTAINABLE SUPPLIES LTD.
Date: Jan 15, 2030.
We are proud to announce that for the 2050 fiscal year, our total carbon footprint was 150.5 metric tonnes.
We strictly adhere to ISO 14001 standards.
Our HR policy strictly prohibits child labor in all manufacturing plants.
"""

print(f"📄 Analyzing fake document...")
data = analyze_document(fake_doc)

if data:
    print("\n✅ WINNING EXTRACTION:")
    print(f"Company: {data.company_name}")
    print(f"Year: {data.report_year}")
    print(f"Emissions: {data.carbon_emissions_mt} MT")
    print(f"Child Labor Policy: {data.has_child_labor_policy}")
    print(f"Certs: {data.certifications}")
else:
    print("❌ Failed to extract.")