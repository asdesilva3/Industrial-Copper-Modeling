# Industrial Copper Modeling


## Table of Contents

1. [Project Overview](#project-overview)
2. [Problem Statement](#problem-statement)
3. [Solution Steps](#solution-steps)
4. [Approach](#approach)
5. [Workflow](#workflow)
6. [Data Description](#data-description)
7. [Learning Outcomes](#learning-outcomes)
8. [Technologies Used](#technologies-used)
9. [How to Run](#how-to-run)



## Project Overview
This project aims to address challenges in the copper industry related to pricing prediction and lead classification using machine learning techniques.

## Problem Statement
The copper industry faces challenges with skewed and noisy data affecting pricing decisions and lead classification. Machine learning models can address these issues by utilizing advanced techniques and algorithms.

## Solution Steps
1. **Exploring Data Skewness and Outliers:** Identify and visualize skewness and outliers in the dataset.
2. **Data Preprocessing:** Handle missing values, treat outliers, address skewness, and encode categorical variables.
3. **Machine Learning Models:**
   - Regression Model: Predict the continuous variable 'Selling_Price'.
   - Classification Model: Predict the status (WON or LOST).
4. **Creating Streamlit Page:** Develop an interactive web application where users can input values for prediction.

## Approach
1. **Data Understanding:** Identify variable types and distributions, and handle garbage values.
2. **Data Preprocessing:** Handle missing values, outliers, and skewness. Encode categorical variables.
3. **EDA:** Visualize outliers and skewness.
4. **Feature Engineering:** Create new features and drop highly correlated columns.
5. **Model Building and Evaluation:** Train and evaluate regression and classification models using appropriate metrics.
6. **Model GUI:** Create an interactive web page using Streamlit for model predictions.

## Workflow

![Copper](https://github.com/asdesilva3/Industrial-Copper-Modeling/assets/148002331/3c7b52c5-a10e-4073-b7ee-b2ad9b8da28b)


## Data Description
The dataset includes various columns such as 

* `id`: Unique identifier for each transaction or item.
* `item_date`: Date when each transaction or item was recorded.
* `quantity tons`: Quantity of the item in tons.
* `customer`: Name or identifier of the customer associated with each transaction.
* `country`: Country associated with each customer.
* `status`: Current status of the transaction or item.
* `item type`: Category or type of the items being sold or produced.
* `application`: Specific use or application of the items.
* `thickness`: Thickness of the items.
* `width`: Width of the items.
* `material_ref`: Reference or identifier for the material used in the items.
* `product_ref`: Reference or identifier for the specific product.
* `delivery date`: Expected or actual delivery date for each item or transaction.
* `selling_price`: Price at which the items are sold.


## Learning Outcomes
The project aims to develop proficiency in Python programming, data preprocessing, EDA, machine learning modeling, and web application development using Streamlit. Key learning outcomes include understanding data analysis techniques, machine learning algorithms, and challenges in the manufacturing domain.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

## How to Run
1. Install the required dependencies using 
`pip install -r requirements.txt`

2. Run the Streamlit application using 
`streamlit run app.py`
