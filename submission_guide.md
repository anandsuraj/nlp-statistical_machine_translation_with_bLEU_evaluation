# Submission Guide: Statistical Machine Translation (SMT) with BLEU

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

## Documentation (The Important Stuff)

### 1. [Implementation Report (Task A)](report.md)
> **What it is**: The main report explaining how we built the SMT system and the custom BLEU evaluation logic.
> **Key Sections**:
> - How we calculated BLEU (math explained simply)
> - Challenges we faced (and fixed!)
> - Screenshots of the app in action

### 2. Quality Improvement Strategy (Task B)
> **File**: `task_b_quality_improvement.pdf` (Located in root folder)
> **What it is**: Our analysis of how to actually improve translation quality.
> **Key Insight**: We found that using **Domain-Specific Constraints** is the most effective way to boost BLEU scores for specific tasks.

### 3. Literature Survey (Part 2)
> **File**: `literature_survey.pdf` (Located in root folder)
> **Topic**: Automatic Evaluation Metrics for Statistical Machine Translation
> **Description**: A comprehensive review of the current state of research in SMT evaluation metrics.

---

## Source Code

### [app.py](app.py)
> The Flask backend. Contains the `calculate_bleu` function which is the core logic of the assignment.

### [automated_evaluation.py](automated_evaluation.py)
> A script we wrote to automatically test the system with 7 different language pairs to prove it works.

### [templates/index.html](templates/index.html)
> The frontend code. Includes the JavaScript logic for the file upload feature.

---

## How to Run

See [README.md](README.md) for simple setup instructions (basically just `pip install` and `python app.py`).
