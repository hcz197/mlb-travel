This program aims to analyze the distance each MLB team traveled for their 2025 regular season.

The main takeaways are:
1. West division teams tend to travel the most given the low density of teams over a vast area
2. Central division teams travel the least because of proximity to division rivals and eastern division teams. 
3. The West Sacramento A's travel ~48,300 miles, almost twice the distance of the Cleveland Guardians' ~25,500 miles.

Install Python3, and run the program with the command below to see for yourself.  
```python3 distance.py```
The program uses the haversine formula to calculate the distance between two coordinates. For simplicity's sake, the coordinates of the home stadiums are used to represent each team's start and end points. 
The distance traveled by each team is compiled over a 162-game regular season. Schedule for each team is collected with MLB's API, so internet connection is required to run the program. 