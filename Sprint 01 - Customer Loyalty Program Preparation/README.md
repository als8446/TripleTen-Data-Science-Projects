# 📊 Project 01 - Customer Loyalty Program Preparation  

## 📌 Project Overview  
As part of the data analytics team at **Store 1**, my task in the first phase was to **prepare the data for analysis**.  
The company was launching a new **Customer Loyalty Program** and needed to ensure its customer database was **clean, consistent, and organized**.  

The main goal of this phase was to support the design of **personalized marketing campaigns** by segmenting customers based on variables such as:  
- Age  
- Purchase history  
- Product categories purchased  

---

## 🎯 My Objectives  
- Clean customer profiles.  
- Standardize names and ages.  
- Calculate total spending per customer.  
- Validate data consistency and correct errors.  
- Prepare the dataset to generate **business KPIs**.  

---

## 📂 Dataset Description  
I worked with a dataset provided as a **Python list** with the following structure:  

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
