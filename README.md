# Statistical Machine Translation with BLEU Evaluation

**Group 5 | NLP Applications Assignment 2**

## 1. Team Members

| Name | Student ID | Role | Contribution |
|------|------------|------|--------------|
| **Karan Sharma** | 2024AB05145 | Documentation, Testing & Visualization | 100% |
| **Neerumalla Kavitha** | 2024AA05879 | Data Preprocessing & N-gram Analysis | 100% |
| **Selva Pandian S** | 2023AC05005 | Backend API & Model Integration | 100% |
| **Shikhar Nigam** | 2024AA05691 | Frontend Development & UI/UX | 100% |
| **Suraj Anand** | 2024AA05731 | System Architecture & BLEU Implementation | 100% |

---

## 2. Execution Instructions

**Prerequisites**: Python 3.8+, pip, Internet connection.

### Step 1: Installation
```bash
cd /your/project/directory
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: Run Application
```bash
python3 app.py
```
*Server starts at `http://localhost:5000`*

---

## 3. Deliverables & Submission


### 3.1 Reports & Documentation (PDFs)

| Content | Submitted File (PDF) | Source File | Description |
| :--- | :--- | :--- | :--- |
| **Implementation Report (Task A)** | `report.pdf` | Detailed report on SMT design, challenges, and results. Includes flow screenshots. |
| **Quality Improvement Strategy (Task B)** | `task_b_quality_improvement.pdf` | Analysis of strategies to improve BLEU scores (Data, Models, Domain). |

### 3.2 Code & Project Files

| Requirement | File / Folder Path | Description |
| :--- | :--- | :--- |
| **Backend Code** | `app.py` | Main Flask application containing translation logic and custom BLEU implementation. |
| **Frontend Code** | `templates/` & `static/` | UI templates (`index.html`) and assets (CSS, JS) for the web interface. |
| **Dependencies** | `requirements.txt` | List of Python libraries required to run the project. |
| **Deployment Config** | `vercel.json` | Configuration file for Vercel deployment. |
| **Execution Screenshots** | `results/output/` | Directory containing all individual screenshots of the application execution. |
