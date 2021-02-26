"""This module provides a set of functions that determine the likelhihood of a flood occuring at
the locations of the DEFRA Monitoring Stations

"""

from floodsystem.utils import sorted_by_key  # noqa


def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples containing station objects and relative water level

    Args:
        stations (list[tuples]): Monitoring Station Objects
        tol ([float]): Threshold Value

    Returns:
        [list(tuples)]: list of tuples containing station objects and relative water level, sorted in descending order
    """
    stations_over_threshold = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level is not None and relative_water_level > tol:
            stations_over_threshold.append((station, station.relative_water_level()))
    return sorted_by_key(stations_over_threshold, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    """Returns a list of N tuples containing stations(objects) and their relative water level

    Args:
        stations (list[tuples]): Monitoring Station Objects
        N ([float]): Number of water station

    Returns:
        [list(tuples)]: list of N tuples containing station objects and relative water level, sorted in descending order
    """
    stations_at_risk = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level is not None:
            stations_at_risk.append((station.name, relative_water_level))

    sorted_list = sorted_by_key(stations_at_risk, 1, reverse=True)

    N_stations_at_risk = []
    for i in range(N):
        N_stations_at_risk.append((sorted_list[i]))

    return N_stations_at_risk
