from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():

    stations = build_station_list()
    centre_coord = (52.2053, 0.1218)
    r = 10
    list_of_stations = stations_within_radius(stations, centre_coord, r)
    print("All stations within {rad}km from {centre}\n: {ans}".format(rad=r, centre=centre_coord, ans=list_of_stations))


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

my_variable = 8
