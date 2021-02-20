# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""
import pytest
from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_typical_range_consistent_inconsistent_data():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (5, 2)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s1.typical_range_consistent()


def test_typical_range_consistent_consistent_data():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (2, 4)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert s2.typical_range_consistent()


def test_typical_range_consistent_none_data():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = None
    river = "River X"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s3.typical_range_consistent()


def test_typical_range_consistent_if_one_is_none_data():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (0, None)
    river = "River X"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    assert not s4.typical_range_consistent()


def test_inconsistent_typical_range_stations_all_inconsistent():
    # Create a first station
    s_id = "test-sid1"
    m_id = "test-m-id"
    label = "a"
    coord = (-2.0, 4.0)
    trange = (2.0, -4)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    # Create a second station
    s_id = "test-sid2"
    m_id = "test-m-id"
    label = "b"
    coord = (-2.0, 4.0)
    trange = (-3, None)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s1, s2]
    expected = ["a", "b"]
    actual = inconsistent_typical_range_stations(stations)
    assert actual == expected


def test_inconsistent_typical_range_stations_all_consistent():
    # Create a first station
    s_id = "test-sid1"
    m_id = "test-m-id"
    label = "a"
    coord = (-2.0, 4.0)
    trange = (2.0, 4)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    # Create a second station
    s_id = "test-sid2"
    m_id = "test-m-id"
    label = "b"
    coord = (-2.0, 4.0)
    trange = (3, 9)
    river = "River X"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s1, s2]
    expected = []
    actual = inconsistent_typical_range_stations(stations)
    assert actual == expected


@pytest.mark.parametrize("trange,latest_level,expected", [((1, 2), 1.5, 0.5),
                                                          ((None, 2), 1.5, None),
                                                          ((1, 2), None, None),
                                                          ((1, 1), 1.5, None),
                                                          ((2, 1), 1.5, None)])
def test_relative_water_level(trange, latest_level, expected):
    # Create a first station
    s_id = "test-sid1"
    m_id = "test-m-id"
    label = "a"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s1.latest_level = latest_level
    actual = s1.relative_water_level()

    assert actual == expected
