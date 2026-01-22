import os
from dotenv import load_dotenv
from langchain_ibm import WatsonxLLM

# 1. Load the secrets
load_dotenv()
api_key = os.getenv("WATSONX_APIKEY")
project_id = os.getenv("WATSONX_PROJECT_ID")

print(f"Testing Connection... Project ID: {project_id[:4]}***")

# 2. Initialize Granite 3.0 (The Chef)
try:
    granite = WatsonxLLM(
        model_id="ibm/granite-3-8b-instruct",  # The 2026 Winner
        url="https://us-south.ml.cloud.ibm.com", # Change if your region is different (e.g., eu-de)
        project_id=project_id,
        apikey=api_key,
        params={
            "decoding_method": "greedy",
            "max_new_tokens": 50
        }
    )

    # 3. The Test Prompt
    response = granite.invoke("Write a one-sentence haiku about coding.")
    print("\n✅ SUCCESS! Granite says:")
    print(f"\"{response.strip()}\"")

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("Tip: Check if your Region URL matches your IBM Cloud region (e.g., dallas vs frankfurt).")