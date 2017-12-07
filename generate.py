import sys

import geopy.distance
import pandas as pd


class Team:
    def __init__(self, name, lat, lon, color):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.color = color
        self.closest = []

    def location(self):
        return (self.lat, self.lon)

    def __str__(self):
        return self.name + ' : (' + str(self.lat) + ', ' + str(self.lon) + '), ' + self.color


class County:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.closest = None

    def location(self):
        return (self.lat, self.lon)

    def __str__(self):
        if(self.closest):
            return self.name + ' : (' + str(self.lat) + ', ' + str(self.lon) + ') : ' + self.closest
        else:
            return self.name + ' : (' + str(self.lat) + ', ' + str(self.lon) + ') '


def set_closest_team(teams, counties):
    for county in counties:
        county.closest = teams[0]
        for team in teams:
            new_distance = geopy.distance.VincentyDistance(
                county.location(), team.location()).km
            old_distance = geopy.distance.VincentyDistance(
                county.location(), county.closest.location()).km
            if new_distance <= old_distance:
                county.closest = team
        # This assigns the county to the closest team to the county
        county.closest.closest.append(county)


def generate_mapchart_json(teams):
    """
    {
    "groups": {
        "#cc3333": {
            "div": "#box0",
            "label": "",
            "paths": [
                "New_Castle__DE",
                "Sussex__DE",
                "Kent__DE"
            ]
        },
        "title": "",
        "hidden": [],
        "borders": "#000000"
    }
    """
    outstring = '{"groups": {'
    for i, team in enumerate(teams):
        outstring += '"' + team.color +  '":{"div":"#box' +  str(i) +  '","label":"' + team.name +  '","paths":['
        if len(team.closest) > 0:
            for county in team.closest:
                outstring += '"' + county.name + '",'
            outstring = outstring[:-1]
        outstring += ']},'
    outstring = outstring[:-1]
    outstring += '},"title":"","hidden":[],"borders":"#000000"}'
    return outstring


def run(filepath):
    data = pd.read_csv(filepath, delimiter=',')
    data2 = pd.read_csv('data/counties.csv', delimiter=',')

    teams = [Team(x[0], x[1], x[2], x[3]) for x in data.values]
    counties = [County(x[0], x[1], x[2]) for x in data2.values]

    set_closest_team(teams, counties)
    mapchart = generate_mapchart_json(teams)
    print(mapchart)


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
