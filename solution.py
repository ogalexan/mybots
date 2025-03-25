import os
import numpy
import pyrosim.pyrosim as pyrosim
import random
import time 

class SOLUTION:
    def __init__(self, nextAvailableID):
        
        self.weights = numpy.random.rand(3,2)
        self.weights = self.weights * 2 - 1
        self.myID = nextAvailableID
    """
    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system('python3 simulate.py '+ str(directOrGUI) + " " + str(self.myID) + " &") 
        fitnessFileName = f"fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.01)
        
        fitnessFile = open(f"fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(fitnessFile.read())
        print(self.fitness)
        fitnessFile.close()
    """

    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()

        os.system('python3 simulate.py '+ str(directOrGUI) + " " + str(self.myID) + " 2&>1 &")

    def Wait_For_Simulation_To_End(self):
        fitnessFileName = f"fitness" + str(self.myID) + ".txt"
        while not os.path.exists(fitnessFileName):
            time.sleep(0.1)
        
        while os.stat(fitnessFileName).st_size == 0:
            time.sleep(0.1)

        with open (fitnessFileName, "r") as f:
            fitness_str = f.read().strip()
            self.fitness = float(fitness_str)
        f.close()
        os.system(f"rm fitness" + str(self.myID) + ".txt")

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")

        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 1

        pyrosim.Send_Cube(name="Box", pos=[x,3,z], size=[length,width,height])
        pyrosim.End()


    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        length = 1
        width = 1
        height = 1
        x = 0
        y = 0
        z = 0

        pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_BackLeg",parent="Torso", child="BackLeg", type = "revolute", position = [1.0,0,1.0])
        pyrosim.Send_Cube(name="BackLeg", pos=[-0.5,0,-0.5], size=[length,width,height])
        pyrosim.Send_Cube(name="FrontLeg", pos=[0.5,0,-0.5], size=[length,width,height])
        pyrosim.Send_Joint(name = "Torso_FrontLeg",parent="Torso", child="FrontLeg", type = "revolute", position = [2.0,0,1.0])

        pyrosim.End()


    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1, linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2, linkName = "FrontLeg")

        pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_BackLeg")
        pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_FrontLeg")

        sensorNeurons = {"Torso" : 0, "BackLeg" : 1, "FrontLeg" : 2}
        motorNeurons = {"Torso_BackLeg" : 0, "Torso_FrontLeg" : 1}

        for currentRow in sensorNeurons.values():
            for currentColumn in motorNeurons.values():
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn+3, weight = self.weights[currentRow][currentColumn])


        pyrosim.End()


    def Mutate(self):
        randomRow = random.randint(0,2)
        randomColumn = random.randint(0,1)
        self.weights[randomRow, randomColumn] = random.random()*2 - 1




