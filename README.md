# Statistical Machine Translation with BLEU Evaluation

**Group 5 | NLP Applications Assignment 2**

This repository contains a comprehensive web-based Statistical Machine Translation (SMT) workbench. It enables real-time text translation across multiple languages while providing an integrated, automated BLEU (Bilingual Evaluation Understudy) score evaluation to objectively measure translation quality against human reference texts.

## 1. System Architecture & Operation

The system handles everything from text ingestion and API-based translation to n-gram precision calculations and final performance scoring.

### Architecture Flow
![Architecture Flow Diagram](results/output/architecture_flow.png)

### Automated Evaluation Script
The application features a robust internal evaluation script that computes the BLEU score by comparing the generated translation against an expected reference sentence.
![Evaluation Calculation](results/output/smt_bleu_score_calculation.png)
![Evaluation Result](results/output/automatic_evalution_result.png)

### User Interface 
The intuitive web frontend allows users to easily input text, select target languages, and view both the translation and its detailed n-gram evaluation metrics instantly.
![UI Localhost](results/output/smt_ui_localhost.png)
![Translation Result Interface](results/output/smt-ui-result.png)

---

## 2. Real-Life Applications
The architecture and evaluation methodologies implemented in this SMT workbench are highly relevant to modern NLP and localization industries:

1. **Automated Content Localization**: E-commerce platforms and global news agencies can use similar pipelines to rapidly translate vast amounts of product descriptions or articles, using BLEU scores to flag low-quality translations for human review.
2. **Customer Support Triage**: Multinational companies can implement SMT to translate incoming foreign-language support tickets into a common language (e.g., English) so support agents can route or answer them effectively.
3. **Legal Document Discovery**: In international law, vast corpuses of foreign documents can be passed through customized SMT systems to quickly identify relevant evidence before paying expensive human translators for certified versions.
4. **Machine Learning Data Augmentation**: AI researchers use established SMT models (like back-translation) to generate synthetic, multi-lingual training data to improve the robustness of other NLP models.

---

## 3. Team Members

| Name | Student ID | Role | Contribution |
|------|------------|------|--------------|
| **Karan Sharma** | 2024AB05145 | Documentation, Testing & Visualization | 100% |
| **Neerumalla Kavitha** | 2024AA05879 | Data Preprocessing & N-gram Analysis | 100% |
| **Selva Pandian S** | 2023AC05005 | Backend API & Model Integration | 100% |
| **Shikhar Nigam** | 2024AA05691 | Frontend Development & UI/UX | 100% |
| **Suraj Anand** | 2024AA05731 | System Architecture & BLEU Implementation | 100% |

---

## 4. Execution Instructions

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

## 5. Deliverables & Submission

### 5.1 Reports & Documentation (PDFs)

| Content | Submitted File (PDF) | Source File | Description |
| :--- | :--- | :--- | :--- |
| **Implementation Report (Task A)** | `report.pdf` | Detailed report on SMT design, challenges, and results. Includes flow screenshots. |
| **Quality Improvement Strategy (Task B)** | `task_b_quality_improvement.pdf` | Analysis of strategies to improve BLEU scores (Data, Models, Domain). |

### 5.2 Code & Project Files

| Requirement | File / Folder Path | Description |
| :--- | :--- | :--- |
| **Backend Code** | `app.py` | Main Flask application containing translation logic and custom BLEU implementation. |
| **Frontend Code** | `templates/` & `static/` | UI templates (`index.html`) and assets (CSS, JS) for the web interface. |
| **Dependencies** | `requirements.txt` | List of Python libraries required to run the project. |
| **Deployment Config** | `vercel.json` | Configuration file for Vercel deployment. |
| **Execution Screenshots** | `results/output/` | Directory containing all individual screenshots of the application execution. |
