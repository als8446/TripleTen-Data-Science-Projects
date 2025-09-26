# ⭐ Project 06 - Video Games Success Analysis  

## 📌 Project Overview  
As part of the analytics team at **Ice online store**, my task was to **identify patterns that determine whether a video game is successful**.  
I analyzed historical data including game sales, platforms, genres, release years, user and critic reviews, and ESRB ratings to guide marketing campaigns and highlight promising games.  

---

## 🎯 My Objectives  
- Load and inspect the dataset (`games.csv`).  
- Clean and preprocess data: standardize columns, correct data types, handle missing values, and calculate total sales.  
- Analyze sales patterns by platform, genre, and year.  
- Explore correlations between user/critic reviews and sales.  
- Build regional profiles (NA, EU, JP) for top platforms and genres.  
- Assess the impact of ESRB ratings on sales.  
- Test hypotheses:  
  - Compare average user scores for Xbox One vs. PC.  
  - Compare average user scores for Action vs. Sports genres.  
- Draw conclusions about factors influencing video game success.  

---

## 📂 Dataset Description  
The project uses one main dataset:  

| Column             | Description |
|-------------------|-------------|
| `Name`            | Game title |
| `Platform`        | Platform (e.g., Xbox, PlayStation) |
| `Year_of_Release`  | Year the game was released |
| `Genre`           | Game genre |
| `NA_sales`        | North America sales (millions USD) |
| `EU_sales`        | Europe sales (millions USD) |
| `JP_sales`        | Japan sales (millions USD) |
| `Other_sales`     | Other regions sales (millions USD) |
| `Critic_Score`    | Maximum 100 |
| `User_Score`      | Maximum 10 |
| `Rating`          | ESRB classification |

---

## 🛠️ My Workflow  
1. **Data Loading & Inspection:**  
   - Examine the dataset, identify missing values, and rename columns.  
2. **Data Preprocessing:**  
   - Convert types, handle TBD values, calculate total sales per game.  
3. **Exploratory Analysis:**  
   - Analyze trends by year, platform, and genre.  
   - Visualize distributions of sales and ratings.  
4. **Regional Analysis:**  
   - Determine top platforms and genres in NA, EU, and JP.  
   - Evaluate ESRB ratings' impact on sales.  
5. **Hypothesis Testing:**  
   - Compare user scores across platforms (Xbox One vs PC).  
   - Compare user scores across genres (Action vs Sports).  
   - Formulate null/alternative hypotheses, choose alpha, and justify statistical tests.  
6. **Conclusions:**  
   - Summarize insights about video game success factors.  

---

## 📚 Tools & Technologies I Used  
- Python  
- pandas, numpy  
- matplotlib, seaborn  
- Statistical analysis and hypothesis testing  
- Data cleaning & preprocessing  
- Exploratory data analysis (EDA)  

---

## ✅ Deliverables  
- Jupyter Notebook with all preprocessing, calculations, analysis, and visualizations.  
- Regional and genre-based sales insights.  
- Hypothesis testing results and conclusions on success factors.  

---

✍️ Author: **Alejandro Loria**  
📅 TripleTen LatAm - Data Scientist Course  
