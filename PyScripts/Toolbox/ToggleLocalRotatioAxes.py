import maya.cmds as cmds


class ToggleLocalAxes():
    def __init__(self):
        self.ToggleAxesWindow = 'ToggleAxesWindow'

    def createWindow(self):

        self.delete()

        self.ToggleAxesWindow = cmds.window(title='Toggle Axes Window Settings', widthHeight=(500, 500))
        self.colLayout = cmds.columnLayout(parent=self.ToggleAxesWindow, adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='toggle', command=self.ToggleAxes())

        cmds.button(parent=self.colLayout, label='Close',
                    command=('cmds.deleteUI(\"' + self.ToggleAxesWindow + '\", window=True)'))

        cmds.setParent('..')

        cmds.showWindow(self.ToggleAxesWindow)

        def delete(self):
            if cmds.window(self.ToggleAxesWindow, exists=True):
                cmds.deleteUI(self.ToggleAxesWindow)

    def ToggleAxes(self):
        sels = cmds.ls(selection=True)
        selsNum = len(sels)

        for i in range(selsNum):
            cmds.toggle(sels[i], localAxis=True)
            cmds.setAttr(sels [i] + '.displayLocalAxis', cb=True)
            cmds.setAttr(sels[i] + '.jointOrientX', cb=True)
            cmds.setAttr(sels[i] + '.jointOrientY', cb=True)
            cmds.setAttr(sels[i] + '.jointOrientZ', cb=True)