# Closest-Teams

This is a small project based on work being done by [Nathan Bingham](https://www.reddit.com/user/nbingham196).

It finds the closest county to each team that is including in each league and presents the output to be imported into [this mapchart map](https://mapchart.net/usa-counties.html).

To generate the json for nhl teams:
```powershell
python generate.py nhl
```

To generate the json for nba teams output to a file:
```powershell
python generate.py nba > output.json
```

Options available:
* nfl
* nba
* mlb
* nhl
* mls
* ncaafbs
* ncaafcs