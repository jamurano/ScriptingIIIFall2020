  import maya.cmds as cmds
import random

def randomGen(duplicateNum):

    #duplicateNum = 0
    for i in range(duplicateNum):
        cmds.polySphere(axis=[0, 0, 0],
                        createUVs=2,
                        object=True,
                        radius=1,
                        subdivisionsAxis=10,
                        subdivisionsHeight=10,
                        sy=10,
                        sx=10)
        transXValue = random.randrange(-10, 10)
        transYValue = random.randrange(0, 20)
        transZValue = random.randrange(-10, 10)
        cmds.xform( translation=[transXValue, transYValue, transZValue],
                    worldSpace=True)

                    cmds.select(objs)
                    cmds.xform(worldSpace=True, translation=[randomX, randomY, randomZ])
