from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.plot import get_historical_water_levels, plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)

    stations_highest_level = stations_highest_rel_level(stations, 5)
    for station, _ in stations_highest_level:
        dates, levels = get_historical_water_levels(station, 2)
        plot_water_level_with_fit(station, dates, levels, 4)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
