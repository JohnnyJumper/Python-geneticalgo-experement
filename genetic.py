import random
import copy
import types


class Genetic:
	def __init__(self, options):
		self.population = options.initialPopulation #array of solutions, each solution is an object
		if (hasattr(options, 'goal')):
			self.goal = options.goal

		self.populationSize = len(self.population)
		self.calculateFitness = options.fitness #takes a singleSolution and calculates it's fitness score should be an int
		self.maxScore = 0
		self.solution = None

		self.alphaThreshold = options.alphaThreshold if hasattr(options, 'alphaThreshold') else 50	
		self.mutationRate = options.mutationRate if hasattr(options, 'mutationRate') else 0.1
		self.mutate = options.mutate if hasattr(options, 'mutate') else None	
		self.calculateInitialFitness()
		

	def calculateInitialFitness(self):
		for solution in self.population:
			solution.fitness = self.calculateFitness(solution)
			if solution.fitness > self.maxScore:
				self.maxScore = solution.fitness
				self.solution = copy.deepcopy(solution)
		# self.printPopulation()


	def printPopulation(self):
		for solution in self.population:
			print((solution.genes, solution.fitness))

	def getScore(self):
		return self.maxScore

	def evolve(self):
		
		for solution in self.population:
			solution.fitness = self.calculateFitness(solution)
			if solution.fitness > self.maxScore:
				self.maxScore = solution.fitness
				self.solution = solution
		self.population = self.repopulate()
		self.calculateInitialFitness()

	def getSolution(self):
		return self.solution


	def pickParent(self):
		for solution in self.population:
			dice = random.random()
			if solution.fitness / dice > self.alphaThreshold:
				return solution
		return None

	def split_genes(self, genes):
	    half = len(genes)//2
	    return genes[:half], genes[half:]


	def mixGenes(self, parentA, parentB):
		left, _ = self.split_genes(parentA.genes)
		_, right = self.split_genes(parentB.genes)
		return left + right


	def repopulate(self):
		nextGeneration = []
		child = types.SimpleNamespace()
		for _ in range(self.populationSize):
			parentA = None
			while (parentA == None):
				parentA = self.pickParent()
			parentB = None
			while (parentB == None):
				parentB = self.pickParent()
			child.genes = copy.deepcopy(self.mixGenes(parentA, parentB))
			if self.mutate:
				dice = random.random()
				if dice < self.mutationRate:
					child.genes = self.mutate(child.genes)
			nextGeneration.append(copy.deepcopy(child))
		return nextGeneration
