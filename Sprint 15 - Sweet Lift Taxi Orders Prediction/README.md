# ⭐ Project 15 - Sweet Lift Taxi Orders Prediction

## 📌 Project Overview
I developed a **time series prediction pipeline** for **Sweet Lift Taxi** to forecast the number of taxi orders at airports.  
The project aimed to help the company attract more drivers during peak hours by accurately predicting upcoming demand.

---

## 🎯 My Objectives
- Load and inspect the dataset (`taxi.csv`).  
- Resample data to hourly intervals to ensure consistency.  
- Explore patterns and trends in historical taxi orders (`num_orders`).  
- Train and evaluate multiple models:
  - Linear regression
  - Random Forest
  - Gradient boosting (XGBoost, LightGBM)
- Tune hyperparameters for better prediction accuracy.  
- Evaluate models on a hold-out test set (10% of data).  
- Ensure predictions meet the operational **RECM ≤ 48** constraint.

---

## 📂 Dataset Description
The dataset contains:

| Column | Description |
|--------|-------------|
| `num_orders` | Number of taxi orders per original timestamp |
| `timestamp` | Original datetime of the order count |

File:
- `/datasets/taxi.csv`

---

## 🛠️ My Workflow

### 1. Data Loading & Preprocessing
- Load CSV and inspect for missing values and anomalies.  
- Resample data to **hourly intervals**.  
- Handle outliers and missing timestamps as needed.

### 2. Feature Engineering
- Create lag features, rolling means, or other time-based features.  
- Encode cyclical features if needed (hour of day, day of week).

### 3. Model Training & Evaluation
- Train multiple regression and boosting models:  
  - **Linear Regression**
  - **Random Forest Regressor**
  - **Gradient Boosting** (XGBoost, LightGBM)  
- Tune hyperparameters where applicable.  
- Evaluate using **RECM** on the test set.

### 4. Reporting
- Present model performance metrics and RECM values.  
- Ensure predictions do not exceed **RECM ≤ 48**.  
- Discuss patterns discovered, limitations, and operational implications.

---
