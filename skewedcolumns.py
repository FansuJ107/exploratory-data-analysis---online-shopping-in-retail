import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataSkew:
    def __init__(self, data):
        self.data = data

    def identify_skewed_columns(self, threshold=0.5):
        skewed_cols = []
        for col in self.data.columns:
            if self.data[col].dtype in ['int64', 'float64']:
                skewness = self.data[col].skew()
                if abs(skewness) > threshold:
                    skewed_cols.append((col, skewness))
        return skewed_cols

    def visualize_skew(self, column):
        plt.figure(figsize=(10, 6))
        plt.hist(self.data[column], bins=30, color='skyblue', edgecolor='black')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

class DataFrameTransform:
    def __init__(self, data):
        self.data = data

    def apply_log_transform(self, column):
        self.data[column] = np.log1p(self.data[column])

    def apply_sqrt_transform(self, column):
        self.data[column] = np.sqrt(self.data[column])

# Load your DataFrame here
data = pd.read_csv('customer_activity.csv')

# Example usage
skew_analyzer = DataSkew(data)
skewed_columns = skew_analyzer.identify_skewed_columns(threshold=0.5)
print("Skewed Columns:")
for col, skewness in skewed_columns:
    print(f"{col}: Skewness = {skewness}")
    skew_analyzer.visualize_skew(col)

transformer = DataFrameTransform(data)
for col, _ in skewed_columns:
    transformer.apply_log_transform(col)  # or apply_sqrt_transform, etc.+9