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
        iterations = 1000;
        for i in range(iterations):
            print(i)
            
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)


            '''
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
            
            '''
            time.sleep(1)


    def __del__(self):
        p.disconnect()




