import application as app
from config import *

def main():
    app.run(fitness, initial_population, crossover_probability, mutation_probability, max_generations)

if __name__ == "__main__":
    main()
