import pandas as pd
from functools import reduce

def clean_1(df):
    # pivoting in order to transpose the years, which are now in different columns
    df=pollution_2 = pd.melt(df, id_vars=['Country/Region', 'Population'], value_vars=['2018', '2019', '2020', '2021', '2022'], var_name='Year', value_name='Pollution')

    # changing columns names and removing "-"
    pollution_2.rename(columns = {"Country/Region": "region", "Population":"population", "Pollution":"pollution", "Year":"year"}, inplace=True)
    pollution_2.drop(pollution_2[pollution_2['pollution'] == '-'].index, inplace = True)
    pollution_2.dropna()
    # removing white spaces
    pollution_2['region'].str.strip()
    pollution_2['year'].str.strip()
    # converting to int
    pollution_2['year'] = pollution_2['year'].astype(int)
    pollution_2['pollution'] = pollution_2['pollution'].astype(float)
    return pollution_2

def clean_2(chargers):
    # taking the columns that interest me
    chargers_2= chargers.iloc[:, [0,5, 7]]
    chargers_2['region'].str.strip()
    # changing columns name
    chargers_2.rename(columns = {"value":"number of chargers"}, inplace=True)
    # created a subset. The dataset I worked with has multiple entries for one same year and same region, that's because 
    # some where introduced later on and were not summed. I created a subset with the sum.
    chargers_3=chargers_2.groupby(['region', 'year'])['number of chargers'].sum()
    return chargers_3

def clean_3(sales):
    sales_2= sales.iloc[:, [0,5, 7]]
    sales_2.rename(columns = {"value":"sales"}, inplace=True)
    sales_2['region'].str.strip()
    # created a subset. The dataset I worked with has multiple entries for one same year and same region, that's because 
    # some where introduced later on and were not summed. I created a subset with the sum.
    sales_3=sales_2.groupby(['region', 'year'])['sales'].sum()
    return sales_3

def clean_4(stock):
    stock_2= stock.iloc[:, [0,5, 7]]
    stock_2.rename(columns = {"value":"stock price %"}, inplace=True)
    stock_2['region'].str.strip()
    return stock_2

def clean_5(deaths):
    deaths_2= deaths.iloc[:, [0,2, 3]]
    deaths_2.rename(columns = {"Entity": "region", "Deaths - Cause: All causes - Risk: Outdoor air pollution - OWID - Sex: Both - Age: All Ages (Number)":"number of deaths by air pollution", "Year":"year"}, inplace=True)
    deaths_2['region'].str.strip()
    # creating a mask to change region names from United States to USA so that it matches the other ddbb.
    mask_USA = deaths_2['region'].str.contains('United States', case=False)
    deaths_2.loc[mask_USA, 'region'] = 'USA' 
    # created a subset. The dataset I worked with has multiple entries for one same year and same region, that's because 
    # some where introduced later on and were not summed. I created a subset with the sum.
    deaths_3=deaths_2.groupby(['region', 'year'])['number of deaths by air pollution'].sum()
    return deaths_3

def merge(tables):
    # merging previous 4 public ddbb + scrapped db. Using outer merge in order to keep as much info as possible
    df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['region', 'year'], how='outer'), tables)
    return df_merged

