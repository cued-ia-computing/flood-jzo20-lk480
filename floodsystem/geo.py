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
    station_rivers_count = Counter([station.river for station in stations])
    sorted_stations_count = list(set([v for k, v in station_rivers_count.items()]))
    station_rivers_rank = [(k, v, sorted_stations_count.index(v) + 1)
                           for k, v in station_rivers_count.items()]

    start_index = len(set(sorted_stations_count))
    result = [(k, v) for k, v, r in station_rivers_rank if r >= start_index - N]
    return sorted_by_key(result, 1, reverse=True)
