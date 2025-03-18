import os
import sys

from PyQt5.QtGui import QIcon, QPainter, QPixmap

import aes_encryption
import md5_digest
import rsa_encryption
# import PyQt5.QtGui
from PyQt5 import QtCore, QtGui, QtWidgets
from Cryptodome import Random
from Cryptodome.Cipher import AES
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from p_ui import Ui_Form


class Ui_mainWindow(object):
    def __init__(self, MainWindow):
        super().__init__()
        self.iv = Random.new().read(AES.block_size)
        self.rsa = rsa_encryption.RsaGenerator()
        self.mainwindow = MainWindow

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1587, 893)
        mainWindow.setFixedSize(1587, 893)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.aesArea = QtWidgets.QLabel(self.centralwidget)
        self.aesArea.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.aesArea.setFont(font)
        self.aesArea.setAutoFillBackground(False)
        self.aesArea.setObjectName("aesArea")
        self.aes_key1 = QtWidgets.QLineEdit(self.centralwidget)
        self.aes_key1.setGeometry(QtCore.QRect(240, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_key1.setFont(font)
        self.aes_key1.setObjectName("aes_key1")
        self.aes_key1.setInputMask('0000-0000-0000-0000;#')
        self.aes_key1_abel = QtWidgets.QLabel(self.centralwidget)
        self.aes_key1_abel.setGeometry(QtCore.QRect(150, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_key1_abel.setFont(font)
        self.aes_key1_abel.setObjectName("aes_key1_abel")
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(140, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")
        self.aes_inputtext = QtWidgets.QTextEdit(self.centralwidget)
        self.aes_inputtext.setGeometry(QtCore.QRect(240, 100, 331, 141))
        self.aes_inputtext.setObjectName("aes_inputtext")
        self.aes_eBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aes_eBtn.setGeometry(QtCore.QRect(490, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_eBtn.setFont(font)
        self.aes_eBtn.setObjectName("aes_eBtn")
        self.encrypted_label = QtWidgets.QLabel(self.centralwidget)
        self.encrypted_label.setGeometry(QtCore.QRect(600, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.encrypted_label.setFont(font)
        self.encrypted_label.setObjectName("encrypted_label")
        self.aes_encrypttext = QtWidgets.QTextEdit(self.centralwidget)
        self.aes_encrypttext.setGeometry(QtCore.QRect(710, 100, 331, 141))
        self.aes_encrypttext.setObjectName("aes_encrypttext")
        self.aes_display_label = QtWidgets.QLabel(self.centralwidget)
        self.aes_display_label.setGeometry(QtCore.QRect(1050, 100, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_display_label.setFont(font)
        self.aes_display_label.setObjectName("aes_display_label")
        self.aes_dBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aes_dBtn.setGeometry(QtCore.QRect(960, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_dBtn.setFont(font)
        self.aes_dBtn.setObjectName("aes_dBtn")
        self.aes_key2 = QtWidgets.QLineEdit(self.centralwidget)
        self.aes_key2.setGeometry(QtCore.QRect(710, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_key2.setFont(font)
        self.aes_key2.setObjectName("aes_key2")
        self.aes_key2.setInputMask('0000-0000-0000-0000;#')
        self.aes_key2_label = QtWidgets.QLabel(self.centralwidget)
        self.aes_key2_label.setGeometry(QtCore.QRect(610, 20, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.aes_key2_label.setFont(font)
        self.aes_key2_label.setObjectName("aes_key2_label")
        self.aes_display = QtWidgets.QTextEdit(self.centralwidget)
        self.aes_display.setGeometry(QtCore.QRect(1210, 100, 331, 141))
        self.aes_display.setObjectName("aes_display")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 250, 1561, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 30, 16, 201))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.MD5_Area = QtWidgets.QLabel(self.centralwidget)
        self.MD5_Area.setGeometry(QtCore.QRect(10, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.MD5_Area.setFont(font)
        self.MD5_Area.setAutoFillBackground(False)
        self.MD5_Area.setObjectName("MD5_Area")
        self.md5_text_label = QtWidgets.QLabel(self.centralwidget)
        self.md5_text_label.setGeometry(QtCore.QRect(150, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_text_label.setFont(font)
        self.md5_text_label.setObjectName("md5_text_label")
        self.nd5_textinput = QtWidgets.QTextEdit(self.centralwidget)
        self.nd5_textinput.setGeometry(QtCore.QRect(240, 280, 331, 141))
        self.nd5_textinput.setObjectName("nd5_textinput")
        self.md5_file_label = QtWidgets.QLabel(self.centralwidget)
        self.md5_file_label.setGeometry(QtCore.QRect(620, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_file_label.setFont(font)
        self.md5_file_label.setObjectName("md5_file_label")
        self.md5_diplay_label = QtWidgets.QLabel(self.centralwidget)
        self.md5_diplay_label.setGeometry(QtCore.QRect(1100, 300, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_diplay_label.setFont(font)
        self.md5_diplay_label.setObjectName("md5_diplay_label")
        self.md5_display = QtWidgets.QTextEdit(self.centralwidget)
        self.md5_display.setGeometry(QtCore.QRect(1210, 280, 331, 141))
        self.md5_display.setObjectName("md5_display")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(0, 430, 1561, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(110, 280, 16, 141))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.rsa_area = QtWidgets.QLabel(self.centralwidget)
        self.rsa_area.setGeometry(QtCore.QRect(10, 550, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.rsa_area.setFont(font)
        self.rsa_area.setAutoFillBackground(False)
        self.rsa_area.setObjectName("rsa_area")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(110, 460, 16, 381))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.rsa_inputtext = QtWidgets.QTextEdit(self.centralwidget)
        self.rsa_inputtext.setGeometry(QtCore.QRect(250, 680, 331, 141))
        self.rsa_inputtext.setObjectName("rsa_inputtext")
        self.rsa_encrypt_label = QtWidgets.QLabel(self.centralwidget)
        self.rsa_encrypt_label.setGeometry(QtCore.QRect(610, 680, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsa_encrypt_label.setFont(font)
        self.rsa_encrypt_label.setObjectName("rsa_encrypt_label")
        self.public_key_label = QtWidgets.QLabel(self.centralwidget)
        self.public_key_label.setGeometry(QtCore.QRect(860, 530, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.public_key_label.setFont(font)
        self.public_key_label.setObjectName("public_key_label")
        self.private_key_label = QtWidgets.QLabel(self.centralwidget)
        self.private_key_label.setGeometry(QtCore.QRect(150, 530, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.private_key_label.setFont(font)
        self.private_key_label.setObjectName("private_key_label")
        self.rsa_text_label = QtWidgets.QLabel(self.centralwidget)
        self.rsa_text_label.setGeometry(QtCore.QRect(150, 680, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsa_text_label.setFont(font)
        self.rsa_text_label.setObjectName("rsa_text_label")
        self.rsa_decryptedtext = QtWidgets.QTextEdit(self.centralwidget)
        self.rsa_decryptedtext.setGeometry(QtCore.QRect(1220, 680, 331, 141))
        self.rsa_decryptedtext.setObjectName("rsa_decryptedtext")
        self.rsa_eBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rsa_eBtn.setGeometry(QtCore.QRect(150, 740, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsa_eBtn.setFont(font)
        self.rsa_eBtn.setObjectName("rsa_eBtn")
        self.rsa_dBtn = QtWidgets.QPushButton(self.centralwidget)
        self.rsa_dBtn.setGeometry(QtCore.QRect(610, 740, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsa_dBtn.setFont(font)
        self.rsa_dBtn.setObjectName("rsa_dBtn")
        self.rsa_encryptedtext = QtWidgets.QTextBrowser(self.centralwidget)
        self.rsa_encryptedtext.setGeometry(QtCore.QRect(720, 680, 331, 141))
        self.rsa_encryptedtext.setObjectName("rsa_encryptedtext")
        self.rsa_decrypt_label = QtWidgets.QLabel(self.centralwidget)
        self.rsa_decrypt_label.setGeometry(QtCore.QRect(1100, 680, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rsa_decrypt_label.setFont(font)
        self.rsa_decrypt_label.setObjectName("rsa_decrypt_label")
        self.md5_textBtn = QtWidgets.QPushButton(self.centralwidget)
        self.md5_textBtn.setGeometry(QtCore.QRect(140, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_textBtn.setFont(font)
        self.md5_textBtn.setObjectName("md5_textBtn")
        self.md5_fileBtn = QtWidgets.QPushButton(self.centralwidget)
        self.md5_fileBtn.setGeometry(QtCore.QRect(610, 350, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_fileBtn.setFont(font)
        self.md5_fileBtn.setObjectName("md5_fileBtn")
        self.private_key = QtWidgets.QTextBrowser(self.centralwidget)
        self.private_key.setGeometry(QtCore.QRect(250, 460, 591, 192))
        self.private_key.setObjectName("private_key")
        self.private_key.setText(self.rsa.private_key.decode())
        self.public_key = QtWidgets.QTextBrowser(self.centralwidget)
        self.public_key.setGeometry(QtCore.QRect(960, 460, 591, 192))
        self.public_key.setObjectName("public_key")
        self.public_key.setText(self.rsa.public_key.decode())
        self.md5_fileinput = QtWidgets.QLineEdit(self.centralwidget)
        self.md5_fileinput.setGeometry(QtCore.QRect(710, 300, 331, 31))

        font = QtGui.QFont()
        font.setPointSize(12)
        self.md5_fileinput.setFont(font)
        self.md5_fileinput.setObjectName("md5_fileinput")
        self.md5_selectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.md5_selectBtn.setGeometry(QtCore.QRect(850, 350, 191, 28))

        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        self.md5_selectBtn.setFont(font)
        self.md5_selectBtn.setObjectName("md5_selectBtn")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1587, 26))

        self.reset_rsa_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_rsa_Btn.setGeometry(QtCore.QRect(140, 570, 93, 51))
        font = QtGui.QFont()
        font.setFamily("华光标题黑_CNKI")
        font.setPointSize(10)
        self.reset_rsa_Btn.setFont(font)
        self.reset_rsa_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_rsa_Btn.setObjectName("reset_rsa_Btn")

        self.reset_aes_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.reset_aes_Btn.setGeometry(QtCore.QRect(1080, 20, 101, 51))
        font = QtGui.QFont()
        font.setFamily("华光中圆_CNKI")
        font.setPointSize(12)
        self.reset_aes_Btn.setFont(font)
        self.reset_aes_Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset_aes_Btn.setObjectName("reset_aes_Btn")
        mainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1587, 33))
        font = QtGui.QFont()
        font.setFamily("华光中长宋_CNKI")
        font.setPointSize(14)
        self.menubar.setFont(font)
        self.menubar.setAutoFillBackground(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menu.setFont(font)
        self.menu.setObjectName("menu")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionone = QtWidgets.QAction(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.actionone.setFont(font)
        self.actionone.setObjectName("actionone")
        self.menu.addAction(self.actionone)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.aes_eBtn.clicked.connect(self.aesEncrypt)
        self.aes_dBtn.clicked.connect(self.aesDecrypt)
        self.md5_textBtn.clicked.connect(self.md5Digest)
        self.rsa_eBtn.clicked.connect(self.rsaEncrypt)
        self.rsa_dBtn.clicked.connect(self.rsaDecrypt)
        self.md5_selectBtn.clicked.connect(self.openfile)
        self.md5_fileBtn.clicked.connect(self.md5Digest_file)
        self.actionone.triggered.connect(self.signature_controller)
        self.reset_aes_Btn.clicked.connect(self.reset_iv)
        self.reset_rsa_Btn.clicked.connect(self.reset_rsa_key)

    def reset_rsa_key(self):
        try:
            self.rsa = rsa_encryption.RsaGenerator()
            self.public_key.setText(self.rsa.public_key.decode())
            self.private_key.setText(self.rsa.private_key.decode())
            QMessageBox.information(self.mainwindow, '提示', 'RSA密钥对已改变！',
                                    QMessageBox.Yes)
        except Exception:
            QMessageBox.information(self.mainwindow, '警告', '出现未知错误！',
                                    QMessageBox.Yes)

    def reset_iv(self):
        try:
            self.iv = Random.new().read(AES.block_size)
            QMessageBox.information(self.mainwindow, '提示', 'iv值已改变！',
                                    QMessageBox.Yes)
        except Exception:
            QMessageBox.information(self.mainwindow, '警告', '出现未知错误！',
                                    QMessageBox.Yes)

    def signature_controller(self):
        self.form = QtWidgets.QWidget()
        self.uform = Ui_Form(self.form)  # 创建PyQt设计的窗体对象
        self.uform.setupUi(self.form)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
        self.form.setWindowTitle("数字签名")
        self.form.setWindowIcon(QIcon(os.path.dirname(__file__) + '/image/icon.png'))
        self.form.show()  # 显示窗体

    def rsaEncrypt(self):
        content_r = self.rsa_inputtext.toPlainText()
        if len(content_r) != 0:
            content = rsa_encryption.encrypt(content_r)
            self.rsa_encryptedtext.setText(content)
        else:
            QMessageBox.information(self.mainwindow, '提示', '初始文本不得为空！',
                                    QMessageBox.Yes)

    def rsaDecrypt(self):
        self.rsa_decryptedtext.setText(rsa_encryption.decrypt())

    def aesEncrypt(self):
        ch = self.aes_key1.text()
        key = ''.join(ch.split('-')).strip()
        if len(key) == 16:
            # print(key)
            data = self.aes_inputtext.toPlainText()
            if len(data) != 0:
                # print(data)
                aes = aes_encryption.AesEncryption(key, self.iv)
                e = aes.encrypt(data)  # 调用加密函数
                self.aes_display.setText(e)
            else:
                QMessageBox.information(self.mainwindow, '提示', '加密文本不得为空，请检查！',
                                        QMessageBox.Yes)
        else:
            QMessageBox.information(self.mainwindow, '提示', '密钥必须为16位，请检查！',
                                    QMessageBox.Yes)

    def aesDecrypt(self):
        ch = self.aes_key2.text()
        key = ''.join(ch.split('-'))
        if len(key) == 16:
            # print(key)
            e = self.aes_encrypttext.toPlainText()
            if len(e) != 0:
                # print(e)
                aes = aes_encryption.AesEncryption(key, self.iv)
                try:
                    d = aes.decrypt(e)  # 调用解密函数
                    self.aes_display.setText(d)
                except Exception:
                    QMessageBox.information(self.mainwindow, '警告', '解密失败，密钥与密文不相对应！',
                                            QMessageBox.Yes)
                    self.aes_encrypttext.setText("")
            else:
                QMessageBox.information(self.mainwindow, '提示', '解密文本不得为空，请检查！',
                                        QMessageBox.Yes)

        else:
            QMessageBox.information(self.mainwindow, '提示', '密钥必须为16位，请检查！',
                                    QMessageBox.Yes)

    def md5Digest(self):
        ch = self.nd5_textinput.toPlainText()
        if len(ch) != 0:
            string_list = ch.strip().split('\\')
            ch = '/'.join(string_list)
            self.md5_display.setText(md5_digest.get_str_md5(ch))
        else:
            QMessageBox.information(self.mainwindow, '提示', '文本不能为空！',
                                    QMessageBox.Yes)

    def md5Digest_file(self):
        ch = self.md5_fileinput.text()
        if len(ch) != 0:
            v = md5_digest.get_file_md5(ch)
            if v:
                self.md5_display.setText(v)
            else:
                QMessageBox.information(self.mainwindow, '警告', '地址格式有误！',
                                        QMessageBox.Yes)
        else:
            QMessageBox.information(self.mainwindow, '提示', '文件地址不能为空！',
                                    QMessageBox.Yes)

    def openfile(self):
        # 实例化QFileDialog
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤

        path = dig.getOpenFileUrl()[0].path()
        if len(path[1:]) and self.md5_fileinput.text() != path[1:]:
            self.md5_fileinput.setText(path[1:])

    def paintEvent(self):
        painter = QPainter(self)
        pixmap = QPixmap("./image/R-C.jpg")
        # 绘制窗口背景，平铺到整个窗口，随着窗口改变而改变
        painter.drawPixmap(self.rect(), pixmap)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.aesArea.setText(_translate("mainWindow", "AES加密"))
        self.aes_key1_abel.setText(_translate("mainWindow", "密钥key:"))
        self.input_label.setText(_translate("mainWindow", "初始文本:"))
        self.aes_eBtn.setText(_translate("mainWindow", "加密"))
        self.encrypted_label.setText(_translate("mainWindow", "加密文本:"))
        self.aes_display_label.setText(_translate("mainWindow", "加密/解密显示:"))
        self.aes_dBtn.setText(_translate("mainWindow", "解密"))
        self.aes_key2_label.setText(_translate("mainWindow", "密钥key:"))
        self.MD5_Area.setText(_translate("mainWindow", "MD5算法"))
        self.md5_text_label.setText(_translate("mainWindow", "文本:"))
        self.md5_file_label.setText(_translate("mainWindow", "文件:"))
        self.md5_diplay_label.setText(_translate("mainWindow", "摘要值:"))
        self.rsa_area.setText(_translate("mainWindow", "RSA加密"))
        self.rsa_encrypt_label.setText(_translate("mainWindow", "加密文本:"))
        self.public_key_label.setText(_translate("mainWindow", "公开密钥:"))
        self.private_key_label.setText(_translate("mainWindow", "秘密密钥:"))
        self.rsa_text_label.setText(_translate("mainWindow", "初始文本:"))
        self.rsa_eBtn.setText(_translate("mainWindow", "加密"))
        self.rsa_dBtn.setText(_translate("mainWindow", "解密"))
        self.rsa_decrypt_label.setText(_translate("mainWindow", "解密文本:"))
        self.md5_textBtn.setText(_translate("mainWindow", "摘要"))
        self.md5_fileBtn.setText(_translate("mainWindow", "摘要"))
        self.md5_selectBtn.setText(_translate("mainWindow", "选择文件"))
        self.reset_rsa_Btn.setText(_translate("mainWindow", "重置密钥"))
        self.reset_aes_Btn.setText(_translate("mainWindow", "重置iv"))
        self.menu.setTitle(_translate("mainWindow", "数字签名"))
        self.actionone.setText(_translate("mainWindow", "数字签名器"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    UI = Ui_mainWindow(MainWindow)  # 创建PyQt设计的窗体对象
    UI.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
