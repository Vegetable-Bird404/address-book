# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ManageSys.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 661)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 31))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.plainTextEditName = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEditName.setMinimumSize(QtCore.QSize(258, 31))
        self.plainTextEditName.setMaximumSize(QtCore.QSize(258, 31))
        self.plainTextEditName.setObjectName("plainTextEditName")
        self.horizontalLayout_2.addWidget(self.plainTextEditName)
        self.pushButtonSearchName = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchName.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButtonSearchName.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtonSearchName.setFont(font)
        self.pushButtonSearchName.setObjectName("pushButtonSearchName")
        self.horizontalLayout_2.addWidget(self.pushButtonSearchName)
        spacerItem = QtWidgets.QSpacerItem(178, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 31))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.plainTextEditID = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(25)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.plainTextEditID.sizePolicy().hasHeightForWidth())
        self.plainTextEditID.setSizePolicy(sizePolicy)
        self.plainTextEditID.setMinimumSize(QtCore.QSize(258, 31))
        self.plainTextEditID.setMaximumSize(QtCore.QSize(258, 31))
        self.plainTextEditID.setObjectName("plainTextEditID")
        self.horizontalLayout_3.addWidget(self.plainTextEditID)
        self.pushButtonSearchID = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSearchID.setMinimumSize(QtCore.QSize(0, 31))
        self.pushButtonSearchID.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtonSearchID.setFont(font)
        self.pushButtonSearchID.setObjectName("pushButtonSearchID")
        self.horizontalLayout_3.addWidget(self.pushButtonSearchID)
        spacerItem1 = QtWidgets.QSpacerItem(178, 31, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(731, 421))
        self.tableWidget.setMaximumSize(QtCore.QSize(731, 421))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtondelete = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtondelete.sizePolicy().hasHeightForWidth())
        self.pushButtondelete.setSizePolicy(sizePolicy)
        self.pushButtondelete.setMinimumSize(QtCore.QSize(141, 30))
        self.pushButtondelete.setMaximumSize(QtCore.QSize(141, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtondelete.setFont(font)
        self.pushButtondelete.setObjectName("pushButtondelete")
        self.horizontalLayout.addWidget(self.pushButtondelete)
        self.pushButtonClear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonClear.setMinimumSize(QtCore.QSize(141, 30))
        self.pushButtonClear.setMaximumSize(QtCore.QSize(141, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtonClear.setFont(font)
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.horizontalLayout.addWidget(self.pushButtonClear)
        self.pushButtonAdd = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAdd.setMinimumSize(QtCore.QSize(141, 30))
        self.pushButtonAdd.setMaximumSize(QtCore.QSize(141, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtonAdd.setFont(font)
        self.pushButtonAdd.setObjectName("pushButtonAdd")
        self.horizontalLayout.addWidget(self.pushButtonAdd)
        self.pushButtonExit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExit.setMinimumSize(QtCore.QSize(141, 30))
        self.pushButtonExit.setMaximumSize(QtCore.QSize(141, 30))
        font = QtGui.QFont()
        font.setFamily("Adobe Fangsong Std")
        font.setPointSize(12)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Address Database"))
        self.label.setText(_translate("MainWindow", "输入姓名:"))
        self.pushButtonSearchName.setText(_translate("MainWindow", "按姓名查找"))
        self.label_2.setText(_translate("MainWindow", "输入学号:"))
        self.pushButtonSearchID.setText(_translate("MainWindow", "按学号查找"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "学号"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "性别"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "年级"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "电话"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "专业"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "地址"))
        self.pushButtondelete.setText(_translate("MainWindow", "删除选中信息"))
        self.pushButtonClear.setText(_translate("MainWindow", "清空数据"))
        self.pushButtonAdd.setText(_translate("MainWindow", "添加信息"))
        self.pushButtonExit.setText(_translate("MainWindow", "退出系统"))