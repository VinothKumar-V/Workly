from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import Sheldon_ui4_out

class sheldonApp(QDialog, Sheldon_ui4_out.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

app = QApplication(sys.argv)
dialog = sheldonApp()
dialog.show()
app.exec_()