import random
import copy


class Chromosome:
    number_of_items = 0
    knapsack_capacity = 0
    items = []

    @classmethod
    def set_number_of_items(cls, number_of_items):
        cls.number_of_items = number_of_items

    @classmethod
    def set_knapsack_capacity(cls, knapsack_capacity):
        cls.knapsack_capacity = knapsack_capacity

    @classmethod
    def set_items(cls, items):
        cls.items = items

    @classmethod
    def crossover(cls, chr1, chr2):
        cut = random.randrange(0, cls.number_of_items)
        new_knapsack = chr1.knapsack[0:cut]
        new_knapsack.extend(chr2.knapsack[cut:cls.number_of_items])
        chromosome = cls(copy.copy(new_knapsack))
        return chromosome

    def __init__(self, knapsack=None):
        if knapsack is None:
            weight = 0
            self.knapsack = [0] * self.number_of_items
            while True:
                i = random.randrange(0, self.number_of_items)
                if self.knapsack[i] == 0:
                    if weight + self.items[i][1] <= self.knapsack_capacity:
                        weight += self.items[i][1]
                        self.knapsack[i] = 1
                    else:
                        break
        else:
            self.knapsack = knapsack

    def get_fitness(self):
        value = 0
        weight = 0
        for i in range(self.number_of_items):
            if self.knapsack[i] == 1:
                value += self.items[i][0]
                weight += self.items[i][1]
                if weight > self.knapsack_capacity:
                    return 0
        return value

    def mutate(self, number_of_mutations):
        for i in random.sample(range(0, self.number_of_items), number_of_mutations):
            self.knapsack[i] = 1 - self.knapsack[i]
