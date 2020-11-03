import maya.cmds as cmds

cmds.polySphere(radius=2,
                subdivisionsX=12,
                subdivisionsY=12,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)

cmds.polySphere(radius=1.5,
                subdivisionsX=12,
                subdivisionsY=12,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)

cmds.move(0,2.6,0,
          objectSpace=True,
          worldSpaceDistance=True)

cmds.polySphere(radius=1,
                subdivisionsX=12,
                subdivisionsY=12,
                axis=[0,1,0],
                createUVs=2,
                constructionHistory=1)

cmds.move(0,4.6,0,
          objectSpace=True,
          worldSpaceDistance=True)

cmds.polyCone(radius=.3,
              height=1.3,
              subdivisionsX=12,
              subdivisionsY=12,
              subdivisionsZ=0,
              axis=[1,0,0],
              roundCap=False,
              createUVs=3,
              constructionHistory=1
              )

cmds.move(1.4,4.5,0,
          objectSpace=True,
          worldSpaceDistance=True)

cmds.polySphere(radius=.2,
                subdivisionsX=8,
                subdivisionsY=8,
                axis=[1,0,0],
                createUVs=2,
                constructionHistory=1
                )

cmds.move(0.8,4.7,0.4,
          objectSpace=True,
          worldSpaceDistance=True)

cmds.polySphere(radius=.2,
                subdivisionsX=8,
                subdivisionsY=8,
                axis=[1,0,0],
                createUVs=2,
                constructionHistory=1)

cmds.move(0.8,4.7,-0.4,
          objectSpace=True,
          worldSpaceDistance=True)
