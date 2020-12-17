import maya.cmds as cmds

class DeleteHistory():
    def __init__(self):
        self.DeleteHistoryWindow = 'DeleteHistory'

    def createWindow(self):
        self.delete()

        self.DeleteHistoryWindow = cmds.window(title = 'Delete History', widthHeight=(300,300))
        self.colLayout = cmds.columnLayout(parent=self.DeleteHistoryWindow, adjustableColumn=True)

        cmds.button(parent=self.colLayout, label='Delete', command=self.deleteHistory())

        cmds.button(parent=self.colLayout, label="Close Window",
                    command=('cmds.deleteUI(\"' + self.DeleteHistoryWindow + '\", window=True)'))

        cmds.setParent('..')

        cmds.showWindow(self.DeleteHistoryWindow)

    def delete(self):
        if cmds.window(self.DeleteHistoryWindow, exists=True):
            cmds.deleteUI(self.DeleteHistoryWindow)

    def DeleteHistory(self):
        self.sel = cmds.ls(selection=True)
        cmds.constructionHistory(query=True, toggle=True)
        cmds.delete(ch=True)