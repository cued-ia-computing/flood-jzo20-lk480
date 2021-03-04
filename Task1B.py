from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance


def run():

    station = build_station_list()
    list_of_stations = stations_by_distance(station, (52.2053, 0.1218))
    ten_closest_stations = [(station.name, station.town, distance) for station, distance in list_of_stations[:10]]
    ten_furthest_stations = [(station.name, station.town, distance) for station, distance in list_of_stations[-10:]]
    print(f"10 closest stations from cambridge \n: {ten_closest_stations}")
    print(f"10 furthest stations from cambridge \n: {ten_furthest_stations}")


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

my_variable = 8
