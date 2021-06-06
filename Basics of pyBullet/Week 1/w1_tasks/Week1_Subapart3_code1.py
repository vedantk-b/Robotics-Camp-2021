import pybullet as p
import numpy as np
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
r2d2StartPos = [2,2,1]
r2d2StartOrientation = p.getQuaternionFromEuler([0,0,0])
dabba_start_positioon = [0,0,1]
r2d2Id = p.loadURDF("r2d2.urdf",r2d2StartPos, r2d2StartOrientation)
dabbaId = p.loadURDF("dabba.urdf", dabba_start_positioon, r2d2StartOrientation)
for i in np.arange (0,10000,0.1):
    if (i%10<9.9/np.sqrt(2)):
        p.setGravity(np.round(i%10, 2),np.round(i%10,2),0)
        print("Gravity = {} ".format((np.round(i%10,2),np.round(i%10,2),0)))
    p.stepSimulation()
    time.sleep(1./240.)

cubePos, cubeOrn = p.getBasePositionAndOrientation(r2d2Id)
print(cubePos,cubeOrn)
p.disconnect()