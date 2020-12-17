import maya.cmds as cmds


class ParentScaleCon():
    def __init__(self):
        self.ConstrainWindow = 'ConstrainWindow'

    def createWindow(self):
        self.delete()

        self.ConstrainWindow = cmds.window(title='Constrain Window', widthHeight=(300, 300))
        self.colLayout = cmds.columnLayout(parent=self.ConstrainWindow, adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='Parent Scale Constrain', command=self.ConstrainWin())

        cmds.button(parent=self.colLayout, label='Close',
                    command=('cmds.deleteUI(\"' + self.ConstrainWindow + '\", window=True)'))

        cmds.setParent('..')

        cmds.showWindow(self.ConstrainWindow)

    def delete(self):
        if cmds.window(self.ConstrainWindow, exists=True):
            cmds.deleteUI(self.ConstrainWindow)

    def ConstrainWin(self):
        sel = cmds.ls(sl=True)

        if len(sel) % 2 == 1:
            cmds.error('Select even number of objects')

            selNum = len(sel)

        for i in range(0, selNum, 2):
            cmds.parentConstraint(sel[i+1], sel[i], maintainOffset=True)
            cmds.scaleConstraint(sel[i+1], sel[i], maintainOffset=True)