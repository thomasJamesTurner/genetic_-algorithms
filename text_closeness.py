import random
from genetic_alogrithms.basic_genetic_algo import Individual


def fitness_func(current_individual):
    total_fitness = len(Individual.target)
    for gs, gt in zip(current_individual.chromosome, Individual.target):
        if gs != gt:
            total_fitness -=1
    return total_fitness

def get_pop_fitness_cutoff(population,average_fitness):
    for i in range(len(population)):
        if(population[i].fitness > average_fitness):
            return i

def main():
    generation = 1
    found = False
    population = []
    Individual.gene_pool = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890, .-;:_!'"#%&/()=?@${[]}\n\r\t\v'''
    Individual.target = '''With a taste of your lips, I'm on a ride You're toxic, I'm slippin' under'''



    for _ in range(100):
        population.append(Individual(fitness_func=fitness_func))

    while(not found):
        population = sorted(population, key = lambda x:x.fitness,reverse=True) 
        if population[0].fitness == len(Individual.target):
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
                     (population[0].fitness / len(Individual.target)) * 100,
                     (average_fitness / len(Individual.target))*100)) 
    
        generation += 1
    print("Generation: {}\tString: {}\tFitness: {} Average Fitness: {}". 
          format(generation, 
                 "".join(population[0].chromosome), 
                 (population[0].fitness / len(Individual.target)) * 100,
                 (average_fitness / len(Individual.target))*100)) 

if __name__ == "__main__":
    main()