# 📊 Project 05 - Megaline Tariff Revenue Analysis  

## 📌 Project Overview  
As part of the analytics team at **Megaline**, my task was to determine **which prepaid plan, Surf or Ultimate, generates more revenue**.  
I analyzed customer data including calls, messages, internet usage, subscription plans, and demographics to understand usage behavior and revenue differences.  

---

## 🎯 My Objectives  
- Load and inspect multiple datasets (`users`, `calls`, `messages`, `internet`, `plans`).  
- Clean and preprocess data, correcting types and handling errors.  
- Calculate monthly usage for calls, messages, and internet per user.  
- Estimate **monthly revenue per user** based on plan limits and extra usage.  
- Explore usage patterns with descriptive statistics and visualizations.  
- Test statistical hypotheses:  
  - Compare revenue between Surf and Ultimate plans.  
  - Compare revenue between New York-New Jersey region and other regions.  
- Summarize findings in conclusions.  

---

## 📂 Dataset Description  
The project uses five datasets:  

| File                | Description |
|--------------------|-------------|
| `users.csv`        | Customer information including ID, name, age, subscription and churn date, city, and plan. |
| `calls.csv`        | Call records with duration, date, and user ID. |
| `messages.csv`     | SMS records with date and user ID. |
| `internet.csv`     | Internet session usage with data volume, date, and user ID. |
| `plans.csv`        | Prepaid plan details including monthly fee, limits, and costs for exceeding limits. |

---

## 🛠️ My Workflow  
1. **Data Loading & Inspection:**  
   - Review datasets and understand structure.  
2. **Data Preprocessing:**  
   - Correct data types.  
   - Handle missing values and errors.  
3. **Revenue Calculation:**  
   - Calculate calls, messages, and data usage per month for each user.  
   - Compute monthly revenue per user considering plan limits and extra usage.  
4. **Exploratory Analysis:**  
   - Visualize distributions of usage and revenue.  
   - Calculate descriptive statistics (mean, variance, standard deviation).  
5. **Hypothesis Testing:**  
   - Compare average revenue between Surf and Ultimate plans.  
   - Compare revenue of NY-NJ customers versus other regions.  
   - Formulate null and alternative hypotheses, select alpha, and justify statistical tests.  
6. **Conclusions:**  
   - Summarize insights about plan profitability and user behavior.  

---

## 📚 Tools & Technologies I Used  
- Python  
- pandas, numpy  
- matplotlib, seaborn  
- Statistical analysis and hypothesis testing  
- Data Cleaning & Preprocessing  

---

## ✅ Deliverables  
- Jupyter Notebook with all preprocessing, calculations, and analysis documented.  
- Visualizations showing usage patterns and revenue distributions.  
- Hypothesis testing results and conclusions about plan profitability.  

---

✍️ Author: **Alejandro Loria**  
📅 TripleTen LatAm - Data Scientist Course  
