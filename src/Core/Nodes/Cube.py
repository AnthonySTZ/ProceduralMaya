from .BaseNode import BaseNode


class Cube(BaseNode):
    def __init__(self):
        super().__init__()
        self._num_inputs = 0
        self._num_outputs = 1

    def getOutput(self, output_index):
        if not (0 < output_index < self._num_outputs):
            raise NotImplementedError(
                "Not Enough Output for the index " + str(output_index)
            )
        return "Create Cube command"
