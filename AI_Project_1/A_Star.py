from Map import Map
from math import sqrt

def calculate_heuristic(node, goal, amount_traversed, map, type):
    if type == False:
        #get node coordinates
        node_location = map.locations_dictionary[node]
        x1 = float(node_location[0])
        y1 = float(node_location[1])

        #get goal coordinates
        goal_location = map.locations_dictionary[goal]
        x2 = float(goal_location[0])
        y2 = float(goal_location[1])

        #calculate straight line distance between node and goal
        estimate = sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    else:
        estimate = 1
    
    return estimate + amount_traversed

def main():
    my_map = Map("connections.txt", "locations.txt")

    print('{:.2f}'.format(calculate_heuristic("A1", "B2", 30.7, my_map, False)))

if __name__ == "__main__":
    main()
