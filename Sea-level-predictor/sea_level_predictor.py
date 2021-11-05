import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x=df.Year
    y=df['CSIRO Adjusted Sea Level']
    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # Create first line of best fit
    x_pred = pd.Series([i for i in range(1880, 2051)])
    lr = linregress(x,y)
    slope = lr.slope
    intercept = lr.intercept
    y_pred = (x_pred*slope)+intercept
    fig = plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    df_new = df.loc[df['Year'] >= 2000]
    x_new = df_new.Year
    y_new = df_new['CSIRO Adjusted Sea Level']
    lr_new = linregress(x_new,y_new)
    slope_new = lr_new.slope
    intercept_new = lr_new.intercept
    x_new_pred = pd.Series([i for i in range(2000, 2051)])
    y_new_pred = (x_new_pred*slope_new)+intercept_new
    fig = plt.plot(x_new_pred,y_new_pred, 'g')

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xticks(range(1850,2100,25))
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
