# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Sheldon_ui4.ui'
#
# Created: Sat Jun  8 19:17:43 2019
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
        self.mainTabWidget.setGeometry(QtCore.QRect(10, 90, 641, 241))
        self.mainTabWidget.setIconSize(QtCore.QSize(40, 40))
        self.mainTabWidget.setObjectName(_fromUtf8("mainTabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 50, 321, 131))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.jiraLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.jiraLabel.setFont(font)
        self.jiraLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.jiraLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.jiraLabel.setTextFormat(QtCore.Qt.RichText)
        self.jiraLabel.setObjectName(_fromUtf8("jiraLabel"))
        self.gridLayout.addWidget(self.jiraLabel, 0, 0, 1, 1)
        self.jiraCountLabel = QtGui.QLabel(self.layoutWidget)
        self.jiraCountLabel.setFrameShape(QtGui.QFrame.WinPanel)
        self.jiraCountLabel.setObjectName(_fromUtf8("jiraCountLabel"))
        self.gridLayout.addWidget(self.jiraCountLabel, 0, 1, 1, 1)
        self.hpsmLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.hpsmLabel.setFont(font)
        self.hpsmLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.hpsmLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.hpsmLabel.setTextFormat(QtCore.Qt.RichText)
        self.hpsmLabel.setObjectName(_fromUtf8("hpsmLabel"))
        self.gridLayout.addWidget(self.hpsmLabel, 1, 0, 1, 1)
        self.jiraCountLabel_2 = QtGui.QLabel(self.layoutWidget)

        self.jiraCountLabel_2.setFrameShape(QtGui.QFrame.WinPanel)
        self.jiraCountLabel_2.setObjectName(_fromUtf8("jiraCountLabel_2"))
        self.gridLayout.addWidget(self.jiraCountLabel_2, 1, 1, 1, 1)
        self.itsmLabel = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Segoe UI Black"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.itsmLabel.setFont(font)
        self.itsmLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.itsmLabel.setFrameShadow(QtGui.QFrame.Sunken)
        self.itsmLabel.setTextFormat(QtCore.Qt.RichText)
        self.itsmLabel.setObjectName(_fromUtf8("itsmLabel"))
        self.gridLayout.addWidget(self.itsmLabel, 2, 0, 1, 1)
        self.jiraCountLabel_3 = QtGui.QLabel(self.layoutWidget)
        self.jiraCountLabel_3.setFrameShape(QtGui.QFrame.WinPanel)
        self.jiraCountLabel_3.setObjectName(_fromUtf8("jiraCountLabel_3"))
        self.gridLayout.addWidget(self.jiraCountLabel_3, 2, 1, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/home button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab, icon, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.updateButton = QtGui.QPushButton(self.tab_2)
        self.updateButton.setGeometry(QtCore.QRect(310, 160, 101, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(10)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName(_fromUtf8("updateButton"))
        self.closeButton = QtGui.QPushButton(self.tab_2)
        self.closeButton.setGeometry(QtCore.QRect(420, 160, 91, 23))
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.openButton = QtGui.QPushButton(self.tab_2)
        self.openButton.setGeometry(QtCore.QRect(520, 160, 101, 23))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.tableWidget = QtGui.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 631, 151))
        self.tableWidget.setAutoScrollMargin(20)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/Jira Button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab_2, icon1, _fromUtf8(""))
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
        self.mainTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "JPMC Shelden", None))
        self.jiraLabel.setText(_translate("Dialog", "No Of Jira Ticket", None))
        self.jiraCountLabel.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">3</span></p></body></html>", None))
        self.hpsmLabel.setText(_translate("Dialog", "No Of HPSM", None))
        self.jiraCountLabel_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">5</span></p></body></html>", None))
        self.itsmLabel.setText(_translate("Dialog", "No Of ITSM", None))
        self.jiraCountLabel_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">2</span></p></body></html>", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab), _translate("Dialog", "Home", None))
        self.updateButton.setText(_translate("Dialog", "Update Ticket", None))
        self.closeButton.setText(_translate("Dialog", "Close Ticket", None))
        self.openButton.setText(_translate("Dialog", "Open In Browser", None))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Ticket Number", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Ticket Description ", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Priority", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Age", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_2), _translate("Dialog", "Jira", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.toolButton_2.setText(_translate("Dialog", "...", None))
