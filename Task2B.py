from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold


def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Obtain list of stations with relative level over given threshold
    result = stations_level_over_threshold(stations, 0.8)

    for station, relative_level in result:
        print(f"{station.name}: {relative_level}")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
