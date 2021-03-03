from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.warning import floodwarning


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    flood_warning = floodwarning(stations, 100)
    print(flood_warning.get_risky_areas())


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
