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


df = pd.read_csv('customer_activity.csv')

transformed_df = DataTransform.convert_to_categorical(df, ['operating_systems', 'browser', 'region', 'traffic_type', 'visitor_type'])
transformed_df = DataTransform.convert_to_numeric(df, ['administrative_duration', 'informational_duration', 'product_related_duration', 'bounce_rates', 'exit_rates', 'page_values'])
transformed_df = DataTransform.convert_month_to_categorical(df, 'month')
