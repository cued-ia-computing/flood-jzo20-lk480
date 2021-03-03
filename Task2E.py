from floodsystem.stationdata import build_station_list, get_historical_water_levels
from floodsystem.plot import plot_water_levels, plot_water_levels_bokeh


def run(plot_type):
    # Build list of stations
    stations = build_station_list()
    station = stations[0]
    dates, levels = get_historical_water_levels(station, 10)
    if plot_type == "matplotlib":
        plot_water_levels(station, dates, levels)
    elif plot_type == "bokeh":
        plot_water_levels_bokeh(station, dates, levels)
    else:
        raise Exception(f"Unknown Plot Type {plot_type}")


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run("matplotlib")
