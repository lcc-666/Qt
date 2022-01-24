import sys

import ui.HorizontalLayout
from PySide2.QtWidgets import QApplication,QMainWindow

if __name__ == '__main__':
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui=ui.HorizontalLayout.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())