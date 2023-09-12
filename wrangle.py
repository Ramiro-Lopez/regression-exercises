 #standard ds imports
import pandas as pd
import numpy as np
import os

#visualization imports
import matplotlib.pyplot as plt
import seaborn as sns

#import custom modules
import env

#ignore warnings
import warnings
warnings.filterwarnings("ignore")


def get_connection(db: str, user: str = env.user, host: str = env.host, password=env.password) -> str:
    return f"mysql+pymysql://{user}:{password}@{host}/{db}"

# ***********************************************************************************************************************************************************

def get_zillow_data(file_name="zillow.csv") -> pd.DataFrame:
    if os.path.isfile(file_name):
        return pd.read_csv(file_name)
    query = """select propertylandusedesc, bedroomcnt, 
               bathroomcnt, calculatedfinishedsquarefeet, 
               taxvaluedollarcnt, yearbuilt, taxamount, fips
               from propertylandusetype 
               join properties_2017
               using (propertylandusetypeid)
               where propertylandusedesc = 'Single Family Residential'
            """
    connection = get_connection("zillow")
    df = pd.read_sql(query, connection)
    df.to_csv(file_name, index=False)
    return df

# ***********************************************************************************************************************************************************

def wrangle_zillow(df):
    '''
    This function takes in a dataframe
    renames the columns and drops nulls values
    Additionally it changes datatypes for appropriate columns
    and renames fips to actual county names.
    Then returns a cleaned dataframe
    '''
    df = df.rename(columns = {'bedroomcnt':'bedrooms',
                     'bathroomcnt':'bathrooms',
                     'calculatedfinishedsquarefeet':'area',
                     'taxvaluedollarcnt':'taxvalue',
                     'fips':'county'})
    
    df = df.dropna()
    
    make_ints = ['bedrooms','area','taxvalue','yearbuilt', 'county']

    for col in make_ints:
        df[col] = df[col].astype(int)
        
    
    
    return df

