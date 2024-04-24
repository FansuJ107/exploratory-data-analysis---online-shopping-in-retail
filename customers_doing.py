import pandas as pd

# Load data into a DataFrame
customer_activity = pd.read_csv('customer_activity.csv')  

# Proportion of sales on weekends vs. weekdays
sales_by_weekend = customer_activity[customer_activity['revenue'] == True].groupby('weekend').size()
sales_percentage_by_weekend = (sales_by_weekend / sales_by_weekend.sum()) * 100

# Regions generating the most revenue
revenue_by_region = customer_activity[customer_activity['revenue'] == True].groupby('region')['page_values'].sum().sort_values(ascending=False)

# Website traffic types and their correlation with sales
traffic_sales = customer_activity[customer_activity['revenue'] == True].groupby('traffic_type').size().sort_values(ascending=False)

# Percentage of time spent on different tasks
total_duration = customer_activity[['administrative_duration', 'informational_duration', 'product_related_duration']].sum()
task_percentage = (total_duration / total_duration.sum()) * 100

# Average duration of informational/administrative tasks
avg_admin_duration = customer_activity.groupby('administrative')['administrative_duration'].mean().sort_values(ascending=False)
avg_info_duration = customer_activity.groupby('informational')['informational_duration'].mean().sort_values(ascending=False)

# Breakdown of months with the most sales
sales_by_month = customer_activity[customer_activity['revenue'] == True].groupby('month').size().sort_values(ascending=False)

# Display results
print("1. Proportion of sales on weekends vs. weekdays:")
print(sales_percentage_by_weekend)
print("\n2. Regions generating the most revenue:")
print(revenue_by_region)
print("\n3. Website traffic types and their correlation with sales:")
print(traffic_sales)
print("\n4. Percentage of time spent on different tasks:")
print(task_percentage)
print("\n5. Average duration of informational/administrative tasks:")
print("Administrative tasks:", avg_admin_duration)
print("Informational tasks:", avg_info_duration)
print("\n6. Breakdown of months with the most sales:")
print(sales_by_month)