import pandas as pd
import matplotlib.pyplot as plt

# Load the data into a DataFrame
customer_data = pd.read_csv('customer_activity.csv')

# Revenue generated by region
revenue_by_region = customer_data.groupby('region')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
revenue_by_region.plot(kind='bar')
plt.title('Revenue Generated by Region')
plt.xlabel('Region')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

# Percentage of returning/new customers making a purchase
customer_purchase_percentage = customer_data.groupby('visitor_type')['revenue'].apply(lambda x: (x == True).sum() / len(x) * 100)
plt.figure(figsize=(8, 6))
customer_purchase_percentage.plot(kind='bar')
plt.title('Percentage of Returning/New Customers Making a Purchase')
plt.xlabel('Visitor Type')
plt.ylabel('Percentage')
plt.xticks(rotation=0)
plt.show()

# Sales comparison between weekends and weekdays
sales_weekend_weekday = customer_data.groupby('weekend')['revenue'].sum()
plt.figure(figsize=(8, 6))
sales_weekend_weekday.plot(kind='bar')
plt.title('Sales Comparison: Weekends vs. Weekdays')
plt.xlabel('Weekend')
plt.ylabel('Revenue')
plt.xticks([0, 1], ['Weekdays', 'Weekends'], rotation=0)
plt.show()

# Most effective months for generating sales
sales_by_month = customer_data.groupby('month')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sales_by_month.plot(kind='bar')
plt.title('Sales by Month')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()

# Contribution of traffic sources to sales
traffic_sales_contribution = customer_data.groupby('traffic_type')['revenue'].sum().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
traffic_sales_contribution.plot(kind='bar')
plt.title('Contribution of Traffic Sources to Sales')
plt.xlabel('Traffic Type')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.show()