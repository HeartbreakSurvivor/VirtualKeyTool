# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'keyedit.ui'
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

class Ui_KeyEdit(object):
    def setupUi(self, KeyEdit):
        KeyEdit.setObjectName(_fromUtf8("KeyEdit"))
        KeyEdit.resize(490, 327)
        self.buttonBox = QtGui.QDialogButtonBox(KeyEdit)
        self.buttonBox.setGeometry(QtCore.QRect(300, 290, 171, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.KeyName1 = QtGui.QLineEdit(KeyEdit)
        self.KeyName1.setEnabled(True)
        self.KeyName1.setGeometry(QtCore.QRect(21, 41, 71, 25))
        self.KeyName1.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName1.setObjectName(_fromUtf8("KeyName1"))
        self.KeyName2 = QtGui.QLineEdit(KeyEdit)
        self.KeyName2.setGeometry(QtCore.QRect(21, 78, 71, 25))
        self.KeyName2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName2.setObjectName(_fromUtf8("KeyName2"))
        self.KeyName3 = QtGui.QLineEdit(KeyEdit)
        self.KeyName3.setGeometry(QtCore.QRect(21, 115, 71, 25))
        self.KeyName3.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName3.setObjectName(_fromUtf8("KeyName3"))
        self.KeyName4 = QtGui.QLineEdit(KeyEdit)
        self.KeyName4.setGeometry(QtCore.QRect(21, 152, 71, 25))
        self.KeyName4.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName4.setObjectName(_fromUtf8("KeyName4"))
        self.KeyName5 = QtGui.QLineEdit(KeyEdit)
        self.KeyName5.setGeometry(QtCore.QRect(21, 189, 71, 25))
        self.KeyName5.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName5.setObjectName(_fromUtf8("KeyName5"))
        self.KeyName6 = QtGui.QLineEdit(KeyEdit)
        self.KeyName6.setGeometry(QtCore.QRect(21, 226, 71, 25))
        self.KeyName6.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName6.setObjectName(_fromUtf8("KeyName6"))
        self.KeyName7 = QtGui.QLineEdit(KeyEdit)
        self.KeyName7.setGeometry(QtCore.QRect(21, 263, 71, 25))
        self.KeyName7.setMaximumSize(QtCore.QSize(16777215, 31))
        self.KeyName7.setObjectName(_fromUtf8("KeyName7"))
        self.VirtualKey1 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey1.setGeometry(QtCore.QRect(130, 40, 69, 25))
        self.VirtualKey1.setObjectName(_fromUtf8("VirtualKey1"))
        self.VirtualKey2 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey2.setGeometry(QtCore.QRect(130, 78, 69, 25))
        self.VirtualKey2.setObjectName(_fromUtf8("VirtualKey2"))
        self.VirtualKey3 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey3.setGeometry(QtCore.QRect(130, 115, 69, 25))
        self.VirtualKey3.setObjectName(_fromUtf8("VirtualKey3"))
        self.VirtualKey4 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey4.setGeometry(QtCore.QRect(130, 152, 69, 25))
        self.VirtualKey4.setObjectName(_fromUtf8("VirtualKey4"))
        self.VirtualKey5 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey5.setGeometry(QtCore.QRect(130, 189, 69, 25))
        self.VirtualKey5.setObjectName(_fromUtf8("VirtualKey5"))
        self.VirtualKey6 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey6.setGeometry(QtCore.QRect(130, 226, 69, 25))
        self.VirtualKey6.setObjectName(_fromUtf8("VirtualKey6"))
        self.VirtualKey7 = QtGui.QComboBox(KeyEdit)
        self.VirtualKey7.setGeometry(QtCore.QRect(130, 263, 69, 25))
        self.VirtualKey7.setObjectName(_fromUtf8("VirtualKey7"))
        self.SendMsg1 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg1.setGeometry(QtCore.QRect(313, 40, 161, 25))
        self.SendMsg1.setObjectName(_fromUtf8("SendMsg1"))
        self.SendMsg2 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg2.setGeometry(QtCore.QRect(313, 78, 161, 25))
        self.SendMsg2.setObjectName(_fromUtf8("SendMsg2"))
        self.SendMsg3 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg3.setGeometry(QtCore.QRect(313, 115, 161, 25))
        self.SendMsg3.setAutoFillBackground(False)
        self.SendMsg3.setObjectName(_fromUtf8("SendMsg3"))
        self.SendMsg4 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg4.setGeometry(QtCore.QRect(313, 152, 161, 25))
        self.SendMsg4.setObjectName(_fromUtf8("SendMsg4"))
        self.SendMsg5 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg5.setGeometry(QtCore.QRect(313, 189, 161, 25))
        self.SendMsg5.setObjectName(_fromUtf8("SendMsg5"))
        self.SendMsg6 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg6.setGeometry(QtCore.QRect(313, 226, 161, 25))
        self.SendMsg6.setObjectName(_fromUtf8("SendMsg6"))
        self.SendMsg7 = QtGui.QLineEdit(KeyEdit)
        self.SendMsg7.setGeometry(QtCore.QRect(313, 263, 161, 25))
        self.SendMsg7.setObjectName(_fromUtf8("SendMsg7"))
        self.layoutWidget = QtGui.QWidget(KeyEdit)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 461, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 23))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.KeyCustome1 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome1.setGeometry(QtCore.QRect(260, 48, 21, 16))
        self.KeyCustome1.setText(_fromUtf8(""))
        self.KeyCustome1.setObjectName(_fromUtf8("KeyCustome1"))
        self.KeyCustome2 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome2.setGeometry(QtCore.QRect(260, 84, 21, 16))
        self.KeyCustome2.setText(_fromUtf8(""))
        self.KeyCustome2.setObjectName(_fromUtf8("KeyCustome2"))
        self.KeyCustome3 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome3.setGeometry(QtCore.QRect(260, 120, 21, 16))
        self.KeyCustome3.setText(_fromUtf8(""))
        self.KeyCustome3.setObjectName(_fromUtf8("KeyCustome3"))
        self.KeyCustome4 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome4.setGeometry(QtCore.QRect(260, 156, 21, 16))
        self.KeyCustome4.setText(_fromUtf8(""))
        self.KeyCustome4.setObjectName(_fromUtf8("KeyCustome4"))
        self.KeyCustome6 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome6.setGeometry(QtCore.QRect(260, 228, 21, 16))
        self.KeyCustome6.setText(_fromUtf8(""))
        self.KeyCustome6.setObjectName(_fromUtf8("KeyCustome6"))
        self.KeyCustome5 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome5.setGeometry(QtCore.QRect(260, 192, 21, 16))
        self.KeyCustome5.setText(_fromUtf8(""))
        self.KeyCustome5.setObjectName(_fromUtf8("KeyCustome5"))
        self.KeyCustome7 = QtGui.QCheckBox(KeyEdit)
        self.KeyCustome7.setGeometry(QtCore.QRect(260, 264, 21, 16))
        self.KeyCustome7.setText(_fromUtf8(""))
        self.KeyCustome7.setObjectName(_fromUtf8("KeyCustome7"))

        self.retranslateUi(KeyEdit)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), KeyEdit.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), KeyEdit.reject)
        QtCore.QMetaObject.connectSlotsByName(KeyEdit)

    def retranslateUi(self, KeyEdit):
        KeyEdit.setWindowTitle(_translate("KeyEdit", "Dialog", None))

        self.KeyName1.setText(_translate("KeyEdit","Dialog",None))
        self.KeyName2.setText(_translate("KeyEdit", "Dialog", None))
        self.KeyName3.setText(_translate("KeyEdit", "Dialog", None))
        self.KeyName4.setText(_translate("KeyEdit", "Dialog", None))
        self.KeyName5.setText(_translate("KeyEdit", "Dialog", None))
        self.KeyName6.setText(_translate("KeyEdit", "Dialog", None))
        self.KeyName7.setText(_translate("KeyEdit", "Dialog", None))

        self.label.setText(_translate("KeyEdit", "按键名称", None))
        self.label_2.setText(_translate("KeyEdit", "虚拟key", None))
        self.label_3.setText(_translate("KeyEdit", "自定义", None))
        self.label_4.setText(_translate("KeyEdit", "内容", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    KeyEdit = QtGui.QDialog()
    ui = Ui_KeyEdit()
    ui.setupUi(KeyEdit)
    KeyEdit.show()
    sys.exit(app.exec_())

