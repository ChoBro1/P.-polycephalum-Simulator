import sys
from heapq import heappush, heapify

def dijsktra(graph, start, dest):
    inf = 10000
    node_data = {}
    for key in graph:
        node_data[key] = {'cost':inf, 'pred':[]}
    node_data[start]['cost'] = 0    #The start points to itself
    visited = []
    current_node = start
    max_steps = len(graph) - 1      #Completes in n-1 steps; n = # of nodes
    for i in range(max_steps):
        if current_node not in visited:
            visited.append(current_node)
            min_heap = []
            # Check the neighbors of current_node
            for j in graph[current_node]:
                if j not in visited:
                    cost = node_data[current_node]['cost'] + graph[current_node][j]
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[current_node]['pred'] \
                                               + list(current_node)
                    heappush(min_heap,(node_data[j]['cost'], j))
        heapify(min_heap)
        current_node = min_heap[0][1]
    print("Shortest Distance in Miles: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))

def input_validation(location, location_list):
    if location in location_list:
        return True
    return False

if __name__ == '__main__':
    # Distance Between Major Cities: https://mileagemath.com/distance/united-states
    # Populations: https://worldpopulationreview.com/us-cities
    locations = ['LA', 'New York', 'Chicago']
    graph = {
        'New York': {'LA':2789, 'Chicago':796 },
        'LA' : {'Chicago':2015, 'New York':2789},
        'Chicago' : {'New York':796, 'LA':2015}
    }

    valid = False
    while not valid:
        start = input("Where are you starting?\n")
        valid = input_validation(start, locations)
    valid = False
    while not valid:
        destination = input("Where do you want to go?\n")
        valid = input_validation(start, locations)
    dijsktra(graph, start, destination)
