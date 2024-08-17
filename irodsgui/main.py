import os
import sys

import irodsgui.globals as glob

from qtpy.QtGui import QIcon
from qtpy.QtCore import QSettings
from qtpy.QtWidgets import QApplication

from irodsgui.utils import assets_folder
from irodsgui.windows.window import Window
from irodsgui.version import __version__


def quit_application():
    print("Quitting application")
    sys.exit(app.exit())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(os.path.join(assets_folder(), 'icon.ico')))
    app.setOrganizationName(glob.app_name)
    app.setApplicationName(glob.app_name)
    app.setApplicationVersion(__version__)
    settings = QSettings()
    win = Window()
    win.show()

    app.setQuitOnLastWindowClosed(True)
    app.lastWindowClosed.connect(quit_application)
    app.exec()
