# ⭐ Project 13 - Sure Tomorrow Insurance Analysis

## 📌 Project Overview
I applied **linear algebra and machine learning** techniques to practical insurance tasks for **Sure Tomorrow**.  
The project aimed to explore client similarity, predict insurance benefits, and ensure privacy through **data masking** without reducing model performance.

---

## 🎯 My Objectives
- Load and inspect the dataset (`insurance_us.csv`).  
- Verify data quality: check for missing values, extreme values, and anomalies.  
- Task 1: Identify clients similar to a given client to support marketing campaigns.  
- Task 2: Predict the probability that a new client will receive insurance benefits and compare ML models vs. dummy models.  
- Task 3: Predict the amount of benefits a new client will receive using **Linear Regression**.  
- Task 4: Implement **data masking / obfuscation** to protect personal data without compromising model performance.  
- Summarize conclusions and insights from each task.

---

## 📂 Dataset Description
The dataset contains the following columns:

| Column | Description |
|--------|-------------|
| `sex`  | Gender of the insured |
| `age`  | Age of the insured |
| `salary` | Annual income |
| `family_members` | Number of family members |
| `target` | Number of insurance benefits received in the last 5 years |

File:
- `/datasets/insurance_us.csv`

---

## 🛠️ My Workflow

### 1. Data Loading & Validation
- Load CSV and inspect for missing values and extreme values.  
- Ensure data is ready for similarity analysis, classification, and regression.

### 2. Task 1: Similarity Analysis
- Use linear algebra techniques to find clients similar to a reference client.  
- Validate results to ensure similarity measures make sense.

### 3. Task 2: Probability Prediction
- Train a classification model to predict whether a new client will receive benefits.  
- Compare model performance against a **dummy classifier**.  
- Explain why the ML model can perform better or worse than a dummy.

### 4. Task 3: Regression for Benefit Amounts
- Train a **Linear Regression** model to predict the number of benefits.  
- Evaluate performance using regression metrics (RMSE, R²).  

### 5. Task 4: Data Masking
- Apply transformations to protect sensitive client information.  
- Ensure that the model's performance is not affected by the masking.

### 6. Reporting
- Document insights for each task: similarity, classification, regression, and privacy.  
- Include assumptions, limitations, and possible improvements.

---
