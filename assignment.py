import random
import math
import matplotlib.pyplot as plt 

dmin_x = -5
dmax_x = 5
dmin_y = -5 
dmax_y = 5

class Chromosome:                     
    def __init__(self, binary = None):
        if binary == None:
            self.binary = random.choices([0, 1], k=10)
        else:
            self.binary = binary
        self.x = self.Representation(dmin_x, dmax_x, self.binary[:5])
        self.y = self.Representation(dmin_y, dmax_y, self.binary[5:])
    
    def __repr__(self):        
        return '{} (x : {}, y : {}) Heuristic: {}'.format(self.binary, self.x, self.y, heuristic(self.x, self.y))

    def Representation(self, dmax, dmin, g):        
        br = [2**-i for i in range(1, len(g) + 1)]
        return dmin + ((dmax - dmin) / sum(br) * sum([g[i] * br[i] for i in range(len(g))]))  

def heuristic(x, y):
    return (((math.cos(x) + math.sin(y))*(math.cos(x) + math.sin(y)))/((x*x) + (y*y)))

def fitness(x, y): #minimum fitness function
    a = 0.00000000000000001
    return 1 / (heuristic (x,y) + a)
    
def exist(s, ch):        
    check = False       
    for i in s:
        if i.binary == ch.binary:
            check = True
    return check

def Parent_selection(k): 
    parents = []
    fitnesses = list(map(lambda p: fitness(p.x, p.y), population))
    weight = [fitnesses[i] / sum(fitnesses) 
                  for i in range(len(population))]

    while len(parents) != k:
        select = random.choices(population, weights=weight)[0]
        if not exist(parents, select):
            parents.append(select)
    return parents

def Crossover(prnt1, prnt2):
    position = random.randint(1, len(prnt1.binary) - 2)

    child1 = prnt1.binary[:position] + prnt2.binary[position:]
    child2 = prnt2.binary[:position] + prnt1.binary[position:]

    prob = random.uniform(0, 100)
    if prob < 0.5:
        mutated = random.randint(0, len(child1) - 1)
        if  child1[mutated] == 1:
            child1[mutated] 
        else:
            child1[mutated] = 1

    prob = random.uniform(0, 100)
    if prob < 0.5:
        mutated = random.randint(0, len(child2) - 1)
        if  child2[mutated] == 1:
            child2[mutated] 
        else:
            child2[mutated] = 1
    
    population.append(Chromosome(child1))
    population.append(Chromosome(child2))

def survivor_selection():
    population.sort(key=lambda p: heuristic(p.x, p.y), reverse=True)

    while len(population) != 40:
        population.pop()

population = []
chromosome = []
generation = 1

while len(population) != 40:
    ch = Chromosome()

    if not exist(population, ch):
        population.append(ch)

survivor_selection()
print('Generation', generation)
print('The Best Chromosome', population[0])

arr_fitness = [0]*130
arr_fitness[generation-1] = fitness(population[0].x, population[0].y)

while generation < 130:
    parent = Parent_selection(2)
    Crossover(parent[0], parent[1])
    survivor_selection()

    generation += 1
    arr_fitness[generation-1] = fitness(population[0].x, population[0].y)
    print('Generation', generation)
    print('The Best Chromosome', population[0])

plt.plot(range(1, generation + 1), arr_fitness)
plt.title("Graph of Fitness Performance")
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.show()