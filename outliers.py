import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Plotter:

    def plot_null_values(df):
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis', yticklabels=False)
        plt.title('Missing Values Heatmap')
        plt.show()
    
  
    def visualise_outliers(df):
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=df, orient='h')
        plt.title('Outlier Visualization')
        plt.show()

class DataFrameTransform:
   
    def check_null_values(df):
        return df.isnull().sum()

   
    def drop_columns_with_null(df, threshold=0.5):
        """
        Drop columns with null values exceeding the specified threshold.
        :param df: DataFrame
        :param threshold: float, threshold for null values percentage
        :return: DataFrame with dropped columns
        """
        null_percentage = df.isnull().mean()
        columns_to_drop = null_percentage[null_percentage > threshold].index
        return df.drop(columns=columns_to_drop)


    def impute_null_values(df, strategy='mean'):
        """
        Impute null values in DataFrame columns.
        :param df: DataFrame
        :param strategy: str, 'mean' or 'median'
        :return: DataFrame with imputed values
        """
        numeric_cols = df.select_dtypes(include=['number']).columns
        if strategy == 'mean':
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
        elif strategy == 'median':
            df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        else:
            raise ValueError("Invalid imputation strategy. Please choose 'mean' or 'median'.")
        return df

   
    def remove_outliers(df, columns, z_threshold=3):
        """
        Remove outliers from the DataFrame.
        :param df: DataFrame
        :param columns: list, columns to check for outliers
        :param z_threshold: int, z-score threshold for identifying outliers
        :return: DataFrame with outliers removed
        """
        df_no_outliers = df.copy()
        for column in columns:
            z_scores = np.abs((df_no_outliers[column] - df_no_outliers[column].mean()) / df_no_outliers[column].std())
            df_no_outliers = df_no_outliers[z_scores < z_threshold]
        return df_no_outliers


# Load your DataFrame
df = pd.read_csv("customer_activity.csv")

# Checking NULL values
null_counts = DataFrameTransform.check_null_values(df)
print("Null Value Counts:")
print(null_counts)

# Dropping columns with more than 50% missing values
cleaned_df = DataFrameTransform.drop_columns_with_null(df, threshold=0.5)
print("Cleaned DataFrame Shape after dropping columns with high NULL values:", cleaned_df.shape)

# Impute NULL values
cleaned_df_imputed = DataFrameTransform.impute_null_values(cleaned_df, strategy='mean')

# Check NULL values after imputation
null_counts_after_imputation = DataFrameTransform.check_null_values(cleaned_df_imputed)
print("Null Value Counts after imputation:")
print(null_counts_after_imputation)

# Plot null values
Plotter.plot_null_values(cleaned_df_imputed)

# Visualize outliers
Plotter.visualise_outliers(cleaned_df_imputed)

# Remove outliers
columns_to_check_for_outliers = cleaned_df_imputed.select_dtypes(include=['number']).columns
cleaned_df_no_outliers = DataFrameTransform.remove_outliers(cleaned_df_imputed, columns_to_check_for_outliers)

# Re-visualize after removing outliers
Plotter.visualise_outliers(cleaned_df_no_outliers)