from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import stations_highest_rel_level


def create_test_station(s_id=None,
                        m_id=None,
                        label=None,
                        coord=None,
                        trange=None,
                        river=None,
                        town=None,
                        latest_level=None):
    return MonitoringStation(s_id, m_id, label, coord, trange, river, town, latest_level)


def test_stations_level_over_threshold():
    # Create Station 1
    s1 = create_test_station(label='station1', trange=(1, 2), latest_level=1.5)
    s2 = create_test_station(label='station2', trange=(1, 2), latest_level=1)
    s3 = create_test_station(label='station3', trange=(1, 2), latest_level=1.2)
    s4 = create_test_station(label='station4', trange=(1, 2), latest_level=2)

    stations = [s1, s2, s3, s4]

    actual = stations_level_over_threshold(stations, 0.1)
    actual_names = []
    for station, level in actual:
        actual_names.append(station.name)
    expected_names = ['station4', 'station1', 'station3']
    assert actual_names == expected_names


def test_stations_highest_rel_level():
    # create stations
    s1 = create_test_station(label='station 1', trange=(0.1, 0.2), latest_level=1.5)
    s2 = create_test_station(label='station 2', trange=(0.1, 0.5), latest_level=1.5)
    s3 = create_test_station(label='station 3', trange=(0.2, 0.4), latest_level=1.5)
    s4 = create_test_station(label='station 4', trange=(0.1, 0.7), latest_level=1.5)
    s5 = create_test_station(label='station 5', trange=(0.8, 0.9), latest_level=1.5)
    s6 = create_test_station(label='station 6', trange=(0.1, 0.9), latest_level=1.5)

    stations = [s1, s2, s3, s4, s5, s6]

    output_station = stations_highest_rel_level(stations, 5)
    actual_N_rivers = []
    # test for stations
    for station, level in output_station:
        actual_N_rivers.append(station.name)
    expected_N_rivers = ['station 1', 'station 5', 'station 3', 'station 2', 'station 4']
    assert actual_N_rivers == expected_N_rivers
