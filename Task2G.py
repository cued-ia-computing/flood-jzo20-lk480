from datetime import date
from collections import defaultdict
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import update_forecasted_levels
from floodsystem.flood import stations_highest_rel_level

# Please see classification methodology .md file

SEVERE = 2.0
HIGH = 1.0
MODERATE = 0.5
LOW = 0.0


def risk_assesment(relative_water_levels):
    """Takes a list of relative water levels by station for each town, computes the
    largest relative water level.

    If largest relative water level is greater than [2.0,] returns Severe.
    If largest relative water level is between than [1.0, 2.0), returns High.
    If largest relative water level is between than [0.5, 1.0), returns Moderate.
    If largest relative water level is greater than [, 0.5), returns Severe.

    Args:
        relative_water_levels ([list]): List of relative water levels

    Returns:
        [str]: Flood Risk Assesment
    """
    max_relative_water_level = max([x for x in relative_water_levels if x is not None])
    if max_relative_water_level >= SEVERE:
        return 'Severe'
    elif HIGH <= max_relative_water_level < SEVERE:
        return 'High'
    elif MODERATE <= max_relative_water_level < HIGH:
        return 'Moderate'
    else:
        return 'Low'


def run(forecast_date, N=50):
    # 1. Build list of all Monitoring Stations
    all_stations = build_station_list()
    # 2. Update latest water levels for each station
    update_water_levels(all_stations)
    # 3. Find N stations with highest latest water level
    stations_rel_level = stations_highest_rel_level(all_stations, N)
    # 4. Unpack list of station objects
    stations = [station for station, _ in stations_rel_level]
    # 5. Forecast level for given date and update the latest-level for each station
    update_forecasted_levels(stations, forecast_date)
    # 6. Create default dictionary with values of an empty list
    relative_levels_by_town = defaultdict(list)

    # 7. Populating relative_levels_town with relative water level for each station in a town
    for station in stations:
        # Exclude stations where the town name is not provided
        if station.town is not None:
            v = relative_levels_by_town[station.town]
            v.append(station.relative_water_level())

    # 8. Create dictionary to store flood warning by town
    flood_warning_by_town = {}

    # 9. Populate dictionary by calling risk_assesment() function with a list of forecasted
    # relative water levels.
    for town, relative_water_levels in relative_levels_by_town.items():
        flood_warning_by_town[town] = risk_assesment(relative_water_levels)

    # 10. Return dictionary of flood warning by town
    return flood_warning_by_town


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    forecast_date = date(2021, 3, 5)
    number_of_stations = 50
    flood_warning_by_town = run(forecast_date, number_of_stations)
    for k, v in flood_warning_by_town.items():
        print(f"{k}: {v}")
