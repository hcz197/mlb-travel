import schedule as sc
import stadiums
import geo

dists = {}

for team, l in sc.schedules.items():
    dists[team] = 0
    for i in range(len(l) - 1):
        stad1 = stadiums.stadiums[l[i]][1]
        stad2 = stadiums.stadiums[l[i + 1]][1]
        dist = geo.haversine(stad1, stad2)
        dists[team] += dist

sorted_dists = dict(sorted(dists.items(), key=lambda x : x[1]))

for team in sorted_dists:
    print(f"{team}: {sorted_dists[team]}")