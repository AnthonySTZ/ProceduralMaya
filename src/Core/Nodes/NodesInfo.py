class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Transform import Transform

        nodes = [Cube, Transform]
        return nodes
