NAME : Jayesh Parsnani
UTA ID: 1001964955

LANGUAGE USED : PYTHON

STRUCTURE OF THE CODE:
1. For running the UCS pass 4 arguments.
2. For running A* pass 5 arguments.



Run : find_route.py with inputefile, source, destination and hueristic value file.
It contain if-else loop for different agruments. 
If 4 agruments are passed first it will call inputfile where we're creating graph of each node connect to other nodes and then it'll call for UCS. Uncomment commented lines to get better understanding of the flow of UCS. 
If 5 arguments are passed it'll go in else loop and it'll call heuristicfile first and then and will call A* algorithm. Uncomment commented lines to get better understanding of the flow of A*.

While loop will work until it is empty. At every step node is put into parsed so that the step won't repeat. If node is not in the parsed, we'll append into parsed and will generate the node connections and will put in fringe.
Same for A*.

Check Example.pdf for clear understanding.