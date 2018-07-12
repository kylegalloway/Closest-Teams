import sys

import geopy.distance
import pandas as pd

from mapchart import Path, Group, MapchartJson


class NamedLocation:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def location(self):
        return (self.lat, self.lon)

    def __str__(self):
        return self.name + ' : (' + str(self.lat) + ', ' + str(self.lon) + ')'


class Team(NamedLocation):
    def __init__(self, name, lat, lon, color):
        super().__init__(name, lat, lon)
        self.color = color
        self.closest_counties = []

    def __str__(self):
        return super().__str__() + ', ' + self.color


class County(NamedLocation):
    def __init__(self, name, lat, lon):
        super().__init__(name, lat, lon)
        self.closest_team = None

    def __str__(self):
        if self.closest_team:
            return super().__str__() + ' : ' + self.closest_team
        else:
            return super().__str__()


def set_closest_team(teams, counties):
    for county in counties:
        county.closest_team = teams[0]
        for team in teams:
            new_distance = geopy.distance.VincentyDistance(
                county.location(), team.location()).km
            old_distance = geopy.distance.VincentyDistance(
                county.location(), county.closest_team.location()).km
            if new_distance <= old_distance:
                county.closest_team = team
        # This adds the county to the closest team's list of closest_counties
        county.closest_team.closest_counties.append(county)


def generate_mapchart_json(teams):
    groups = []
    for i, team in enumerate(teams):
        paths = []
        for county in team.closest_counties:
            paths.append(Path(county.name))
        groups.append(Group(team.name, team.color, i, paths))

    return MapchartJson(groups)


def run(filepath):
    data = pd.read_csv(filepath, delimiter=',')
    data2 = pd.read_csv('data/counties.csv', delimiter=',')

    teams = [Team(x[0], x[1], x[2], x[3]) for x in data.values]
    counties = [County(x[0], x[1], x[2]) for x in data2.values]

    set_closest_team(teams, counties)
    mapchart = generate_mapchart_json(teams)
    print(str(mapchart))


def file_name_from_league(league):
    if league == "nfl":
        return "nfl_teams.csv"
    elif league == "nba":
        return "nba_teams.csv"
    elif league == "mlb":
        return "mlb_teams.csv"
    elif league == "nhl":
        return "nhl_teams.csv"
    elif league == "mls":
        return "mls_teams.csv"
    elif league == "ncaafbs":
        return "ncaafbs_teams.csv"
    elif league == "ncaafcs":
        return "ncaafcs_teams.csv"


def print_usage(input=None):
    if input:
        print("You input" + input)
    print("Usage: python read.py <league> where league is one of the following:")
    print("\t - nfl")
    print("\t - nba")
    print("\t - mlb")
    print("\t - nhl")
    print("\t - mls")
    print("\t - ncaafbs")
    print("\t - ncaafcs")


def main():
    if len(sys.argv) == 2:
        filename = "data/" + file_name_from_league(str(sys.argv[1]))
        if filename:
            run(filename)
        else:
            print_usage(str(sys.argv[1]))
    else:
        print_usage()


if __name__ == '__main__':
    main()
