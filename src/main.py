import os
import sys
from dotenv import load_dotenv

load_dotenv()

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from importlib import reload
import Core.ProcCore as ProcCore

reload(ProcCore)

ProcCore.reloadLib()
ProcCore.createWindow()
