import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import re
import numpy as np
import requests
from bs4 import BeautifulSoup
import pycountry
import pycountry_convert as pc
import country_converter as coco
import geopandas as gpd
from matplotlib.colors import ListedColormap
from functools import reduce
import os

def convert(df1,df2,df3,df4):
    df1=chargers=pd.read_csv("data/IEA-EV-dataEV charging pointsEVHistorical.csv")
    df2=sales=pd.read_csv("data/IEA-EV-dataEV salesCarsHistorical.csv") 
    df3=stock=pd.read_csv("data/IEA-EV-dataEV stock shareCarsHistorical.csv") 
    df4=deaths=pd.read_csv("data/number-of-deaths-by-risk-factor.csv") 
    return chargers, sales, stock, deaths


def scrape_iqair():
    print("---SCRAPPINGGG---")
    os.system("say scraping")
    url = "https://www.iqair.com/world-most-polluted-countries"
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    results=soup.find_all("div", attrs = {"class": "inner-table"})
    df=pd.read_html(results[0].prettify())[0]
    return df
