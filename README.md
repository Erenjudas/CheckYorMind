# CheckYorMind Pro v4.0 🧠

**Your Complete Mental Health Intelligence System**

A professional, AI-powered mental health diagnostic platform that combines machine learning predictions, personalized AI recommendations, and real-world doctor connections—all in 5 minutes.

---

## 🎯 What is CheckYorMind?

**CheckYorMind** = "Check" (Assess) + "Yor" (Your) + "Mind" (Mental Wellness)

### The Problem We're Solving
- ❌ 45% of tech workers experience burnout
- ❌ Workplace stigma prevents help-seeking
- ❌ Mental health professionals are difficult to locate
- ❌ Screening tools are fragmented and inaccessible
- ❌ Critical gap between diagnosis and professional care

**CheckYorMind closes that gap completely.**

---

## 🏗️ 3-Layer Intelligent System

### Layer 1: 🔍 ML-Powered Screening
- **Analyzes 23 behavioral & workplace indicators**
- **82.4% accuracy** via Random Forest Classifier
- **Training Data:** 1,400+ real mental health survey responses
- **Result:** Binary treatment recommendation in milliseconds
- **Technology:** Scikit-learn Random Forest

### Layer 2: 💡 AI-Powered Guidance
- **Google Gemini 2.5-Flash API** generates personalized recommendations
- **3-5 evidence-based wellness strategies**
- **Professional English** (no jargon, no markdown)
- **Customized to YOUR situation**
- **Real-time response generation** (~800ms)

### Layer 3: 🗺️ Care Connection
- **SerpApi Google Maps integration** finds nearby psychiatrists
- **Real-time location-based search**
- **Returns 3-6 qualified professionals** with full contact info
- **Works globally** (Pakistan, USA, and beyond)
- **Zero friction** from diagnosis to professional care

---

## 📁 Project Structure

```
CheckYorMind/
├── app.py                      # Main Flask application (all integrations)
├── models.py                   # Model utilities
├── check_gemini.py             # API diagnostic tool
├── requirements.txt            # Python dependencies
├── .env                        # Environment variables (API keys - DO NOT COMMIT)
├── .gitignore                  # Git ignore rules
├── models/
│   ├── mind_model.pkl          # Trained Random Forest classifier
│   └── encoders.pkl            # Label encoders for categorical features
├── templates/
│   └── index.html              # Multi-step diagnostic form (5 steps, glassmorphism design)
├── static/                     # CSS, JS, images, assets
├── data/                       # Data processing & analysis
│   ├── cleaned_survey.csv      # Processed dataset
│   ├── survey.csv              # Original dataset
│   ├── data_cleaning.py        # Data processing pipeline
│   ├── visualize_and_clean.py  # Data visualization
│   └── ml/
│       └── train_model.py      # ML training script
├── docs/                       # Project documentation
│   └── PROJECT_REPORT.md       # Technical architecture & implementation
├── notebooks/                  # Jupyter notebooks (experiments)
├── outputs/                    # Generated visualizations & reports
└── README.md                   # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager
- Free API keys from:
  - Google Gemini: https://aistudio.google.com/app/apikey
  - SerpApi: https://serpapi.com (free tier available)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/CheckYorMind.git
cd CheckYorMind
```

**2. Create virtual environment (recommended)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure environment variables**
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_gemini_api_key_here
SERP_API_KEY=your_serpapi_key_here
```

**⚠️ IMPORTANT:** Never commit `.env` to GitHub! It's already in `.gitignore`.

**5. Run the application**
```bash
python app.py
```

**6. Access the platform**
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 📊 Complete User Workflow

```
┌──────────────────────────────────────────┐
│ STEP 1: IDENTITY PROFILE (2 min)         │
│ Age, Gender, Country, Employment Type    │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│ STEP 2: WORKPLACE ECOSYSTEM (1.5 min)    │
│ Tech Company, Remote, Organization Size  │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│ STEP 3: SUPPORT SYSTEMS (1 min)          │
│ Health Benefits, Wellness Programs       │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│ STEP 4: RELATIONAL DYNAMICS (1 min)      │
│ Supervisor Trust, Peer Support           │
└──────────────────────────────────────────┘
                    ↓
┌──────────────────────────────────────────┐
│ STEP 5: CLINICAL INDICATORS (30 sec)     │
│ Family History, Workplace Impact         │
└──────────────────────────────────────────┘
                    ↓
        ✅ RESULTS DELIVERED
                    ↓
        🔍 ML Prediction (82.4%)
        💡 AI Wellness Advice
        🗺️ Nearby Psychiatrists
