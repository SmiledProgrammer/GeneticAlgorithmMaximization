from app import application
import config as cfg

def main():
    application.run(cfg.fitness_function, cfg.initial_population, cfg.crossover_probability, cfg.mutation_probability, cfg.max_generations)

if __name__ == "__main__":
    main()
