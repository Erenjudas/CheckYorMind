import os
import pickle
import pandas as pd
from google import genai
from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests

# Env vars load karein
load_dotenv()

# --- Gemini Config ---
api_key = os.getenv("GEMINI_API_KEY")
client = None
gemini_available = False

if api_key:
    try:
        # Latest SDK Client
        client = genai.Client(api_key=api_key)
        gemini_available = True
        print(f"INFO: Gemini Client initialized (API Key detected).")
    except Exception as e:
        print(f"ERROR: Client init failed: {e}")

# --- SerpApi Config ---
serpapi_key = os.getenv("SERP_API_KEY")  # Fixed: Was looking for "SERPAPI_API_KEY"
serpapi_available = bool(serpapi_key)
if serpapi_available:
    print(f"INFO: SerpApi Key detected and loaded successfully.")


def search_nearby_psychiatrists(location: str, limit: int = 6):
    """
    Uses SerpApi Google Maps engine to find nearby psychiatrists.
    Returns a list of dicts: {name, phone, address}
    """
    print(f"\n{'='*60}")
    print(f"🔍 SERP API DEBUG START - Psychiatrist Search")
    print(f"{'='*60}")
    
    # Debug 1: Check API Key
    print(f"[1] SerpApi Available: {serpapi_available}")
    print(f"[2] API Key Status: {'✓ Loaded' if serpapi_key else '✗ NOT LOADED'}")
    if serpapi_key:
        print(f"    Key Preview: {serpapi_key[:10]}...{serpapi_key[-10:]}")
    
    # Debug 2: Check Location Input
    print(f"[3] Location Input: '{location}'")
    print(f"    Type: {type(location)}")
    print(f"    Is Empty: {not location or not location.strip()}")
    
    if not serpapi_available or not serpapi_key:
        print(f"❌ ERROR: SerpApi key not available. Aborting search.")
        print(f"{'='*60}\n")
        return []

    if not location or not location.strip():
        print(f"❌ ERROR: Location is empty or null. Aborting search.")
        print(f"{'='*60}\n")
        return []

    # Debug 3: Build Parameters
    params = {
        "engine": "google_maps",
        "q": "psychiatrist",
        "location": location.strip(),
        "type": "search",
        "api_key": serpapi_key,
    }
    print(f"[4] Request Parameters:")
    print(f"    Engine: {params['engine']}")
    print(f"    Query: {params['q']}")
    print(f"    Location: {params['location']}")
    print(f"    URL: https://serpapi.com/search.json?...")

    try:
        print(f"[5] Sending HTTP request to SerpApi...")
        resp = requests.get("https://serpapi.com/search.json", params=params, timeout=20)
        resp.raise_for_status()
        print(f"    ✓ HTTP Status: {resp.status_code}")
        
        data = resp.json() or {}
        print(f"[6] Response Received:")
        print(f"    Response Keys: {list(data.keys())}")
        
        # Debug 4: Check for Errors
        if "error" in data:
            print(f"    ❌ SerpApi Error: {data['error']}")
            print(f"{'='*60}\n")
            return []
        
        results = data.get("local_results") or []
        print(f"    Local Results Found: {len(results)}")

        # Debug 5: Process Results
        doctors = []
        for idx, r in enumerate(results):
            name = (r.get("title") or "").strip()
            phone = (r.get("phone") or r.get("phone_number") or "").strip()
            address = (r.get("address") or "").strip()

            if not name:
                continue

            doctor_obj = {
                "name": name,
                "phone": phone if phone else "N/A",
                "address": address if address else "N/A",
            }
            doctors.append(doctor_obj)
            print(f"    [{idx+1}] {name}")
            print(f"        📞 Phone: {phone if phone else 'Not Available'}")
            print(f"        📍 Address: {address if address else 'Not Available'}")

            if len(doctors) >= limit:
                break

        print(f"[7] Final Results: {len(doctors)} psychiatrists found and processed")
        print(f"✅ SUCCESS: SerpApi search completed!")
        print(f"{'='*60}\n")
        return doctors
        
    except requests.exceptions.Timeout:
        print(f"❌ TIMEOUT: SerpApi request took too long (>20s)")
        print(f"{'='*60}\n")
        return []
    except requests.exceptions.ConnectionError as e:
        print(f"❌ CONNECTION ERROR: {str(e)}")
        print(f"{'='*60}\n")
        return []
    except Exception as e:
        print(f"❌ SYSTEM ERROR: {type(e).__name__}")
        print(f"   Message: {str(e)}")
        print(f"{'='*60}\n")
        return []

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

# --- Load ML Core ---
try:
    model_path = os.path.join(BASE_DIR, 'models/mind_model.pkl')
    encoder_path = os.path.join(BASE_DIR, 'models/encoders.pkl')
    
    model = pickle.load(open(model_path, 'rb'))
    encoders = pickle.load(open(encoder_path, 'rb'))
    ml_status = "active"
    print("SUCCESS: ML Core (Pickle) loaded successfully.")
except Exception as e:
    print(f"ML Load Error: {e}")
    ml_status = "offline"

