# from main import Ui_MainWindow
from PyQt6 import QtWidgets
import sys  
import intro, main, mahoa, giaima
import Caesar.MaHoaCaesar as MaHoaCaesar, Caesar.GiaiMaCaesar as GiaiMaCaesar
import Vignere.MaHoaVignere as MaHoaVignere , Vignere.GiaiMaVignere as GiaiMaVignere
import Trithemius.MaHoaTrithemius as MaHoaTrithemius, Trithemius.GiaiMaTrithemius as GiaiMaTrithemius
import ChuyenViHaiDong.MaHoaChuyenViHaiDong as MaHoaChuyenViHaiDong, ChuyenViHaiDong.GiaiMaChuyenViHaiDong as GiaiMaChuyenViHaiDong
import ChuyenViNhieuDong.MaHoaChuyenViNhieuDong as MaHoaChuyenViNhieuDong, ChuyenViNhieuDong.GiaiMaChuyenViNhieuDong as GiaiMaChuyenViNhieuDong
import Belasco.MaHoaBelasco as MaHoaBelasco, Belasco.GiaiMaBelasco as GiaiMaBelasco
import XOR.MaHoaXOR as MaHoaXOR, XOR.GiaiMaXOR as GiaiMaXOR
import RSA.MaHoaRSA as MaHoaRSA,  RSA.GiaiMaRSA as GiaiMaRSA
import SDES.MaHoaSDES as MaHoaSDES, SDES.GiaiMaSDES as GiaiMaSDES
ui=''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

def introUI():
    global ui 
    ui = intro.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBatDau.clicked.connect(main_UI)
    MainWindow.show()


def main_UI():
    global ui 
    ui = main.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnMa_Hoa.clicked.connect(mahoa_UI)
    ui.btnGiai_Ma.clicked.connect(giaima_UI)
    MainWindow.show()

def mahoa_UI():
    global ui 
    ui = mahoa.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnback.clicked.connect(main_UI)
    ui.btnCaesar.clicked.connect(mahoaCeasar_UI)
    ui.btnVignere.clicked.connect(maHoaVignere_UI)
    ui.btnTrithemius.clicked.connect(mahoatrithemius_UI)
    ui.btnBelasco.clicked.connect(mahoabelasco_UI)
    ui.btnChuyenViHaiDong.clicked.connect(mahoachuyenvi_UI)
    ui.btnChuyenViNhieuDong.clicked.connect(mahoachuyenvinhieudong_UI)
    ui.btnXor.clicked.connect(mahoaxor_UI)
    ui.btnRSA.clicked.connect(mahoarsa_UI)
    ui.btnSDES.clicked.connect(mahoasdes_UI)
    MainWindow.show()

def giaima_UI():
    global ui 
    ui = giaima.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnback_2.clicked.connect(main_UI)
    ui.btnCaesar.clicked.connect(giaiMaCeasar_UI)
    ui.btnVignere.clicked.connect(giaimaVignere_UI)
    ui.btnTrithemius.clicked.connect(giaimatrithemius_UI)
    ui.btnBelasco.clicked.connect(giaimabelasco_UI)
    ui.btnChuyenViHaiDong.clicked.connect(giaimachuyenvi_UI)
    ui.btnChuyenViNhieuDong.clicked.connect(giaimachuyenvinhieudong_UI)
    ui.btnXor.clicked.connect(giaimaxor_UI)
    ui.btnRSA.clicked.connect(giaimarsa_UI)
    ui.btnSDES.clicked.connect(giaimasdes_UI)
    MainWindow.show()


def mahoaCeasar_UI():
    global ui 
    ui = MaHoaCaesar.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMa.clicked.connect(giaiMaCeasar_UI)
    MainWindow.show()


def giaiMaCeasar_UI():
    global ui 
    ui = GiaiMaCaesar.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoa.clicked.connect(mahoaCeasar_UI)


def maHoaVignere_UI():
    global ui
    ui = MaHoaVignere.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaVignere.clicked.connect(giaimaVignere_UI)

def giaimaVignere_UI():
    global ui
    ui = GiaiMaVignere.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaVignere.clicked.connect(maHoaVignere_UI)


def mahoatrithemius_UI():
    global ui
    ui = MaHoaTrithemius.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaTrithemius.clicked.connect(giaimatrithemius_UI)

def giaimatrithemius_UI():
    global ui
    ui = GiaiMaTrithemius.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaTrithemius.clicked.connect(mahoatrithemius_UI)


def mahoabelasco_UI():
    global ui
    ui = MaHoaBelasco.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaBelasco.clicked.connect(giaimabelasco_UI)


def giaimabelasco_UI():
    global ui
    ui = GiaiMaBelasco.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaBelasco.clicked.connect(mahoabelasco_UI)

def mahoachuyenvi_UI():
    global ui
    ui = MaHoaChuyenViHaiDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaChuyenViHaiDong.clicked.connect(giaimachuyenvi_UI)

def giaimachuyenvi_UI():
    global ui
    ui = GiaiMaChuyenViHaiDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaChuyenViHaiDong.clicked.connect(mahoachuyenvi_UI)

def mahoachuyenvinhieudong_UI():
    global ui
    ui = MaHoaChuyenViNhieuDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaChuyenViNhieuDong.clicked.connect(giaimachuyenvinhieudong_UI)

def giaimachuyenvinhieudong_UI():
    global ui
    ui = GiaiMaChuyenViNhieuDong.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaChuyenViNhieuDong.clicked.connect(mahoachuyenvinhieudong_UI)


def mahoaxor_UI():
    global ui
    ui = MaHoaXOR.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaXOR.clicked.connect(giaimaxor_UI)

def giaimaxor_UI():
    global ui
    ui = GiaiMaXOR.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaXOR.clicked.connect(mahoaxor_UI)

def mahoarsa_UI():
    global ui
    ui = MaHoaRSA.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaRSA.clicked.connect(giaimarsa_UI)

def giaimarsa_UI():
    global ui
    ui = GiaiMaRSA.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnMaHoaRSA.clicked.connect(mahoarsa_UI)

def mahoasdes_UI():
    global ui
    ui = MaHoaSDES.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(mahoa_UI)
    ui.btnGiaiMaSDES.clicked.connect(giaimasdes_UI)

def giaimasdes_UI():
    global ui
    ui = GiaiMaSDES.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.btnBack.clicked.connect(giaima_UI)
    ui.btnMaHoaSDES.clicked.connect(mahoasdes_UI)


introUI() 
sys.exit(app.exec())