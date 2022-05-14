import sys
from queue import PriorityQueue
from inputfilename import *
from algorithms import *

# If there are 5 arguments, it will go in if loop.
# First argument : File Name
# Second argument : Source
# Third argument : Destination
# Fourth argument : File Name
if len(sys.argv) == 4:
    file_name = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    graph = inputfile(file_name)  # Graph : One node connected to other possible nodes.
    route, node_expanded, distance = UniformCostSearch(source, destination, graph)
    print("nodes expanded: {}".format(node_expanded))
    print("distance: {} km".format(distance))
    print("route:")
    node_count = source
    if len(route) == 0:
        print("none")
    else:
        for path in route[::-1]:
            print("{} to {}, {} km".format(node_count, path, graph[node_count][path]))
            node_count = path


# If there are 5 arguments, it will go in else loop.
# First argument : File Name
# Second argument : Source
# Third argument : Destination
# Fourth argument : Heuristiv File Name
elif len(sys.argv) == 5:
    file_name = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    heuristic_name = sys.argv[4]
    graph = inputfile(file_name)
    h_value = heuristicfile(heuristic_name)      # All Heuristics Values.
    route, node_expanded, distance = Astar(source, destination, graph, h_value)
    print("nodes expanded: {}".format(node_expanded))
    print("distance: {} km".format(distance))
    print("route:")
    node_count = source
    if len(route) == 0:
        print("none")
    else:
        for path in route[::-1]:
            print("{} to {}, {} km".format(node_count, path, graph[node_count][path]))
            node_count = path


# ['Luebeck', 'Hamburg', '63']
# ['Hamburg', 'Bremen', '116']
# ['Hamburg', 'Hannover', '153']
# ['Hamburg', 'Berlin', '291']
# ['Bremen', 'Hannover', '132']
# ['Bremen', 'Dortmund', '234']
# ['Hannover', 'Magdeburg', '148']
# ['Hannover', 'Kassel', '165']
# ['Magdeburg', 'Berlin', '166']
# ['Berlin', 'Dresden', '204']
# ['Dresden', 'Leipzig', '119']
# ['Leipzig', 'Magdeburg', '125']
# ['Dortmund', 'Duesseldorf', '69']
# ['Kassel', 'Frankfurt', '185']
# ['Frankfurt', 'Dortmund', '221']
# ['Frankfurt', 'Nuremberg', '222']
# ['Leipzig', 'Nuremberg', '263']
# ['Dortmund', 'Saarbruecken', '350']
# ['Saarbruecken', 'Frankfurt', '177']
# ['Saarbruecken', 'Karlsruhe', '143']
# ['Karlsruhe', 'Stuttgart', '71']
# ['Stuttgart', 'Frankfurt', '200']
# ['Stuttgart', 'Munich', '215']
# ['Stuttgart', 'Nuremberg', '207']
# ['Nuremberg', 'Munich', '171']
# ['Manchester', 'Birmingham', '84']
# ['Birmingham', 'Bristol', '85']
# ['Birmingham', 'London', '117']


# ('Grapg is', 
# {'Saarbruecken': {'Dortmund': 350.0, 'Frankfurt': 177.0, 'Karlsruhe': 143.0}, 
# 'Nuremberg': {'Stuttgart': 207.0, 'Leipzig': 263.0, 'Frankfurt': 222.0, 'Munich': 171.0}, 
# 'Hannover': {'Kassel': 165.0, 'Magdeburg': 148.0, 'Bremen': 132.0, 'Hamburg': 153.0}, 
# 'Dresden': {'Berlin': 204.0, 'Leipzig': 119.0}, 
# 'Luebeck': {'Hamburg': 63.0}, 
# 'Dortmund': {'Saarbruecken': 350.0, 'Duesseldorf': 69.0, 'Frankfurt': 221.0, 'Bremen': 234.0}, 
# 'Leipzig': {'Nuremberg': 263.0, 'Magdeburg': 125.0, 'Dresden': 119.0}, 
# 'Bremen': {'Dortmund': 234.0, 'Hannover': 132.0, 'Hamburg': 116.0}, 
# 'Munich': {'Stuttgart': 215.0, 'Nuremberg': 171.0}, 
# 'Birmingham': {'London': 117.0, 'Manchester': 84.0, 'Bristol': 85.0}, 
# 'Stuttgart': {'Nuremberg': 207.0, 'Frankfurt': 200.0, 'Munich': 215.0, 'Karlsruhe': 71.0}, 
# 'Berlin': {'Magdeburg': 166.0, 'Dresden': 204.0, 'Hamburg': 291.0}, 
# 'Magdeburg': {'Berlin': 166.0, 'Hannover': 148.0, 'Leipzig': 125.0}, 
# 'Duesseldorf': {'Dortmund': 69.0}, 
# 'Bristol': {'Birmingham': 85.0}, 
# 'Hamburg': {'Luebeck': 63.0, 'Berlin': 291.0, 'Hannover': 153.0, 'Bremen': 116.0}, 
# 'Manchester': {'Birmingham': 84.0}, 
# 'Kassel': {'Hannover': 165.0, 'Frankfurt': 185.0}, 
# 'Frankfurt': {'Saarbruecken': 177.0, 'Dortmund': 221.0, 'Nuremberg': 222.0, 'Kassel': 185.0, 'Stuttgart': 200.0}, 
# 'London': {'Birmingham': 117.0}, 
# 'Karlsruhe': {'Saarbruecken': 143.0, 'Stuttgart': 71.0}})



# Note : Was unable to do the node generated part, as I was not able to get the correct answer for that.