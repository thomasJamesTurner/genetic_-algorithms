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
    def swap_mutation(chromosome):
        if len(chromosome) < 2:
            return chromosome
            
        idx1, idx2 = random.sample(range(len(chromosome)), 2)
        chromosome[idx1], chromosome[idx2] = chromosome[idx2], chromosome[idx1]
        return chromosome
    @staticmethod
    def ordered_crossover(parent1, parent2):
        """
        werserves orders of genes and ensures 
        each element in the gene_pool appears once
        """
        size = len(Individual.gene_pool)
        
        start, end = sorted(random.sample(range(size), 2))
        child = [None] * size
        for i in range(start, end + 1):
            child[i] = parent1.chromosome[i]
        parent2_idx = 0
        child_idx = 0
        
        while child_idx < size:
            if child_idx >= start and child_idx <= end:
                child_idx = end + 1
                continue
                
            while parent2.chromosome[parent2_idx] in child:
                parent2_idx = (parent2_idx + 1) % size
                
            child[child_idx] = parent2.chromosome[parent2_idx]
            child_idx += 1
            parent2_idx = (parent2_idx + 1) % size
            
        return child
    @staticmethod
    def set_chromosome_length_limits(min_length=1, max_length=100):
        Individual.min_chromosome_length = min_length
        Individual.max_chromosome_length = max_length

    @staticmethod
    def mate(parent_1, parent_2):
        child_chromosome = Individual.ordered_crossover(parent_1, parent_2)
        if random.random() < Individual.mutation_chance:
            child_chromosome = Individual.swap_mutation(child_chromosome)
            
        return Individual(fitness_func=Individual.fitness_func, chromosome=child_chromosome)
    
    @staticmethod
    def create_gnome():
        chromosome = Individual.gene_pool.copy()
        random.shuffle(chromosome)
        return chromosome
