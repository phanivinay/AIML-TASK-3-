# -------------------------------
# Task 3: Linear Regression in Python
# House Price Prediction Example
# -------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# -------------------------------
# 1. Import and preprocess dataset
# -------------------------------

df = pd.read_csv(r"C:\Users\phaniandey\Downloads\AIML-TASK3\house_prices.csv")
      # <-- change filename if needed
print("Dataset head:")
print(df.head())

# Select features (X) and target (y)
# Example: using Area and Bedrooms to predict Price
X = df[['Area', 'Bedrooms']]
y = df['Price']

# -------------------------------
# 2. Split train-test data
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# 3. Fit Linear Regression model
# -------------------------------

model = LinearRegression()
model.fit(X_train, y_train)

# Model coefficients
print("\nIntercept:", model.intercept_)
print("Coefficients:", model.coef_)

# -------------------------------
# 4. Model Evaluation
# -------------------------------

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE  :", mae)
print("MSE  :", mse)
print("R²   :", r2)

# -------------------------------
# 5. Plot Regression Line (for single feature)
# Example: Area vs Price
# -------------------------------

plt.scatter(df['Area'], df['Price'])
plt.xlabel("Area")
plt.ylabel("Price")

# Regression line (using only area)
area_only = df[['Area']]
price_pred_line = model.predict(df[['Area', 'Bedrooms']])

plt.plot(df['Area'], price_pred_line, linewidth=2)
plt.title("Regression Line: Area vs Price")
plt.show()
