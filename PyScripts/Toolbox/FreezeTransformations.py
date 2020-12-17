import maya.cmds as cmds

class FreezeTransform():
    def __init__(self):
        self.FreezeTransWindow = 'freezeWindow'

    def createWindow(self):

        self.delete()

        self.FreezeTransWindow = cmds.window(title = 'Freeze Window', widthHeight=(300,300))
        self.colLayout = cmds.columnLayout(parent=self.FreezeTransWindow, adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='FreezeTransform', command=self.FreezeTrans())

        cmds.button(parent=self.colLayout, label='Close Window',
                    command=('cmds.deleteUI(\"' + self.FreezeTransWindow + '\", window=True)'))

        cmds.setParent("..")

        cmds.showWindow(self.FreezeTransWindow)

    def delete(self):
        if cmds.window(self.FreezeTransWindow, exists=True):
            cmds.deleteUI(self.FreezeTransWindow)

    def FreezeTrans(self):
        self.sel = cmds.ls(selection=True)
        cmds.makeIdentity(self.sel, apply=True, t=1, r=1, s=1, n=0, pn=1)