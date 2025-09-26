# ⭐ Project 08 - Chicago Taxi Trips Analysis

## 📌 Project Overview
As a data analyst for **Zuber**, a ride-sharing startup in Chicago, I analyzed taxi trips data to **identify travel patterns** and evaluate the **impact of weather on trip durations**. The project combined SQL queries, Python analysis, data visualization, and hypothesis testing.

---

## 🎯 Objectives
- Analyze taxi trips data for November 2017.  
- Aggregate trips by taxi company and neighborhood.  
- Join trip data with weather records to classify conditions as `"Good"` or `"Bad"`.  
- Identify the most active taxi companies and neighborhoods.  
- Conduct exploratory data analysis (EDA) using Python.  
- Test the hypothesis: `"Average trip duration from the Loop to O'Hare changes on rainy Saturdays"`.

---

## 📂 Dataset Description
- **neighborhoods**: Neighborhood names and IDs.  
- **cabs**: Taxi vehicle IDs and company names.  
- **trips**: Trip details including start/end locations, timestamps, duration, and distance.  
- **weather_records**: Hourly weather records with temperature and description.  
- **project_sql_result_01.csv**: Number of trips per company (Nov 15–16, 2017).  
- **project_sql_result_04.csv**: Average trips ending per neighborhood.  
- **project_sql_result_07.csv**: Trip durations from the Loop to O'Hare with weather conditions.

---

## 🛠️ Workflow
1. **SQL Analysis:**  
   - Aggregate trips by company and neighborhood.  
   - Join trips with weather records.  
   - Identify top taxi companies and neighborhoods.
2. **EDA in Python:**  
   - Import SQL result CSVs.  
   - Visualize trips per company and top 10 drop-off neighborhoods.  
   - Interpret patterns and trends.  
3. **Hypothesis Testing:**  
   - Compare trip durations on rainy vs. clear Saturdays.  
   - Define null and alternative hypotheses.  
   - Apply statistical tests to draw conclusions.

---

## 📚 Tools & Technologies Used
- Python, pandas, matplotlib, seaborn  
- SQL for data querying  
- Hypothesis testing and data visualization

---

## ✅ Deliverables
- SQL queries for aggregation and joins  
- Python notebooks for EDA  
- Visualizations for company trips and neighborhood drop-offs  
- Hypothesis testing results and interpretation  

---

✍️ Author: **Alejandro Loria**  
📅 TripleTen LatAm - Data Scientist Course
