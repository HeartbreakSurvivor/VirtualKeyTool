# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainboard.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_UsartTool(object):
    def setupUi(self, UsartTool):
        UsartTool.setObjectName(_fromUtf8("UsartTool"))
        UsartTool.resize(472, 323)
        self.SwitchButton = QtGui.QPushButton(UsartTool)
        self.SwitchButton.setGeometry(QtCore.QRect(40, 252, 141, 31))
        self.SwitchButton.setObjectName(_fromUtf8("SwitchButton"))
        self.layoutWidget = QtGui.QWidget(UsartTool)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 74, 211))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.SerialnumLabel = QtGui.QLabel(self.layoutWidget)
        self.SerialnumLabel.setObjectName(_fromUtf8("SerialnumLabel"))
        self.verticalLayout.addWidget(self.SerialnumLabel)
        self.DataBitsLabel = QtGui.QLabel(self.layoutWidget)
        self.DataBitsLabel.setObjectName(_fromUtf8("DataBitsLabel"))
        self.verticalLayout.addWidget(self.DataBitsLabel)
        self.BaudRateLabel = QtGui.QLabel(self.layoutWidget)
        self.BaudRateLabel.setObjectName(_fromUtf8("BaudRateLabel"))
        self.verticalLayout.addWidget(self.BaudRateLabel)
        self.StopBitsLabel = QtGui.QLabel(self.layoutWidget)
        self.StopBitsLabel.setObjectName(_fromUtf8("StopBitsLabel"))
        self.verticalLayout.addWidget(self.StopBitsLabel)
        self.ParityLabel = QtGui.QLabel(self.layoutWidget)
        self.ParityLabel.setObjectName(_fromUtf8("ParityLabel"))
        self.verticalLayout.addWidget(self.ParityLabel)
        self.textEdit = QtGui.QTextEdit(UsartTool)
        self.textEdit.setGeometry(QtCore.QRect(270, 40, 191, 111))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.DataReceiveArea = QtGui.QLabel(UsartTool)
        self.DataReceiveArea.setGeometry(QtCore.QRect(270, 10, 121, 21))
        self.DataReceiveArea.setObjectName(_fromUtf8("DataReceiveArea"))
        self.DataSendArea = QtGui.QLabel(UsartTool)
        self.DataSendArea.setGeometry(QtCore.QRect(270, 170, 81, 31))
        self.DataSendArea.setObjectName(_fromUtf8("DataSendArea"))
        self.SendDataButton = QtGui.QPushButton(UsartTool)
        self.SendDataButton.setGeometry(QtCore.QRect(270, 270, 75, 23))
        self.SendDataButton.setObjectName(_fromUtf8("SendDataButton"))
        self.ClearDataButton = QtGui.QPushButton(UsartTool)
        self.ClearDataButton.setGeometry(QtCore.QRect(370, 270, 75, 23))
        self.ClearDataButton.setObjectName(_fromUtf8("ClearDataButton"))
        self.DataToSend = QtGui.QLineEdit(UsartTool)
        self.DataToSend.setGeometry(QtCore.QRect(270, 210, 191, 31))
        self.DataToSend.setObjectName(_fromUtf8("DataToSend"))
        self.layoutWidget1 = QtGui.QWidget(UsartTool)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 10, 111, 231))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.SerialNumComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.SerialNumComboBox.setObjectName(_fromUtf8("SerialNumComboBox"))
        self.verticalLayout_2.addWidget(self.SerialNumComboBox)
        self.DatabitsComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.DatabitsComboBox.setObjectName(_fromUtf8("DatabitsComboBox"))
        self.DatabitsComboBox.addItem(_fromUtf8(""))
        self.DatabitsComboBox.addItem(_fromUtf8(""))
        self.DatabitsComboBox.addItem(_fromUtf8(""))
        self.DatabitsComboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.DatabitsComboBox)
        self.BaudRataComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.BaudRataComboBox.setObjectName(_fromUtf8("BaudRataComboBox"))
        self.BaudRataComboBox.addItem(_fromUtf8(""))
        self.BaudRataComboBox.addItem(_fromUtf8(""))
        self.BaudRataComboBox.addItem(_fromUtf8(""))
        self.BaudRataComboBox.addItem(_fromUtf8(""))
        self.BaudRataComboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.BaudRataComboBox)
        self.StopBitsComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.StopBitsComboBox.setObjectName(_fromUtf8("StopBitsComboBox"))
        self.StopBitsComboBox.addItem(_fromUtf8(""))
        self.StopBitsComboBox.addItem(_fromUtf8(""))
        self.StopBitsComboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.StopBitsComboBox)
        self.ParityComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.ParityComboBox.setObjectName(_fromUtf8("ParityComboBox"))
        self.ParityComboBox.addItem(_fromUtf8(""))
        self.ParityComboBox.addItem(_fromUtf8(""))
        self.ParityComboBox.addItem(_fromUtf8(""))
        self.ParityComboBox.addItem(_fromUtf8(""))
        self.ParityComboBox.addItem(_fromUtf8(""))
        self.verticalLayout_2.addWidget(self.ParityComboBox)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.SwitchButton.raise_()
        self.textEdit.raise_()
        self.DataReceiveArea.raise_()
        self.DataSendArea.raise_()
        self.SendDataButton.raise_()
        self.ClearDataButton.raise_()
        self.DataToSend.raise_()

        self.retranslateUi(UsartTool)
        QtCore.QMetaObject.connectSlotsByName(UsartTool)

    def retranslateUi(self, UsartTool):
        UsartTool.setWindowTitle(_translate("UsartTool", "Dialog", None))
        self.SwitchButton.setText(_translate("UsartTool", "打开串口", None))
        self.SerialnumLabel.setText(_translate("UsartTool", "串口号：", None))
        self.DataBitsLabel.setText(_translate("UsartTool", "数据位：", None))
        self.BaudRateLabel.setText(_translate("UsartTool", "波特率：", None))
        self.StopBitsLabel.setText(_translate("UsartTool", "停止位：", None))
        self.ParityLabel.setText(_translate("UsartTool", "奇偶校验位：", None))
        self.DataReceiveArea.setText(_translate("UsartTool", "数据接收区域：", None))
        self.DataSendArea.setText(_translate("UsartTool", "数据发送区域：", None))
        self.SendDataButton.setText(_translate("UsartTool", "发送", None))
        self.ClearDataButton.setText(_translate("UsartTool", "清除", None))
        self.DatabitsComboBox.setItemText(0, _translate("UsartTool", "5", None))
        self.DatabitsComboBox.setItemText(1, _translate("UsartTool", "6", None))
        self.DatabitsComboBox.setItemText(2, _translate("UsartTool", "7", None))
        self.DatabitsComboBox.setItemText(3, _translate("UsartTool", "8", None))
        self.BaudRataComboBox.setItemText(0, _translate("UsartTool", "4800", None))
        self.BaudRataComboBox.setItemText(1, _translate("UsartTool", "9600", None))
        self.BaudRataComboBox.setItemText(2, _translate("UsartTool", "19200", None))
        self.BaudRataComboBox.setItemText(3, _translate("UsartTool", "57600", None))
        self.BaudRataComboBox.setItemText(4, _translate("UsartTool", "115200", None))
        self.StopBitsComboBox.setItemText(0, _translate("UsartTool", "1", None))
        self.StopBitsComboBox.setItemText(1, _translate("UsartTool", "1.5", None))
        self.StopBitsComboBox.setItemText(2, _translate("UsartTool", "2", None))
        self.ParityComboBox.setItemText(0, _translate("UsartTool", "None", None))
        self.ParityComboBox.setItemText(1, _translate("UsartTool", "Odd", None))
        self.ParityComboBox.setItemText(2, _translate("UsartTool", "Even", None))
        self.ParityComboBox.setItemText(3, _translate("UsartTool", "Mark", None))
        self.ParityComboBox.setItemText(4, _translate("UsartTool", "Space", None))
