# Submission: Statistical Machine Translation with BLEU Evaluation
**Group 5 | NLP Applications Assignment 2**

## 1. Team Members
| Name | Student ID | Role |
|------|------------|------|
| **Suraj Anand** | 2024AA05731 | System Architecture & BLEU Implementation |
| **SELVA PANDIAN S** | 2023AC05005 | Backend API & Model Integration |
| **Shikhar Nigam** | 2024AA05691 | Frontend Development & UI/UX |
| **NEERUMALLA KAVITHA** | 2024AA05879 | Data Preprocessing & N-gram Analysis |
| **Karan Sharma** | 2024AB05145 | Documentation, Testing & Visualization |

---

## 2. Project Guide
**IMPORTANT**: The `README.md` file is the central document for this project. It contains detailed verification for all assignment points, installation steps, and architectural decisions. Please refer to it first to understand the whole project.

| Primary File | Path | Description |
| :--- | :--- | :--- |
| **Project README** | `README.md` | **Start Here**. Complete guide to project structure, installation, and strict assignment compliance. |

---

## 3. Automated Execution
We have provided a streamlined Flask application to run the entire system (Translation + Evaluation).

| Script | Command | Description |
| :--- | :--- | :--- |
| **Main Application** | `python3 app.py` | **Run this to launch the system.** It starts the Flask server, loads the translation model, and serves the UI at http://localhost:5000. |

---

## 4. Deliverables & Navigation
*Key files required for the assignment.*

| Requirement | File / Folder Path | Description |
| :--- | :--- | :--- |
| **Backend Code** | `app.py` | Main Flask application containing translation logic and custom BLEU implementation. |
| **Frontend Code** | `templates/` & `static/` | UI templates (`index.html`) and assets (CSS, JS) for the web interface. |
| **Dependencies** | `requirements.txt` | List of Python libraries required to run the project. |
| **Deployment Config** | `vercel.json` | Configuration file for Vercel deployment. |

---

## 5. Reports & Visuals Location
*All detailed text, specific metrics, strategies, and screenshots are located in the project root.*

| Content | Path |
| :--- | :--- |
| **Implementation Report (Task A)** | `report.md` | Detailed report on SMT system design, challenges, and results. |
| **Quality Improvement Strategy (Task B)** | `task_b_quality_improvement.pdf` | Analysis of strategies to improve BLEU scores (Data, Models, Domain). |