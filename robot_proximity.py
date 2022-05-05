import requests
import json
import math

r = requests.get("https://60c8ed887dafc90017ffbd56.mockapi.io/robots")

robot_data = r.json()


def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def closest_robot(loadId, x, y):

    closest_robot = None
    min_distance_to_goal = float("inf")
    for robot in robot_data:
        distance_to_load = distance(robot['x'], robot['y'], x, y)
        if distance_to_load <= 10 and (min_distance_to_goal <= 10):
            if (robot['batteryLevel'] > closest_robot['batteryLevel']):
                closest_robot = robot
                min_distance_to_goal = distance_to_load
        elif distance_to_load < min_distance_to_goal:
            closest_robot = robot
            min_distance_to_goal = distance_to_load
    
    return json.dumps({
        "robotId" : closest_robot['robotId'],
        "distanceToGoal" : "{:.1f}".format(min_distance_to_goal),
        "batteryLevel" : closest_robot['batteryLevel']
    })

        
def main():
    print(closest_robot("8", 50, 50))

main()

