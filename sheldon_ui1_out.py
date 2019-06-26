# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Sheldon_ui1.ui'
#
# Created: Sat Apr 27 13:00:07 2019
#      by: PyQt4 UI code generator 4.10
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(750, 436)
        self.mainTabWidget = QtGui.QTabWidget(Dialog)
        self.mainTabWidget.setGeometry(QtCore.QRect(11, 86, 641, 241))
        self.mainTabWidget.setIconSize(QtCore.QSize(40, 40))
        self.mainTabWidget.setObjectName(_fromUtf8("mainTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/home button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab, icon, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/Jira Button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab_2, icon1, _fromUtf8(""))
        self.updateButton = QtGui.QPushButton(Dialog)
        self.updateButton.setGeometry(QtCore.QRect(334, 340, 101, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.openButton = QtGui.QPushButton(Dialog)
        self.openButton.setGeometry(QtCore.QRect(550, 340, 101, 23))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setGeometry(QtCore.QRect(444, 340, 91, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(11, 21, 80, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/file icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(90, 20, 81, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon3)
        self.toolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))

        self.retranslateUi(Dialog)
        self.mainTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "JPMC Shelden", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab), _translate("Dialog", "Home", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_2), _translate("Dialog", "Jira", None))
        self.updateButton.setText(_translate("Dialog", "Update Ticket", None))
        self.openButton.setText(_translate("Dialog", "Open In Browser", None))
        self.closeButton.setText(_translate("Dialog", "Close Ticket", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.toolButton_2.setText(_translate("Dialog", "...", None))

