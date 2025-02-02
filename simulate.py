import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.setGravity(0,0,-9.8,physicsClient)
p.loadSDF("world.sdf")
for i in range(1000):
    p.stepSimulation()
    print(i)
    time.sleep(1)
p.disconnect()
