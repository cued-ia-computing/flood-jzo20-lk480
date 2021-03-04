from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Obtain list of stations with highest relative water level
    result = stations_highest_rel_level(stations, 10)

    for station, relative_level in result:
        print(f"{station.name}: {relative_level}")


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
