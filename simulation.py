import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim 

from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        
        self.physicsClient = p.connect(p.GUI)
        
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        self.world = WORLD()
        self.robot = ROBOT()

        p.setGravity(0,0,-9.8)

        #pyrosim.Prepare_To_Simulate(self.robot.robotId)


    def Run(self):
        iterations = 10;
        for i in range(iterations):
            print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)

            time.sleep(1)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()




