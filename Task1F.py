from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def run():
    stations = build_station_list()
    result = inconsistent_typical_range_stations(stations)
    print(f"List of stations with inconsistent typical range data \n {result}")


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
