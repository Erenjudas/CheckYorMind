# CheckYorMind Pro v4.0 - Quick Reference Guide

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone repository
git clone https://github.com/yourusername/CheckYorMind.git
cd CheckYorMind

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
# Create .env file with:
GEMINI_API_KEY=your_key_here
SERP_API_KEY=your_key_here

# 5. Run application
python app.py

# 6. Open browser
# Navigate to: http://127.0.0.1:5000
```

---

## 🔑 Getting API Keys

### Google Gemini API
1. Visit: https://aistudio.google.com/app/apikey
2. Click "Create API Key"
3. Copy key to .env as `GEMINI_API_KEY=`

### SerpApi
1. Visit: https://serpapi.com
2. Sign up (free tier available)
3. Copy key from dashboard to .env as `SERP_API_KEY=`

---

## 📁 Key Files Explained

| File | Purpose |
|------|---------|
| `app.py` | Main Flask backend (all API integrations) |
| `templates/index.html` | 5-step diagnostic form UI |
| `models/mind_model.pkl` | Trained ML model (82.4% accuracy) |
| `requirements.txt` | Python dependencies |
| `.env` | API keys (never commit!) |
| `README.md` | GitHub guide & quick start |
| `PROJECT_REPORT.md` | Complete technical documentation |

---

## 🎯 How It Works

**User Flow:**
```
Fill Form (5 min)
    ↓
ML Prediction (< 1 sec)
    ↓
If Treatment Needed:
  ├→ Gemini AI generates wellness tips (800ms)
  └→ SerpApi finds nearby psychiatrists (2-3 sec)
    ↓
Display Results
```

**Architecture:**
- **Layer 1:** Random Forest ML (82.4% accurate)
- **Layer 2:** Google Gemini AI (personalized guidance)
- **Layer 3:** SerpApi (doctor locator)

---

## 🧪 Testing APIs

```bash
# Test Gemini API
python check_gemini.py

# Test Flask app startup
python app.py
# Look for:
# ✅ "Gemini Client initialized"
# ✅ "SerpApi Key detected"
# ✅ "Running on http://127.0.0.1:5000"
```

---

## 🔐 Security Checklist

- [ ] `.env` file created with API keys
- [ ] `.env` is in `.gitignore` (never commit!)
- [ ] No hardcoded keys in `app.py`
- [ ] All API calls are server-side only
- [ ] Running on localhost (development)

---

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Python Code | 1,200+ lines |
| HTML Template | 509+ lines |
| ML Accuracy | 82.4% |
| Training Samples | 1,400+ |
| API Integrations | 3 (Gemini, SerpApi, ML) |
| Response Time | < 5 seconds |
| Doctor Results | 3-6 per location |

---

## 🐛 Troubleshooting

### "Gemini API key not found"
```bash
# Check .env file exists
ls -la .env

# Verify GEMINI_API_KEY is set
cat .env | grep GEMINI_API_KEY

# Run from project root directory
cd c:\Users\Administrator\Desktop\CheckYorMind
python app.py
```

### "SerpApi key not loaded"
```bash
# Verify SERP_API_KEY in .env
cat .env | grep SERP_API_KEY

# Check key is active at https://serpapi.com
# Ensure no typos in .env
```

### "Models not found"
```bash
# Verify files exist
ls -la models/mind_model.pkl
ls -la models/encoders.pkl

# Retrain if needed
python data/ml/train_model.py
```

---

## 🚀 Deployment Options

### Local (Development)
```bash
python app.py
# Access at http://127.0.0.1:5000
```

### Docker
```bash
docker build -t checkyor-mind .
docker run -p 5000:5000 checkyor-mind
```

### Cloud (Azure, AWS, GCP)
See `PROJECT_REPORT.md` for detailed deployment guide

---

## 📚 Documentation

- **README.md** - Quick start guide
- **PROJECT_REPORT.md** - Complete technical docs
- **app.py** - Source code with comments
- **GITHUB_SETUP_COMPLETE.md** - GitHub upload checklist

---

## 🤝 Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing`
3. Commit: `git commit -m "Add amazing feature"`
4. Push: `git push origin feature/amazing`
5. Open Pull Request

---

## 📞 Support

- **Issues:** GitHub Issues
- **Questions:** GitHub Discussions
- **Email:** [Your contact]

---

## 🎯 Key Features

✅ ML Screening with 82.4% accuracy  
✅ AI-powered wellness recommendations  
✅ Real-time psychiatrist locator  
✅ 5-minute diagnosis process  
✅ 100% privacy protection  
✅ Global coverage (Pakistan, USA, etc.)  
✅ No insurance required  

---

**Version:** v4.0  
**Status:** Production Ready  
**Last Updated:** January 2026
