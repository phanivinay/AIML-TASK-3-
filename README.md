Task 3: Linear Regression – AIML Project

This project demonstrates the implementation of Simple and Multiple Linear Regression using Python.
You will learn how to preprocess data, train regression models, evaluate performance, and interpret results.

📌 Objective

Understand the concepts of linear regression

Implement simple and multiple linear regression using scikit-learn

Evaluate model performance using MAE, MSE, RMSE, R² Score

Visualize regression results and regression line

Interpret model coefficients

🛠 Tools & Libraries Used

Python

Pandas – Data Handling

NumPy – Numerical Operations

Scikit-learn – Regression Models

Matplotlib / Seaborn – Visualization

📂 Dataset

You can use any numeric dataset suitable for regression, such as:

✔ House Price Prediction Dataset
✔ Salary vs Experience Dataset
✔ Advertising Dataset

Example dataset (House Price Prediction):
👉 Click here to download dataset (replace link in your repository)

📘 Steps Performed in the Project
1️⃣ Import & Load Dataset

Load CSV file using pandas

Check shape, null values, and statistical summary

2️⃣ Data Preprocessing

Handle missing values

Convert categorical columns (if any)

Select input features (X) and target variable (y)

3️⃣ Train-Test Split

Use:

from sklearn.model_selection import train_test_split


Split the dataset (80% training, 20% testing)

4️⃣ Build Linear Regression Model

Use:

from sklearn.linear_model import LinearRegression


Fit the model

Predict values

5️⃣ Model Evaluation

Metrics used:

MAE – Mean Absolute Error

MSE – Mean Squared Error

RMSE – Root Mean Squared Error

R² Score – Coefficient of Determination

6️⃣ Plotting the Regression Line

Visualize relationship between feature and target

Plot regression line for simple regression

7️⃣ Interpret Model Coefficients

Understand slope & intercept

Analyze how features impact the target variable

📊 Output

Regression Model Performance

Plot of regression line

Predicted vs Actual values table

Insights & interpretation
