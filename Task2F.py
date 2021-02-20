from floodsystem.stationdata import build_station_list
from floodsystem.plot import get_historical_water_levels, plot_water_level_with_fit


def run():
    # Build list of stations
    stations = build_station_list()
    station = stations[0]
    dates, levels = get_historical_water_levels(station, 10)
    plot_water_level_with_fit(station, dates, levels, 10)


if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
