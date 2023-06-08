from __future__ import annotations
from ast import Tuple
import copy
import random
import statistics



class GeneticSolution():
	
	pathing_costs = None
	data = None
	verbose = False

	def __init__(self, max_possible_value):
		self.set_values(GeneticSolution.generate_random_solution_values(max_possible_value))
		self.score = GeneticSolution.calculate_score(self.values)

	def set_values(self, values):
		self.values = values
		self.score = GeneticSolution.calculate_score(self.values)



	@classmethod
	def calculate_score(cls, chain: list[int]) -> int:
		"""Calculates the score from a given list

		Args:
			chain (list[int]): list to give a score to

		Returns:
			int: score
		"""
		previous_value = None
		sum = 0
		for i in chain:
			if previous_value is None:
				previous_value = i
			else:
				sum += cls.pathing_costs[previous_value][i]
				previous_value = i
		return sum



	@classmethod
	def get_best_solution(cls) -> GeneticSolution:
		"""Find the best solution in the current dataset

		Returns:
			GeneticSolution: best solution
		"""
		min = cls.data[0]
		for s in cls.data:
			if s.score < min.score:
				min = s
		return min



	@classmethod
	def fitting(cls) -> Tuple[list, list]:
		"""Fitting function for the genetic algorithm.
		Splits the dataset into 2 sub-sets of equal size and return those in a tuple
		First element contains the 'fit' values (the good half)
		Second element contains the 'unfit' values (the bad half)

		Returns:
			Tuple[list, list]: Tuple(fit_data, unfit_data)
		"""
		median = cls.get_median_value()
		if cls.verbose: print("median:", median)
		fit = []
		unfit = []
		for s in cls.data:
			if s.score < median:
				unfit.append(s)
			else:
				fit.append(s)
		return (fit, unfit)
	


	@classmethod
	def crossover(cls, dataset: list[GeneticSolution], probability: float):
		"""Mix/recombinate solutions between them; from the given dataset
		The probability is used to limit the quantity of data that gets affected/
		Ex: probability = 0.7 => 70% of data is mixed together, 30% is left unchanged

		Args:
			dataset (list[GeneticSolution]): dataset
			probability (float): probability to execute the crossover process (bewteen 0 and 1)
		"""
		while len(dataset) >= 2:
			d1 = random.choice(dataset)
			dataset.remove(d1)
			d2 = random.choice(dataset)
			dataset.remove(d2)

			# probability match => crossover
			if random.random() < probability:
				old_value_for_print_d1 = d1.to_string()
				old_value_for_print_d2 = d2.to_string()
				cls.crossover_a_b(d1, d2)
				if cls.verbose: print("crossover :", old_value_for_print_d1, "=>", d1.to_string())
				if cls.verbose: print("crossover :", old_value_for_print_d2, "=>", d2.to_string())
	


	@classmethod
	def crossover_a_b(cls, a: GeneticSolution, b: GeneticSolution):
		"""Sub-function of 'crossover()'

		Args:
			a (GeneticSolution): solution a
			b (GeneticSolution): solution b
		"""
		
		possible_values = copy.deepcopy(a.values)
		possible_values.sort()
		
		a_first_half = a.values[0:int(len(a.values)/2)]
		a_second_half = a.values[int(len(a.values)/2):]
		b_first_half = b.values[0:int(len(b.values)/2)]
		b_second_half = b.values[int(len(b.values)/2):]
		
		new_a_values = a_first_half + b_second_half
		new_b_values = b_first_half + a_second_half

		new_a_values = cls.fix_chain(new_a_values, possible_values)
		new_b_values = cls.fix_chain(new_b_values, possible_values)

		a.set_values(new_a_values)
		b.set_values(new_b_values)


	
	@classmethod
	def fix_chain(cls, new_a: list[int], possible_values: list[int]) -> list[int]:
		"""Fixes broken solutions originating from the crossover process
		Some solutions contain duplicates, and are missing some possible values
		This function will fix the broken parts by replacing incorrect nodes with valid ones

		Args:
			new_a (list[int]): a list of 'int' values to fix
			possible_values (list[int]): list of all possible values, for reference

		Returns:
			_type_: list 'new_a' given as parameter, repaired
		"""

		# gather all unique values
		unique_values = []
		duplicate_values = []
		for i in new_a:
			try:
				# value already exists
				unique_values.index(i)
				duplicate_values.append(i)
			except ValueError:
				# value does not already exist
				unique_values.append(i)
		
		# No duplicate, all good, return
		if len(unique_values) == len(possible_values): return new_a

		# gather missing values
		missing_values = copy.deepcopy(possible_values)
		for i in unique_values:
			missing_values.remove(i)
		
		# let's go
		for i in duplicate_values:
			# randomize : do we replace this value in the first half, or the second half ?
			if random.random() < 0.5:
				index_to_replace = new_a.index(i)
			else:
				index_to_replace = new_a.index(i, int(len(new_a)/2))
			
			inserted_value = missing_values.pop()
			new_a[index_to_replace] = inserted_value
		
		return new_a



	@classmethod
	def mutation(cls, dataset: list[GeneticSolution], probability: float, max_possible_value: int):
		"""Mutates all solutions from the given dataset, following the given probability
		The probability is used to limit the quantity of data that gets affected
		Ex: probability = 0.01 => 1% of data is mutated, 99% is left unchanged

		Args:
			dataset (list[GeneticSolution]): dataset
			probability (float): probability to execute the mutation process (bewteen 0 and 1)
			max_possible_value (int): max possible value, for reference
		"""
		for d in dataset:
			if (random.random() < probability):
				old_value_for_print = d.to_string()
				random_index_1 = -1
				random_index_2 = -1
				while (random_index_1 == random_index_2):
					random_index_1 = random.randint(0, max_possible_value - 1)
					random_index_2 = random.randint(0, max_possible_value - 1)
				d.values[random_index_1], d.values[random_index_2] = d.values[random_index_2], d.values[random_index_1]
				if cls.verbose: print("mutated :", old_value_for_print, "=>", d.to_string())



	@classmethod
	def remove_unfit_from_data(cls, unfit: list[GeneticSolution], max_possible_value: int):
		# remove all unfit values
		size = len(unfit)
		for i in unfit:
			cls.data.remove(i)
		# Refill with new random ones
		for _ in range(0, size):
			cls.data.append(GeneticSolution(max_possible_value))



	@classmethod
	def get_average_value(cls) -> float:
		"""Get the average value of the current dataset

		Returns:
			float: average
		"""
		avg = None
		sum = 0
		for s in cls.data:
			sum += s.score
		avg = float(sum / len(cls.data))
		return avg
	
	@classmethod
	def get_median_value(cls) -> int:
		"""Get the median value of the current dataset

		Returns:
			int: median
		"""
		median = None
		all = []
		for s in cls.data:
			all.append(s.score)
		median = statistics.median(all)
		return median


	def print(self):
		print(self.to_string())

	def to_string(self):
		return "" + str(self.score) + " <- " + str(self.values)

	@classmethod
	def print_data(cls):
		for s in cls.data:
			s.print()
	
	@staticmethod
	def print_solution_list(sl):
		for s in sl:
			s.print()



	@classmethod
	def generate_random_solution_values(cls, max_possible_value: int) -> list[int]:
		"""Generates values for a random solution

		Args:
			max_possible_value (int): max possible value, for reference

		Returns:
			list[int]: An array containing all possible values once, in a random order
		"""
		possible_values = list(range(0, max_possible_value))
		ret = []
		while len(possible_values) > 0:
			index_to_remove = random.randint(0, len(possible_values) - 1)
			ret.append(possible_values.pop(index_to_remove))
		return ret

	@classmethod
	def generate_data(cls, max_possible_value: int, data_limit: int):
		"""Called at startup.
		Build an internal dataset of random possible solutions

		Args:
			max_possible_value (int): max possible value, for reference
			data_limit (_type_): number of random solutions to generate
		"""
		ret = []
		for i in range(0, data_limit):
			ret.append(GeneticSolution(max_possible_value))
		cls.data = ret
	


	@classmethod
	def generate_pathing_cost(cls, max_possible_value: int, min_score: int, max_score: int):
		"""Called at startup.
		Build the lists necessary to simulate each path's cost

		Args:
			max_possible_value (int): max possible value, for reference
			min_score (int): minimum score for a path
			max_score (int): maximum score for a path
		"""
		# create 2-dimensional array full of 'None'
		ret = []
		for y in range(0, max_possible_value):
			ret.append([None for _ in range(0, max_possible_value)])

		for y in range(0, max_possible_value):
			costs = []
			for x in range(0, max_possible_value):
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
		cls.pathing_costs = ret		