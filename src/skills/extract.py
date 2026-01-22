# src/skills/extract.py
import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# --- IMPORTS ---
# We need both the Data Structure (Recipe) and the Validator (Inspector)
from src.skills.structure import SustainabilityData
from src.guardrails.validators import silent_review

# Load keys
load_dotenv()

def get_granite_chef():
    """Initialize the Granite 3.0 Model."""
    return WatsonxLLM(
        model_id="ibm/granite-3-8b-instruct",
        url="https://us-south.ml.cloud.ibm.com",
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        apikey=os.getenv("WATSONX_APIKEY"),
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 500,
            "min_new_tokens": 1
        }
    )

def analyze_document(doc_text: str, max_retries: int = 2) -> SustainabilityData:
    """
    Extracts data with an ALTK Self-Healing Loop.
    """
    granite = get_granite_chef()
    parser = PydanticOutputParser(pydantic_object=SustainabilityData)

    # Base Prompt
    prompt_template = """<|system|>
You are an expert ESG Auditor. Extract precise sustainability data.
{format_instructions}

<|user|>
Document Text: "{text}"

{feedback}

Extract the data now.
<|assistant|>
"""
    
    current_feedback = ""
    
    for attempt in range(max_retries + 1):
        print(f"🔄 Attempt {attempt + 1}...")
        
        # Build prompt with dynamic feedback (if retrying)
        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["text", "feedback"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )
        
        chain = prompt | granite | parser
        
        try:
            # 1. Generate
            result = chain.invoke({"text": doc_text, "feedback": current_feedback})
            
            # 2. Silent Review (The ALTK Step)
            is_valid, message = silent_review(result)
            
            if is_valid:
                print("✅ ALTK Check Passed.")
                return result
            else:
                print(f"⚠️ ALTK Flagged: {message}")
                # Add feedback for the next loop so Granite fixes its mistake
                current_feedback = f"PREVIOUS ERROR: {message}. Please correct this."
                
        except Exception as e:
            print(f"⚠️ Parsing Error: {e}")
            current_feedback = f"PREVIOUS OUTPUT FORMAT ERROR: {str(e)}. Follow JSON schema strictly."

    print("❌ Max retries reached. Human intervention needed.")
    return None