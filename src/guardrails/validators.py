from src.skills.structure import SustainabilityData
import datetime

def silent_review(data: SustainabilityData) -> tuple[bool, str]:
    """
    Acts as the ALTK Silent Review component.
    Returns: (is_valid, error_message)
    """
    current_year = datetime.datetime.now().year
    
    # Rule 1: No Time Travel
    if data.report_year > current_year:
        return False, f"Error: Report year {data.report_year} is in the future. Check context."
    
    if data.report_year < 2010:
        return False, f"Error: Report year {data.report_year} is too old (pre-2010)."

    # Rule 2: Physics check (Negative emissions)
    if data.carbon_emissions_mt is not None and data.carbon_emissions_mt < 0:
        return False, f"Error: Carbon emissions cannot be negative ({data.carbon_emissions_mt})."

    # Rule 3: Logic Check (Company Name)
    if "unknown" in data.company_name.lower() or len(data.company_name) < 2:
        return False, "Error: Company name looks invalid or generic."

    return True, "Verified"