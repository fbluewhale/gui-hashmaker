# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_page.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import hashlib

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 771, 61))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(0, 20, 112, 23))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(110, 20, 112, 23))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(240, 20, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 200, 771, 51))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 771, 70))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 270, 771, 121))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 841, 601))
        self.label_2.setStyleSheet("image: url(:/newPrefix/Screenshot from 2020-04-13 13-01-36.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/images.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.textBrowser.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.generate_hash)
        self.radioButton.clicked.connect(self.tt)
        self.radioButton_2.clicked.connect(self.tc)
        self.radioButton_3.clicked.connect(self.te)
        #QtCore.QMetaObject.connectSlotsByName(self.tt)

    t = 0
    def tt(self):
        self.t = 1
    def tc(self):
        self.t = 3
    def te(self):
        self.t = 2

    def generate_hash(self):
        textboxValue = self.textEdit.toPlainText()
        print(textboxValue,self.t)
        if self.t == 0:
            self.textBrowser.clear()
            self.textBrowser.append("please choose a type")
        elif self.t == 1:
            self.textBrowser.clear()
            hash_obj = hashlib.sha256(textboxValue.encode())
            self.textBrowser.append(hash_obj.hexdigest())
        elif self.t == 2:
            self.textBrowser.clear()
            hash_obj = hashlib.md5(textboxValue.encode())
            self.textBrowser.append(hash_obj.hexdigest())
        elif self.t == 3:
            self.textBrowser.clear()
            hash_obj = hashlib.sha1(textboxValue.encode())
            self.textBrowser.append(hash_obj.hexdigest())


        #self.textBrowser.append(textboxValue)
        #self.textEdit.setText("")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "hash type"))
        self.radioButton.setText(_translate("MainWindow", "sha256"))
        self.radioButton_3.setText(_translate("MainWindow", "md5"))
        self.radioButton_2.setText(_translate("MainWindow", "sha1"))
        self.pushButton.setText(_translate("MainWindow", "genrate"))
        self.label.setText(_translate("MainWindow", "input"))

import ts

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
