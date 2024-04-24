import matplotlib.pyplot as plt
import pandas as pd

# Load data into a DataFrame
customer_activity = pd.read_csv('customer_activity.csv')  

# Drop rows with missing values in the 'operating_systems' column
customer_activity = customer_activity.dropna(subset=['operating_systems'])

# Count of operating systems used to visit the site and the percentage of the total
operating_system_counts = customer_activity['operating_systems'].value_counts()
operating_system_percentages = operating_system_counts / operating_system_counts.sum() * 100

plt.figure(figsize=(10, 6))
operating_system_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Operating Systems Used to Visit the Site')
plt.xlabel('Operating System')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
operating_system_percentages.plot(kind='pie', autopct='%1.1f%%', colors=['lightcoral', 'lightgreen', 'lightblue'])
plt.title('Percentage of Operating Systems Used to Visit the Site')
plt.ylabel('')
plt.tight_layout()
plt.show()

# Define the list of mobile operating systems
mobile_os_list = ['Android', 'iOS']

# Define the list of desktop operating systems
desktop_os_list = ['Windows', 'MACOS', 'ChromeOS', 'Ubuntu', 'Other']

# Filter for mobile operating systems and count occurrences
mobile_os_counts = customer_activity['operating_systems'].isin(mobile_os_list).sum()

# Filter for desktop operating systems and count occurrences
desktop_os_counts = customer_activity['operating_systems'].isin(desktop_os_list).sum()

# Plot the bar chart for mobile and desktop operating systems
plt.figure(figsize=(10, 6))
plt.bar(['Mobile', 'Desktop'], [mobile_os_counts, desktop_os_counts], color=['lightgreen', 'skyblue'])
plt.title('Number of Users Visiting the Site by Operating System Type')
plt.xlabel('Operating System Type')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# Most commonly used browsers and their breakdown on mobile versus desktop
browser_counts = customer_activity['browser'].value_counts()

# Define the list of mobile browsers
mobile_browser_list = ['Chrome Mobile', 'Safari', 'Samsung Internet']

# Define the list of desktop browsers
desktop_browser_list = ['Chrome', 'Edge', 'Firefox',
                        'Sogou Explorer', 'Opera', 'Yandex', 'QQ Browser',
                        'Internet Explorer', 'UC Browser', 'Undetermined']

# Filter for mobile browsers based on mobile operating systems
mobile_browser_counts = customer_activity[customer_activity['browser'].isin(mobile_browser_list)]['browser'].value_counts()

# Filter for desktop browsers based on desktop operating systems
desktop_browser_counts = customer_activity[customer_activity['browser'].isin(desktop_browser_list)]['browser'].value_counts()

plt.figure(figsize=(12, 6))
plt.bar(mobile_browser_counts.index, mobile_browser_counts.values, color='lightgreen', label='Mobile')
plt.bar(desktop_browser_counts.index, desktop_browser_counts.values, color='skyblue', label='Desktop')
plt.title('Most Commonly Used Browsers by Operating System Type')
plt.xlabel('Browser')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Analysis of popular operating systems and discrepancies in regions
popular_os = operating_system_counts.idxmax()
region_os_counts = customer_activity.groupby('region')['operating_systems'].apply(lambda x: (x == popular_os).sum())
region_os_counts.plot(kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Count of ' + popular_os + ' Users by Region')
plt.xlabel('Region')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()