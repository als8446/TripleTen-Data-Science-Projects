# ⭐ Project 16 - Film Junky Union Movie Review Sentiment

## 📌 Project Overview
I developed a **text classification pipeline** for **Film Junky Union** to automatically detect negative movie reviews.  
The system helps the community filter and categorize reviews efficiently, providing quick insights for movie enthusiasts.

---

## 🎯 My Objectives
- Load and inspect the IMDB reviews dataset (`imdb_reviews.tsv`).  
- Preprocess text data, handle missing values, and explore data quality.  
- Perform exploratory data analysis, including **class imbalance evaluation**.  
- Train at least **three classification models**:
  - Logistic Regression
  - Gradient Boosting
  - Another chosen model (e.g., Random Forest or SVM)
- Evaluate models on a test set, ensuring **F1 score ≥ 0.85**.  
- Make predictions on custom reviews and analyze differences across models.  
- Summarize findings and model insights.

---

## 📂 Dataset Description
The dataset contains:

| Column | Description |
|--------|-------------|
| `review` | Text of the movie review |
| `pos` | Target: '0' = negative, '1' = positive |
| `ds_part` | Dataset part: 'training' / 'test' |

File:
- `/datasets/imdb_reviews.tsv`

---

## 🛠️ My Workflow

### 1. Data Loading & Preprocessing
- Load TSV and inspect for missing or malformed data.  
- Basic text preprocessing: lowercasing, removing punctuation, tokenization if needed.  
- Optionally use embeddings (e.g., BERT for sample subset).

### 2. Exploratory Data Analysis
- Evaluate **class distribution** and possible imbalance.  
- Visualize review lengths, word frequencies, or sentiment patterns.

### 3. Feature Engineering
- Convert text to numerical representations:
  - TF-IDF, CountVectorizer, or embeddings.  
- Split data into training and test sets.

### 4. Model Training & Evaluation
- Train multiple models:  
  - **Logistic Regression**
  - **Gradient Boosting**
  - **Random Forest / SVM / Other**  
- Evaluate using **F1 score** and other classification metrics.  
- Test models on custom reviews and compare predictions.

### 5. Reporting
- Present F1 scores and accuracy per model.  
- Discuss insights about negative review detection, class imbalance, and limitations.  
- Optionally include BERT-based embeddings for small-scale experiments.

---
