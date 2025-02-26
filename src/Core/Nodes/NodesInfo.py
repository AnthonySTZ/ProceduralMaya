class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Transform import Transform
        from Core.Nodes.Null import Null

        nodes = [Cube, Transform, Null]
        return nodes
