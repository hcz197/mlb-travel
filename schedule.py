import urllib.request as request
import json
import stadiums

url = "https://statsapi.mlb.com/api/v1/schedule?sportId=1&season=2025&gameType=R&startDate=2025-03-18&endDate=2025-09-28"
response = request.urlopen(url)

data = json.loads(response.read())
dates = data["dates"]
schedules = {}

with open("schedule.json", "w") as f:
    f.write(json.dumps(data, indent=2))


""" for i in range(0, len(dates)):
    #print(dates[i])
    if (dates[i]["date"] == "2025-06-06"):
        print(i)
        break

print(json.dumps(dates[73]["games"], indent=2)) 

with open("compare.json", "w") as f:
    f.write(json.dumps(dates[12]["games"][13], indent=2))

with open("compare2.json", "w") as f:
    f.write(json.dumps(dates[12]["games"][14], indent=2)) """

for date in dates:
    games = date["games"]
    for game in games:
        #print("rescheduleDate" in game)
        if "rescheduleDate" in game or "resumeDate" in game:
            continue
        teams = game["teams"]
        awayteam = teams["away"]["team"]["name"]
        hometeam = teams["home"]["team"]["name"]

        away = stadiums.teams[awayteam]
        home = stadiums.teams[hometeam]

        schedules.setdefault(away, []).append(home)
        schedules.setdefault(home, []).append(home)

""" for team in schedules:
    print(team + " " + str(len(schedules[team]))) """

# print(json.dumps(data["dates"][100]["games"][0]["teams"], indent=2))


# data["dates"] - *list* of all games
# dict -> list (dates) -> dict -> list (games) -> dicts
