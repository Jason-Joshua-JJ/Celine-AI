# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'celineui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_celineUI(object):
    def setupUi(self, celineUI):
        celineUI.setObjectName("celineUI")
        celineUI.resize(1824, 990)
        self.centralwidget = QtWidgets.QWidget(celineUI)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-420, -140, 4341, 1391))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\JJ Network\Celine Assi\Pictures\celine.jpg"))
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(False)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 860, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 860, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 30, 531, 441))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("D:/JJ Network/Celine Assi/Pictures/updatess.gif"))
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(410, 70, 301, 61))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(20)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"font-size:25px;")
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(410, 140, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(18)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setStyleSheet("background:transparent;\n"
"border-radius:none;\n"
"font-size:25px;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        celineUI.setCentralWidget(self.centralwidget)

        self.retranslateUi(celineUI)
        QtCore.QMetaObject.connectSlotsByName(celineUI)

    def retranslateUi(self, celineUI):
        _translate = QtCore.QCoreApplication.translate
        celineUI.setWindowTitle(_translate("celineUI", "MainWindow"))
        self.pushButton.setText(_translate("celineUI", "Run"))
        self.pushButton_2.setText(_translate("celineUI", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    celineUI = QtWidgets.QMainWindow()
    ui = Ui_celineUI()
    ui.setupUi(celineUI)
    celineUI.show()
    sys.exit(app.exec_())
