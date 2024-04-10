import yaml
from sqlalchemy import create_engine
import pandas as pd

# Extract the credentials from the yaml file into a dictionary.
def extract_credentials():

    '''
    This function is used to extract the credentials from yaml to a dictionary to establish connection with the RDS.

    Returns:
        (dict): the credentials in dictionary format.
    '''

    with open('credentials.yaml', 'r') as file:
        return yaml.safe_load(file)

# Store the dictionary into a variable.
credentials: dict = extract_credentials()

# Creates class object to connect to RDS database and extract data.
class RDSDatabaseConnector():

    '''
    This class is used to establish a connection with the AiCore RDS containing loan payments information.

    Attributes:
        credentials_dict (dict): the dictionary containing the 'Host', 'Password', 'User', 'Database' and 'Port' required for the sqlalchemy to establish a connection with the RDS
    '''

    def __init__(self, credentials_dict: dict):

        '''
        This method is used to initialise this instance of the RDSDatabaseConnector class.

        Attributes:
            credentials_dict (dict): the dictionary containing the 'Host', 'Password', 'User', 'Database' and 'Port' required for the sqlalchemy to establish a connection with the RDS
        '''
        
        self.credentials_dict = credentials_dict # when class is initiated it requires the credentials argument.

    # Initialises SQLAlchemy engine.
    def create_engine(self):
        
        '''
        This method is used to create the SQLAlchemy engine which will be required to connect to the AiCore RDS.
        '''

        self.engine = create_engine(f"postgresql+psycopg2://{self.credentials_dict['RDS_USER']}:{self.credentials_dict['RDS_PASSWORD']}@{self.credentials_dict['RDS_HOST']}:{self.credentials_dict['RDS_PORT']}/{self.credentials_dict['RDS_DATABASE']}")

    # Establishes a connection to the database and creates a pandas dataframe from the 'customer_activity' table.
    def extract_customer_data(self):

        '''
        This method is used to establish a connection to the RDS and extract the necessary 'customer_activity' table into a pandas dataframe.

        Returns:
            (pd.DataFrame): a dataframe containing all the data from the 'customer_activity' table in the RDS that will be analysed.
        '''

        with self.engine.connect() as connection:
            self.customer_activity_df = pd.read_sql_table('customer_activity', self.engine)
            return self.customer_activity_df
    
# Writes the pandas dataframe into a csv file.
def save_data_to_csv(customer_activity_df: pd.DataFrame):

    '''
    This function is used to write the 'customer_activity' dataframe into a csv file using a context manager.

    Args:
        loans_df (pd.DataFrame): The 'customer_activity' dataframe that will be written into a csv file..
    '''

    with open('customer_activity.csv', 'w') as file:
        customer_activity_df.to_csv(file, encoding= 'utf-8', index= False)

def load_data_from_csv(file):
    return pd.read_csv(file)

if __name__ == '__main__':
    connector = RDSDatabaseConnector(credentials) # Instantiates the 'RDSDatabaseConnector' class using the .
    # Calling all defined methods:
    connector.create_engine() # Creates the sqlalchemy engine to establish connection.
    customer_activity_df: pd.DataFrame = connector.extract_customer_data() # Extracts sql data to a pandas dataframe.
    save_data_to_csv(customer_activity_df) # Writes the dataframe into a csv file.
    data = load_data_from_csv('customer_activity.csv')
    print("Data shape:", data.shape)
    print("Sample of the data:")
    print(data.head())
    print(data.columns)