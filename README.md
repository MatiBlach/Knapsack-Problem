# Genetic Algorithm for Solving the Knapsack Problem

## Overview
This project implements a **Genetic Algorithm** to solve the **0/1 Knapsack Problem**. The goal is to maximize the value of items selected to be placed in a knapsack without exceeding a given weight capacity.

The algorithm follows these steps:
1. **Initial Population**: A random population of individuals is generated, where each individual represents a set of items to be included in the knapsack (True for selected, False for not selected).
2. **Fitness Function**: The fitness of an individual is calculated based on the total value of selected items, penalized if the total weight exceeds the knapsack capacity.
3. **Selection**: Individuals are selected for reproduction based on their fitness using a **weighted random selection** process.
4. **Crossover**: Selected pairs of individuals cross over to produce new offspring by combining parts of their chromosomes (genetic material).
5. **Mutation**: With a certain probability, mutations are applied to offspring by flipping the selection of an item.
6. **Replacement**: The best individuals (elite) from the current population are retained, and the remaining population is replaced by the offspring.

## Parameters
- **Population Size**: 100
- **Generations**: 200
- **Selection Size**: 20
- **Elite Size**: 2
- **Mutation Rate**: 0.9

## Outputs
- **Best Solution**: The list of item names in the optimal solution that provides the highest value without exceeding the knapsack capacity.
- **Best Solution Value**: The total value of the best solution.
- **Execution Time**: The time it took to run the genetic algorithm.
- **Fitness Evolution Plot**: A plot showing how the fitness of the population evolves over generations.

## Example Usage
```python
from data import get_big

# Load items and knapsack capacity
items, knapsack_max_capacity = get_big()

# Run the genetic algorithm
best_solution, best_fitness, total_time = genetic_algorithm(items, knapsack_max_capacity)
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
print("Execution Time:", total_time)
