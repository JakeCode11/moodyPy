import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from moodyUI import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.stackedWidget.setCurrentWidget(self.ui.page)

        #buttons to face playground
        self.ui.startBtn.clicked.connect(self.showFacePG)
        self.ui.facePGBtn.clicked.connect(self.showFacePG)
        self.ui.facePGBtn2.clicked.connect(self.showFacePG)
        self.ui.facePGBtn3.clicked.connect(self.showFacePG)

        #buttons to text playground (type)
        self.ui.textPGTypeBtn.clicked.connect(self.showTextPGType)
        self.ui.textPGTypeBtn2.clicked.connect(self.showTextPGType)
        self.ui.textPGTypeBtn3.clicked.connect(self.showTextPGType)

        #buttons to text playground (image)
        self.ui.textPGImageBtn.clicked.connect(self.showTextPGImage)
        self.ui.textPGImageBtn2.clicked.connect(self.showTextPGImage)
        self.ui.textPGImageBtn3.clicked.connect(self.showTextPGImage)

        #buttons to quiz mode
        self.ui.quizModeBtn.clicked.connect(self.showQuiz)
        self.ui.quizModeBtn2.clicked.connect(self.showQuiz)
        self.ui.quizModeBtn3.clicked.connect(self.showQuiz)

    def show(self):
        self.main_win.show()
    
    def showFacePG(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def showTextPGType(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def showTextPGImage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)

    def showQuiz(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
