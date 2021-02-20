import numpy as np
from mock import Mock
from floodsystem.station import MonitoringStation
from floodsystem.geo import (stations_by_distance, rivers_by_station_number, stations_within_radius,
                             stations_by_river, rivers_with_station)
import pytest


def create_mock_station(**kwargs):
    mock = Mock(spec=MonitoringStation, **kwargs)
    mock.name = kwargs.get('label')
    return mock


# test for 1B
def test_stations_by_distance():
    # Create the first station
    s1 = create_mock_station(coord=(50.8167, -0.2667), river='Adur')

    # Create the second station
    s2 = create_mock_station(coord=(51.5855, -0.616), river='Thames')

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
    # Create station 1
    s1 = create_mock_station(coord=(50.8167, -0.2667), label='station 1')

    # Create station 2
    s2 = create_mock_station(coord=(51.5855, -0.616), label='station 2')

    centre_coord = (51.0017, -2.6363)

    radius_from_centre = 200

    stations = [s1, s2]

    actual_sorted_rivers = stations_within_radius(stations, centre_coord, radius_from_centre)
    # test for stations
    expected_sorted_rivers = ['station 1', 'station 2']
    assert actual_sorted_rivers == expected_sorted_rivers


# test for 1D
def test_rivers_with_station():
    # This is looks like a dodgy test as we are creating stations with the same co-ordinates but with different names
    s1 = create_mock_station(coord=(50.8167, -0.2667), river="Adur")

    s2 = create_mock_station(coord=(50.8167, -0.2667), river="Adur")

    s3 = create_mock_station(coord=(51.5855, -0.616), river="Thames")

    s4 = create_mock_station(coord=(51.5855, -0.616), river="Ail")

    s5 = create_mock_station(coord=(51.5855, -0.616), river="Ail")

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

    s1 = create_mock_station(coord=(50.9167, -0.2687), river="Adur", label="station 1")

    s2 = create_mock_station(coord=(50.8167, -0.2667), river="Adur", label="station 2")

    s3 = create_mock_station(coord=(51.5855, -0.616), river="Thames", label="station 3")

    s4 = create_mock_station(coord=(51.5855, -0.6126), river="Ail", label="station 4")

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
