from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number


def run():
    N = 9  # As stated in demonstration program requirements
    stations = build_station_list()
    result = rivers_by_station_number(stations, N)
    print(f"List of {N} rivers with the greatest number of monitoring stations \n {result}")


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
