# ⭐ Project 12 - Gold Recovery Prediction

## 📌 Project Overview

I developed a machine learning pipeline to predict gold recovery from ore processing data.
The project involved cleaning and analyzing raw data, handling missing values and anomalies, and training models to predict recovery rates.
The evaluation metric was sMAPE, which measures relative prediction error.

⸻

## 🎯 My Objectives
	•	Load and explore the datasets: gold_recovery_train.csv, gold_recovery_test.csv, gold_recovery_full.csv.
	•	Verify and compute rougher.output.recovery to ensure correctness.
	•	Identify missing features in the test set and handle them.
	•	Preprocess data: handle missing values, remove anomalies, and normalize features.
	•	Analyze metal concentrations (Au, Ag, Pb) across purification stages.
	•	Compare particle size distributions between train and test datasets.
	•	Build a custom function to compute sMAPE.
	•	Train multiple models, perform cross-validation, and select the best model.
	•	Evaluate the model on the test dataset and report results.

⸻

## 📂 Dataset Description

Three datasets are provided:

File	Description
gold_recovery_train.csv	Training set with features and targets
gold_recovery_test.csv	Test set with features only
gold_recovery_full.csv	Complete dataset containing all features

	•	Indexed by date and time.
	•	Some features are missing in the test set due to later measurement.
	•	Targets available only in the training set: rougher.output.recovery, final.output.recovery.

⸻

## 🛠️ My Workflow

1. Data Preparation
	•	Load CSV files and inspect data for missing values and anomalies.
	•	Verify rougher.output.recovery calculations and compute mean absolute error.
	•	Remove or impute missing values and eliminate outliers.
	•	Normalize and preprocess features for modeling.

2. Exploratory Data Analysis
	•	Analyze changes in metal concentrations (Au, Ag, Pb) across stages: raw → rougher concentrate → final concentrate.
	•	Compare particle size distributions between training and test sets.
	•	Analyze total substance concentrations and remove unrealistic values.

3. Modeling
	•	Define a function to calculate sMAPE.
	•	Train multiple regression models: Linear Regression, Random Forest, Gradient Boosting.
	•	Perform cross-validation and select the model with the lowest sMAPE.
	•	Validate the model on the test dataset.

4. Reporting
	•	Present sMAPE and other evaluation metrics for rougher and final recovery.
	•	Summarize preprocessing steps, anomalies handled, and feature importance.
	•	Provide insights into model reliability and potential improvements.

⸻

## 📊 Outcome

The model provided accurate predictions of gold recovery rates, demonstrating effective preprocessing, analysis, and predictive modeling on industrial ore processing datasets.
