from load_plugin import load_plugin

load_plugin()
from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform

cube_01 = Cube()
cube_02 = Cube()
transform_01 = Transform()

transform_01.setInput(0, cube_01)

print(transform_01.inputConnection(0))
print(transform_01.input(0))
