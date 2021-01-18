class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def how_far_from(self, point):
		if self.x == point.x:
			return 0 
		
		higher_point, lower_point = (self, point) if self.y > point.y else (point, self) 

		#Pythagorean theorem
		distance = ((higher_point.x - lower_point.x) ** 2 + (higher_point.y - lower_point.y) ** 2) ** 0.5
		return distance

	def closest_point(self, points):
		distance = 1e9
		for p in points:
			if self.how_far_from(p) < distance and not self is p:
				closestP = p
				distance = self.how_far_from(p)

		return distance, closestP


def find_closest_pair(list_of_points):
	distance = 1e9
	for i in range(0, len(list_of_points) - 1):
		tmp = list_of_points[i].closest_point(list_of_points)

		if tmp[0] < distance:
			distance = tmp[0]
			closest_pair = [list_of_points[i], tmp[1]]

	return closest_pair
