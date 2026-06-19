This program aims to analyze the distance each MLB team traveled for their 2025 regular season.  

The main takeaways are:
1. West division teams tend to travel the most given the low density of teams over a vast area
2. Central division teams travel the least because of proximity to division rivals and eastern division teams. 
3. The West Sacramento A's traveled ~49,000 miles in 2005, almost twice the distance of the Cincinnati Reds' ~25,972 miles.

Install Python3, and run the program with the command below to see for yourself.  
```python3 distance.py```  
  
The program uses the haversine formula to calculate the distance between two coordinates. For simplicity's sake, the coordinates of the home stadiums are used to represent each team's start and end points. 
The distance traveled by each team is compiled over a 162-game regular season. Schedule for each team is collected with MLB's API, so internet connection is required to run the program. 

This program has not accounted for a few games played at neutral fields, including:
- Tokyo Dome (MLB Tokyo Series 2025)
- Bristol Motor Speedway (MLB Speedway Classic '25) 
- Bowman Field (MLB Little League Classic 2025)  

because the venue data are hardcoded as of right now. This should be fixed when venue data is parsed from MLB's API.  

This program does not account for end of season travel, as it focuses on regular season and playoff teams don't all travel home after the regular season.