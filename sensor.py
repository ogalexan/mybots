import pybullet as p
import pybullet_data
import numpy
import pyrosim.pyrsosim as pyrosim 

import constants as c

class SENSOR:
    def __init__(self):
        self.linkName = linkName
        self.values = numpy.zeros(c.iterations)
        

    def Get_Value():
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

