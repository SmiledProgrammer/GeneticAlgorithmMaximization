MAX_POPULATION_AMOUNT = 1000
MAX_POPULATION_SIZE = 100

import random

def flip(probability: float) -> float:
    return random.random() < probability

from typing import List

Allele = bool
Chromosome = List[Allele]

class Individual:
    def __init__(self, chromosome: Chromosome, x: float, fitness: float, parent1: int, parent2: int, cross_point: int):
        self.chromosome = chromosome
        self.x = x
        self.fitness = fitness
        self.parent1 = parent1
        self.parent2 = parent2
        self.cross_point = cross_point

Population = List[Individual]
