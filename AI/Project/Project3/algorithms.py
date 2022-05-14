import sys
from queue import PriorityQueue
from inputfilename import *

# Implementing A* search algorithm.
# Source = source_node
# Destination = dest_node
# heuristic value of each node = val
def Astar(source_node, dest_node, graph, h_value): 
    print("Graph with A*")
    print("\n")
    node_expanded = 0
    fringe = PriorityQueue()
    fringe.put((0, source_node))
    node_visited = {}
    node_visited[source_node] = ("", 0)
    node_explored = [] # whatever nodes we'll find, we'll add here.
    while not fringe.empty():
        x, countnode = fringe.get()
        node_expanded += 1
        if countnode == dest_node:
            break
        if countnode in node_explored:
            continue
        node_explored.append(countnode)
        for i in graph[countnode]:
            if i not in node_visited:
                node_visited[i] = (countnode, graph[countnode][i] + node_visited[countnode][1])
            fringe.put((graph[countnode][i] + node_visited[countnode][1] + h_value[i], i))
    route = []
    distance = "infinity"
    if dest_node in node_visited:
        dist = 0.0
        countnode = dest_node
        while countnode != source_node:
            dist += graph[node_visited[countnode][0]][countnode]
            route.append(countnode)
            countnode = node_visited[countnode][0]
    return route, node_expanded, dist


# Implementing uniform cost search algorithm.
# src = node
# dest = dest_node
def UniformCostSearch(source_node, dest_node, graph): 
    print("*****Graph with uniform cost search.*****")
    print("\n")
    # print("Graph For UCS is :", graph)
    # print("\n")
    node_expanded = 0
    fringe = PriorityQueue()
    fringe.put((0, source_node))
    # print("fringe is ",fringe.get())
    node_visited = {}
    node_visited[source_node] = ("", 0)
    # print("Visited is",visited)
    parsed = []
    while not fringe.empty():
        x, node_count = fringe.get()
        # print("X and node_count",X,node_count)
        node_expanded += 1
        if node_count == dest_node:
            break
        if node_count in parsed:
            continue
        parsed.append(node_count)
        for i in graph[node_count]:
            # print(graph[node_count])
            # print(graph[node_count][i] +visited[node_count][1])
            fringe.put((graph[node_count][i]+node_visited[node_count][1], i))

            if i not in node_visited:
                node_visited[i] = (node_count, graph[node_count][i]+node_visited[node_count][1])
    route = []
    distance = "infinity"
    if dest_node in node_visited:
        distance = 0.0
        node_count = dest_node
        while node_count != source_node:
            distance += graph[node_visited[node_count][0]][node_count]
            route.append(node_count)
            node_count = node_visited[node_count][0]
    return route, node_expanded, distance


