# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, latest_level=None):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = latest_level

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """ Method which checks typical high/low range data for consistency. If data is consistent
        method returns True, if data is inconsistent method returns False.

        Returns:
            [boolean]: Returns True if data is consistent; Returns False if data is None or inconsistent
        """
        if self.typical_range is None:
            return False
        elif self.typical_range[0] is None or self.typical_range[1] is None:
            return False
        elif self.typical_range[0] >= self.typical_range[1]:
            return False
        else:
            return True

    def relative_water_level(self):
        """Returns latest water level as a fraction of the typical range
        e.g. 1.0 corresponds to a level equalling typical_high
             0.0 corresponds to a level equalling typical_low

        Returns:
            [float]: water level as a fraction of the typical range
        """
        # Test
        if self.typical_range_consistent() is True and self.latest_level is not None:
            return (self.latest_level - self.typical_range[0]) / (self.typical_range[1] - self.typical_range[0])


def inconsistent_typical_range_stations(stations):
    """ Function that takes a list of station objects and returns a list containing
    the station names of stations where data is inconsistent or missing (None)

    Args:
        stations [list[tuples]]: list of station objects

    Returns:
        [list[strings]]: Returns a list of station names
    """
    result = []
    for station in stations:
        if not station.typical_range_consistent():
            result.append(station.name)

    return result
