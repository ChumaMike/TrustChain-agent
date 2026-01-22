from pydantic import BaseModel, Field
from typing import Optional, List

class SustainabilityData(BaseModel):
    """
    The 'Strict Recipe' for extracting ESG data from messy documents.
    This acts as the Mellea Generative Slot.
    """
    company_name: str = Field(
        ..., 
        description="The official name of the supplier company found in the document."
    )
    report_year: int = Field(
        ..., 
        description="The year this report or certificate covers (e.g., 2024)."
    )
    carbon_emissions_mt: Optional[float] = Field(
        None, 
        description="Total Scope 1+2 carbon emissions in Metric Tonnes. Return 0 if not found."
    )
    has_child_labor_policy: bool = Field(
        False, 
        description="True ONLY if the document explicitly mentions prohibition of child labor or forced labor."
    )
    certifications: List[str] = Field(
        default_factory=list,
        description="List of ISO certifications mentioned (e.g., 'ISO 14001', 'ISO 9001')."
    )