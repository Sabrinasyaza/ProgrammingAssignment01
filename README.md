# ProgrammingAssignment01

# GENETIC ALGORITHM (GA)

Genetic Algorithm (GA) is a metaheuristic search method that has been used in Artificial Intelligence. Genetic Algorithm usually used to identify the optimize solutions of search problem. 

## PURPOSE

This purpose of this programming assignment is to analyze and design Genetic Algorithm program in order to finds the minimum value of the heuristic function. 

## HOW TO RUN THE PROGRAM 

We have used the Genetic Algorithm program in order find the optimize solutions for the programming assignment. First and foremost, we have initiate a random population for the chromosome. Next, for the fitness function, we used the minimum fitness function which is 1/(heuristic + a). The a value is refer to a random value that nearest to null. The objective of the fitness function is to evaluate the solution that represented by the chromosome. Furthermore, we have choose the Roulette Wheel Selection methods for the parent selection. We chose Roulette Wheel Selection method to select two individuals randomly in order to generate a new offspring for the next generation. In addition, for the crossover part, we used a single-point which is it will randomly select a point from two parents to generate a new offspring. For survivor selection, we used a generational replacement in order to generate n offsprings where n is the population size of the chromosome. 
Lasly, once reached the maximum generation, the looping will facing a stopping criteria. 
