# Artificial Intelligence Implementing various search algorithms 
Programming language: python3

Implemented the search algorithm using A* search and uniform cost search algorithms

In file find_route.py parse_argument parses command line arguments and identifies if it's a uninformed or informed search 
if the heuristic file is specified in the command line arguments A* search algorithms will be used else uniform cost search will be used
Function read_file will read the input file and store the graph information in a dictionary. 
and function read_heuristic_file will read the heuristic file and store the information as dictionary
The function uniform_cost_search and astar_search expands the graph and finds the number of nodes expanded and generated along with the distance information the path is found by backtracking the parent node from which we found the optimal path to the destination.
The output function prints the output to console after running the program
 
Commnads to run on local system:
Copy all the files in same folder. Open terminal and type 

For Informed search type 
python3 find_route.py input1.txt Bremen Kassel h_kassel.txt

For uninformed search 
python3 find_route.py input1.txt Bremen Kassel

references: 
https://www.redblobgames.com/pathfinding/a-star/implementation.html
https://towardsdatascience.com/a-star-a-search-algorithm-eb495fb156bb
