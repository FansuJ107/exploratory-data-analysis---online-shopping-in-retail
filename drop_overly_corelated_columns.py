import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

class Plotter:
    
    def plot_correlation_matrix(df):
        # Drop non-numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Matrix')
        plt.show()


class DataFrameTransform:
   
    def remove_highly_correlated_columns(df, threshold=0.8):
        """
        Remove highly correlated columns from the DataFrame.
        :param df: DataFrame
        :param threshold: float, correlation threshold
        :return: DataFrame with highly correlated columns removed
        """
        # Drop non-numeric columns
        numeric_df = df.select_dtypes(include=[np.number])
        
        corr_matrix = numeric_df.corr().abs()
        upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
        to_drop = [column for column in upper.columns if any(upper[column] > threshold)]
        return df.drop(columns=to_drop)

# Load your DataFrame
df = pd.read_csv("customer_activity.csv")

# Compute and visualize the correlation matrix
Plotter.plot_correlation_matrix(df)

# Identify and decide which columns to remove based on a correlation threshold
threshold = 0.8  
# Drop non-numeric columns before computing the correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
correlation_matrix = numeric_df.corr().abs()
highly_correlated_columns = correlation_matrix[correlation_matrix > threshold].stack().index.tolist()

# Print highly correlated columns
print("Highly correlated columns:")
for pair in highly_correlated_columns:
    if pair[0] != pair[1]:
        print(pair)

# Remove highly correlated columns
cleaned_df = DataFrameTransform.remove_highly_correlated_columns(df, threshold=threshold)
print("Cleaned DataFrame Shape after removing highly correlated columns:", cleaned_df.shape)