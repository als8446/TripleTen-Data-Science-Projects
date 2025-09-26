# ⭐ Project 14 - Rusty Bargain Car Price Prediction

## 📌 Project Overview
I developed a **car price prediction pipeline** for **Rusty Bargain**, a used car sales platform.  
The project aimed to accurately estimate car market values based on historical listings, technical specifications, and features while balancing prediction quality, speed, and training time.

---

## 🎯 My Objectives
- Load and inspect the dataset (`car_data.csv`).  
- Preprocess data: handle missing values, encode categorical features, normalize numerical features, and address outliers.  
- Train and evaluate multiple regression models:
  - **Linear Regression** as a sanity check
  - **Random Forest** with hyperparameter tuning
  - **Gradient Boosting** (LightGBM) with hyperparameter tuning
  - Optional: **CatBoost** and **XGBoost**
- Compare models on:
  - Prediction quality using **RECM**
  - Prediction speed
  - Training time
- Select the best model balancing accuracy and performance.

---

## 📂 Dataset Description
The dataset contains the following columns:

| Column | Description |
|--------|-------------|
| `DateCrawled` | Date the profile was crawled |
| `VehicleType` | Vehicle body type |
| `RegistrationYear` | Vehicle registration year |
| `Gearbox` | Transmission type |
| `Power` | Engine power (CV) |
| `Model` | Vehicle model |
| `Mileage` | Vehicle mileage (km) |
| `RegistrationMonth` | Month of registration |
| `FuelType` | Fuel type |
| `Brand` | Vehicle brand |
| `NotRepaired` | Whether the car was repaired |
| `DateCreated` | Profile creation date |
| `NumberOfPictures` | Number of photos |
| `PostalCode` | Owner postal code |
| `LastSeen` | Last seen date |
| `Price` | Target: car price (EUR) |

File:
- `/datasets/car_data.csv`

---

## 🛠️ My Workflow

### 1. Data Loading & Preprocessing
- Load CSV and inspect for missing values and anomalies.  
- Encode categorical variables (OHE or library-specific).  
- Normalize numerical features and handle outliers.  

### 2. Model Training & Evaluation
- Train multiple regression models:
  - **Linear Regression** as baseline
  - **Random Forest Regressor**
  - **Gradient Boosting** (LightGBM)
  - Optional: **CatBoost** and **XGBoost**
- Tune hyperparameters where applicable.  
- Evaluate using:
  - **RECM**
  - Prediction speed
  - Training time

### 3. Model Comparison
- Compare all models to select the best trade-off between accuracy, speed, and training efficiency.  
- Validate predictions on a hold-out test set.

### 4. Reporting
- Present model performance metrics, feature importance, and training time.  
- Summarize findings, observations, and recommendations for Rusty Bargain’s app.

---
