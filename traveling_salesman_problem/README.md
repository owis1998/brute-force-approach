# traveling-salesman-problem
python program to get optimal solution for traveling salesman problem

i used brute force approche, the time complexity is O(n!) !! it takes to much.
i represented the cities as a graph in dictionary, any argument pass to the algorithm function should be a dic and list of vertex, like this:

vertices_list = ['B', 'C', 'D', 'E', 'F', 'G', 'H']
adj_list = {
			 'B' : [('C', 8), ('F', 7), ('H', 9)],
			 'C' : [('D', 1), ('E', 2), ('F', 4), ('B', 8)],
			 'D' : [('C', 1), ('E', 4)],
			 'E' : [('C', 2), ('D', 4), ('G', 3)],
			 'G' : [('E', 3), ('F', 1), ('H', 5)],
			 'H' : [('B', 9), ('G', 5)],
			 'F' : [('C', 4), ('B', 7), ('G', 1)]
			}
