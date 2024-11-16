from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalandSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalandSlot(self):
        self.pushButtonNew.clicked.connect(self.process_new)
        self.pushButtonSolve.clicked.connect(self.process_solve)


    def process_solve(self):
        try:
            n=int(self.lineEditInputN.text())
            k=int(self.lineEditInputK.text())
            result=sum_50(n, k)
            dd = f"Sum of {n}&{k}={result}"
            self.lineEditS.setText(dd)
            self.lineEditS.setStyleSheet("color:green")

        except ValueError:
            self.labelError.setText("Nhập sai r")
            self.labelError.setStyleSheet("color:red")

    def process_new(self):
        self.lineEditInputN.setText("")
        self.lineEditInputK.setText("")
        self.lineEditS.setText("")
        self.lineEditS.setFocus()
        self.lineEditInputN.setFocus()
        self.lineEditInputK.setFocus()