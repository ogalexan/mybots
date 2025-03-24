from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
    def __init__(self):
        os.system(f"rm brain*.nndf")
        os.system(f"rm fitness*.txt")

        self.parents = {}
        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1

    def Evolve(self):

        self.Evaluate(self.parents)
        '''
        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")

        for i in self.parents:
            self.parents[i].Wait_For_Simulation_To_End()
        '''
        
        #Evaluate("GUI")
        

        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()
            

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

    def Spawn(self):
        self.children = {}
        for i in self.parents:
            child = copy.deepcopy(self.parents[i])
            child.myID = self.nextAvailableID
            self.children[i] = child
            self.nextAvailableID += 1
    
    def Mutate(self):
        for i in self.children:
            self.children[i].Mutate()

    def Select(self):
        for i in self.parents:
            if self.children[i].fitness < self.parents[i].fitness:
                print(self.parents[i].myID)
                print(self.children[i].myID)
                self.parents[i] = self.children[i]
                print(self.parents[i].myID)

    def Print(self):
        print(" ")
        for i in self.parents:
            print("Parent: "+ str(i) + " :" + str(self.parents[i].fitness) + " Child: " + str(i) + " :" + str(self.children[i].fitness))
        print(" ")

    def Show_Best(self):        
        bestKey = min(self.parents, key = lambda i: self.parents[i].fitness)
        self.parents[bestKey].Start_Simulation("GUI")

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()

