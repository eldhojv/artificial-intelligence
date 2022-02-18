#---------------------------------------------------------
#
# Author : Eldho
# Written Date   : 09/20/2021
# Modified date : 09/21/2021
# Search algoritim to find route between any two cities
# 
#---------------------------------------------------------

import sys
from queue import PriorityQueue

def output(route, expanded, produce, distance, max_node, origin, graph):
    print("Nodes Popped: ", len(route))
    print("Nodes Expanded: ",expanded)
    print("Nodes produce: ",produce)
    print("Distance: ", distance, " km")
    print("Route:")
    node_count = origin
    if len(route) == 0:
        print("None")
    else:
        for path in route[::-1]:
            print(node_count, "to", path , graph[node_count][path], " km".format(node_count, path, graph[node_count][path]))
            node_count = path
    return

def astar_search(graph, origin, dest, val): 
    produce = 0
    expand = 0
    frng = PriorityQueue()
    frng.put((0, origin))
    hit = {}
    hit[origin] = ("", 0)
    explored = []
    mnode = 0
    while not frng.empty():
        if len(frng.queue) > mnode:
            mnode = len(frng.queue)
        _, countnode = frng.get()
        expand += 1
        if countnode == dest:
            break
        if countnode in explored:
            continue
        explored.append(countnode)
        for i in graph[countnode]:
            produce += 1
            if i not in hit:
                hit[i] = (countnode, graph[countnode][i] + hit[countnode][1])
                frng.put((graph[countnode][i] + hit[countnode][1] + val[i], i))
    route = []
    dist = "infinity"
    if dest in hit:
        dist = 0.0
        countnode = dest
        while countnode != origin:
            dist += graph[hit[countnode][0]][countnode]
            route.append(countnode)
            countnode = hit[countnode][0]
    output(route, expand, produce, dist, mnode, origin, graph)
    return 

def uniform_cost_search(graph, origin, dest):
    produce = 0
    expand = 0
    frng = PriorityQueue()
    frng.put((0, origin))
    hit = {}
    hit[origin] = ("", 0)
    parsed = []
    max_node = 0
    while not frng.empty():
        if len(frng.queue) > max_node:
            max_node = len(frng.queue)
        _, node_count = frng.get()
        expand += 1
        if node_count == dest:
            break
        if node_count in parsed:
            continue
        parsed.append(node_count)
        for i in graph[node_count]:
            produce += 1
            frng.put((graph[node_count][i]+hit[node_count][1], i))
            if i not in hit:
                hit[i] = (node_count, graph[node_count][i]+hit[node_count][1])
    route = []
    distance = "infinity"
    if dest in hit:
        distance = 0.0
        node_count = dest
        while node_count != origin:
            distance += graph[hit[node_count][0]][node_count]
            route.append(node_count)
            node_count = hit[node_count][0]
    output(route, expand, produce, distance, max_node, origin, graph)
    return 


# reads the heuristic file and creates a dictionary
def read_heuristic_file(filename): 
    val = {}
    file = open(filename, 'r')
    lines = file.readlines()
    file.close()
    for line in lines[:-1]:
        data = line.split()
        val[data[0]] = float(data[1])
    return val

# read_file function reads the input file and creates a dictionary with cost associated with its locations
def read_file(file_name): 
    graph = {}
    file = open(file_name, 'r')
    lines = file.readlines()
    file.close()
    for line in lines[:-1]:
        data = line.split()
        if data[0] in graph:
            graph[data[0]][data[1]] = float(data[2])
        else:
            graph[data[0]] = {data[1]: float(data[2])}
        if data[1] in graph:
            graph[data[1]][data[0]] = float(data[2])
        else:
            graph[data[1]] = {data[0]: float(data[2])}
    return graph

# function that determines if the search is informed or uninformed
# if heuristic is not provided then program must do uninformed search
# and if heuristic is provided then program should do informed search
def search(args):
    if len(args) == 3:
        uniform_cost_search(read_file(args[0]), args[1], args[2])
    if len(args) == 4:
        astar_search(read_file(args[0]), args[1], args[2], read_heuristic_file(args[3]))
    return

def parse_arguments():
    if len(sys.argv) == 4 or len(sys.argv) == 5:
        search(sys.argv[1:])
    else:
        print("Incorrect number of arguments > ")
        print("For uninformed search: python3 find_route input_filename.txt origin_city destination_city")
        print("For informed search: python3 find_route input_filename.txt origin_city destination_city heuristic_filename.txt")
    return

if __name__ == "__main__":
    parse_arguments()
