import math

def get_all_possible_combinations(vertices_list):
	my_list = [i for i in range(1, len(vertices_list) + 1)]
	r = 1
	possible_combinations = []
	for r in range(1, len(my_list) + 1):
		index = 0
		x = 1
		for _ in range(0, int(math.factorial(len(my_list)) / math.factorial(len(my_list) - r))):
			for j in range(0, math.factorial(len(my_list) - r)):
				if len(possible_combinations) < math.factorial(len(my_list)):
					possible_combinations.append(str(x))
					continue

				while True:
					if possible_combinations[index].find(str(x)) == -1:
						possible_combinations[index] += str(x)
						break
					else:
						if x == len(my_list):
							x = 1
						else:
							x += 1

				index += 1

			x += 1
			if x > len(my_list):
				x = 1

	return possible_combinations

def are_they_adjacent(ver1, ver2, adj_list):
	for i in adj_list[ver1]:
		if i[0] == ver2:
			return True
	else:
		return False

def are_all_connected_to_each_other(tour, vertices_list, adj_list):
	for i in range(0, len(tour) - 1):
		ver1 = vertices_list[int(tour[i]) - 1]
		ver2 = vertices_list[int(tour[i + 1]) - 1]
		if not are_they_adjacent(ver1, ver2, adj_list):
			return False
	else:
		return True


def get_tour_cost(tour, adj_list):
	total_cost = 0
	for i in range(0, len(tour) - 1):
		ver1 = vertices_list[int(tour[i]) - 1]
		ver2 = vertices_list[int(tour[i + 1]) - 1]
		for i in adj_list[ver1]:
			if i[0] == ver2:
				total_cost += i[1]

	return total_cost 
		

def algorithm(vertices_list, adj_list):
	possible_combinations = get_all_possible_combinations(vertices_list)
	optimal_cost, op_tour = 1e9, None

	for pc in possible_combinations:
		for tour in pc:
			first_vertex = vertices_list[int(pc[0]) - 1]
			last_vertex = vertices_list[int(pc[-1]) - 1]
			if are_they_adjacent(first_vertex, last_vertex, adj_list):
				if are_all_connected_to_each_other(pc, vertices_list, adj_list):
					tour_cost = get_tour_cost(pc + pc[0], adj_list)
					if optimal_cost > tour_cost:
						optimal_cost, op_tour = tour_cost, pc + pc[0]

	optimal_tour = ''
	for k in op_tour:
		optimal_tour += vertices_list[int(k) - 1]

	return optimal_cost, optimal_tour
