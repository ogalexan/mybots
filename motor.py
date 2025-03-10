import pybullet_data
import pyrosim.pyrosim as pyrosim 
import numpy
import constants as c
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName 
    
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
                
        self.frequency = c.BackLegFrequency
        self.offset = c.BackLegPhaseOffset
        self.amplitude = c.BackLegAmplitude
        
        if self.jointName == b"Torso_BackLeg":
            freq = self.frequency / 2.0
        else:
            freq = self.frequency


        self.motorValues = numpy.zeros(c.iterations)
        for i in range(c.iterations):
            self.motorValues[i] = self.amplitude * numpy.sin(freq * (2 * numpy.pi * i / (c.iterations - 1)) + self.offset)

        #self.motorValues = [self.amplitude * numpy.sin(self.frequency * j + self.offset) for j in c.targetAngles]


    def Set_Value(self, robot, desiredAngle):

        pyrosim.Set_Motor_For_Joint(
                bodyIndex = robot.robotId,
                jointName = self.jointName,
                controlMode = p.POSITION_CONTROL,
                targetPosition = desiredAngle,
                maxForce = c.maxForce)


    def Save_Values(self):
        numpy.save("motor_" + self.jointName + ".npy", self.motorValues)



