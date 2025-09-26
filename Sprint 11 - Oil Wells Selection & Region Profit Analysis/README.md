# ⭐ Project 11 - Oil Wells Selection & Region Profit Analysis (OilyGiant)

## 📌 Project Overview
I built a pipeline to help **OilyGiant** choose the best region to drill **200 new oil wells**.  
For each of three regions I trained a **linear regression** model to predict reserves (in thousands of barrels), selected the top 200 candidate wells, calculated potential profit under given economics and budget, and quantified risk using **bootstrapping**.

---

## 🎯 My Objectives
- Load exploration datasets for three regions (`geo_data_0.csv`, `geo_data_1.csv`, `geo_data_2.csv`).  
- Train and validate a **LinearRegression** model (75% train / 25% validation) for each region.  
- Predict reserves for validation and for the full sample, compute RMSE and mean predicted reserves.  
- Select the best 200 candidate wells per region by predicted reserves.  
- Compute expected revenue and profit per region under the \$100M budget constraint.  
- Use **1000 bootstrap samples** to estimate profit distribution, 95% CI, and probability of loss (loss = negative profit).  
- Keep only regions with loss risk < **2.5%** and choose the region with highest mean profit.

---

## 📂 Dataset Description
Each region dataset contains 500 exploration samples with these columns:

| Column | Description |
|--------|-------------|
| `id`   | unique well identifier |
| `f0`   | feature 0 (geological parameter) |
| `f1`   | feature 1 |
| `f2`   | feature 2 |
| `product` | target: reserves (thousands of barrels) |

Files:
- `/datasets/geo_data_0.csv`
- `/datasets/geo_data_1.csv`
- `/datasets/geo_data_2.csv`

---

## 🛠️ My Workflow

### 1. Data loading & preprocessing
- Load CSVs and inspect for missing values / outliers.
- (Optional) basic feature scaling or polynomial expansion — note: constraint requires using linear regression for training; feature engineering is permitted.

### 2. Modeling per region
For each region:
- Split data 75% train / 25% validation (random_state fixed for reproducibility).
- Train `sklearn.linear_model.LinearRegression`.
- Predict on validation set; compute and report:
  - Mean predicted reserves (validation)
  - RMSE on validation
- Save predictions and ground truth for later analysis.

### 3. Candidate selection & profit calculation
- For each region, predict reserves for the **full set** and choose the top **200** samples by predicted `product`.
- Compute total predicted units for those 200 wells.
- Economic parameters:
  - Budget per 200 wells = \$100,000,000
  - Revenue per unit (1 = 1000 barrels) = \$4,500
  - Break-even per well (units) = (Budget / 200) / 4500 ≈ 111.11 units
- Compute potential profit:
  - Revenue = total_units * 4500
  - Profit = Revenue - Budget

### 4. Bootstrapping risk analysis
- For the selected 200 predicted reserves (array `preds_200`), run **1000 bootstrap samples**:
  - For each bootstrap iteration, sample with replacement 200 predictions, compute Revenue and Profit.
- From bootstrap distribution compute:
  - Mean profit
  - 95% confidence interval (2.5% and 97.5% percentiles)
  - Probability of loss = fraction of bootstrap iterations with Profit < 0
- Keep regions with `probability_of_loss < 0.025` (2.5%) and choose the one with highest mean profit.

### 5. Reporting
- Present per-region: validation RMSE, mean predicted reserves, selected 200 total predicted units, mean profit, 95% CI, loss risk (%).
- Recommend region(s) that satisfy risk criterion and maximize expected profit.
- Discuss assumptions, possible model improvements, and caveats.

---
