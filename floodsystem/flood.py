"""This module provides a set of functions that determine the likelhihood of a flood occuring at
the locations of the DEFRA Monitoring Stations

"""

from floodsystem.utils import sorted_by_key  # noqa


def stations_level_over_threshold(stations, tol=None):
    """Returns a list of tuples containing station objects and relative water level

    Args:
        stations (list[tuples]): Monitoring Station Objects
        tol ([float, None]): Threshold Value which defaults to None

    Returns:
        [list(tuples)]: list of tuples containing station objects and relative water level, sorted in descending order
    """
    stations_over_threshold = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level is not None and (tol is None or relative_water_level > tol):
            stations_over_threshold.append((station, relative_water_level))
    return sorted_by_key(stations_over_threshold, 1, reverse=True)


def stations_highest_rel_level(stations, N):
    """Returns a list of N tuples containing stations(objects) and their relative water level

    Args:
        stations (list[tuples]): Monitoring Station Objects
        N ([float]): Number of water station

    Returns:
        [list(tuples)]: list of N tuples containing station objects and relative water level, sorted in descending order
    """
    # sorted_list = stations_level_over_threshold(stations)
    # unable to filter out extreme value

    stations_rel_level = []

    for station in stations:
        # check if water level consistent
        rel_level = station.relative_water_level()

        # check if water level reasonable
        if rel_level is not None:

            # check if current water level not extreme
            if rel_level <= 30:
                stations_rel_level.append((station.name, rel_level))

    sorted_list = sorted(stations_rel_level, key=lambda x: x[1], reverse=True)

    return sorted_list[:N]
