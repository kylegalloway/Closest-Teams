# Closest-Teams

This is a small project based on work done by [Nathan Bingham](https://www.reddit.com/user/nbingham196).

It finds the closest county to each team that is in a given league and emits output that can be imported into [this mapchart map](https://mapchart.net/usa-counties.html).

To generate the json for a given league:

```powershell
python generate.py <league>
```

To generate the json for nba teams output to a file:

```powershell
python generate.py nba > output.json
```

League options available:

* nfl
* nba
* mlb
* nhl
* mls
* ncaafbs
* ncaafcs

Colors from [here](https://teamcolorcodes.com/). I tried to use contrasting colors in most places.

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