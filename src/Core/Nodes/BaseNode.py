import abc


class BaseNode:
    def __init__(self):
        self._inputs = []
        self._outputs = []
        self._parameters = {}

    @abc.abstractmethod
    def getOutput(self, output_index):
        raise NotImplementedError("Output not implemented")
