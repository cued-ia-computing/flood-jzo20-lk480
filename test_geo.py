import numpy as np
from mock import Mock
from floodsystem.station import MonitoringStation
from floodsystem.geo import (stations_by_distance, rivers_by_station_number, stations_within_radius,
                             stations_by_river, rivers_with_station)
import pytest


def create_mock_station(**kwargs):
    mock = Mock(spec=MonitoringStation, **kwargs)
    return mock


# test for 1B
def test_stations_by_distance():
    # Create the first station
    s1 = create_mock_station(coord=(50.8167, -0.2667), river='Adur', trange=(-2.3, 3.4445))

    # Create the second station
    s2 = create_mock_station(coord=(51.5855, -0.616), river='Thames', trange=(-2.3, 3.4445))

    ref_point = (51.0017, -2.6363)

    stations = [s1, s2]

    sorted_pairs = stations_by_distance(stations, ref_point)
    # test for rivers
    actual_sorted_rivers = [x.river for x, distance in sorted_pairs]
    expected_sorted_rivers = ['Thames', 'Adur']
    assert actual_sorted_rivers == expected_sorted_rivers

    # test for distances
    actual_sorted_distances = [distance for x, distance in sorted_pairs]
    expected_distances = [154.7439, 167.404]
    assert np.allclose(actual_sorted_distances, expected_distances)


# test for 1C
def test_stations_within_radius():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 1"
    coord = (50.8167, -0.2667)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 2"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Thames"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    centre_coord = (51.0017, -2.6363)

    radius_from_centre = 200

    stations = [s1, s2]

    sorted_pairs = stations_within_radius(stations, centre_coord, radius_from_centre)
    # test for stations
    actual_sorted_rivers = sorted_pairs
    expected_sorted_rivers = ['station 1', 'station 2']
    assert actual_sorted_rivers == expected_sorted_rivers


# test for 1D
def test_rivers_with_station():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 1"
    coord = (50.8167, -0.2667)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (50.9167, -0.2687)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Thames"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Ail"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Ail"
    town = "My Town"
    s5 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s1, s2, s3, s4, s5]

    sorted_pairs = rivers_with_station(stations)
    # test for length
    actual_sorted_length = len(sorted_pairs)
    expected_sorted_length = 3
    assert actual_sorted_length == expected_sorted_length

    # test for river
    actual_sorted_rivers = sorted_pairs
    expected_sorted_rivers = ['Adur', 'Ail', 'Thames']
    assert actual_sorted_rivers == expected_sorted_rivers


def test_stations_by_river():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 2"
    coord = (50.8167, -0.2667)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 1"
    coord = (50.9167, -0.2687)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 3"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Thamus"
    town = "My Town"
    s3 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "station 4"
    coord = (51.5855, -0.6126)
    trange = (-2.3, 3.44451)
    river = "Ail"
    town = "My Town"
    s4 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations = [s1, s2, s3, s4]

    stations_dict = stations_by_river(stations)
    # test for stations
    actual_sorted_rivers = sorted(stations_dict['Adur'])
    expected_sorted_rivers = ['station 1', 'station 2']
    assert actual_sorted_rivers == expected_sorted_rivers


def test_rivers_by_station_number():
    # Create a list of mock classes
    rivers = ['a'] * 10 + ['b'] * 10 + ['c'] * 5 + ['d'] * 20 + ['e'] * 20 + ['f'] * 21
    stations = []
    for river in rivers:
        stations.append(create_mock_station(river=river))
    N = 2
    expected_output = [('f', 21), ('d', 20), ('e', 20)]
    actual_output = rivers_by_station_number(stations, N)
    # test for sorted list
    assert actual_output == expected_output


def test_rivers_by_station_number_with_negative_N():
    # Create a list of mock classes
    stations = []
    N = -5
    # I found here how to assert when my function raises an exception with N<0
    # https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
    with pytest.raises(AssertionError):
        rivers_by_station_number(stations, N)

    # Testing with N = 0
    N = 0
    with pytest.raises(AssertionError):
        rivers_by_station_number(stations, N)


def test_rivers_by_station_number_with_max_N():
    # Create a list of mock classes
    rivers = ['a'] * 10 + ['b'] * 10 + ['c'] * 5 + ['d'] * 20 + ['e'] * 20 + ['f'] * 21
    stations = []
    for river in rivers:
        stations.append(create_mock_station(river=river))
    N = 4
    expected_output = [('f', 21), ('d', 20), ('e', 20), ('a', 10), ('b', 10), ('c', 5)]
    actual_output = rivers_by_station_number(stations, N)
    # test for sorted list
    assert actual_output == expected_output
