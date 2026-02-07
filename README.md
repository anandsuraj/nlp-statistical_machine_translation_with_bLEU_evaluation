# Statistical Machine Translation with BLEU Evaluation

**NLP Applications - Assignment 2 - Group 5**

## Team Members

| Name | Student ID | Role |
|------|------------|------|
| **Suraj Anand** | 2024AA05731 | System Architecture & BLEU Implementation |
| **SELVA PANDIAN S** | 2023AC05005 | Backend API & Model Integration |
| **Shikhar Nigam** | 2024AA05691 | Frontend Development & UI/UX |
| **NEERUMALLA KAVITHA** | 2024AA05879 | Data Preprocessing & N-gram Analysis |
| **Karan Sharma** | 2024AB05145 | Documentation, Testing & Visualization |

This project implements a Statistical Machine Translation (SMT) system with automatic BLEU score evaluation. The application provides a web-based interface for translating text between multiple languages and evaluating translation quality using the BLEU (Bilingual Evaluation Understudy) metric.

## Features

- **Multi-language Translation**: Support for English, Hindi, Spanish, French, German, Chinese, Japanese, and Arabic
- **BLEU Score Evaluation**: Automatic computation of BLEU scores with detailed metrics
- **N-gram Precision Analysis**: Breakdown of 1-gram, 2-gram, 3-gram, and 4-gram precision
- **Multiple Reference Support**: Evaluate translations against multiple reference translations
- **Modern Web Interface**: Responsive, user-friendly design
- **Detailed Metrics**: Brevity penalty, precision tables, and quality assessment

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Translation**: Google Translate API via googletrans library
- **NLP Processing**: NLTK for tokenization
- **Frontend**: HTML5, CSS3, JavaScript
- **Evaluation**: Custom BLEU score implementation

## Screenshot Navigation

Screenshots demonstrating the application flow (Task A requirement) can be found in the `implementation_report.md` file, which includes placeholders for:

1.  **Home Page**: Initial state with language selection.
2.  **Translation Result**: Showing translated text.
3.  **Reference Entry**: Manual input and file upload tabs.
4.  **BLEU Results**: Distinct score display and N-gram table.
5.  **Multiple References**: Evaluation with multiple inputs.

*Note: For the best experience, please run the application locally to see the interactive UI live.*

- Python 3.8+
- pip (Python package manager)
- Internet connection (for Google Translate API)

## Installation

### Step 1: Clone or Navigate to Project Directory

```bash
cd /your/project/directory
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- googletrans (translation API)
- nltk (natural language processing)
- transformers (neural models fallback)
- torch (deep learning framework)
- sacrebleu (BLEU validation)

### Step 4: Download NLTK Data

The application will automatically download required NLTK data on first run. If you want to do it manually:

```bash
python3 -c "import nltk; nltk.download('punkt')"
```

## Running the Application

### Start the Flask Server

```bash
python3 app.py
```

You should see output like:
```
 * Running on http://0.0.0.0:5000
 * Debug mode: on
```

### Access the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage Guide

### 1. Translation

1. **Select Languages**: Choose source and target languages from the dropdowns
2. **Enter Text**: Type or paste the text you want to translate
3. **Translate**: Click the "Translate" button
4. **View Results**: The translated text will appear in the results section

### 2. BLEU Evaluation

1. **Complete Translation**: First translate some text (see step 1)
2. **Add Reference(s)**: 
   - **Manual Entry**: Type reference translation(s) in the text areas
   - **Upload File**: Upload a .txt file with one reference per line
3. **Evaluate**: Click "Evaluate BLEU Score"
4. **View Metrics**:
   - Overall BLEU score (0-1 scale)
   - Quality assessment (Poor/Fair/Good/Excellent)
   - N-gram precision table (1-4 grams)
   - Brevity penalty
   - Length statistics

### Example Translation

**Source (English)**: "Hello, how are you today?"  
**Target Language**: Hindi  
**Translation**: "नमस्ते, आज आप कैसे हैं?"

**Reference Translation**: "नमस्ते, आप आज कैसे हो?"  
**BLEU Score**: ~0.65 (Good quality)

## Project Structure (Part 1 Submission)

```
assignment2/
├── app.py                      # Flask backend (Task A)
├── requirements.txt            # Python dependencies
├── README.md                   # Installation & usage guide
├── task_b_quality_improvement.pdf # Task B strategies
├── report.md                   # Task A report
├── vercel.json                 # Deployment config
├── templates/
│   └── index.html             # Main web interface
└── static/
    ├── css/
    │   └── style.css          # Styling
    └── js/
        └── script.js          # Frontend logic
