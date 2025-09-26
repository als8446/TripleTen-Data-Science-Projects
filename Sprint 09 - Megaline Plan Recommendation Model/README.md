# ⭐ Project 09 - Megaline Plan Recommendation Model

## 📌 Project Overview
I built a classification model to recommend Megaline’s new prepaid plans (**Smart** or **Ultra**) based on user monthly behavior. The goal was to produce a model with an accuracy of **at least 0.75** on the test set, so Megaline can automatically suggest the best new plan to legacy customers.

---

## 🎯 My Objectives
- Explore and clean the dataset located at `/datasets/users_behavior.csv`.  
- Split the data into **train**, **validation**, and **test** sets.  
- Engineer any necessary features and scale where appropriate.  
- Train and tune models (tried Logistic Regression, RandomForest, XGBoost).  
- Select the best model using validation metrics and evaluate it on the test set.  
- Perform a sanity check (e.g., baseline comparison, permutation test or simple perturbation) to verify model robustness.

---

## 📂 Dataset Description
The dataset contains monthly behavioral metrics per user:

| Column     | Description |
|------------|-------------|
| `calls`    | Number of calls |
| `minutes`  | Total call minutes |
| `messages` | Number of SMS |
| `mb_used`  | Internet usage in megabytes |
| `is_ultra` | Target label: 1 = Ultra, 0 = Smart |

File: `/datasets/users_behavior.csv`

---

## 🛠️ My Workflow
1. **Exploration & Preprocessing**
   - Load dataset and inspect distributions, missing values, and outliers.
   - If needed, fill or drop missing values (documented in notebook).
   - Create derived features (e.g., `avg_call_length = minutes / calls` with safe handling of zero calls).
   - Scale numeric features when required (StandardScaler or RobustScaler).

2. **Data Split**
   - Stratified split into train (60%), validation (20%), test (20%) to preserve class balance.

3. **Modeling & Tuning**
   - Baseline: dummy classifier (stratified) to set a lower bound.
   - Try models: Logistic Regression, RandomForestClassifier, XGBoost (or GradientBoosting).
   - Hyperparameter tuning using GridSearchCV or RandomizedSearchCV on the training set with cross-validation; evaluate on validation set.
   - Select final model based on validation accuracy, precision/recall (if class balance is an issue), and calibration.

4. **Evaluation**
   - Evaluate selected model on the test set and report accuracy, confusion matrix, precision, recall, F1-score.
   - Check that test accuracy ≥ **0.75** (project threshold). If not reached, summarize steps taken and possible improvements.

5. **Sanity Checks (Optional Task)**
   - Compare model vs baseline.
   - Perform a permutation importance or small perturbation test to ensure the model isn't relying on brittle patterns.
   - Validate model stability across different random seeds / splits.

---

## 📈 Example Code Snippet (outline)
```python
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyClassifier

df = pd.read_csv('/datasets/users_behavior.csv')
X = df[['calls','minutes','messages','mb_used']].copy()
y = df['is_ultra']

# Feature engineering
X['avg_call_length'] = X['minutes'] / X['calls'].replace(0, 1)

# Train/val/test split (stratified)
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, stratify=y_temp, random_state=42)  # 0.25 * 0.8 = 0.2

# Scaling
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val)
X_test_s = scaler.transform(X_test)

# Baseline
dummy = DummyClassifier(strategy='stratified', random_state=42)
dummy.fit(X_train_s, y_train)
print('Baseline accuracy:', accuracy_score(y_val, dummy.predict(X_val_s)))

# Model example: RandomForest
rf = RandomForestClassifier(random_state=42)
param_dist = {'n_estimators':[100,200,500], 'max_depth':[None,10,20], 'min_samples_leaf':[1,2,4]}
search = RandomizedSearchCV(rf, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy', random_state=42)
search.fit(X_train_s, y_train)
best = search.best_estimator_

y_pred = best.predict(X_val_s)
print('Validation accuracy:', accuracy_score(y_val, y_pred))
print(classification_report(y_val, y_pred))

# Final evaluation on test set
y_test_pred = best.predict(X_test_s)
print('Test accuracy:', accuracy_score(y_test, y_test_pred))
print(confusion_matrix(y_test, y_test_pred))
