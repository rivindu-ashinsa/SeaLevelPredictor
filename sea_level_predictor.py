import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],color='red')


    # Create first line of best fit
    slope,intercept,rvalue,pvalue,stderr = linregress(df['Year'],df['CSIRO Adjusted Sea Level'])


    # Create second line of best fit
    years = pd.Series([i for i in range(1880, 2051)])
    sea_levels = slope * years + intercept


    # Add labels and title
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],color='red')
    plt.plot(years,sea_levels)
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(['Original Data','Fitted Line'])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()