```

---

## 🛠️ Technology Stack

| Layer | Component | Technology |
|-------|-----------|-----------|
| **Backend** | Web Framework | Flask 3.0.0 |
| | ML Engine | Scikit-learn (Random Forest) |
| | AI Integration | Google Gemini 2.5-Flash API |
| | Doctor Search | SerpApi (Google Maps) |
| | Async Data | Pandas, NumPy |
| **Frontend** | Styling | Tailwind CSS (glassmorphism) |
| | Interactivity | Alpine.js |
| | Templating | Jinja2 |
| **Data** | ML Training | 1,400+ survey responses |
| | Model Format | Pickle serialization |
| | Accuracy | 82.4% on test data |

---

## 📈 Key Metrics

- ✅ **ML Accuracy:** 82.4% on test data
- ✅ **ML Training Data:** 1,400+ survey responses
- ✅ **API Response Time:** ~800ms for full analysis
- ✅ **Doctor Search Results:** 3-6 per location
- ✅ **Form Completion Time:** ~5 minutes
- ✅ **Supported Locations:** Pakistan, USA, and beyond

---

## � Security & Privacy

- ✅ API keys stored in `.env` (never committed)
- ✅ `.gitignore` protects sensitive files
- ✅ No personal data stored in models
- ✅ All ML preprocessing happens server-side
- ✅ Professional tone & non-judgmental recommendations

---

## 📚 Documentation

- **Technical Details:** See `docs/PROJECT_REPORT.md`
- **API Keys Setup:** See "Configure environment variables" above
- **ML Training:** See `data/ml/train_model.py`
- **Data Pipeline:** See `data/data_cleaning.py`

---

## 🔧 Troubleshooting

### Issue: "Gemini API key not found"
**Solution:** Verify `.env` file has `GEMINI_API_KEY=your_key` and run from project root.

### Issue: "SerpApi key not loaded"
**Solution:** Verify `.env` file has `SERP_API_KEY=your_key`. Check key is active at https://serpapi.com.

### Issue: "Model loading failed"
**Solution:** Verify `models/mind_model.pkl` and `models/encoders.pkl` exist. Retrain if needed: `python data/ml/train_model.py`

---

## 🤝 Contributing

Contributions welcome! To contribute:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is open source. See LICENSE file for details.

---

## 👨‍💻 Author

**CheckYorMind Pro v4.0** - Built with ❤️ for mental health awareness

---

## 🚀 Live Demo

Access the platform at: **http://127.0.0.1:5000** (after running `python app.py`)

---

## 📞 Support

For issues, questions, or feedback:
- Open an issue on GitHub
- Check `docs/PROJECT_REPORT.md` for technical details
- Review `app.py` comments for implementation details

---

**Last Updated:** January 2026  
**Status:** ✅ Production Ready (v4.0)  
**All APIs Integrated:** ✅ Gemini | ✅ SerpApi | ✅ ML Model

## 🎯 Features

### Multi-Step Diagnostic Form
- **Step 1**: Identity Profile (Age, Gender, Country, Employment)
- **Step 2**: Workplace Ecosystem (Tech company, Remote work, Org size)
- **Step 3**: Support Systems (Benefits, Care options, Wellness programs)
- **Step 4**: Relational Dynamics (Supervisor trust, Peer support)
- **Step 5**: Clinical Indicators (Family history, Work interference)

### Hybrid AI Analysis
- **ML Prediction**: 82% accurate Random Forest classifier
- **Gemini AI**: Personalized wellness recommendations in Roman Urdu

### Professional UI/UX
- Emerald & Slate color theme
- Glassmorphism effects
- Smooth micro-animations
- Fully responsive design

## 🧠 Technical Stack

- **Backend**: Flask (Python)
- **ML**: Scikit-learn (Random Forest)
- **AI**: Google Gemini Pro API
- **Frontend**: HTML5, Tailwind CSS, Alpine.js
- **Data**: Pandas, NumPy

## 📊 Model Details

- **Algorithm**: Random Forest Classifier
- **Features**: 24 workplace & clinical indicators
- **Accuracy**: 82.4%
- **Training Data**: Mental Health in Tech Survey

## 🔒 Privacy & Security

- All data processed in-memory during session
- No persistent storage of user inputs
- API keys secured via environment variables
- Localhost-only deployment (development mode)

## 📝 License

Educational & Portfolio Project

## 👥 Team

CheckYorMind Framework • Hybrid Intelligence 2026
