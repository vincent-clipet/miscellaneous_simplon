from __future__ import annotations
from ast import Tuple
import copy
import random
import statistics



class GeneticSolution():
	
	pathing_costs = None
	data = None

	def __init__(self, max_possible_value):
		self.values = GeneticSolution.generate_random_solution(max_possible_value)
		self.score = GeneticSolution.calculate_score(self.values)



	@classmethod
	def calculate_score(cls, chain: list[int]) -> int:
		previous_value = None
		sum = 0
		for i in chain:
			if previous_value is None:
				previous_value = i
			else:
				sum += GeneticSolution.pathing_costs[previous_value][i]
				previous_value = i
		return sum



	@classmethod
	def get_best_solution(cls) -> GeneticSolution:
		max = GeneticSolution.data[0]
		for s in GeneticSolution.data:
			if s.score >= max.score:
				max = s
		return max



	@classmethod
	def fitting(cls) -> Tuple[list, list]:
		median = GeneticSolution.get_median_value()
		print("median:", median)
		fit = []
		unfit = []
		for s in GeneticSolution.data:
			if s.score < median:
				unfit.append(s)
			else:
				fit.append(s)
		return (fit, unfit)
	


	@staticmethod
	def crossover(dataset, probability):
		pass

	@staticmethod
	def mutation(dataset, probability, max_possible_value):
		for d in dataset:
			if (random.random() < probability):
				old_value_for_print = d.to_string()
				random_index_1 = -1
				random_index_2 = -1
				while (random_index_1 == random_index_2):
					random_index_1 = random.randint(0, max_possible_value - 1)
					random_index_2 = random.randint(0, max_possible_value - 1)
				d.values[random_index_1], d.values[random_index_2] = d.values[random_index_2], d.values[random_index_1]
				print("mutated :", old_value_for_print, "=>", d.to_string())



	@classmethod
	def get_average_value(cls) -> float:
		avg = None
		sum = 0
		for s in GeneticSolution.data:
			sum += s.score
		avg = float(sum / len(GeneticSolution.data))
		return avg
	
	@classmethod
	def get_median_value(cls) -> int:
		median = None
		all = []
		for s in GeneticSolution.data:
			all.append(s.score)
		median = statistics.median(all)
		return median


	def print(self):
		print(self.to_string())

	def to_string(self):
		return "" + str(self.score) + " <- " + str(self.values)

	@classmethod
	def print_data(cls):
		for s in GeneticSolution.data:
			s.print()
	
	@staticmethod
	def print_solution_list(sl):
		for s in sl:
			s.print()



	@classmethod
	def generate_random_solution(cls, max_possible_value: int):
		possible_values = list(range(0, max_possible_value))
		ret = []
		while len(possible_values) > 0:
			index_to_remove = random.randint(0, len(possible_values) - 1)
			ret.append(possible_values.pop(index_to_remove))
		return ret

	@classmethod
	def generate_data(cls, max_possible_value, data_limit) -> list[GeneticSolution]:
		ret = []
		for i in range(0, data_limit):
			ret.append(GeneticSolution(max_possible_value))
		GeneticSolution.data = ret
	
	@classmethod
	def generate_pathing_cost(cls, possible_values_count: int, min_score: int, max_score: int):
		# create 2-dimensional array full of 'None'
		ret = []
		for y in range(0, possible_values_count):
			ret.append([None for _ in range(0, possible_values_count)])

		for y in range(0, possible_values_count):
			costs = []
			for x in range(0, possible_values_count):
				if x == y:
					costs.append(0)
				else:
					existing_value = ret[x][y]
					# this pathing cost does not exist, create it
					if (existing_value is None):
						costs.append(random.randint(min_score, max_score))
					# this pathing cost already exists elsewhere, copy it here
					else:
						costs.append(existing_value)
			ret[y] = costs
		GeneticSolution.pathing_costs = ret