import math

def get_all_possible_combinations(my_list):
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


def get_minimum_total_cost(jops_array):
	my_list = [i for i in range(1, len(jops_array) + 1)]
	possible_combinations = get_all_possible_combinations(my_list)
	minimum_cost = 1e9

	for pc in possible_combinations:
		tmp = 0
		for i in range(0, len(pc)):
			tmp += jops_array[i][int(pc[i]) - 1]
			
		if minimum_cost > tmp:
			minimum_cost, combination = tmp, pc

	return minimum_cost, combination
