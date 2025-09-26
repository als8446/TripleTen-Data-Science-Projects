# ⭐ Project 10 - Beta Bank Customer Churn Prediction

## 📌 Project Overview
I built a churn prediction pipeline for **Beta Bank** with the goal of identifying customers likely to leave the bank. My primary objective was to maximize the **F1 score** (required threshold: **≥ 0.59**) and to measure **AUC-ROC** for model comparison.

Dataset: `/datasets/Churn.csv`

---

## 🎯 My Objectives
- Load and prepare the dataset; document preprocessing steps.
- Explore class balance and train an initial baseline model (no imbalance handling).
- Improve model quality using **at least two** methods to address class imbalance.
- Tune models using train/validation splits and select the best model.
- Evaluate the final model on the test set and report **F1** and **AUC-ROC**.
- Provide interpretation and suggestions for business action.

---

## 📂 Dataset Description
Key columns in `Churn.csv`:

| Column             | Description |
|--------------------|-------------|
| `RowNumber`        | Row index |
| `CustomerId`       | Unique customer id |
| `Surname`          | Customer surname |
| `CreditScore`      | Credit score |
| `Geography`        | Country / region |
| `Gender`           | Male / Female |
| `Age`              | Customer age |
| `Tenure`           | Years with bank |
| `Balance`          | Account balance |
| `NumOfProducts`    | Number of bank products used |
| `HasCrCard`        | Has credit card (1/0) |
| `IsActiveMember`   | Active member (1/0) |
| `EstimatedSalary`  | Estimated salary |
| `Exited`           | Target: churn (1) or stay (0) |

---

## 🛠️ My Workflow

### 1. Data loading & exploration
- Load CSV, inspect columns, missing values, types.
- Drop or preserve identifier columns (`RowNumber`, `CustomerId`, `Surname`) as appropriate.
- Basic EDA: class balance, feature distributions, correlations.

### 2. Preprocessing
- Handle categorical variables: `Geography`, `Gender` (One-Hot or ordinal encoding as appropriate).
- Scale numeric features (StandardScaler or RobustScaler for heavy-tailed features).
- Impute missing values (if any) with sensible strategies and document choices.
- Create a few derived features if helpful (e.g., `balance_per_product = Balance / (NumOfProducts+1)`).

### 3. Baseline model (no imbalance correction)
- Make train/validation/test split (e.g., 60% train, 20% val, 20% test) with **stratify** on `Exited`.
- Train a baseline model (Logistic Regression / RandomForest) and evaluate on validation set.
- Record baseline F1 and AUC-ROC.

### 4. Handling class imbalance (use **at least two** methods)
I tried multiple approaches; examples below:

**A. Resampling**
- **Oversampling** the minority class with SMOTE (Synthetic Minority Oversampling Technique).
- **Undersampling** the majority class (RandomUnderSampler) or combined (SMOTEENN, SMOTETomek).

**B. Algorithmic / Loss-based**
- Use tree-based models with `class_weight='balanced'` (e.g., RandomForest with class weights) or logistic regression with class weights.
- Use `scale_pos_weight` for XGBoost / LightGBM.

**C. Threshold tuning**
- Tune decision threshold using precision-recall tradeoff on validation set to maximize F1.

I evaluated combinations (resampling + model type + hyperparams) and selected the one with best validation F1.

### 5. Model selection & hyperparameter tuning
- Use cross-validated `RandomizedSearchCV` or `GridSearchCV` on training data (or nested CV) for hyperparameters.
- Use validation set to compare models and pick the final estimator.
- Metrics to prioritize: **F1 (primary)**, precision, recall, and **AUC-ROC** (secondary but reported).

### 6. Final evaluation
- Retrain the chosen pipeline on train+validation if desired.
- Evaluate final model on **test set** and report:
  - **F1 score** (must be ≥ 0.59 to pass)
  - **AUC-ROC**
  - Confusion matrix
  - Precision, recall, F1, support

### 7. Interpretation & recommendations
- Feature importance (for tree models) or coefficients (for linear models).
- Business recommendations on who to target (e.g., high churn probability + high lifetime value).
- Next steps and potential data improvements.

---

## 📈 Example code outline

```python
import pandas as pd
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, roc_auc_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
from imblearn.pipeline import Pipeline as ImbPipeline

df = pd.read_csv('/datasets/Churn.csv')
# Drop identifiers
df = df.drop(['RowNumber','CustomerId','Surname'], axis=1)

X = df.drop('Exited', axis=1)
y = df['Exited']

# Train/val/test split (stratified)
X_trainval, X_test, y_trainval, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, test_size=0.25, stratify=y_trainval, random_state=42) # 0.25*0.8=0.2

# Preprocessing: categorical & numeric
num_features = ['CreditScore','Age','Tenure','Balance','NumOfProducts','EstimatedSalary']
cat_features = ['Geography','Gender','HasCrCard','IsActiveMember']

num_transformer = Pipeline([('scaler', StandardScaler())])
cat_transformer = Pipeline([('ohe', OneHotEncoder(handle_unknown='ignore'))])

preproc = ColumnTransformer([('num', num_transformer, num_features),
                             ('cat', cat_transformer, cat_features)])

# Approach A: SMOTE + RandomForest
smote = SMOTE(random_state=42)
rf = RandomForestClassifier(random_state=42, n_jobs=-1)

pipe = ImbPipeline([('preproc', preproc), ('smote', smote), ('clf', rf)])
param_dist = {'clf__n_estimators':[100,300], 'clf__max_depth':[None,10,20], 'clf__min_samples_leaf':[1,2,5]}
search = RandomizedSearchCV(pipe, param_distributions=param_dist, n_iter=10, cv=5, scoring='f1', random_state=42)
search.fit(X_train, y_train)

best = search.best_estimator_
y_val_pred = best.predict(X_val)
print('Val F1:', f1_score(y_val, y_val_pred))
print('Val AUC:', roc_auc_score(y_val, best.predict_proba(X_val)[:,1]))
