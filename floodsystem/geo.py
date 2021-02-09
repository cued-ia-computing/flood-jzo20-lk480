# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit


def stations_by_distance(stations, p):
    station_by_distance = []
    for station in stations:
        station_by_distance.append((station, haversine(station.coord, p, unit=Unit.KILOMETERS)))

    return sorted_by_key(station_by_distance, 1)


def stations_within_radius(stations, centre, r):
    stations_within_radius = []
    for station in stations:
        if r >= haversine(station.coord, centre, unit=Unit.KILOMETERS):
            stations_within_radius.append(station.name)

    return sorted(stations_within_radius)


def rivers_with_station(stations):
    rivers_with_station_set = {station.river for station in stations}
    rivers_with_station_list = []
    for name in rivers_with_station_set:
        rivers_with_station_list.append(name)

    return sorted(rivers_with_station_list)


def stations_by_river(stations):
    stations_by_river_dict = {}
    station = stations
    for i in range(len(stations)):
        if not station[i].river in stations_by_river_dict:
            stations_by_river_dict[station[i].river] = []
            stations_by_river_dict[station[i].river].append(station[i].name)
        else:
            stations_by_river_dict[station[i].river].append(station[i].name)

    return stations_by_river_dict
