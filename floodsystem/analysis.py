"""This module contains a collection of functions related to fitting a
least-squares polynomial to historical water levels data

"""

import numpy as np
import matplotlib.pyplot as plt  # noqa
import matplotlib
from floodsystem.stationdata import get_historical_water_levels


def polyfit(dates, levels, p):
    """Given the water-level time history, this function computes a
    least squares fit polynomial of degree p to the water level data.

    Args:
        dates ([list]): List of dates
        levels ([list]): List of river water levels
        p ([int]): Degree of polynomial

    Returns:
        [tuple]: returns tuple of 1D polynomial representing a least squares fit and time shift
    """
    assert isinstance(p, int) and p > 0, f"{p} is not a positive integer"

    x = matplotlib.dates.date2num(dates)
    y = levels
    try:
        # Find coefficients of best-fit polynomial f(x) of degree p
        p_coeff = np.polyfit(x - x[0], y, p)
        # Convert coefficient into a polynomial that can be evaluated
        poly = np.poly1d(p_coeff)
        # Returns a 1D polynomial and time-axis shift
        return poly, x[0]
    except TypeError:
        # workaround to handle unexpected numpy polyfit errors
        return None, x[0]


def update_forecasted_levels(stations, forecast_date, num_days=30):
    """Forecasts the water level for the given date using polynomial regression with
    a given lookback period.

    Args:
        stations (list[MonitoringStation]): List of Monitoring Station Objects
        forecast_date ([Date]): Date to be forecasted
        num_days (int, optional): Number of days to retrieve historical data. Defaults to 30.
    """
    for station in stations:
        print(f"Fetching forecasted level for {station.name}")
        dates, levels = get_historical_water_levels(station, num_days)
        if len(dates) != 0 and len(levels) != 0:
            model, d0 = polyfit(dates, levels, 4)
            if model is not None:
                dn = matplotlib.dates.date2num(forecast_date)
                station.latest_level = model(dn - d0)
