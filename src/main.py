import os
import sys

plugin_path = os.path.join(os.environ["PROCEDURAL_MAYA"], "src")

sys.path.insert(0, plugin_path)

from importlib import reload
import UI.MainWindow as MainWindow
import Lib.CompactQt.Qt as Qt

reload(MainWindow)
reload(Qt)

MainWindow.createWindow()
