import os
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QPainter, QPixmap

import ui


# 程序入口，程序从此处启动PyQt设计的窗体
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()  # 创建窗体对象
    UI = ui.Ui_mainWindow(MainWindow)  # 创建PyQt设计的窗体对象
    UI.setupUi(MainWindow)  # 调用PyQt窗体的方法对窗体对象进行初始化设置
    MainWindow.setWindowTitle("简易加密演示工具")

    MainWindow.setWindowIcon(QIcon(os.path.dirname(__file__) + '/image/softwareIcon.png'))
    MainWindow.show()  # 显示窗体
    sys.exit(app.exec_())  # 程序关闭时退出进程
