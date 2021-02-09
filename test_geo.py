import numpy as np
from floodsystem.station import MonitoringStation
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius


def test_stations_by_distance():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (50.8167, -0.2667)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (51.5855, -0.616)
    trange = (-2.3, 3.4445)
    river = "Thames"
    town = "My Town"
    s2 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

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


def test_stations_within_radius():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "A"
    coord = (50.8167, -0.2667)
    trange = (-2.3, 3.4445)
    river = "Adur"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "B"
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
    actual_sorted_rivers = tuple((x for x in sorted_pairs))
    expected_sorted_rivers = ('A', 'B')
    assert actual_sorted_rivers == expected_sorted_rivers
