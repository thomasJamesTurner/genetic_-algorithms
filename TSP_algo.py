import random
from graphs.graph import Graph
from genetic_alogrithms.permutation_genetic_algo import Individual

global tsp_graph
def fitness_func(current_individual):
    total_weight = 0
    for i in range(len(current_individual.chromosome) - 1):
        src = current_individual.chromosome[i]
        dest = current_individual.chromosome[i + 1]
        # Find the edge in the adjacency list
        for neighbor, weight in tsp_graph.adj_list.get(src, []):
            if neighbor == dest:
                total_weight += weight
                break
        else:
            # Edge doesn't exist
            weight += 1000000
    return total_weight

def get_pop_fitness_cutoff(population,average_fitness):
    for i in range(len(population)):
        if(population[i].fitness > average_fitness):
            return i

def main():
    global tsp_graph
    tsp_graph = Graph.create_random_graph(6,12)
    generation = 1
    found = False
    population = []
    Individual.gene_pool = tsp_graph.get_nodes()
    Individual.set_chromosome_length_limits(6,12)



    for _ in range(100):
        population.append(Individual(fitness_func=fitness_func))

    while(not found):
        population = sorted(population, key = lambda x:x.fitness,reverse=True) 
        if generation > 2000:
            break

        average_fitness = sum([i.fitness for i in population]) / len(population)
        new_generation = []
        cut_off = get_pop_fitness_cutoff(population,average_fitness)
        new_generation.extend(population[:cut_off])

        for _ in range(len(population) - len(new_generation)):
            if(cut_off == 0):
                cut_off = int(len(population)*0.1)
            parent1 = random.choice(population[:cut_off]) 
            parent2 = random.choice(population[:cut_off]) 
            child = Individual.mate(parent1,parent2) 
            new_generation.append(child) 
        population = new_generation 

        print("Generation: {}\tString: {}\tFitness: {} Average Fitness: {}". 
                format(generation, 
                       "".join(population[0].chromosome), 
                       population[0].fitness,
                       average_fitness))

    
        generation += 1
    print("Generation: {}\tString: {}\tFitness: {} Average Fitness: {}". 
              format(generation, 
                     "".join(population[0].chromosome), 
                     population[0].fitness ,
                     average_fitness))

if __name__ == "__main__":
    main()