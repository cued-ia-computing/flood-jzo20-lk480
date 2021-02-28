from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt  # noqa
from floodsystem.analysis import polyfit


def test_polyfit():

    dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1)]
    levels = [0.2, 0.7, 0.95]
    actual = polyfit(dates, levels, 1)
    assert isinstance(actual[0], np.poly1d)
