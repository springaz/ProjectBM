# Form implementation generated from reading ui file 'MaHoaRSA.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import savefile, openfile
import RSA.RSA as RSA
from RSA.RSA import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(628, 813)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.EdtPath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EdtPath.setGeometry(QtCore.QRect(120, 100, 371, 22))
        self.EdtPath.setObjectName("EdtPath")
        self.input = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.input.setGeometry(QtCore.QRect(40, 190, 561, 171))
        self.input.setObjectName("input")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnChonFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChonFile.setGeometry(QtCore.QRect(510, 100, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnChonFile.setFont(font)
        self.btnChonFile.setObjectName("btnChonFile")
        self.btnChonFile.clicked.connect(self.btnChonFile_Click)
        self.result = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 450, 561, 171))
        self.result.setObjectName("result")
        self.btnGiaiMaRSA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGiaiMaRSA.setGeometry(QtCore.QRect(430, 650, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGiaiMaRSA.setFont(font)
        self.btnGiaiMaRSA.setObjectName("btnGiaiMaRSA")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 551, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.btnMaHoaRSA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMaHoaRSA.setGeometry(QtCore.QRect(260, 390, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnMaHoaRSA.setFont(font)
        self.btnMaHoaRSA.setObjectName("btnMaHoaRSA")
        self.btnMaHoaRSA.clicked.connect(self.btnMaHoa_Click)
        self.btnSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(260, 650, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.btnSaveFile_Click)
        self.btnBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(90, 650, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 420, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(parent=MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave_File = QtGui.QAction(parent=MainWindow)
        self.actionSave_File.setObjectName("actionSave_File")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionM_h_a = QtGui.QAction(parent=MainWindow)
        self.actionM_h_a.setObjectName("actionM_h_a")
        self.actionGi_i_m = QtGui.QAction(parent=MainWindow)
        self.actionGi_i_m.setObjectName("actionGi_i_m")
        self.actionExit_2 = QtGui.QAction(parent=MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addSeparator()
        self.menuMenu.addAction(self.actionM_h_a)
        self.menuMenu.addAction(self.actionGi_i_m)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit_2)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Chọn file
    def btnChonFile_Click(self):
        open_path_file = openfile.pathFile()
        self.EdtPath.setText(open_path_file)

        open_file = openfile.openFileDialog(open_path_file)
        self.input.setText(open_file)
    
    #Mã hóa
    def btnMaHoa_Click(self):
        input = self.input.toPlainText()
        MaHoa = RSA.MaHoa(input,e,n)
        self.result.setPlainText(str(MaHoa))

    # Button Save
    def btnSaveFile_Click(self):
        res = self.result.toPlainText()
        savefile.saveFile(res)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Nội dung mã hóa"))
        self.label_2.setText(_translate("MainWindow", "File Path:"))
        self.btnChonFile.setText(_translate("MainWindow", "Chọn File"))
        self.btnGiaiMaRSA.setText(_translate("MainWindow", "Giải mã"))
        self.label.setText(_translate("MainWindow", "Mã hóa văn bản bằng RSA"))
        self.btnMaHoaRSA.setText(_translate("MainWindow", "Mã hóa"))
        self.btnSave.setText(_translate("MainWindow", "Lưu File"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.label_4.setText(_translate("MainWindow", "Kết quả:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave_File.setText(_translate("MainWindow", "Save File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionM_h_a.setText(_translate("MainWindow", "Mã hóa"))
        self.actionGi_i_m.setText(_translate("MainWindow", "Giải mã"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
