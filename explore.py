import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

# *****************************************************************************************************

cols = ['parcel_id', 'bed_rooms', 'bath_rooms', 'finished_sqft', 'year_built', 'county', 'log_error']

def plot_variable_pair(df, cols= cols):
    for i in cols:
        sns.lmplot(x=i, y="tax_value", data=df, line_kws={'color': 'red'})
        plt.show()


# *****************************************************************************************************

var1 = train[['area', 'taxvalue', 'yearbuilt', 'taxamount']]
var2 = train[['county', 'bedrooms', 'bathrooms']]

def plot_categorical_and_continuius_vars(df):
    for var1, var2 in zip(var1, var2):
        sns.lmplot(y=var1, x=var2, data=train.sample(1000), line_kws={'color': 'red'})
        plt.show()