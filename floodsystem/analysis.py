"""This module contains a collection of functions related to fitting a
least-squares polynomial to historical water levels data

"""

import numpy as np
import matplotlib


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
    # Find coefficients of best-fit polynomial f(x) of degree p
    p_coeff = np.polyfit(x - x[0], y, p)
    # Convert coefficient into a polynomial that can be evaluated
    poly = np.poly1d(p_coeff)
    # Returns a 1D polynomial and time-axis shift
    return poly, x[0]
