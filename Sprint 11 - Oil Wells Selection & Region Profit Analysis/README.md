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

## 📈 Example code outline

```python
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

REVENUE_PER_UNIT = 4500  # $ per 1 (thousand barrels)
BUDGET = 100_000_000
TOP_K = 200
BOOTSTRAP_N = 1000

def train_and_validate(df, random_state=42):
    X = df[['f0','f1','f2']]
    y = df['product']
    X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.75, random_state=random_state)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_val)
    rmse = mean_squared_error(y_val, y_pred, squared=False)
    return model, rmse, y_val.values, y_pred

def select_top_k_preds(model, df_full, k=TOP_K):
    preds = model.predict(df_full[['f0','f1','f2']])
    df_full = df_full.copy()
    df_full['pred'] = preds
    top = df_full.nlargest(k, 'pred')
    return top['pred'].values  # predicted units for top k

def compute_profit(pred_units):
    total_units = pred_units.sum()
    revenue = total_units * REVENUE_PER_UNIT
    profit = revenue - BUDGET
    return profit, revenue, total_units

def bootstrap_profit(preds_200, n=BOOTSTRAP_N, random_state=42):
    rng = np.random.default_rng(random_state)
    profits = []
    for _ in range(n):
        sample = rng.choice(preds_200, size=len(preds_200), replace=True)
        profit, _, _ = compute_profit(sample)
        profits.append(profit)
    profits = np.array(profits)
    mean_profit = profits.mean()
    ci = np.percentile(profits, [2.5, 97.5])
    loss_prob = (profits < 0).mean()
    return mean_profit, ci, loss_prob, profits

# Example usage:
df0 = pd.read_csv('/datasets/geo_data_0.csv')
model0, rmse0, y_val0, y_pred0 = train_and_validate(df0)
top200_preds0 = select_top_k_preds(model0, df0, k=200)
mean_profit0, ci0, loss_prob0, profits0 = bootstrap_profit(top200_preds0)
