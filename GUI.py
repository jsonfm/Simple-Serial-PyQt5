# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(548, 411)
        MainWindow.setStyleSheet("#connectBtn:checked{\n"
"background-color: rgb(115, 210, 22);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setObjectName("clearBtn")
        self.horizontalLayout_6.addWidget(self.clearBtn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.Terminal = QtWidgets.QTextBrowser(self.centralwidget)
        self.Terminal.setObjectName("Terminal")
        self.verticalLayout_2.addWidget(self.Terminal)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setObjectName("input")
        self.horizontalLayout_4.addWidget(self.input)
        self.sendBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sendBtn.setObjectName("sendBtn")
        self.horizontalLayout_4.addWidget(self.sendBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.portList = QtWidgets.QComboBox(self.centralwidget)
        self.portList.setObjectName("portList")
        self.horizontalLayout.addWidget(self.portList)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.BaudList = QtWidgets.QComboBox(self.centralwidget)
        self.BaudList.setObjectName("BaudList")
        self.horizontalLayout_2.addWidget(self.BaudList)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.connectBtn = QtWidgets.QPushButton(self.centralwidget)
        self.connectBtn.setCheckable(True)
        self.connectBtn.setObjectName("connectBtn")
        self.horizontalLayout_3.addWidget(self.connectBtn)
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setObjectName("updateBtn")
        self.horizontalLayout_3.addWidget(self.updateBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 548, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TERMINAL SERIAL"))
        self.clearBtn.setText(_translate("MainWindow", "CLEAR"))
        self.sendBtn.setText(_translate("MainWindow", "ENVIAR"))
        self.label_2.setText(_translate("MainWindow", "Port:"))
        self.label_3.setText(_translate("MainWindow", "Baudrate:"))
        self.connectBtn.setText(_translate("MainWindow", "CONECTAR"))
        self.updateBtn.setText(_translate("MainWindow", "ACTUALIZAR"))


