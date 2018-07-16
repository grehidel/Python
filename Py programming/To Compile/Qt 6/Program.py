import sys
from PyQt4 import QtGui,QtCore

class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setGeometry(50,50,800,800)
        self.setWindowTitle('Am just GreHiDeL ')
        self.setWindowIcon(QtGui.QIcon('mimi.jpg'))
        # defining a menu bar
        leave=QtGui.QAction("Leave",self)
        leave.setShortcut("Ctrl+Q")
        leave.setStatusTip("Say Goodbye")
        leave.triggered.connect(self.quit)

        #defining history
        history_1=QtGui.QAction('History',self)
        history_1.setShortcut("Ctrl+H")
        history_1.setStatusTip("View History")
        history_1.triggered.connect(self.history)

        self.statusBar()
        mainMenu=self.menuBar()
        fileMenu=mainMenu.addMenu('&Progress')
        fileMenu.addAction(leave)
        # define history
        history=self.menuBar()
        history_menu=history.addMenu('History')
        history_menu.addAction(history_1)
        self.action()

    def action(self):
        btn1=QtGui.QPushButton('Leave',self)
        btn1.clicked.connect(self.quit)
        btn1.resize(50,50)
        btn1.move(750,750)
        self.show()

    def history(self):
        try:
            for i in range(10):
                print(1)
        except(ValueError):
            print(2)

    def quit(self):
        sys.exit()


def run():
    app=QtGui.QApplication(sys.argv)
    GUI=Window()
    sys.exit(app.exec_())
run()
               
