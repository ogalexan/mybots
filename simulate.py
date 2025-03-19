import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim 
import numpy
import random 
import constants as c
import sys 

from simulation import SIMULATION

directOrGUI = sys.argv[1]

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()


'''
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
iterations = c.iterations
backLegSensorValues = c.backLegSensorValues
frontLegSensorValues = c.frontLegSensorValues
angles = c.angles
targetAngles = c.targetAngles

#numpy.save('data/targetAngles.npy', targetAngles)
#exit()

BLamplitude = c.BackLegAmplitude
BLfrequency = c.BackLegFrequency
BLphaseOffset = c.BackLegPhaseOffset
BLmotorVectors = c.BackLegMotorVectors

FLamplitude = c.FrontLegAmplitude
FLfrequency = c.FrontLegFrequency
FLphaseOffset = c.FrontLegPhaseOffset
FLmotorVectors = c.FrontLegMotorVectors

#numpy.save('data/targetAngles.npy', motorVectors)
#exit()


for i in range(iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    print(i)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b'Torso_BackLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = BLmotorVectors[i],
            maxForce = c.maxForce)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = FLmotorVectors[i],
            maxForce = c.maxForce)


    time.sleep(1)
p.disconnect()
print(backLegSensorValues)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
'''



