from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river


def run():
    # Build the MoniteringStation list
    stations = build_station_list()

    # Part 1, first 10 river with at least one station
    num_station_atleast_one = rivers_with_station(stations)
    first_ten = num_station_atleast_one[:10]
    # printing the length and first 10
    print('{} stations. First 10 - {}'.format(len(num_station_atleast_one), first_ten))

    # Part 2
    Obj_around_river = stations_by_river(stations)
    Aire = sorted(Obj_around_river['River Aire'])
    Cam = sorted(Obj_around_river['River Cam'])
    Thames = sorted(Obj_around_river['River Thames'])
    print('River Aire stations: {}\n River Cam stations: {}\n River Thames stations: {}\n'.format(Aire, Cam, Thames))

    # Without getting a dictionary
    # for river in ["River Aire", "River Cam", "River Thames"]:
    #    station_list = []

    #    for station in stations_by_river(stations)[river]: (couldn't work)

    #    for station in stations: (but this works)
    #        if river == station.river:
    #            station_list.append(station.name)
    #    print(sorted(station_list))


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()

my_variable = 8
