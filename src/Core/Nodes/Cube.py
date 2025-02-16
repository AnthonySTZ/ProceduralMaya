from .BaseNode import BaseNode


class Cube(BaseNode):
    def __init__(self):
        super().__init__()
        self._num_inputs = 0
        self._num_outputs = 1
        self._parameters = {"width": 1.0, "height": 1.0, "depth": 1.0}

    def getOutput(self, output_index):
        if not (0 <= output_index < self._num_outputs):
            raise NotImplementedError("Invalid output index " + str(output_index))
        return "Create Cube command with : " + str(self._parameters)
