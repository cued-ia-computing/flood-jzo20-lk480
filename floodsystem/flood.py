from floodsystem.utils import sorted_by_key  # noqa


def stations_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for station in stations:
        relative_water_level = station.relative_water_level()
        if relative_water_level is not None and station.latest_level > tol:
            stations_over_threshold.append((station, station.relative_water_level()))
    return sorted_by_key(stations_over_threshold, 1, reverse=True)
