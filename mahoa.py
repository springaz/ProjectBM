# Form implementation generated from reading ui file 'mahoa.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(712, 414)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 0, 261, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 90, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setToolTipDuration(-1)
        self.label_2.setLineWidth(0)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnCaesar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnCaesar.setGeometry(QtCore.QRect(30, 160, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnCaesar.setFont(font)
        self.btnCaesar.setObjectName("btnCaesar")
        self.btnVignere = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnVignere.setGeometry(QtCore.QRect(250, 160, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnVignere.setFont(font)
        self.btnVignere.setObjectName("btnVignere")
        self.btnBelasco = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnBelasco.setGeometry(QtCore.QRect(30, 230, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnBelasco.setFont(font)
        self.btnBelasco.setObjectName("btnBelasco")
        self.btnTrithemius = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnTrithemius.setGeometry(QtCore.QRect(250, 230, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTrithemius.setFont(font)
        self.btnTrithemius.setObjectName("btnTrithemius")
        self.btnChuyenViHaiDong = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChuyenViHaiDong.setGeometry(QtCore.QRect(250, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnChuyenViHaiDong.setFont(font)
        self.btnChuyenViHaiDong.setObjectName("btnChuyenViHaiDong")
        self.btnXor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnXor.setGeometry(QtCore.QRect(470, 160, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnXor.setFont(font)
        self.btnXor.setObjectName("btnXor")
        self.btnChuyenViNhieuDong = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnChuyenViNhieuDong.setGeometry(QtCore.QRect(30, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnChuyenViNhieuDong.setFont(font)
        self.btnChuyenViNhieuDong.setObjectName("btnChuyenViNhieuDong")
        self.btnback = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnback.setGeometry(QtCore.QRect(10, 10, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnback.setFont(font)
        self.btnback.setObjectName("btnback")
        self.btnRSA = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnRSA.setGeometry(QtCore.QRect(470, 230, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnRSA.setFont(font)
        self.btnRSA.setObjectName("btnRSA")
        self.btnSDES = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnSDES.setGeometry(QtCore.QRect(470, 300, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnSDES.setFont(font)
        self.btnSDES.setObjectName("btnSDES")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 712, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(parent=self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMa_Hoa = QtGui.QAction(parent=MainWindow)
        self.actionMa_Hoa.setObjectName("actionMa_Hoa")
        self.actionGiai_Ma = QtGui.QAction(parent=MainWindow)
        self.actionGiai_Ma.setObjectName("actionGiai_Ma")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionMa_Hoa)
        self.menuMenu.addAction(self.actionGiai_Ma)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Chương trình mã hóa - giải mã văn bản"))
        self.label.setText(_translate("MainWindow", "Mã hóa văn bản"))
        self.label_2.setText(_translate("MainWindow", "Vui lòng chọn thuật toán muốn mã hóa"))
        self.btnCaesar.setText(_translate("MainWindow", "Caesar"))
        self.btnVignere.setText(_translate("MainWindow", "Vigenere"))
        self.btnBelasco.setText(_translate("MainWindow", "Belasco"))
        self.btnTrithemius.setText(_translate("MainWindow", "Trithemius"))
        self.btnChuyenViHaiDong.setText(_translate("MainWindow", "Chuyển vị hai dòng"))
        self.btnXor.setText(_translate("MainWindow", "XOR"))
        self.btnChuyenViNhieuDong.setText(_translate("MainWindow", "Chuyển vị nhiều dòng"))
        self.btnback.setText(_translate("MainWindow", "Back"))
        self.btnRSA.setText(_translate("MainWindow", "RSA"))
        self.btnSDES.setText(_translate("MainWindow", "SDES"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionMa_Hoa.setText(_translate("MainWindow", "Mã hóa"))
        self.actionGiai_Ma.setText(_translate("MainWindow", "Giải mã"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())