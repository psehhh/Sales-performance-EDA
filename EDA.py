import numpy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Superstore.csv", encoding='latin1')  
print(df.head())

#EDA
df.info()
df.isnull().sum()
df.duplicated().sum()

df['Order Date']= pd.to_datetime(df['Order Date'])
df['Ship Date']= pd.to_datetime(df['Ship Date'])
df['Month_Year'] = df['Order Date'].dt.to_period('M')

region_data= df.groupby("Region")[['Sales', 'Profit']].sum().sort_values("Sales", ascending=False)
print(region_data)

region_data.plot(kind="bar", figsize=(10,6))
plt.title("Sales and Profit by Region")
plt.ylabel("Amount")
plt.xlabel("Region")
plt.show()

cat_data= df.groupby(["Category", "Sub-Category"])['Sales'].sum().sort_values(ascending=False)
print(cat_data)
cat_data.plot(kind='bar', figsize=(12,6), color='black')
plt.title("Sales by Sub-Category")
plt.ylabel("Sales")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

monthly_sales= df.groupby("Month_Year")['Sales'].sum()
print(monthly_sales)

monthly_sales.plot(kind='line')
plt.title("Monthly Sales Trend")
plt.ylabel("Sales")
plt.xlabel("Month-Year")
plt.show()

top_products= df.groupby("Product Name")["Profit"].sum().sort_values(ascending=False).head(10)

top_products.plot(kind= "barh", color="cyan")
plt.title("Top 10 Profitable Products")
plt.xlabel("Total Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

corr = df[['Sales', 'Quantity', 'Discount', 'Profit']].corr()

plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()
