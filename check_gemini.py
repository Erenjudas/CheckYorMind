import os
from google import genai
from dotenv import load_dotenv

def check_api():
    print("--- CheckYorMind: Gemini API Diagnostic Tool ---")
    
    # 1. Load Environment
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("ERROR: GEMINI_API_KEY not found in .env file!")
        return
    
    print(f"INFO: API Key found: {api_key[:10]}...")
    
    # 2. Initialize Client
    try:
        client = genai.Client(api_key=api_key)
        print("SUCCESS: Gemini client initialized.")
    except Exception as e:
        print(f"ERROR: Failed to initialize client: {e}")
        return

    # 3. List Models (Verification)
    try:
        models = [m.name for m in client.models.list()]
        print(f"INFO: ALL Available models: {models}")
        # Automatically pick the first one that is NOT an embedding model
        model_name = next(m for m in models if "embedding" not in m.lower())
        print(f"INFO: Selected model for test: {model_name}")
    except Exception as e:
        print(f"WARNING: Could not list models: {e}")
        model_name = "gemini-1.5-flash"

    # 4. Tokenization & Generation Test
    test_prompt = "Hello Gemini, are you working? Provide a 1-sentence supportive health tip."
    
    print(f"DEBUG: Sending test prompt: '{test_prompt}'")
    
    try:
        # Token Count
        tokens = client.models.count_tokens(model=model_name, contents=test_prompt)
        print(f"SUCCESS: Tokenization working. Total tokens: {tokens.total_tokens}")
        
        # Generation
        response = client.models.generate_content(model=model_name, contents=test_prompt)
        
        if response and hasattr(response, 'text') and response.text:
            print("\nSUCCESS: API IS WORKING!")
            print(f"GEMINI RESPONSE: {response.text}")
        else:
            print("\nFAILURE: API returned an empty response.")
            
    except Exception as e:
        print(f"\nERROR: API ERROR: {str(e)}")

if __name__ == "__main__":
    check_api()
