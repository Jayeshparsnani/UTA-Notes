import copy

# Parents in the network
parents = {
    'A': ['B','E'], 
    'B': None, 
    'E': None, 
    'J': ['A'], 
    'M': ['A']
}

# Given probability
given_probability = {
    "B": 0.001,
    "E": 0.002,
    "A|B,E": 0.95,
    "A|B,nE": 0.94,
    "A|nB,E": 0.29,
    "A|nB,nE": 0.001,
    "J|A": 0.90,
    "J|nA": 0.05,
    "M|A": 0.70,
    "M|nA": 0.01
}

# Finding the probability.
def find_probability(phase):
    if phase[0] == "n":
        return (1 - find_probability(phase[1:])) # Recursive call.
    if phase in given_probability:
        return given_probability[phase]

# finding parent.
def find_parent(array):
    current_array = []
    for node in array:
        current_term = node + "|"
        if node[0] == "n":
            parent_node = parents[node[1:]]
        else:
            parent_node = parents[node]

        if parent_node != None:
            for p in parent_node:
                if p in array:
                    current_term = current_term + p + ","
                else:
                    current_term = current_term + "n" + p + ","
        
        current_term = current_term[0:len(current_term)-1]
        current_array.append(current_term)
    return current_array  

# Computing probability.
reqd_terms = ['A', 'B', 'E', 'J', 'M']
def prob_compute(array):
    if len(array) == 5:
        current_array = find_parent(array)
        product = 1
        for node in current_array:
            product = product * find_probability(node)
        return product
    else:
        # if node is not present add the node.
        for node_missed in reqd_terms:
            if node_missed in array:
                continue
            else:
                flag = False
                for array_node in array:
                    if node_missed == array_node[1:]:
                        flag = True
                        break

                if flag == True:
                    continue
                else:
                    missedNode = node_missed
                    break
        #compute false and true value for the missed node.
        array1 = copy.deepcopy(array)
        array2 = copy.deepcopy(array)
        array1.append(missedNode)
        array2.append("n"+missedNode)
        return prob_compute(array1) + prob_compute(array2)

def reqd_notations(array):
    current_array = []
    for node in array:
        # if node is true.
        if node[1] == "t":
            current_array.append(node[0])
        else:
            # if node is false
            current_array.append("n"+node[0])
    return current_array