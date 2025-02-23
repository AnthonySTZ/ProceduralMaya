from Core.Nodes.NodeConnection import NodeConnection


class NodeConnections:
    """
    Store all connections using a dictionary

    key : Input -> Can avoid input being linked 2 times
    value: Output
    """

    def __init__(self):
        self._connections = {}

    def addConnection(self, input, output):
        if input.getType() != NodeConnection.INPUT:
            print("Wrong IO type, expected 'INPUT'")
            return
        if input in self._connections:
            print(
                "Input is already connected"
            )  # TODO: handle this by overiding connection
            return

        self._connections[input] = output
