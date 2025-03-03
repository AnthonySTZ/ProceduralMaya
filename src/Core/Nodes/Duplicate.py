from .BaseNode import BaseNode
from Core.Field.Float3 import Float3
from Core.Field.UnsignedInt import UnsignedInt
from Core.Field.Types import Types

try:
    import maya.cmds as mc  # type: ignore
    import maya.mel as mel  # type: ignore
except:
    pass


class Duplicate(BaseNode):

    ScaRotTsl = 0
    ScaTslRot = 1
    RotScaTsl = 2
    RotTslSca = 3
    TslScaRot = 4
    TslRotSca = 5

    def __init__(self):
        super().__init__()
        self._name = "duplicate"
        self._icon = "duplicate_icon.png"
        self._num_inputs = 1
        self._num_outputs = 1
        self._parameters = {
            "Amount": UnsignedInt(0),
            "Transform Order": Types(
                "Scale Rot Trans",
                {
                    "Scale Rot Trans": self.ScaRotTsl,
                    "Scale Trans Rot": self.ScaTslRot,
                    "Rot Scale Trans": self.RotScaTsl,
                    "Rot Trans Scale": self.RotTslSca,
                    "Trans Scale Rot": self.TslScaRot,
                    "Trans Rot Scale": self.TslRotSca,
                },
            ),
            "Translate": Float3(0.0, 0.0, 0.0),
            "Rotate": Float3(0.0, 0.0, 0.0),
            "Scale": Float3(1.0, 1.0, 1.0),
        }

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) is None:
            print("No connection !")
            return

        current_xform = self.input(0).commandAtIndex(0)

        shapes = mc.listRelatives(current_xform, shapes=True)
        order = self._parameters["Transform Order"].getValue()

        amount = self._parameters["Amount"].value
        duplicated_list = []
        last_dup = shapes
        for _ in range(amount):
            duplicated = mel.eval("duplicate -rc -rr " + " ".join(last_dup) + ";")
            mel.eval("select -r " + " ".join(duplicated) + ";")
            self.transformBaseOnOrder(order)
            duplicated_list.append(duplicated[0])
            print("ListRelatives...")
            print(duplicated_list)
            last_dup = mc.listRelatives(duplicated[0], shapes=True)

        if amount > 0:
            merge_command = self.createMergeCommand(current_xform, duplicated_list)
            merged_xform = mel.eval(merge_command)
            mel.eval("DeleteHistory;")
            for dup in duplicated_list:
                if mc.objExists(dup):
                    mel.eval("delete " + dup + ";")
            current_xform = [merged_xform[0]]

        return current_xform

    def createMergeCommand(self, xform_1, xform_2):
        command = "polyUnite " + " ".join(xform_1) + " " + " ".join(xform_2) + ";"
        return command

    def transformBaseOnOrder(self, order):
        translate_command = self.createTranslateCommand()
        rotate_command = self.createRotateCommand()
        scale_command = self.createScaleCommand()

        if order == self.ScaRotTsl:
            mel.eval(scale_command)
            mel.eval(rotate_command)
            mel.eval(translate_command)
            return

        if order == self.ScaTslRot:
            mel.eval(scale_command)
            mel.eval(translate_command)
            mel.eval(rotate_command)
            return

        if order == self.RotScaTsl:
            mel.eval(rotate_command)
            mel.eval(scale_command)
            mel.eval(translate_command)
            return

        if order == self.RotTslSca:
            mel.eval(rotate_command)
            mel.eval(translate_command)
            mel.eval(scale_command)
            return

        if order == self.TslScaRot:
            mel.eval(translate_command)
            mel.eval(scale_command)
            mel.eval(rotate_command)
            return

        if order == self.TslRotSca:
            mel.eval(translate_command)
            mel.eval(rotate_command)
            mel.eval(scale_command)
            return

    def createTranslateCommand(self):
        translate = " -t " + self._parameters["Translate"].toStr()
        command = "polyMoveVertex" + translate + ";"
        return command

    def createRotateCommand(self):
        rotate = " -ro " + self._parameters["Rotate"].toStr()
        command = "polyMoveVertex" + rotate + ";"
        return command

    def createScaleCommand(self):
        scale = " -s " + self._parameters["Scale"].toStr()
        command = "polyMoveVertex" + scale + ";"
        return command
