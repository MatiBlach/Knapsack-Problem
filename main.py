from itertools import compress
import random
import time
import matplotlib.pyplot as plt

from data import *

def initial_population(individual_size, population_size):
    return [[random.choice([True, False]) for _ in range(individual_size)] for _ in range(population_size)]

def fitness(items, knapsack_max_capacity, individual):
    total_weight = sum(compress(items['Weight'], individual))
    if total_weight > knapsack_max_capacity:
        return 0
    return sum(compress(items['Value'], individual))

def population_best(items, knapsack_max_capacity, population):
    best_individual = None
    best_individual_fitness = -1
    for individual in population:
        individual_fitness = fitness(items, knapsack_max_capacity, individual)
        if individual_fitness > best_individual_fitness:
            best_individual = individual
            best_individual_fitness = individual_fitness
    return best_individual, best_individual_fitness


items, knapsack_max_capacity = get_big()
print(items)

population_size = 100
generations = 200
n_selection = 20
n_elite = 2

mutation_rate = 0.9

start_time = time.time()
best_solution = None
best_fitness = 0
population_history = []
best_history = []
population = initial_population(len(items), population_size)
for _ in range(generations):
    population_history.append(population)

    # TODO: implement genetic algorithm
    
    # evaluation
    best_individual, best_individual_fitness = population_best(items, knapsack_max_capacity, population)
    if best_individual_fitness > best_fitness:
        best_solution = best_individual
        best_fitness = best_individual_fitness
    best_history.append(best_fitness)

    # selection
    total_fitness = sum(fitness(items, knapsack_max_capacity, individual) for individual in population)
    selection_probabilities = [fitness(items, knapsack_max_capacity, individual) / total_fitness for individual in population]
    total_probability = sum(selection_probabilities)
    #selection_probabilities = [prob / total_probability for prob in selection_probabilities]    
    selected_indexes = random.choices(range(population_size),k=n_selection,weights=selection_probabilities)
    selected_population = [population[i] for i in selected_indexes]
    
    # crossover
    new_population = []
    while len(new_population) < population_size:
        parent1, parent2 = random.sample(selected_population, 2)
        crossover_point = random.randint(1,len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        new_population.extend([child1, child2])

    
    # mutation
    for i in range(len(new_population)):
        if random.random() < mutation_rate:
            mutation_point = random.randint(0, len(new_population[i]) - 1)
            new_population[i][mutation_point] = not new_population[i][mutation_point]
            
    # replacement
    population.sort(key=lambda individual: fitness(items, knapsack_max_capacity, individual), reverse=True)
    new_population.sort(key=lambda individual: fitness(items, knapsack_max_capacity, individual), reverse=True)
    elite = population[:n_elite]
    population = elite + new_population[:population_size - n_elite]
    
end_time = time.time()
total_time = end_time - start_time
print('Best solution:', list(compress(items['Name'], best_solution)))
print('Best solution value:', best_fitness)
print('Time: ', total_time)

# plot generations
x = []
y = []
top_best = 10
for i, population in enumerate(population_history):
    plotted_individuals = min(len(population), top_best)
    x.extend([i] * plotted_individuals)
    population_fitnesses = [fitness(items, knapsack_max_capacity, individual) for individual in population]
    population_fitnesses.sort(reverse=True)
    y.extend(population_fitnesses[:plotted_individuals])
plt.scatter(x, y, marker='.')
plt.plot(best_history, 'r')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.show()
