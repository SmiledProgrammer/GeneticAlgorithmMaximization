def fitness(x: float) -> float:
    return -0.2*x**2 + 5.5*x + 6

initial_population = range(-1, 29)
crossover_probability = 0.5
mutation_probability = 0.01
max_generations = 100
