from __future__ import annotations
import math
import random
from src.genetic_solution import GeneticSolution



##########
# CONFIG #
##########

DEBUG = False
STOP_EACH_ITERATION = False

ITERATIONS = 1000

MAX_POSSIBLE_VALUE = 30
DATA_LIMIT = 300
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

GeneticSolution.verbose = DEBUG
GeneticSolution.generate_pathing_cost(MAX_POSSIBLE_VALUE, MIN_DISTANCE, MAX_DISTANCE)
GeneticSolution.generate_data(MAX_POSSIBLE_VALUE, DATA_LIMIT)


if DEBUG:
    print("===== DATA =====")
    GeneticSolution.print_data()

    print("===== PATHING COSTS =====")
    print(GeneticSolution.pathing_costs)



last_best_solution = None
if not DEBUG: print("===== BEST SOLUTION ======")



for iter in range(0, ITERATIONS):


    # Fitting
    fit_unfit = GeneticSolution.fitting()
    fit = fit_unfit[0]
    unfit = fit_unfit[1]
    if DEBUG:
        print(f"===== FITTING ===== ({len(fit)} | {len(unfit)})")
        print("Fit:", len(fit))
        GeneticSolution.print_solution_list(fit)
        print("Unfit:", len(unfit))
        GeneticSolution.print_solution_list(unfit)
    


    # Crossover
    if DEBUG: print("===== CROSSOVER =====")
    GeneticSolution.crossover(fit, PROBABILITY_CROSSOVER)



    # Display best solution found
    if DEBUG: print("===== BEST SOLUTION ======")
    current_best_solution  = GeneticSolution.get_best_solution()

    if last_best_solution is None:
        last_best_solution = GeneticSolution.get_best_solution()
        print()
        print(f">>>   Initial solution : {last_best_solution.to_string()}")
        print()
    elif current_best_solution.score < last_best_solution.score:
        print(f">>>   New best   |   {last_best_solution.score} -> {current_best_solution.score}   |   ({iter} iterations)")
        last_best_solution = current_best_solution
        last_best_solution.print()
        print()
    else:
        if DEBUG: print("No changes. Current best version: ", last_best_solution.to_string())



    # Mutations
    if DEBUG: print("===== MUTATIONS ======")
    GeneticSolution.remove_unfit_from_data(unfit, MAX_POSSIBLE_VALUE)
    GeneticSolution.mutation(unfit, PROBABILITY_MUTATION, MAX_POSSIBLE_VALUE)



    if STOP_EACH_ITERATION: input()