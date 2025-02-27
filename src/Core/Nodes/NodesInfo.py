class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Sphere import Sphere
        from Core.Nodes.Transform import Transform
        from Core.Nodes.Merge import Merge
        from Core.Nodes.Null import Null

        nodes = [Cube, Sphere, Transform, Merge, Null]
        return nodes