```

## Screenshot Navigation

Screenshots demonstrating the application flow (Task A requirement) can be found in the `implementation_report.md` file, which includes placeholders for:

1.  **Home Page**: Initial state with language selection.
2.  **Translation Result**: Showing translated text.
3.  **Reference Entry**: Manual input and file upload tabs.
4.  **BLEU Results**: Distinct score display and N-gram table.
5.  **Multiple References**: Evaluation with multiple inputs.

*Note: For the best experience, please run the application locally to see the interactive UI live.*

## BLEU Score Explanation

**BLEU (Bilingual Evaluation Understudy)** is an automatic metric for evaluating machine translation quality by comparing it to human reference translations.

### Components:

1. **Modified N-gram Precision**: Measures how many n-grams in the candidate translation match the reference(s)
   - 1-gram: Individual words
   - 2-gram: Word pairs
   - 3-gram: Word triplets
   - 4-gram: Word quadruplets

2. **Brevity Penalty (BP)**: Penalizes translations that are too short
   - BP = 1 if candidate length ≥ reference length
   - BP = e^(1 - r/c) otherwise

3. **Final BLEU Score**: 
   ```
   BLEU = BP × exp(Σ log(p_n) / N)
   ```
   where p_n is the precision for n-grams

### Score Interpretation:

- **< 0.3**: Poor translation quality
- **0.3 - 0.5**: Fair translation, understandable but with errors
- **0.5 - 0.7**: Good translation, mostly accurate
- **> 0.7**: Excellent translation, very close to reference

## Troubleshooting

### Translation Not Working

**Issue**: "Translation failed" error  
**Solution**: 
- Check internet connection
- Google Translate API may have rate limits
- Try again after a few seconds

### BLEU Score is 0

**Issue**: BLEU score shows 0.0000  
**Solution**:
- Ensure reference translation is in the same language as candidate
- Check that reference is not empty
- Try more similar reference translations

### Module Not Found Error

**Issue**: `ModuleNotFoundError: No module named 'flask'`  
**Solution**:
```bash
pip install -r requirements.txt
```

### Port Already in Use

**Issue**: `Address already in use`  
**Solution**:
```bash
# Change port in app.py, last line:
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

## Learning Outcomes

As a student working on this project, I learned:

1. **Statistical Machine Translation**: Understanding how SMT systems work and their components
2. **Evaluation Metrics**: Deep dive into BLEU score computation and its mathematical foundation
3. **Web Development**: Building full-stack applications with Flask
4. **API Integration**: Using external translation services
5. **NLP Concepts**: Tokenization, n-grams, and text processing
6. **Software Engineering**: Code organization, documentation, and user experience design

##  References

- Papineni et al. (2002). "BLEU: a Method for Automatic Evaluation of Machine Translation"
- Google Translate API Documentation
- NLTK Documentation
- Flask Documentation

## Author

**Student**: Suraj Anand
**Course**: M.Tech AIML Semester 3  
**Assignment**: Assignment 2 - Statistical Machine Translation with BLEU Evaluation

## License

This is an academic project created for educational purposes.

---

**Note**: This implementation uses Google Translate API (via googletrans library) for demonstration purposes. In production SMT systems, trained statistical models (like Moses) or neural machine translation models would be used.