@app.route('/')
def home():
    return render_template('index.html', 
                           prediction=None, 
                           advice=None, 
                           exercises=None,
                           psychiatrists=None,
                           location=None,
                           ml_status=ml_status, 
                           gemini_status="active" if gemini_available else "offline",
                           serpapi_status="active" if serpapi_available else "offline")

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.to_dict()
    
    print(f"\n{'='*60}")
    print(f"📋 FORM SUBMISSION DEBUG")
    print(f"{'='*60}")
    print(f"Total Form Fields Received: {len(user_input)}")
    print(f"Form Fields: {list(user_input.keys())}")
    
    # Feature columns list
    feature_cols = ['Age', 'Gender', 'Country', 'self_employed', 'family_history', 'work_interfere', 
                    'no_employees', 'remote_work', 'tech_company', 'benefits', 'care_options', 
                    'wellness_program', 'seek_help', 'anonymity', 'leave', 'mental_health_consequence', 
                    'phys_health_consequence', 'coworkers', 'supervisor', 'mental_health_interview', 
                    'phys_health_interview', 'mental_vs_physical', 'obs_consequence']
    
    # Data Preprocessing
    processed_input = {}
    for col in feature_cols:
        val = user_input.get(col, '').strip()
        
        # Default values agar input khali ho
        if not val:
            if col == 'Age': val = '30'
            elif col == 'Gender': val = 'Male'
            else: val = 'No'
        
        if col in encoders:
            try:
                processed_input[col] = encoders[col].transform([val])[0]
            except:
                processed_input[col] = 0 # Default to 0 if encoding fails
        else:
            try:
                processed_input[col] = int(val)
            except:
                processed_input[col] = 30

    # --- ML Prediction ---
    input_df = pd.DataFrame([processed_input])[feature_cols]
    prediction_num = model.predict(input_df)[0]
    result = "Treatment Recommended" if prediction_num == 1 else "No Immediate Treatment Needed"

    # --- AI Analysis (Gemini) ---
    ai_advice = "AI analysis temporarily offline."
    exercises = None
    
    if gemini_available and client:
        try:
            # Use the latest available model
            TARGET_MODEL = "gemini-2.5-flash"
            
            if result == "Treatment Recommended":
                prompt_text = (
                    "You are Dr. Hybrid, a professional mental wellness advisor. "
                    "A user has been identified as needing mental health support. "
                    f"User details: Age {user_input.get('Age', 'unknown')}, Location: {user_input.get('Country', 'unknown')}. "
                    "Provide 3-5 professional, evidence-based mental wellness recommendations in clear English. "
                    "Format as simple numbered points (1. 2. 3. etc). "
                    "Do NOT use asterisks, bold text, or markdown formatting. "
                    "Be empathetic, practical, and actionable. Focus on immediate wellness strategies."
                )
            else:
                prompt_text = (
                    "You are Dr. Hybrid, a professional mental wellness advisor. "
                    f"A user's mental health assessment shows: {result}. "
                    f"User age: {user_input.get('Age', 'unknown')}. "
                    "Provide 2-3 brief, professional mental wellness tips in clear English. "
                    "Do NOT use asterisks, bold text, or markdown formatting. "
                    "Keep it positive, practical, and easy to understand."
                )

            # Generate Content with explicit model reference
            print(f"DEBUG: Calling {TARGET_MODEL} with prompt...")
            response = client.models.generate_content(
                model=TARGET_MODEL,
                contents=prompt_text
            )
            
            if response and hasattr(response, 'text') and response.text:
                # Clean the response: remove asterisks and markdown formatting
                clean_text = response.text.strip()
                clean_text = clean_text.replace('**', '').replace('*', '').replace('##', '').replace('#', '')
                
                if result == "Treatment Recommended":
                    exercises = clean_text
                    ai_advice = "Professional wellness recommendations have been generated based on your profile."
                else:
                    ai_advice = clean_text
                print(f"SUCCESS: {TARGET_MODEL} response received: {ai_advice[:100]}...")
            else:
                ai_advice = "ML prediction ready. Professional wellness analysis is being prepared."
                print("WARNING: Empty response from Gemini")
        
        except Exception as e:
            print(f"Gemini API Error: {type(e).__name__}: {str(e)}")
            ai_advice = f"Professional assessment in progress. Please try again momentarily."

    # --- SerpApi: Nearby Psychiatrists (only when Treatment Recommended) ---
    # IMPORTANT: Get location from Country field (or add a separate location field)
    location = user_input.get("Country", "").strip()
    print(f"📍 Location for psychiatrist search: '{location}'")
    
    psychiatrists = []
    if result == "Treatment Recommended" and location:
        print(f"🔍 Triggering SerpApi search for psychiatrists in {location}...")
        psychiatrists = search_nearby_psychiatrists(location=location, limit=6)
        print(f"📊 Psychiatrists returned: {len(psychiatrists)}")
    else:
        if result != "Treatment Recommended":
            print(f"⚠️  Skipping SerpApi - Result is: {result}")
        if not location:
            print(f"⚠️  Skipping SerpApi - No location provided")

    print(f"{'='*60}\n")

    return render_template('index.html', 
                           prediction=result, 
                           advice=ai_advice, 
                           exercises=exercises,
                           psychiatrists=psychiatrists,
                           location=location,
                           user_data=user_input, 
                           ml_status=ml_status, 
                           gemini_status="active" if gemini_available else "offline",
                           serpapi_status="active" if serpapi_available else "offline")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)