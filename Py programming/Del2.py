from PyQt4 import QtCore, QtGui
#import gui_5
from apps_5 import print_situation
import sys
 
 
if __name__ == "__main__":
 
    app = QtGui.QApplication(sys.argv)
 
    gui_master = gui_5.QtGui.QWidget()
    master = gui_5.Ui_Form()
    master.setupUi(gui_master)
 
    master.checkBox.clicked.connect(print_situation)
 
    gui_master.show()
    sys.exit(app.exec_())
