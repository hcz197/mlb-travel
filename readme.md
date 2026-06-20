This program aims to analyze the distance each MLB team traveled for their 2025 regular season. It also utilizes Folium to present a visualization of each team's travel path throughout March - September 2025.  
  
The main takeaways are:
1. West division teams tend to travel the most given the low density of teams over a vast area
2. Central division teams travel the least because of proximity to division rivals and eastern division teams. 
3. The West Sacramento A's traveled ~49,000 miles in 2025, almost twice the distance of the Cincinnati Reds' ~26,000 miles.

Install Python3, and run the program with the command ```python3 distance.py```  to see for yourself.  
For visualization, run ```python3 visualize.py``` to generate ```map.html``` file, which shows all thirty home ballparks and filters to show  each team's travel paths in 2025.  
  
The program uses the haversine formula to calculate the distance between two coordinates. For simplicity's sake, the coordinates of the home stadiums are used to represent each team's start and end points.
The distance traveled by each team is compiled over a 162-game regular season. Schedule for each team is collected with MLB's API, so internet connection is required to run the program. 


This program has not accounted for a few games played at neutral fields, including:
- Tokyo Dome (MLB Tokyo Series 2025)
- Bristol Motor Speedway (MLB Speedway Classic '25) 
- Bowman Field (MLB Little League Classic 2025)  

because the venue data are hardcoded as of right now. This should be fixed when venue data is parsed from MLB's API.  

This program does not account for end of season travel, as it focuses on regular season and playoff teams don't all travel home after the regular season.  
  
Future plans:
- Replace hardcoded data with stream from MLB API
- Visualization - partially done
- (Maybe) GUI