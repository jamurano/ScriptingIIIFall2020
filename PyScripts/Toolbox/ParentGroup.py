import maya.cmds as cmds


class ParentGroupUI():
    def __init__(self):
        self.ParentGroupWindow = 'ParentGroup'

    def create(self):
        self.delete()

        self.ParentGroupWindow = cmds.window(title='Parent Group Window', widthHeight=(300, 300))
        self.colLayout = cmds.columnLayout(parent=self.ParentGroupWindow, adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='Group', command=self.ParentGroupWin())

        cmds.button(parent=self.colLayout, label='Close',
                    command=('cmds.deleteUI(\"' + self.ParentGroupWindow + '\", window=True)'))

        cmds.setParent('..')

        cmds.showWindow(self.ParentGroupWindow)

    def delete(self):
        if cmds.window(self.ParentGroupWindow, exists=True):
            cmds.deleteUI(self.ParentGroupWindow)

    def ParentGroupWin(self):
        self.sel = cmds.ls(selection=True)

        for self.s in self.sel:
            self.Grps = cmds.group(em=True)
            cmds.parent(self.s, self.Grps)