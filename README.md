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

## Examples of output

### NFL

![NFL](images/nfl.png?raw=true "NFL")

### NBA

![NBA](images/nba.png?raw=true "NBA")

### MLB

![MLB](images/mlb.png?raw=true "MLB")

### NHL

![NHL](images/nhl.png?raw=true "NHL")

### MLS

![MLS](images/mls.png?raw=true "MLS")

### NCAAFBS

![NCAAFBS](images/ncaafbs.png?raw=true "NCAAFBS")

### NCAAFCS

![NCAAFCS](images/ncaafcs.png?raw=true "NCAAFCS")