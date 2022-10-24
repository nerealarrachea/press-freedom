from lib2to3.pgen2.pgen import DFAState
import pandas as pd

def all_clean(df):
    df['Change in position'] = df['Position 2021'] - df['Position 2022']
    df.loc['Mexico', 'Region'] = 'North America'
    df.loc['Nicaragua', 'Region'] = 'South America'
    return df 

def merging(var1,var2,var3):
    df_hdi = pd.merge(var1, var2, on=["Year", "Country code", "Country"], how="left")
    df_hdi = pd.merge(df_hdi, var3, on=["Year", "Country code", "Country"], how="left")
    df_hdi = df_hdi.set_index('Country')
    df_hdi.drop(['Country code', 'Year'], axis = 1, inplace = True) 
    return df_hdi

def merging_(df_1,df_2):
    df = pd.merge(df_1, df_2, on=["Country"], how="left") 
    return df
