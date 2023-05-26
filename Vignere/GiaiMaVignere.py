# Form implementation generated from reading ui file 'GiaiMaVignere.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import savefile, openfile 
import Vignere.vignere as vignere

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(628, 831)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnGiaiMaVignere = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnGiaiMaVignere.setGeometry(QtCore.QRect(260, 470, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnGiaiMaVignere.setFont(font)
        self.btnGiaiMaVignere.setObjectName("btnGiaiMaVignere")
        self.btnGiaiMaVignere.clicked.connect(self.btnGiaiMa_clicked)
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 490, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.btnBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBack.setGeometry(QtCore.QRect(90, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnBack.setFont(font)
        self.btnBack.setObjectName("btnBack")
        self.result = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 520, 561, 171))
        self.result.setObjectName("result")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.input = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.input.setGeometry(QtCore.QRect(40, 190, 561, 171))
        self.input.setObjectName("input")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 370, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.btnChonFile = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChonFile.setGeometry(QtCore.QRect(510, 100, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnChonFile.setFont(font)
        self.btnChonFile.setObjectName("btnChonFile")
        self.btnChonFile.clicked.connect(self.btnChonFile_Click)
        self.EdtPath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.EdtPath.setGeometry(QtCore.QRect(120, 100, 371, 22))
        self.EdtPath.setObjectName("EdtPath")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.btnSave = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(260, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.btnSaveFile_Click)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(40, 410, 561, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.btnMaHoaVignere = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnMaHoaVignere.setGeometry(QtCore.QRect(430, 720, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btnMaHoaVignere.setFont(font)
        self.btnMaHoaVignere.setObjectName("btnMaHoaVignere")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 0, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
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
        self.actionOpenFile = QtGui.QAction(parent=MainWindow)
        self.actionOpenFile.setObjectName("actionOpenFile")
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
        self.menuFile.addAction(self.actionOpenFile)
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

    # Chon file text
    def btnChonFile_Click(self):
        open_path_file = openfile.pathFile()
        self.EdtPath.setText(open_path_file)

        open_file = openfile.openFileDialog(open_path_file)
        self.input.setText(open_file)

    # button Giai Ma
    def btnGiaiMa_clicked(self):
        input = self.input.toPlainText()
        key = self.lineEdit.text()
        GiaiMa = vignere.GiaiMa(input,key)
        self.result.setText(GiaiMa)

    # Button Save
    def btnSaveFile_Click(self):
        res = self.result.toPlainText()
        savefile.saveFile(res)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chương trình mã hóa - giải mã văn bản"))
        self.btnGiaiMaVignere.setText(_translate("MainWindow", "Giải mã"))
        self.label_4.setText(_translate("MainWindow", "Kết quả:"))
        self.btnBack.setText(_translate("MainWindow", "Back"))
        self.label_2.setText(_translate("MainWindow", "File Path:"))
        self.label_5.setText(_translate("MainWindow", "Key"))
        self.btnChonFile.setText(_translate("MainWindow", "Chọn File"))
        self.label_3.setText(_translate("MainWindow", "Nội dung giải mã"))
        self.btnSave.setText(_translate("MainWindow", "Lưu File"))
        self.btnMaHoaVignere.setText(_translate("MainWindow", "Mã hóa"))
        self.label.setText(_translate("MainWindow", "Giải mã văn bản bằng Vignere"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionOpenFile.setText(_translate("MainWindow", "Open File"))
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