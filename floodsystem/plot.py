""" This modules contains a collection of functions to plot water levels data"""

import datetime
import matplotlib.pyplot as plt
import matplotlib
from bokeh.plotting import figure, output_file, show
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit


def get_historical_water_levels(station, num_days):
    """Utility function that gets historical water level data from the
    data fetcher.

    Args:
        station ([MonitoringStation]): An instance of a MonitoringStation
        num_days ([int]): Number of days to retrieve historical data

    Returns:
        [tuple]: returns list of dates and list of water-levels (m).
    """
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=num_days))
    return dates, levels


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
    fig, ax1 = plt.subplots()
    ax1.plot(x, y, '.')
    ax1.set_xlabel('Dates')
    ax1.set_ylabel("Water Level (m)")
    # Plot polynomial fit at 30 points along interval (note that polynomial
    # is evaluated using the shift x)
    x1 = np.linspace(x[0], x[-1], 30)
    ax1.plot(x1, poly(x1 - x[0]), label="Regression Line")
    ax1.legend(loc='center left')
    ax2 = ax1.twinx()
    ax2.plot(x1, np.full(len(x1), station.typical_range[0]), label="Low", color='tab:green')
    ax2.plot(x1, np.full(len(x1), station.typical_range[1]), label="High", color='tab:red')
    ax2.set_ylabel("Typical High/Low Range")
    ax2.legend()
    plt.title(station.name)
    # Display plot
    plt.show()
