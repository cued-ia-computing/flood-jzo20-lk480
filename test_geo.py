import numpy as np
from mock import Mock
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance


def create_mock_station(**kwargs):
    mock = Mock(spec=MonitoringStation, **kwargs)
    return mock


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
