import pandas as pd

data = {
    "Area": [1200,1500,1600,1700,1800,2000,2200,2400,2600,3000],
    "Bedrooms": [2,3,3,3,4,3,4,4,5,5],
    "Price": [150000,180000,200000,200000,250000,270000,300000,320000,350000,400000]
}

df = pd.DataFrame(data)
df.to_csv("house_prices.csv", index=False)

print("Created house_prices.csv successfully!")
