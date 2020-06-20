import sys
from PyQt5 import QtWidgets

from Login_ui.Login_ui_main import Login
from Monitoring_GUI.ui_main import Monitor_form

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    login = Login()
    if login.exec_() == QtWidgets.QDialog.Accepted:
        w = Monitor_form()
        app.aboutToQuit.connect(w.onExit)
        sys.exit(app.exec())


