class IOItem:

    INPUT = 0
    OUTPUT = 1

    def __init__(self, node_item, io, iotype):
        self._node_item = node_item
        self._io = io
        self._type = iotype

    def getNodeItem(self):
        return self._node_item

    def getIO(self):
        return self._io

    def getType(self):
        return self._type
