import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from src.skills.structure import SustainabilityData

# Load the keys
load_dotenv()

def get_granite_chef():
    """Initialize the Granite 3.0 Model."""
    return WatsonxLLM(
        model_id="ibm/granite-3-8b-instruct",
        url="https://us-south.ml.cloud.ibm.com", # Update if your region is different
        project_id=os.getenv("WATSONX_PROJECT_ID"),
        apikey=os.getenv("WATSONX_APIKEY"),
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 500,
            "min_new_tokens": 1
        }
    )

def analyze_document(doc_text: str) -> SustainabilityData:
    """
    Takes raw text (from Docling) and forces Granite to fill our Mellea Recipe.
    """
    granite = get_granite_chef()
    parser = PydanticOutputParser(pydantic_object=SustainabilityData)

    # The Prompt Template (Granite 3.0 Instruct Format)
    prompt = PromptTemplate(
        template="""<|system|>
You are an expert ESG Auditor. Your goal is to extract precise sustainability data from supplier text.
Use the following format instructions to structure your output.
{format_instructions}

<|user|>
Here is the supplier document text:
"{text}"

Extract the data now.
<|assistant|>
""",
        input_variables=["text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    # The Chain: Prompt -> Granite -> Parser (Structured Output)
    chain = prompt | granite | parser
    
    print("⚡ Granite is reading the document...")
    try:
        result = chain.invoke({"text": doc_text})
        return result
    except Exception as e:
        print(f"⚠️ Parsing Error: {e}")
        return None