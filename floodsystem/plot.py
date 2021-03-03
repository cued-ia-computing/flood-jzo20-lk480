""" This modules contains a collection of functions to plot water levels data"""

import matplotlib.pyplot as plt
import matplotlib
from bokeh.plotting import figure, output_file, show
import numpy as np
from floodsystem.analysis import polyfit


def plot_water_levels(station, dates, levels):

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(f"Station {station.name}")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_levels_bokeh(station, dates, levels):

    # output to static HTML file
    output_file("water_levels_bokeh.html")

    # create a new plot with a title and axis labels
    p = figure(title=f"Station {station.name}", x_axis_label='date', y_axis_label='water level (m)')

    # add a line renderer with legend and line thickness
    p.line(dates, levels, legend_label="Water Level", line_width=2)

    # show the results
    show(p)


def plot_water_level_with_fit(station, dates, levels, p):
    """Plots the polynomial regression line of order p

    Args:
        station ([MonitoringStation]): Monitoring Station with a series of attributes
        dates ([date]): List of dates
        levels ([list(floats)]): List of water levels for monitoring stations
        p ([int]): order of regression polynomial
    """
    poly, d0 = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    y = levels
    plt.plot(x, y, '.')
    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    # Get the current figure for re-sizing
    fig = plt.gcf()
    fig.set_size_inches(12, 7, forward=True)
    # Get the current axis to get the date formatter
    ax = plt.gca()
    hfmt = matplotlib.dates.DateFormatter('%d/%m/%y %H:%M')
    # Set the date formatter for the x-axis
    ax.xaxis.set_major_formatter(hfmt)
    ax.plot(x1, poly(x1 - x[0]), label="Regression Line")
    ax.plot(x1, np.full(len(x1), station.typical_range[0]),
            label="Low", color='tab:green')
    ax.plot(x1, np.full(len(x1), station.typical_range[1]),
            label="High", color='tab:red')
    plt.xlabel('Dates (DD/MM/YY HH:MI')
    plt.xticks(rotation=30)
    plt.ylabel("Water Level (m)")
    plt.legend(loc='center left')
    plt.title(station.name)
    # Display plot
    plt.show()
