import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Path to your Excel file
file_path = r"/content/shopping_trends_large.csv"
print(f"File path: {file_path}")

# Read the Excel file
shop = pd.read_csv(file_path)

# Display basic information
print(shop.head())
print(shop.dtypes)
print(shop.columns)
print(shop.info())
print(shop.isnull().sum())
#1. What is the overall distribution of customer ages in the dataset?
plt.figure(figsize=(8, 5))
sns.histplot(shop['Age'], kde=True, bins=20)
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
#2. How does the average purchase amount vary across different product categories?
avg_purchase_by_category = shop.groupby('Category')['Purchase Amount'].mean()
print(avg_purchase_by_category)
avg_purchase_by_category.plot(kind='bar', title='Average Purchase by Category', figsize=(8, 5))
plt.ylabel('Average Purchase Amount')
plt.show()
#3Which gender has the highest number of purchases?
gender_purchases = shop['Gender'].value_counts()
print(gender_purchases)
gender_purchases.plot(kind='bar', title='Purchases by Gender', color=['blue', 'pink'])
plt.xlabel('Gender')
plt.ylabel('Number of Purchases')
plt.show()
#4 What are the most commonly purchased items in each category?
top_items_per_category = shop.groupby('Category')['Item'].value_counts().groupby(level=0).head(1)
print(top_items_per_category)
#4. What are the most commonly purchased items in each category?
top_items_per_category = shop.groupby('Category')['Item'].value_counts().groupby(level=0).head(1)
print(top_items_per_category)
#5. Are there any specific seasons or months where customer spending is significantly higher?
shop['Month'] = pd.to_datetime(shop['Purchase Date']).dt.month
seasonal_spending = shop.groupby('Month')['Purchase Amount'].sum()
print(seasonal_spending)
seasonal_spending.plot(kind='line', title='Customer Spending by Month', marker='o')
plt.ylabel('Total Spending')
plt.show()
#6. What is the average rating given by customers for each product category?
avg_rating_by_category = shop.groupby('Category')['Rating'].mean()
print(avg_rating_by_category)
avg_rating_by_category.plot(kind='bar', title='Average Rating by Category', figsize=(8, 5))
plt.ylabel('Average Rating')
plt.show()
#7. Are there any notable differences in purchase behavior between subscribed and non-subscribed customers?
subscribed_behavior = shop.groupby('Subscription Status')['Purchase Amount'].mean()
print(subscribed_behavior)
subscribed_behavior.plot(kind='bar', title='Purchase Behavior: Subscribed vs Non-Subscribed')
plt.ylabel('Average Purchase Amount')
plt.show()
#8. Which payment method is the most popular among customers?
popular_payment_methods = shop['Payment Method'].value_counts()
print(popular_payment_methods)
popular_payment_methods.plot(kind='pie', autopct='%1.1f%%', title='Most Popular Payment Methods')
plt.show()
#9. Do customers who use promo codes tend to spend more than those who don't?
promo_vs_no_promo = shop.groupby('Promo Code Used')['Purchase Amount'].mean()
print(promo_vs_no_promo)
promo_vs_no_promo.plot(kind='bar', title='Spending: Promo Code vs No Promo Code')
plt.ylabel('Average Purchase Amount')
plt.show()
#10. How does the frequency of purchases vary across different age groups?
age_groups = pd.cut(shop['Age'], bins=[0, 18, 30, 50, 70], labels=['Teen', 'Young Adult', 'Middle-Aged', 'Senior'])
age_group_purchases = shop.groupby(age_groups)['Purchase Amount'].count()
print(age_group_purchases)
age_group_purchases.plot(kind='bar', title='Frequency of Purchases by Age Group')
plt.ylabel('Number of Purchases')
plt.show()


