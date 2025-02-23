class IO:
    INPUT = 0
    OUTPUT = 1

    def __init__(self, node, index, type):
        self._node = node
        self._index = index
        self._type = type

    def getType(self):
        return self._type
