import maya.cmds as cmds

class ToolboxUI():
    def _init_(self):
        self.my_window = 'MyTools'

    def createWindow(self):
        self.my_window = cmds.window(title="MyTools",
                                      widthHeight=(300,200))
        self.colLayout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='Renamer UI', command=lambda *x: self.call_renamerUI())
        cmds.button(parent=self.colLayout, label='Snowman', command=lambda *x: self.call_snowman())
        cmds.button(parent=self.colLayout, label='Random Duplicate Obj', command=lambda *x: self.call_randomDuplicateObj())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def RenamerWindow(self):
        renamerWindowUI = renamer.RenamerUI.createWindow()
        renamerWindowUI()

    def SnowmanWindow(self):
        snowmanWindowUI = snowman.SnowmanUI.createWidow()
        snowmanWindowUI()

    def call_RanDupWindow(self):
        randomDupGenUI = randGen.RandomGeneratorUI.createWindow()
        randomDupGenUI()