from population import Population
from chromosome import Chromosome

if __name__ == '__main__':

    file = open("knapsack_3.txt", "r")
    line = file.readline()
    number_of_items, knapsack_capacity = map(int, line.split())
    items = []
    while True:
        line = file.readline()
        if not line:
            break
        items.append(list(map(int, line.split())))

    number_of_generations = 100
    population_size = 1000
    children_size = 2000
    tournament_size = 5
    mutation_rate = 0.02

    Chromosome.set_number_of_items(number_of_items)
    Chromosome.set_knapsack_capacity(knapsack_capacity)
    Chromosome.set_items(items)
    population = Population(population_size, children_size, tournament_size, mutation_rate)
    population.generate(number_of_generations)
    population.print_answer()
    population.show_statistics()
