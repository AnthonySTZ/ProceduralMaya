class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Sphere import Sphere
        from Core.Nodes.Transform import Transform
        from Core.Nodes.Duplicate import Duplicate
        from Core.Nodes.Merge import Merge
        from Core.Nodes.Null import Null

        nodes = [Cube, Sphere, Transform, Duplicate, Merge, Null]
        return nodes
