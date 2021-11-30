import genetic_algorithm as ga

def fitness(x: float) -> float:
    return -0.2*x**2 + 5.5*x + 6

def main():
    genetic_alg = ga.GeneticAlgorithm()
    pop = list(range(-1, 29))
    crossprob = 0.5
    mutprob = 0.4
    maxgenerations = 100
    genetic_alg.setup(fitness, pop, crossprob, mutprob, maxgenerations)
    [max_x, max_value, best_fitness, avg_fitness, worst_fitness] = genetic_alg.find_max()

if __name__ == "__main__":
    main()
