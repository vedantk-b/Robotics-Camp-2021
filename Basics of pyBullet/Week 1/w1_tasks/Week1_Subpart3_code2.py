import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
planeId = p.loadURDF("plane.urdf")
p.setGravity(0,0,-10)

for i in range(10000):
    a = 0
    b = 1
    print('Points on x-axis on which the drop falls are: ')
    for j in range(i):
        temp = a
        a = a + b
        b = temp
        print(a)
        dropStartPos = [a,0,5]
        dropStartOrientation = p.getQuaternionFromEuler([0,0,0])
        dropId = p.loadURDF("sphere.urdf",dropStartPos, dropStartOrientation)
    for j in range(240):
        p.stepSimulation()
        time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(dropId)
print(cubePos,cubeOrn)
p.disconnect()