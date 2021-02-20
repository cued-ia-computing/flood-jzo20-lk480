import datetime
import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_file, show
from floodsystem.datafetcher import fetch_measure_levels


def get_historical_water_levels(station, num_days):
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
