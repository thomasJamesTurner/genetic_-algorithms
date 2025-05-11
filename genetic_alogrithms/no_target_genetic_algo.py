import random

class Individual:

    mutation_chance = 0.05
    gene_pool = []
    fitness_func = None
    def __init__(self,fitness_func, chromosome = None):
        Individual.fitness_func = fitness_func
        if(chromosome != None):
            self.chromosome = chromosome
        else:
            self.chromosome = Individual.create_gnome()
        self.fitness = self.calc_fitness()
    def calc_fitness(self):
        return Individual.fitness_func(self)

    @staticmethod
    def set_gene_pool(genes):
        Individual.gene_pool = genes

    @staticmethod
    def mutate():
        i = random.randint(0,len(Individual.gene_pool)-1)
        return Individual.gene_pool[i]
    @staticmethod
    def set_chromosome_length_limits(min_length=1, max_length=100):
        Individual.min_chromosome_length = min_length
        Individual.max_chromosome_length = max_length

    @staticmethod
    def mate(parent_1, parent_2):
        child_chromosome = [] 
        for gnome_1, gnome_2 in zip(parent_1.chromosome, parent_2.chromosome):     
            prob = random.random() 
            if prob < (1-Individual.mutation_chance)/2: 
                child_chromosome.append(gnome_1) 

            elif prob < 1-Individual.mutation_chance: 
                child_chromosome.append(gnome_2) 
            else: 
                child_chromosome.append(Individual.mutate())

            # Only add a gene if we're below the maximum length
            if prob < 0.02 and len(child_chromosome) < Individual.max_chromosome_length:
                child_chromosome.append(Individual.mutate())
                
            # Only remove a gene if we're above the minimum length
            if prob > 0.98 and len(child_chromosome) > Individual.min_chromosome_length:
                child_chromosome.pop()

        return Individual(fitness_func=Individual.fitness_func,chromosome=child_chromosome) 
    @staticmethod
    def create_gnome():
        return [Individual.mutate() for _ in range(len(Individual.gene_pool))]
