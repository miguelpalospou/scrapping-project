import src.transformation as clean
import src.scraper as extract
import src.visualization as viz
import os


df=extract.scrape_iqair()
df1=extract.convert_1()
df2=extract.convert_2()
df3=extract.convert_3()
df4=extract.convert_4()
extract.scrape_iqair()
extract.convert_1(df1)
extract.convert_2(df2)
extract.convert_3(df3)
extract.convert_4(df4)



clean.clean_1(df)
clean.clean_2(df)
clean.clean_3(df)
clean.clean_4(df)
clean.clean_5(df)
clean.merge(df)

viz.corr_matrix (df)
viz.heat_map (df)
viz.pollution_plot(df)
viz.pollution_plot(df)
viz.deaths_plot(df)
viz.sales_chargers(df) 
viz.sales_pollution (df)
