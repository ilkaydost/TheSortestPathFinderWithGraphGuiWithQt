from Form1 import Ui_Form
from PyQt5 import QtWidgets
import ShortestPath

import sys

class Driver(QtWidgets.QWidget):

    def __init__(self):

        super(Driver, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        


app = QtWidgets.QApplication([])
application = Driver()
application.show()
sys.exit(app.exec_())





