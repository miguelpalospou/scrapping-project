import src.transformation as clean
import src.scraper as extract
import src.visualization as viz
import os
from functools import reduce
import seaborn as sns


df=extract.scrape_iqair()
df1=extract.convert_1()
df2=extract.convert_2()
df3=extract.convert_3()
df4=extract.convert_4()
"""
extract.scrape_iqair()
extract.convert_1(df1)
extract.convert_2(df2)
extract.convert_3(df3)
extract.convert_4(df4)
"""


tables = [clean.clean_1(df),clean.clean_2(df1),clean.clean_3(df2), clean.clean_4(df3),clean.clean_5(df4)]

df = clean.merge(tables)

valu = viz.corr_matrix(df)
viz.heat_map (valu)
viz.pollution_plot(df)
viz.pollution_plot(df)
viz.deaths_plot(df)
viz.sales_chargers(df) 
viz.sales_pollution (df)
