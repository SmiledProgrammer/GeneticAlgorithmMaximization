import sys
import matplotlib.pyplot as plt
from typing import List
from typing import Callable

from chromosomes import setup_chromosomes
from chromosomes import print_chromosome_value_range
from genetic_algorithm import GeneticAlgorithm
from plots import display_function_plot
from plots import display_fitness_plots

def fetch_args(): # TODO: remove
    arglen = len(sys.argv)
    if arglen > 4:
        raise ValueError('Too many arguments.')
    if arglen > 3:
        mutation_probability = float(sys.argv[3])
    else:
        mutation_probability = 0.01
    if arglen > 2:
        crossover_probability = float(sys.argv[2])
    else:
        crossover_probability = 0.5
    if arglen > 1:
        max_generations = int(sys.argv[1])
    else:
        max_generations = 100
    return [max_generations, crossover_probability, mutation_probability]

def run(fitness_function: Callable, initial_population: List[float], crossover_probability: float, mutation_probability: float, max_generations: int):
    print('Starting the optimization...')
    #[maxgenerations, crossprob, mutprob] = fetch_args()

    chrlen = 32#25
    chrprec = 10**6
    chroffset = 14.0
    setup_chromosomes(chrlen, chrprec, chroffset)

    ga = GeneticAlgorithm()
    ga.setup(fitness_function, initial_population, crossover_probability, mutation_probability, max_generations)

    [max_x, max_value, max_fitness, min_fitness, avg_fitness] = ga.find_max()
    print('Best: x = {}, f(x) = {}'.format(max_x, max_value))

    figname = 'f(x) = -0.2x^2 + 5.5x + 6'
    display_function_plot(fitness_function, figname, max_x, max_value, initial_population[0], initial_population[-1])
    display_fitness_plots(max_generations, max_fitness, min_fitness, avg_fitness)
    
    plt.show()
