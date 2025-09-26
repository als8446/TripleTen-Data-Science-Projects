# ⭐ Project 17 - Good Seed Alcohol Age Verification

## 📌 Project Overview
I developed a **computer vision model** for **Good Seed** to automatically verify the age of customers purchasing alcohol.  
The system helps the supermarket ensure compliance with legal age restrictions using images captured at checkout.

---

## 🎯 My Objectives
- Load and explore the dataset of customer images with age labels.  
- Perform **exploratory data analysis** to understand dataset quality and distribution.  
- Preprocess images for model training: resizing, normalization, and augmentation.  
- Train a **CNN-based model** on GPU to predict age from images.  
- Evaluate model performance and accuracy.  
- Report findings and conclude on model effectiveness for age verification.

---

## 📂 Dataset Description
The dataset contains labeled images of customers:

| Feature | Description |
|---------|-------------|
| `image` | Photograph of a person at checkout |
| `age`   | Age label corresponding to the person |

File:
- `/datasets/good_seed_images/`

---

## 🛠️ My Workflow

### 1. Data Loading & Preprocessing
- Load image dataset and inspect quality.  
- Resize and normalize images.  
- Apply data augmentation to increase model robustness.

### 2. Exploratory Data Analysis
- Check distribution of age labels.  
- Visualize sample images and basic statistics.

### 3. Model Training
- Train CNN-based model using **TensorFlow/Keras** on GPU.  
- Split dataset into training, validation, and test sets.  
- Tune model hyperparameters and monitor training metrics.

### 4. Evaluation
- Evaluate model accuracy on test set.  
- Analyze predictions to identify common errors.  
- Compare performance against baseline methods.

### 5. Reporting
- Summarize model accuracy and reliability for age verification.  
- Provide recommendations for deployment and further improvements.

---
