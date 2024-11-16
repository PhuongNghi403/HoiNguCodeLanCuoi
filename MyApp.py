from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEx import MainWindowEx

app=QApplication([])
mainwindow=QMainWindow()
myui=MainWindowEx()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()