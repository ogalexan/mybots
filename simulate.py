import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim 
import numpy
import random 

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8)
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
iterations = 1000
backLegSensorValues = numpy.zeros(iterations)
frontLegSensorValues = numpy.zeros(iterations)
angles = [i * (2* numpy.pi) / (iterations - 1) for i in range(iterations)]
targetAngles = numpy.sin(numpy.array(angles))
targetAngles = targetAngles * (numpy.pi / 4)

#numpy.save('data/targetAngles.npy', targetAngles)
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
            targetPosition = targetAngles[i],
            maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = b'Torso_FrontLeg',
            controlMode = p.POSITION_CONTROL,
            targetPosition = targetAngles[i],
            maxForce = 500)


    time.sleep(1)
p.disconnect()
print(backLegSensorValues)
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)



