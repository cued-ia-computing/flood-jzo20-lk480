from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold


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
