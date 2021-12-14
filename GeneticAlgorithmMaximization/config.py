# Fitness function
# (as a python function definition)
fitness_function = lambda x : \
    -0.2*x**2 + 5.5*x + 6

# Initial population
# (as a list of int values)
initial_population = \
    range(-1, 29)

# Probability of crossover of two chromosomes
# (value range: <0, 1>)
crossover_probability = \
    0.6

# Probability of mutation of an allele
# (value range: <0, 1>)
mutation_probability = \
    0.02

# Maximum number of generations
# (as an integer)
max_generations = \
    100
