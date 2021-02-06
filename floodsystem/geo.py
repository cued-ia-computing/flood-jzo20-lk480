# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from collections import Counter


def stations_by_distance(stations, p):
    station_by_distance = []
    for station in stations:
        station_by_distance.append((station, haversine(station.coord, p, unit=Unit.KILOMETERS)))

    return sorted_by_key(station_by_distance, 1)


def rivers_by_station_number(stations, N):
    # Counting the number of stations associated with each river
    # The Counter will return a dict e.g. {'river1' : 10, 'river2': 8, etc.}
    station_rivers_count = Counter([station.river for station in stations])
    # station_rivers_count.items() returns a list of tuples e.g. [('river1',10), ('river2',8), etc.]
    # We then iterate through to obtain a list of unique values for the number of stations i.e no repeated values
    stations_count = list(set([v for k, v in station_rivers_count.items()]))
    # We produce a list of tuples e.g. [('river1',10,5),('river2',8,2)]
    # Tuple contains river name, number of stations, rank
    # index(v)+1 sets the rank to start at value 1 instead of 0
    station_rivers_rank = [(k, v, stations_count.index(v) + 1)
                           for k, v in station_rivers_count.items()]
    # start_index is number of unique values present e.g. 25
    start_index = len(set(stations_count))
    # result outputs a list of tuples containing the river name and number of associated stations
    # number of tuples is dependent on the value of N and the number of rivers with equal number of stations
    result = [(k, v) for k, v, r in station_rivers_rank if r >= start_index - N]
    # returns sorted list in descending order
    return sorted_by_key(result, 1, reverse=True)
