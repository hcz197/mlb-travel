import schedule as sc
import stadiums
import geo
import os
import json

if not os.path.exists("schedule.json"): sc.scrape()

dates = sc.load()
schedules = sc.build_sc(dates)

dists = {}
for team, loc in schedules.items():
    dists[team] = 0
    for i in range(len(loc) - 1):
        stad1 = stadiums.stadiums[loc[i]][1]
        stad2 = stadiums.stadiums[loc[i + 1]][1]
        dist = geo.haversine(stad1, stad2)
        dists[team] += dist

sorted_dists = dict(sorted(dists.items(), key=lambda x : x[1], reverse=True))

print("\nRank | Team | Distance")
print("-------------------------")
for rank, team in enumerate(sorted_dists, 1):
    print(f"{rank:<4} | {team:<4} | {sorted_dists[team]:.2f} mi")

print("\n")