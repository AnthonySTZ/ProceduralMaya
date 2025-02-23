import os

os.system("cls")
import sys

from dotenv import load_dotenv

load_dotenv()

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from Core.Nodes.Cube import Cube
from Core.Nodes.Transform import Transform

cube_01 = Cube()
transform_01 = Transform()

transform_01.setInput(0, cube_01)

# print(cube_01.input(0))
