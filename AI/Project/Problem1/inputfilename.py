# Open the input file and will return graph.
def inputfile(filename): 
    graph_tracing = {}
    with open(filename, 'r') as file: #open the inputfile.
        content = file.readlines() # Reading lines from the file.
        file.close()
    for line in content[:-1]:
        data_info = line.split() # Data in the file in list format.
        # print(data) 
        if data_info == 'END OF INPUT': # Make the graph from the data.
            return graph_tracing
        else:
            if data_info[0] in graph_tracing:
                graph_tracing[data_info[0]][data_info[1]] = float(data_info[2])
            else:
                graph_tracing[data_info[0]] = {data_info[1]: float(data_info[2])}
            if data_info[1] in graph_tracing:
                graph_tracing[data_info[1]][data_info[0]] = float(data_info[2])
            else:
                graph_tracing[data_info[1]] = {data_info[0]: float(data_info[2])}
    return graph_tracing
 
# Open the heuristic file and will return Name of city and its heuristic value in Dictionary.
def heuristicfile(filename): 
    heuristic_value = {}
    with open(filename, 'r') as file: #open the inputfile.
        content = file.readlines() # Reading lines from the file.
        file.close()
    for line in content[:-1]:
        data_info = line.split()
        if data_info == 'END OF INPUT': # Will return the heuristive value.
            return heuristic_value
        else:
            heuristic_value[data_info[0]] = float(data_info[1])
    return heuristic_value