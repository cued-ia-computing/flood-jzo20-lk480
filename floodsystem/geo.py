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
