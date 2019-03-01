import genetic
import random
import types
import copy

# random.seed(datetime.datetime.now())

def getRandomGenes(size):
	letters = 'abcdefghi  jklmn opqrstuvwxyz '	
	genes = random.sample(letters, size)
	return genes

def generateInitialPopulation(size):
	population = []
	solution = types.SimpleNamespace()
	for _ in range(900):
		solution.genes = getRandomGenes(size)
		solution.fitness = 0
		population.append(copy.deepcopy(solution))
	return population

def calcFitness(solution):
	goal = 'to be or not to be'
	correct = 0
	for i in range(len(goal)):
		if goal[i] == solution.genes[i]:
			correct += 1
	return correct / len(goal)
		 

def mutate(genes):
	letters = 'abc defghijklmn opqrstuvwxyz'	
	gen = random.sample(letters, len(genes))
	return gen	

def main():
	goal = 'to be or not to be'

	options = types.SimpleNamespace()
	options.initialPopulation =  generateInitialPopulation(len(goal))
	options.fitness = calcFitness
	options.mutate = mutate
	options.mutationRate = 0.7
	options.alphaThreshold = 0.01
	gen = genetic.Genetic(options)
	while(gen.getScore() < 0.8):
		gen.evolve()
		print('score = ', gen.getScore())
		print('solution = ', gen.getSolution())
		print('-----------')


main()