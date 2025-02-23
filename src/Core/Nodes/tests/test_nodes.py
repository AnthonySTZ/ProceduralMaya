from load_plugin import load_plugin

load_plugin()
from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform
from Core.Nodes.Scene import Scene

scene = Scene()

cube_01 = Cube()
cube_02 = Cube()
transform_01 = Transform()

scene.addNode(cube_01)
scene.addNode(cube_02)
scene.addNode(transform_01)

print(cube_02.getName())
print(scene.getNodes())

# transform_01.setInput(0, cube_01)

# print(transform_01.inputConnection(0))
# print(transform_01.input(0))
