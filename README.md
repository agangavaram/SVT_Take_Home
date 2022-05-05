# SVT_Take_Home

The current function returns the robot which is best to transport the load based on proximity to the load. If there is more than 1 robot within 10 distance units of the load, it returns the one with the most battery remaining. It makes a GET request to the API endpoint, parses the robot location data, and returns a json with the robotId, distanceToGoal, and batteryLevel.

I had a lot of fun making this simplified API, and if I had more time, I would want to add several more functions to it, namely:

1. Given several different charging centers, return a list of robots with battery below a certain threshold, and their corresponding closest charging center.

2. Given the rate the battery dies at, several different charging centers, and a threshold, return a list of robots with the amount of time left before the battery dies and the closest charging center

3. Given distance to the closest charging center, and the rate the battery dies at while moving a certain speed, return a list of robots in necessity of charging.

4. Build a frontend to take this information and display an interactive map that shows the position of the robots, their battery levels, and ids. The user can also place loads on the map, and the closest robot will be highlighted

For the first 3 features, I would build a python function that made requests to the API endpoint and then used the respective formula to calculate battery life time and distance to charging center. For the frontend, I would use React and query the API in python for the information about the robots, battery levels, and ids. 
