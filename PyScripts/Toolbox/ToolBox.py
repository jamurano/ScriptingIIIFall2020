import maya.cmds as cmds

class ToolboxUI():
    def _init_(self):
        self.my_window = 'MyTools'

    def createWindow(self):
        self.my_window = cmds.window(title="MyTools",
                                      widthHeight=(300,200))
        self.colLayout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='Renamer UI', command=self.call_renamerUI())
        cmds.button(parent=self.colLayout, label='Snowman', command=self.call_snowman())
        cmds.button(parent=self.colLayout, label='Random Duplicate Obj',
                    command=self.call_randomDuplicateObj())
        cmds.button(parent=self.colLayout, label='Freeze Transforms', command=self.call_freezeTrans())
        cmds.button(parent=self.colLayout, label='Delete History', command=self.call_deleteHist())
        cmds.button(parent=self.colLayout, label='Group', command=self.call_group())
        cmds.button(parent=self.colLayout, label='Constrain', command=self.call_constrain())
        cmds.lbutton(parent=self.colLayout, label='Toggle', command=self.call_toggle())

        cmds.button(label='Close', command=('cmds.deleteUI(\"' + self.my_window + '\", window=True)'))

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

    def call_FreezeWindow(self):
        freezeUI = freeze.FreezeUI.createWindow()
        freezeUI()

    def call_DeleteHistoryWindow(self):
        deleteHistoryUI = deleteHistory.DeleteHistoryUI.createWindow()
        deleteHistoryUI()

    def call_ParentGroupWindow(self):
        parentGroupUI = parent.ParentGroupUI.createWindow()
        parentGroupUI()

    def call_ConstrainWindow(self):
        constrainUI = constrain.ConstrainUI.createWindow()
        constrainUI()

    def call_ToggleWindow(self):
        toggleUI = toggle.ToggleUI.createWindow()
        toggleUI()