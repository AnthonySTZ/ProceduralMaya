import abc


class BaseNode:
    def __init__(self):
        self._num_inputs = 0
        self._num_outputs = 0
        self._inputs = {}
        self._outputs = {}
        self._parameters = {}

    @abc.abstractmethod
    def getOutput(self, output_index):
        raise NotImplementedError("Output not implemented")
