import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
from matplotlib.colors import ListedColormap
import os

def corr_matrix (df):
    print("---plotting---")
    os.system("say plotting")

    correlation_matrix=df_merged.corr()
    plt.savefig("images/correlationmatrix")
    plt.show()

def heat_map (df):
    print("---plotting---")
    sns.heatmap(correlation_matrix);
    plt.savefig("heat_map")
    plt.show()

def pollution_plot (df):
    print("---plotting---")
    map_1=df_merged[["region", "year", "pollution"]].groupby("region").agg({"pollution":"mean"})

    # Load shapefile of world countries
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge dataframe with shapefile using country names as the key
    merged = world.merge(map_1, left_on='name', right_on='region')

    # Create choropleth map using population data
    ax = merged.plot(column='pollution', cmap='Blues', figsize=(25, 10), edgecolor='black', linewidth=0.5, missing_kwds={'color': 'white'}, legend=True)

    # Add title and axis labels
    ax.set_title('Pollution worldwide', fontsize=20)
    ax.set_xlabel('Longitude', fontsize=15)
    ax.set_ylabel('Latitude', fontsize=15)

    plt.savefig("images/plot_pollution")
    plt.show()

def deaths_plot (df):
    print("---plotting---")
    latest_data = df_merged[['region', 'year', 'number of deaths by air pollution']].groupby('region').agg({"number of deaths by air pollution":"mean"})

    # Load shapefile of world countries
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

    # Merge dataframe with shapefile using country names as the key
    merged = world.merge(latest_data, left_on='name', right_on='region')

    # Create choropleth map using population data
    ax = merged.plot(column='number of deaths by air pollution', cmap='Reds', figsize=(25, 10), edgecolor='black', linewidth=0.5, missing_kwds={'color': 'white'}, legend=True)

    # Add title and axis labels
    ax.set_title('number of deaths by air pollution', fontsize=20)
    ax.set_xlabel('Longitude', fontsize=15)
    ax.set_ylabel('Latitude', fontsize=15)

    plt.savefig("images/plot_deaths")
    plt.show()

def sales_chargers (df):
    print("---plotting---")
    condition_1 = df_merged['number of chargers'] < 20000
    sns.set(style="ticks")
    chargers_plot=df_merged[condition_1]
    sns.scatterplot(x="number of chargers", y="sales", data=chargers_plot)
    plt.title("Sales vs number of chargers", y=1.05)
    plt.savefig("sales_chargers")
    plt.show()



def sales_pollution (df):
    print("---plotting---")
    sns.set(style="ticks")
    condition_2 = df_merged['pollution'] < 30
    pollution_plot=df_merged[condition_2]
    sns.scatterplot(x="pollution", y="sales", data=pollution_plot)
    plt.title("Sales vs pollution", y=1.05)
    plt.title("Sales vs number of chargers", y=1.05)
    plt.savefig("sales_pollution")
    plt.show()