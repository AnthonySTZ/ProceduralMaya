from .BaseNode import BaseNode


class Null(BaseNode):

    def __init__(self):
        super().__init__()
        self._name = "Null"
        self._num_inputs = 1
        self._num_outputs = 1

    def commandAtIndex(self, index):
        if index != 0:
            print("Index out of range !")
            return

        if self.input(0) is None:
            print("No connection !")
            return

        current_xform = self.input(0).commandAtIndex(0)
        return current_xform
