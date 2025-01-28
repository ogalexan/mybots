import pyrosim.pyrosim as pyrosim
pyrosim.Start_SDF("boxes.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0
# pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x,y,z], size=[length,width,height])


for i in range(-1,2):
    #pyrosim.Send_Cube(name="Box", pos=[i,y,z], size=[length,width,height])
    for j in range(-1,2):
        for k in range(0,3):
            pyrosim.Send_Cube(name="Box", pos=[i,j,k], size=[0.9 **k,0.9 **k,0.9 **k])


#for k in range(1,4):
    #        pyrosim.Send_Cube(name="Box", pos=[i,j,k], size=[length * (1 - 0.9 **(j-1)),width * (1 - 0.9 **(j-1)),height * (1 - 0.9 **(j-1))])

#boxname = "Box" + str(i+j)
        

pyrosim.End()
