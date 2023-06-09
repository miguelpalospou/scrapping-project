![iron](https://coursereport-s3-production.global.ssl.fastly.net/uploads/school/logo/84/original/logo-ironhack-blue.png)

# II - DATA PIPELINES

## The aim of this project is to build a data pipeline to enrich an existing public dataset. For this goal, multiple public datasets will be combined together with a database scrapped from a website.


## As we all know, there is a growing tendency to purchase electric cars. Not only they are becoming popular but also governments are fostering it by providing aids for people to purchase electric cars.

### This project goal is to democratize data about electric cars evolution and its enviromental and health impact, if any.


#### The chosen scrapped dataset was "World-most-polluted-countries" from iqair.com. The scrapped table provides historical data about the most polluted country and region ranking based on annual average PM2.5 concentration (μg/m³).

####  In order to enrich this dataset, 3 other indicators will be considered and added: 1) charging points around the world, 2) sales cars history, 3) EV stock share and 4) number of deaths by risk factor

# The following hypotheses were formulated to guide the analysis:

### The more charging stations, the higher the sales.
### The higher stock share, the higher the sales.
### The higher the sales, the less deaths.
### The more sales, the less the pollution.

# Conclusions:

## Is there any correlation at all?

### we can clearly see there is a clear correlation between population and number of deaths.
### There is also a strong positive correlation between sales and number of chargers.
### We can also infer that higher EV sales doesn't imply lower pollution, but we would need more data in order to take conclusions out of this.

![heat_map](https://user-images.githubusercontent.com/128624198/235621256-5bf58bff-98b3-46c4-87cb-c4ee90ddf62c.png)

![plot_deaths](https://user-images.githubusercontent.com/128624198/235621278-12ee06e5-565d-4004-9400-e448d01de332.png)

![sales_pollution](https://user-images.githubusercontent.com/128624198/235621197-caf483dc-4f4a-49de-85d6-ed0628615b09.png)

![sales_chargers](https://user-images.githubusercontent.com/128624198/235621299-79a6c22b-053c-4789-ac5e-d17726246d99.png)





![alternative text](/Users/miguelpalospou/Desktop/IRONHACK/Projects/Project-II-Scrappiing/images/heat_map.png)

![alternative text](/Users/miguelpalospou/Desktop/IRONHACK/Projects/Project-II-Scrappiing/images/plot_deaths.png)

![alternative text](![alternative text](/Users/miguelpalospou/Desktop/IRONHACK/Projects/Project-II-Scrappiing/images/plot_pollution.png)

![alternative text](/Users/miguelpalospou/Desktop/IRONHACK/Projects/Project-II-Scrappiing/images/sales_pollution.png)








# How to run it?
- execute main.py file through bash.
- Have fun
