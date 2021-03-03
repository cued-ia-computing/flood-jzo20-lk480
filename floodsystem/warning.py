# create a new class for task 2G
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit

from numpy import mean
import matplotlib.dates
import datetime


# create new class
class floodwarning():

    def __init__(self, stations, limit=10):
        self.stations = stations
        self.limit = limit

    def get_risky_areas(self):
        risky_areas = {}
        for station, water_level in stations_highest_rel_level(self.stations, self.limit):

            # check if the area is likely to be flooded
            if water_level > 5:
                water_level = 'flooded'

            # if not flooded, run assesment
            elif water_level > 1:

                # Number of days to go back to
                dt = 3
                # assess whether water level is rising/falling
                dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))

                # Polynomial coeff
                p = 4
                poly, shift = polyfit(dates, levels, p)
                dates_float = matplotlib.dates.date2num(dates)
                # Derivate of best-fit polynomial
                poly_deriv = poly.deriv()

                # Rate of change of water level by extrapolating from the latest 15 values
                roc_water_level = poly_deriv(dates_float - shift)[:15]

                # Average rate of change to predict whether water level is rising/falling
                mean_roc_water_level = mean(roc_water_level)

                # Assessing severity of risk of flood
                if mean_roc_water_level > 1.25:
                    water_level = 'Severe'  # Severe risk of flooding
                elif mean_roc_water_level > 0.75:
                    water_level = 'High'  # High risk of flooding
                elif mean_roc_water_level > 0.25:
                    water_level = 'Moderate'  # Moderate risk of flooding
                else:
                    water_level = 'Low'

            # water level lower than typical high
            # not a concern yet
            else:
                water_level = 'Low'

            risky_areas[station.name] = water_level

        return dict(sorted(risky_areas.items(), key=lambda x: x[0]))
