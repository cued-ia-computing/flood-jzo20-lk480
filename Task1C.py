from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius


def run():

    station = build_station_list()
    centre_coord = (52.2053, 0.1218)
    r = 10
    list_of_stations = stations_within_radius(station, centre_coord, r)
    print("All stations within {radius}km from {centre}\n: {answer}".format(radius=r, centre=centre_coord, answer=list_of_stations))


if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***")
    run()

my_variable = 8
