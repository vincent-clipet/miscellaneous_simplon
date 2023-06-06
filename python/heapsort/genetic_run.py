from __future__ import annotations
import math
import random
from src.genetic_solution import GeneticSolution



##########
# CONFIG #
##########

MAX_POSSIBLE_VALUE = 10
DATA_LIMIT = 20
PROBABILITY_CROSSOVER = 0.5
PROBABILITY_MUTATION = 0.02

MIN_DISTANCE = 10
MAX_DISTANCE = 30



#############
# FUNCTIONS #
#############




#######
# RUN #
#######

GeneticSolution.generate_pathing_cost(MAX_POSSIBLE_VALUE, MIN_DISTANCE, MAX_DISTANCE)
GeneticSolution.generate_data(MAX_POSSIBLE_VALUE, DATA_LIMIT)

print("Data: ")
GeneticSolution.print_data()

print("Best solution: ")
GeneticSolution.get_best_solution().print()

fit_unfit = GeneticSolution.fitting()
fit = fit_unfit[0]
unfit = fit_unfit[1]
print("Fit:", len(fit))
GeneticSolution.print_solution_list(fit)
print("Unfit:", len(unfit))
GeneticSolution.print_solution_list(unfit)

print("Mutations: ")
GeneticSolution.mutation(unfit, PROBABILITY_MUTATION, MAX_POSSIBLE_VALUE)
