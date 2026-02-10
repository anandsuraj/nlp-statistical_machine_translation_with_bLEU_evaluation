# Submission Guide: SMT with BLEU Evaluation

**Group 5 | NLP Assignment 2**

## 1. Team Members

| Name | Student ID | Role | Contribution |
|------|------------|------|--------------|
| **Karan Sharma** | 2024AB05145 | Documentation, Testing & Visualization | 100% |
| **Neerumalla Kavitha** | 2024AA05879 | Data Preprocessing & N-gram Analysis | 100% |
| **Selva Pandian S** | 2023AC05005 | Backend API & Model Integration | 100% |
| **Shikhar Nigam** | 2024AA05691 | Frontend Development & UI/UX | 100% |
| **Suraj Anand** | 2024AA05731 | System Architecture & BLEU Implementation | 100% |

---

## 2. Project Documents

Here are the files you need to check:

### Implementation Report (Task A)
**File Path**: `report.md`
This report explains how we built the project. It covers:
- How we calculated the BLEU score.
- The problems we faced and how we solved them.
- Screenshots of the application.

### Quality Improvement Strategy (Task B)
**File Path**: `task_b_quality_improvement.pdf` (In the root folder)
This document explains our ideas on how to improve duplicate translation quality.

### Literature Survey (Part 2)
**File Path**: `part2_literature_survey.pdf` (In the root folder)
This is a survey of different ways to evaluate Machine Translation systems.

### Application Screenshots
**Folder Path**: `results/output`
These are screenshots showing the application results.

### Live Demo
**Link**: `https://nlpsmt.vercel.app/`
You can check out the live version of the project here.

---

## 3. Code Files

### app.py
**File Path**: `app.py`
This is the main Python code. It handles the website and the BLEU score logic.

### automated_evaluation.py
**File Path**: `automated_evaluation.py`
We wrote this script to test the system automatically with different languages.

### index.html
**File Path**: `templates/index.html`
This is the HTML file for the website. It also has the JavaScript for file uploads.

---

## 4. How to Run

1. Install the requirements: `pip install -r requirements.txt`
2. Run the app: `python app.py`
3. Open `http://localhost:5000` in your browser.