import sys

PYQT6 = True
PYSIDE2 = True


try:
    print("Importing PyQt6...")
    from PyQt6.QtCore import *
    from PyQt6.QtWidgets import *
    from PyQt6.QtGui import *
    from PyQt6.QtCore import pyqtSignal as SIGNAL

    print("PyQt6 successfully imported")
    PYQT6 = True

except ImportError:
    print("PyQt6 not available !")
    PYQT6 = False

if not PYQT6:
    try:
        print("Try Importing PySide2...")
        from PySide2.QtCore import *
        from PySide2.QtWidgets import *
        from PySide2.QtGui import *
        from PySide2.QtCore import Signal as SIGNAL

        print("PySide2 successfully imported")
        PYSIDE2 = True
    except ImportError:
        print("PySide2 not available !")
        PYSIDE2 = False

if not PYQT6 and not PYSIDE2:
    print("Error importing Qt modules !")
    sys.exit(0)
