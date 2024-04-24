# Project Title
Exploratory Data Analysis - Online Shopping in Retail

# Table of Contents
A description of the project
Installation instructions
Usage Instructions
File structure of the project
License Information


# A description of the project
The project involves analysing data for a large retail company where you have the task to conduct exploratory data analysis on a dataset of online shopping website activity. With the increasing popularity of online shopping, this dataset provides valuable insights into consumer behaviour. Various statistical and visualisation techniques are used to explore the data and draw meaningful insights and help provide a better understanding of customer behaviour and help the business optimise marketing strategies and improve their customer experience. The data contains information about the website activity of users over one year. Each sample represents the user interacting with the website during a shopping session. Overall, this project will showcase the power of exploratory data analysis in uncovering valuable insights from large datasets and how to leveraged these insights to drive business success

# Installation instructions
Download and clone repository:
Copy the repository URL by clicking '<> Code' above the list of files in GitHub Repo. Then copy and paste the 'HTTPS' URL:
in your CLI go to the location where you wish to clone your directory.
Type the following 'git clone' command with the 'HTTPS' URL:
https://github.com/FansuJ107/exploratory-data-analysis---online-shopping-in-retail.git

# Usage Instructions
1. Run the 'db_utils.py' file to extract the data from an AWS Relational Database and write it into the appropriate csv file. This requires the .yaml credentials for the AWS RDS.
Since this is confidential, SKIP THIS STEP, This file has already been run and the csv file has been included within this repository, as 'customer_activity.csv'.
2. The 'imputevalues.py', 'skewedcolumns.py' 'outliers.py' and 'drop_overly_corelated_columns.py' files can be updated to see in more detail the transformations that were done on every column at these steps.

# File structure of project
- credentials.yaml: File to store the database credentials. This file has been added to the .gitignore file in our repository as we don't want our credentials being pushed to GitHub for security reasons.

- customer_activity.csv: The data stored from the credentials.yaml file now in a table.

- dataframeinfo.py:  This is a script used to extract information from the DataFrame and its columns to extract meaningful information.

- datatransform.py: This is a script used to transform the columns and put into the correct format.

- db_utils.py: This is a script which extracts the data from a AWS RDS using the credentials.yaml file and ends up creating the customer_activity.csv file

- drop_overly_corelated_columns.py: This is a script which identifies highly correlated columns and remove them to improve the quality of the data.

- imputevalues.py: This is a script where we identify the variables with missing values and determine the percentage of missing values in each variable. Depending on the extent of missing data, you may choose to either impute the missing values or remove them from the dataset.

- outliers.py: This is a script where we remove outliers from the dataset which improvse the quality and accuracy of the analysis as outliers can distort the analysis results.

- skewedcolumns.py: This is a script where we skew the columns as it can lead to biased models and inaccurate results, so it's important to address this issue before proceeding with any analysis.

- customers_doing.py: This is a script where we get a visual representation of the performance of the website

- customer_software.py: This is a script where we get a visual representation of what systems our users are using to visit the website.

- effective_marketing.py: This is a script where we get a visual representation of the traffic coming to the website to see if the marketing team can make any improvements to their existing strategy. 

- revenue_generated.py: This is a script where we get a visual representation of where the website revenue is being generated and identifying any problematic areas in the data.

# License
This is an open source public repository. The dataset was obtained from Aicore. AiCore provided the necessary credentials to download the dataset from AWS RDS (these are not publicly available).
