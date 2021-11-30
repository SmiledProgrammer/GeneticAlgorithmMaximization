from random import random
from common import flip
from common import Allele
from common import Chromosome
from common import Population

class GeneticAlgorithm:
    def __init__(self):
        self.chomosome_length = 30
        self.two_powers = [] # TODO: fill

    def setup(self, fitness_func: function, init_pop: Population, crossover_prob: float, mutation_prob: float, max_generations: int):
        self.fitness_function = fitness_func
        self.population = init_pop
        self.crossover_probability = crossover_prob
        self.mutation_probability = mutation_prob
        self.max_generations = max_generations
    
    def find_max(self):
        pass # TODO

    def fitness_to_chromosome(self, fitness: float) -> Chromosome:
        chrom = Chromosome()
        for i in range(self.chromosome_length):
            pass # TODO


    def select(self, population_size: int, fitness_sum: float, population: Population) -> int:
        j = 0
        part_sum = 0.0
        rnd = fitness_sum * random()
        while True:
            j = j + 1
            part_sum = part_sum + population[j].fitness # TODO: optimize and calculate partsums earlier
            if part_sum >= rnd or j == population_size:
                break
        return j

    def mutate(self, allele: Allele) -> Allele:
        if flip(self.mutation_probability):
            return not allele
        else:
            return allele

    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        if flip(self.crossover_probability):
            crosspoint = random(0, self.chomosome_length - 1)
        else:
            crosspoint = self.chomosome_length
        child1 = Chromosome()
        child2 = Chromosome()
        for j in range(0, crosspoint):
            child1[j] = mutate(parent1[j])
            child2[j] = mutate(parent2[j])
        for j in range(crosspoint, self.chomosome_length):
                child1[j] = mutate(parent2[j])
                child2[j] = mutate(parent1[j])
        return child1, child2, crosspoint
