class NodeConnections:
    """
    Store all connections using a dictionary

    key : Input -> Can avoid input being linked 2 times
    value: Output
    """

    def __init__(self):
        self._connections = {}
