import base64
import os
import sys

from Cryptodome.PublicKey import RSA
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from digital_signature import combine, verifier


class Ui_Form(object):
    def __init__(self, Form):
        super().__init__()
        self.Form = Form

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(781, 301)
        self.sBnt1 = QtWidgets.QPushButton(Form)
        self.sBnt1.setGeometry(QtCore.QRect(40, 80, 93, 28))
        self.sBnt1.setObjectName("sBnt1")
        self.sBnt2 = QtWidgets.QPushButton(Form)
        self.sBnt2.setGeometry(QtCore.QRect(430, 80, 93, 28))
        self.sBnt2.setObjectName("sBnt2")
        self.textEdit1 = QtWidgets.QTextEdit(Form)
        self.textEdit1.setGeometry(QtCore.QRect(40, 140, 301, 81))
        self.textEdit1.setObjectName("textEdit1")
        self.textEdit2 = QtWidgets.QTextEdit(Form)
        self.textEdit2.setGeometry(QtCore.QRect(430, 140, 301, 81))
        self.textEdit2.setObjectName("textEdit2")
        self.dBnt1 = QtWidgets.QPushButton(Form)
        self.dBnt1.setGeometry(QtCore.QRect(40, 240, 161, 28))
        self.dBnt1.setObjectName("dBnt1")
        self.dBnt2 = QtWidgets.QPushButton(Form)
        self.dBnt2.setGeometry(QtCore.QRect(430, 240, 171, 28))
        self.dBnt2.setObjectName("dBnt2")
        self.lineEdit1 = QtWidgets.QLineEdit(Form)
        self.lineEdit1.setGeometry(QtCore.QRect(40, 40, 321, 21))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Form)
        self.lineEdit2.setGeometry(QtCore.QRect(430, 40, 321, 21))
        self.lineEdit2.setObjectName("lineEdit2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.dBnt1.clicked.connect(self.signer)
        self.dBnt2.clicked.connect(self.verify)
        self.sBnt1.clicked.connect(self.openfile_sBnt1)
        self.sBnt2.clicked.connect(self.openfile_sBnt2)

    def signer(self):
        file_path = self.lineEdit1.text()

        if len(file_path) != 0:
            string_list = file_path.strip().split('\\')
            file_path = '/'.join(string_list)
            sign = combine(file_path)
            if sign == "Err 101":
                QMessageBox.information(self.Form, '提示', '未找到私钥！',
                                        QMessageBox.Yes)
            elif sign == "Err 102":
                QMessageBox.information(self.Form, '提示', '未找到原数据！',
                                        QMessageBox.Yes)
            else:
                obj_path = self.textEdit1.toPlainText()
                if len(obj_path) != 0:
                    try:
                        sign_file = open(obj_path, 'wb')
                        sign_file.write(sign.encode('utf-8'))
                        sign_file.close()
                        QMessageBox.information(self.Form, '提示', '已提交！',
                                                QMessageBox.Yes)
                    except Exception:
                        QMessageBox.information(self.Form, '警告', "未知错误，检查地址格式（以'/'划分）或地址是否存在！",
                                                QMessageBox.Yes)
                else:
                    QMessageBox.information(self.Form, '警告', '不得输入空地址！',
                                            QMessageBox.Yes)
        else:
            QMessageBox.information(self.Form, '提示', '地址不能为空！',
                                    QMessageBox.Yes)

    def verify(self):
        file_path = self.lineEdit2.text()

        if len(file_path) != 0:
            if os.path.isfile(file_path):
                try:
                    sign_file = open(file_path, 'rb')
                    data_r, signature_r = list(sign_file.read().decode('utf-8').split("==========\n"))
                    sign_file.close()
                    try:
                        data = eval(data_r)
                        signature = eval(signature_r)
                        public_key = RSA.import_key(open("public_key.pem").read())
                        obj_path = self.textEdit2.toPlainText()
                        if len(obj_path) != 0:
                            try:
                                newfile_r = base64.b64decode(data)
                                newfile = open(obj_path, 'wb')
                                newfile.write(newfile_r)
                                newfile.close()
                            except IOError:
                                QMessageBox.information(self.Form, '提示', '读写错误！',
                                                        QMessageBox.Yes)
                            else:
                                ch = verifier(public_key, data, signature)
                                QMessageBox.information(self.Form, '提示', ch,
                                                        QMessageBox.Yes)

                        else:
                            QMessageBox.information(self.Form, '警告', '地址为空！',
                                                    QMessageBox.Yes)

                    except Exception:
                        QMessageBox.information(self.Form, '警告', "未知错误，有可能是公钥未放入软件安装目录下！",
                                                QMessageBox.Yes)
                except Exception:
                    QMessageBox.information(self.Form, '警告', "未找到文件或地址错误！",
                                            QMessageBox.Yes)
            else:
                QMessageBox.information(self.Form, '警告', '路径不存在！',
                                        QMessageBox.Yes)
        else:
            QMessageBox.information(self.Form, '提示', '地址不能为空！',
                                    QMessageBox.Yes)

    def openfile_sBnt1(self):
        # 实例化QFileDialog
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤

        path = dig.getOpenFileUrl()[0].path()
        if len(path[1:]) and self.lineEdit1.text() != path[1:]:
            self.lineEdit1.setText(path[1:])

    def openfile_sBnt2(self):
        # 实例化QFileDialog
        dig = QFileDialog()
        # 设置可以打开任何文件
        dig.setFileMode(QFileDialog.AnyFile)
        # 文件过滤

        path = dig.getOpenFileUrl()[0].path()
        if len(path[1:]) and self.lineEdit2.text() != path[1:]:
            self.lineEdit2.setText(path[1:])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sBnt1.setText(_translate("Form", "选择文件"))
        self.sBnt2.setText(_translate("Form", "选择文件"))
        self.dBnt1.setText(_translate("Form", "签名并保存签名文件"))
        self.dBnt2.setText(_translate("Form", "检验签名并读取文件"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    UForm = Ui_Form(form)  # 创建PyQt设计的窗体对象
    UForm.setupUi(form)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    form.setWindowTitle("数字签名")
    form.setWindowIcon(QIcon(os.path.dirname(__file__) + '/image/softwareIcon.png'))
    form.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
