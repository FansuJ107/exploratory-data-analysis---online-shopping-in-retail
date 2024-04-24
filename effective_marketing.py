import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV or database
customer_activity = pd.read_csv('customer_activity.csv')

# Visualize traffic generating most revenue by region
revenue_by_region = customer_activity.groupby('region')['page_values'].sum().sort_values(ascending=False)
revenue_by_region.plot(kind='bar', xlabel='Region', ylabel='Total Revenue', title='Revenue by Region')
plt.show()

# Identify traffic with the highest bounce rate by region
highest_bounce_rates = customer_activity.groupby(['region', 'traffic_type'])['bounce_rates'].mean().unstack()
highest_bounce_rates.plot(kind='bar', stacked=True, xlabel='Region', ylabel='Mean Bounce Rate', 
                          title='Mean Bounce Rate by Traffic Type and Region')
plt.legend(title='Traffic Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

# Determine months with the most sales from ads traffic
ads_traffic = customer_activity[customer_activity['traffic_type'].str.contains('ads', case=False)]
sales_by_month = ads_traffic.groupby('month')['revenue'].sum()

# Ensure all months are included in the visualization
all_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales_by_month = sales_by_month.reindex(all_months, fill_value=0)

sales_by_month.plot(kind='line', marker='o', xlabel='Month', ylabel='Total Sales', 
                    title='Total Sales from Ads Traffic by Month')
plt.xticks(rotation=45)
plt.show()