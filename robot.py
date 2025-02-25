import pybullet as p
import pyrosim.pyrosim as pyrosim

from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.motors = {}

        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()


    def Prepare_To_Sense(self):
        self.sensors = {}

        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self):
        self.sensors = sensor.Get_Value()
        
        for i in self.sensors:
            self.values = sensor.Get_Value(i)

