import stadiums
import schedule
#import distance
import folium

m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)
stads = stadiums.stadiums
for team in stads:
    venue, coords = stads[team]
    folium.Marker(location=[coords[0], coords[1]], popup=f"{team} - {venue}").add_to(m)


schedules = schedule.build_sc(schedule.load())
for team in schedules:
    sc = schedules[team]
    fg = folium.FeatureGroup(name=team, show=False)

    for i in range(len(sc) - 1):
        if (sc[i] == sc[i + 1]): continue
        venue1, coords1 = stads[sc[i]]
        venue2, coords2 = stads[sc[i + 1]]
        folium.PolyLine(
            locations=[[coords1[0], coords1[1]], [coords2[0], coords2[1]]],
            color="cadetBlue",
            weight=2,
            opacity=0.5
        ).add_to(fg)

    fg.add_to(m)

folium.LayerControl().add_to(m)

m.save("map.html")


