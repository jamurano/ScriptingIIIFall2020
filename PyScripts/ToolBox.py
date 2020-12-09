import maya.cmds as cmds

class Toolbox_UI():
    def _init_(self):
        self.my_window = 'mytools_ui'

    def create(self):
        self.my_window = cmdes.window(self.my_window,
                                      title='toolbox',
                                      widthHeight=(300,300))
        self.col_layout = cmds.columnLayout(parent=self.my_window,
                                            adjustableColumn=True)

        cmds.button(parent=self.col_layout, label='Renamer UI', c=lambda *x: self.call_renamerUI())
        cmds.button(parent=self.col_layout, label='Snowman', c=lambda *x: self.call_snowman())
        cmds.button(parent=self.col_layout, label='Random Duplicate Obj', c=lambda *x: self.call_randomDuplicateObj())

        cmds.showWindow(self.my_window)

    def delete(self):
        if cmds.window(self.my_window, exists=True):
            cmds.deleteUI(self.my_window)

    def call_renamerUI(self):
        import renamer
        reload(renamer)
        renamerUI_instance = renamer.RenamerUI()
        renamerUI_instance.create()

    def call_snowman(self):
        import tools
        reload(tools)

        tools.create_snowman()

    def call_randomDuplicateObj(self):
        import tools
        reload(tools)

        tools.create_randomDuplicateObj()