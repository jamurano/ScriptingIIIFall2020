import maya.cmds as cmds


def SequentialRenamer(stringName):
    sel = cmds.ls(selection=True)
    selectedObjs = 1

    for obj in sel:
        selection_input = stringName.count("#")
        string_parts = stringName.partition("#" * selection_input)
        sequential_numbering = str(selectedObjs)

        if string_parts[1]:
            sequential_numbering = sequential_numbering.zfill(3)
            cmds.rename(string_parts[0] + sequential_numbering + string_parts[2])

        selectedObjs += 1


SequentialRenamer("Sphere_###_Obj")
