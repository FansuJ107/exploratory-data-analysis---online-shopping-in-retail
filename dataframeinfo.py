import pandas as pd
from db_utils import RDSDatabaseConnector

class DataTransform:
    
    def convert_to_categorical(df, columns):
        for col in columns:
            df[col] = df[col].astype('category')
        return df


    def convert_to_numeric(df, columns):
        for col in columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        return df

   
    def convert_month_to_categorical(df, month_column):
        df[month_column] = df[month_column].astype('category')
        return df

    
    def convert_weekend_to_binary(df, weekend_column):
        df[weekend_column] = df[weekend_column].astype(int)  # Convert boolean to integer directly
        return df


class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        return self.df.dtypes

    def extract_statistics(self):
        return self.df.describe()

    def count_distinct_values(self):
        distinct_counts = {}
        for col in self.df.select_dtypes(include=['category', 'object']):
            distinct_counts[col] = self.df[col].nunique()
        return distinct_counts

    def print_shape(self):
        print("DataFrame shape:", self.df.shape)

    def count_null_values(self):
        null_counts = self.df.isnull().sum()
        null_percentage = (null_counts / len(self.df)) * 100
        return pd.DataFrame({'Null Count': null_counts, 'Null Percentage': null_percentage}, index=self.df.columns)


if __name__ == "__main__":
    df = pd.read_csv("customer_activity.csv")

    transformed_df = DataTransform.convert_to_categorical(df, ['operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type'])
    transformed_df = DataTransform.convert_to_numeric(df, ['administrative_duration', 'informational_duration', 'product_related_duration', 'bounce_rates', 'exit_rates', 'page_values'])
    transformed_df = DataTransform.convert_month_to_categorical(df, 'month')

    info = DataFrameInfo(transformed_df)
    print("Column Data Types:")
    print(info.describe_columns())
    print("\nStatistics:")
    print(info.extract_statistics())
    print("\nDistinct Value Counts:")
    print(info.count_distinct_values())
    print("\nDataFrame Shape:")
    info.print_shape()
    print("\nNull Value Counts:")
    print(info.count_null_values())
