# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Sheldon_ui5.ui'
#
# Created: Wed Jun 26 11:18:31 2019
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import yaml

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

ticket_list = list()
render_data = list()
index = 0
file = "tickets.csv"
profile_file = "profile.yaml"


try:
    with open(profile_file, 'r') as profile:
        profile_info = yaml.load(profile)
        user_sid = profile_info['sid']
        first_name = profile_info['first_name']
        second_name = profile_info['second_name']
except:
    print("Unable to open config file {}".format(profile_file))
    exit(1)


try:
    fn = open(file, 'r')
    for line in fn:
        line = line.strip()
        line_fields = line.split(',')
        render_data.append(line_fields)
        index +=1
except:
    print("Unable to open the file {}".format(file))
    exit(1)



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
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/HP-service-manager.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab_2, icon1, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tableWidget_2 = QtGui.QTableWidget(self.tab_3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 631, 151))
        self.tableWidget_2.setAutoScrollMargin(20)
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, item)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(390, 160, 101, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 160, 101, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/Jira Button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab_3, icon2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget_3 = QtGui.QTableWidget(self.tab_4)
        self.tableWidget_3.setGeometry(QtCore.QRect(0, 0, 631, 151))
        self.tableWidget_3.setAutoScrollMargin(20)
        self.tableWidget_3.setRowCount(10)
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 170, 0))
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(1, 4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setItem(2, 3, item)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(40)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.pushButton_3 = QtGui.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(410, 160, 91, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 160, 91, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/ITSM.jpg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainTabWidget.addTab(self.tab_4, icon3, _fromUtf8(""))
        self.toolButton = QtGui.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(11, 21, 80, 61))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/file icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon4)
        self.toolButton.setIconSize(QtCore.QSize(50, 50))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(90, 20, 81, 61))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("Myicons/setting.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon5)
        self.toolButton_2.setIconSize(QtCore.QSize(50, 50))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))

        self.retranslateUi(Dialog, render_data)
        self.mainTabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, render_data):
        Dialog.setWindowTitle(_translate("Dialog", "Workly", None))
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
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        render_data = [ render_data[x] for  x in range(len(render_data)) if int(render_data[x][4]) == int(user_sid)]


        if render_data:
            for i in range(len(render_data)):
                ticket, description, priority, age, sid = render_data[i]
                print("iamhere")
                item = self.tableWidget.item(i, 0)
                item.setText(_translate("Dialog", ticket, None))
                item = self.tableWidget.item(i, 1)
                item.setText(_translate("Dialog", description, None))
                item = self.tableWidget.item(i, 2)
                item.setText(_translate("Dialog", priority, None))
                item = self.tableWidget.item(i, 3)
                item.setText(_translate("Dialog", age, None))


        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_2), _translate("Dialog", "HPSM", None))
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Summary", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Epic", None))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Sprint", None))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Due Date", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        item = self.tableWidget_2.item(0, 0)
        item.setText(_translate("Dialog", "Config Delta Initail Dev Release", None))
        item = self.tableWidget_2.item(0, 1)
        item.setText(_translate("Dialog", "Config Delta 2.0", None))
        item = self.tableWidget_2.item(0, 2)
        item.setText(_translate("Dialog", "060106302019", None))
        item = self.tableWidget_2.item(0, 3)
        item.setText(_translate("Dialog", "30/June/2019", None))
        item = self.tableWidget_2.item(1, 0)
        item.setText(_translate("Dialog", "Auto Patching Script", None))
        item = self.tableWidget_2.item(1, 1)
        item.setText(_translate("Dialog", "Manual Control", None))
        item = self.tableWidget_2.item(1, 2)
        item.setText(_translate("Dialog", "060106302019", None))
        item = self.tableWidget_2.item(1, 3)
        item.setText(_translate("Dialog", "30/June/2019", None))
        self.tableWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Dialog", "Update WorkLog", None))
        self.pushButton_2.setText(_translate("Dialog", "Open In Browser", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_3), _translate("Dialog", "JIRA", None))
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Change Number", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Change Title", None))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Change Status", None))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Start Date", None))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "End Date", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        item = self.tableWidget_3.item(0, 0)
        item.setText(_translate("Dialog", "C04218747", None))
        item = self.tableWidget_3.item(0, 1)
        item.setText(_translate("Dialog", "AIM installation on Prod Server", None))
        item = self.tableWidget_3.item(0, 2)
        item.setText(_translate("Dialog", "Ready To Implement", None))
        item = self.tableWidget_3.item(0, 3)
        item.setText(_translate("Dialog", "06/26/2019 5:30", None))
        item = self.tableWidget_3.item(0, 4)
        item.setText(_translate("Dialog", "06/27/2019 5:30", None))
        item = self.tableWidget_3.item(1, 0)
        item.setText(_translate("Dialog", "C04218843", None))
        item = self.tableWidget_3.item(1, 1)
        item.setText(_translate("Dialog", "AIX Upgrade", None))
        item = self.tableWidget_3.item(1, 2)
        item.setText(_translate("Dialog", "Pending Approval", None))
        item = self.tableWidget_3.item(1, 3)
        item.setText(_translate("Dialog", "06/26/2019 5:30", None))
        item = self.tableWidget_3.item(1, 4)
        item.setText(_translate("Dialog", "06/29/2019 5:30", None))
        self.tableWidget_3.setSortingEnabled(__sortingEnabled)
        self.pushButton_3.setText(_translate("Dialog", "Accept Task", None))
        self.pushButton_4.setText(_translate("Dialog", "Open In Browser", None))
        self.mainTabWidget.setTabText(self.mainTabWidget.indexOf(self.tab_4), _translate("Dialog", "ITSM", None))
        self.toolButton.setText(_translate("Dialog", "...", None))
        self.toolButton_2.setText(_translate("Dialog", "...", None))

