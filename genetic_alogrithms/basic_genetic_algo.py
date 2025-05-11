import random



class Individual:
    mutation_chance = 0.05
    target = None
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

        return Individual(fitness_func=Individual.fitness_func,chromosome=child_chromosome) 
    @staticmethod
    def create_gnome():
        return [Individual.mutate() for _ in range(len(Individual.target))]