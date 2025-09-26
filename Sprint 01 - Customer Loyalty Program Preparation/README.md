# 📊 Project 01 - Customer Loyalty Program Preparation  

## 📌 Project Overview  
The e-commerce company **Store 1** is preparing the launch of a new **Customer Loyalty Program**.  
To achieve this, the company needs to analyze its customer database and ensure the data is **clean, consistent, and well-organized**.  

The main objective is to design **personalized campaigns** and **optimize marketing actions** by segmenting customers based on variables such as:  
- Age  
- Purchase history  
- Product categories purchased  

As part of the analytics team, your task in this first phase is to **prepare the data for analysis**.  

---

## 🎯 Project Objectives  
- Clean customer profiles.  
- Standardize names and ages.  
- Calculate the total spending per customer.  
- Validate data consistency and correct errors.  
- Prepare data to generate **business KPIs**.  

---

## 📂 Dataset Description  
The dataset is provided as a **Python list** with the following structure:  

| Column Name         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `usuario_id`        | Unique identifier for each customer                                         |
| `usuario_nombre`    | Customer’s name                                                             |
| `usuario_edad`      | Customer’s age                                                              |
| `categorias_fav_low`| List of favorite product categories purchased (e.g., ELECTRÓNICA, DEPORTE) |
| `gasto_por_categoria` | List of integers with the total amount spent per favorite category        |

**Example of raw data (Python list):**
```python
usuarios = [ 
    ['32415', ' mike_reed ', 32.0, ['ELECTRÓNICA', 'DEPORTE', 'LIBROS'], [894, 213, 173]],
    ['31980', 'kate morgan', 24.0, ['ROPA', 'LIBROS'], [439, 390]],
    ['32156', ' john doe ', 37.0, ['ELECTRÓNICA', 'HOGAR', 'COMIDA'], [459, 120, 99]],
    ['32761', 'SAMANTHA SMITH', 29.0, ['ROPA', 'ELECTRÓNICA', 'BELLEZA'], [299, 679, 85]],
    ...
]
