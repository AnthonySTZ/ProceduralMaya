class NodesInfo:

    @staticmethod
    def getNodes():
        from Core.Nodes.Cube import Cube
        from Core.Nodes.Sphere import Sphere
        from Core.Nodes.Transform import Transform
        from Core.Nodes.Duplicate import Duplicate
        from Core.Nodes.Merge import Merge
        from Core.Nodes.Null import Null
        from Core.Nodes.Import import Import
        from Core.Nodes.Bend import Bend
        from Core.Nodes.Twist import Twist

        nodes = [Cube, Sphere, Transform, Duplicate, Merge, Null, Import, Bend, Twist]
        return nodes
