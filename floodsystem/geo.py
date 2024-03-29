# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from collections import Counter


def stations_by_distance(stations, p):
    """ Computes the distance from reference point (p) and the
    coordinates of a station using haversine function. This distance is appended to a list
    which is then sorted by distance.

    Args:
        stations [list]: List of MonitoringStation objects
        p [float]: [description]

    Returns:
        [list[tuples]]: Sorted list of tuples containing station name, town, distance.
    """
    station_by_distance = []
    for station in stations:
        station_by_distance.append((station, haversine(station.coord, p, unit=Unit.KILOMETERS)))

    return sorted_by_key(station_by_distance, 1)


def stations_within_radius(stations, centre, r):
    """returns a list of all stations within radius r of a geographic coordinate x

    Args:
        stations [list]: List of MonitoringStation objects
        centre [tuple]: geographic point to measure relative distances from
        r ([float]): radius from a given point; computed using haversine formula

    Returns:
        [list]: returns a list of station names in alphabetical order
    """
    stations_within_radius = []
    for station in stations:
        if r >= haversine(station.coord, centre, unit=Unit.KILOMETERS):
            stations_within_radius.append(station.name)

    return sorted(stations_within_radius)


def rivers_with_station(stations):
    """ Function which given a list of station objects returns a list containing
    the names of the rivers with at least 1 monitoring station

    Args:
        stations [list]: List of MonitoringStation objects

    Returns:
        [list]: returns a unique list of stations with at least one monitoring station
        in alphabetical order
    """
    rivers_with_station_set = {station.river for station in stations}
    rivers_with_station_list = []
    for name in rivers_with_station_set:
        rivers_with_station_list.append(name)

    return sorted(rivers_with_station_list)


def stations_by_river(stations):
    """Returns a dictionary which maps the river names to a list of station objects for the given
    river

    Args:
        stations ([list]): List of MonitoringStation objects

    Returns:
        [dictionary]: returns a dictionary which maps the river name (key) to list of station objects (value)
    """
    stations_by_river_dict = {}
    station = stations
    for i in range(len(stations)):
        if not station[i].river in stations_by_river_dict:
            stations_by_river_dict[station[i].river] = []
            stations_by_river_dict[station[i].river].append(station[i].name)
        else:
            stations_by_river_dict[station[i].river].append(station[i].name)

    return stations_by_river_dict


def rivers_by_station_number(stations, N):
    """ Determines the N rivers with the greatest number of monitoring station,
    outputted as a list of tuples containg the river name and the number of stations
    associated with the river.

    Args:
        stations [list]: List of MonitoringStation objects
        N [integer]: N rivers with the greatest number of monitoring stations

    Returns:
        [list[tuples]]: Sorted list of tuples containing river name, number of stations
    """
    assert N > 0, "N (rivers) cannot be 0 or negative number"
    # Counting the number of stations associated with each river
    # The Counter will return a dict e.g. {'river1' : 10, 'river2': 8, etc.}
    station_rivers_count = Counter([station.river for station in stations])
    # station_rivers_count.items() returns a list of tuples e.g. [('river1',10), ('river2',8), etc.]
    # We then iterate through to obtain a list of unique values for the number of stations i.e no repeated values
    stations_count = sorted(list(set([v for k, v in station_rivers_count.items()])))
    # We produce a list of tuples e.g. [('river1',10,5),('river2',8,2)]
    # Tuple contains river name, number of stations, rank
    # index(v)+1 sets the rank to start at value 1 instead of 0
    station_rivers_rank = [(k, v, stations_count.index(v) + 1)
                           for k, v in station_rivers_count.items()]
    # start_index is number of unique values present e.g. 25
    start_index = len(set(stations_count))
    # result outputs a list of tuples containing the river name and number of associated stations
    # number of tuples is dependent on the value of N and the number of rivers with equal number of stations
    result = [(k, v) for k, v, r in station_rivers_rank if r > start_index - N]
    # returns sorted list in descending order
    return sorted_by_key(result, 1, reverse=True)
