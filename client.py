import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox, QListWidgetItem, QDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer, QThread
from PyQt5.QtGui import QTextCharFormat, QKeyEvent, QStandardItemModel, QStandardItem

from Login import *
from ManageSys import *
from InsertInfo import *

import sqlite3  # 导入 sqlite 库

class login_window(QtWidgets.QMainWindow, Ui_Form):
    """登录界面类
    使用同一组lineEdit登录或注册 初始化存储用户数据的数据库‘user.db’
    Methods:
        register_button:注册后用户名和密码将存储到user.db的user表格中
        login_button:登录时用当前lineEdit匹配数据库中的信息 验证密码
    """
    def __init__(self):
        super(login_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        self.init()

    def init(self):
        self.pushButton.clicked.connect(self.login_button)  # 连接槽
        self.pushButtonreg.clicked.connect(self.register_button)

        # 连接数据库
        self.conn = sqlite3.connect('user.db')
        self.conn.row_factory = sqlite3.Row  # 设置返回结果为字典形式
        # 创建一个游标对象
        self.cursor = self.conn.cursor()
        # 创建表
        sql_text = '''CREATE TABLE IF NOT EXISTS user
                          (Username TEXT,
                           Password TEXT
                           );'''
        # 执行sql语句
        self.cursor.execute(sql_text)

    def register_button(self):
        # 直接用登陆界面输入的注册 就不新建一个窗口了
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        data = [(username, password)]
        self.cursor.executemany('INSERT INTO user VALUES (?,?)', data)
        self.conn.commit()
        QMessageBox.information(self, '通知', '注册成功')

    def login_button(self):
        if self.lineEdit_2.text() == "":
            QMessageBox.warning(self, '警告', '密码为空，请重新输入！')
            return None
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        # 查询用户表中是否存在匹配的用户名和密码
        self.cursor.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
        user = self.cursor.fetchone()
        if user:
            Ui_Main = main_window()  # 生成主窗口的实例
            self.hide()
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.conn.close()
            Ui_Main.show()
        else:
            QMessageBox.warning(self, '警告', '用户名或密码错误，请重新输入！')



class main_window(QtWidgets.QMainWindow, Ui_MainWindow):
    """ 主界面类
    初始化数据库'database.db' 如果没有表database则创建 读取已有数据刷新表格
    重要标志位：clickflag 功能：只有当人为编辑表格（双击为前提）才触发ChangeDatabase 通过代码修改的表格不执行该函数
    Methods:
        slot:(槽函数)
            closeEvent:重写关闭窗口事件
            handle_cell_clicked(row, column):表格点击事件 返回选中行列号 更新当前选中tablewidget行号和数据库的ROWID（当不存在删除条目情况时两者相差1）
            openDialog:打开插入条目子窗口
            ClearDatabase:清空数据库中内容（不包括表头）
            DeleteDatabase:删除选中数据，并刷新ROWID为相对索引
            SearchDatabase(value):两个按键同时连接，但传入不同参数，决定按姓名还是学号搜索，搜索结束后会在表中隐藏其他信息，当搜索框内无值时，搜索操作为refresh_table
            ChangeDatabase(item):直接编辑表格内容，并同步更新数据库，更新标志位clickflag为0
            flagset:双击触发事件，使能tablewidget编辑属性，设定clickflag为1

        AddDatabase(student_info):接收从子窗口返回的学生信息
        refresh_table:根据数据库刷新表格内容
    """
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)  # 创建窗体对象
        # 初始化信号槽
        self.pushButtonAdd.clicked.connect(self.openDialog)  # 添加信息
        self.pushButtonExit.clicked.connect(self.close)
        self.pushButtonClear.clicked.connect(self.ClearDatabase)
        self.pushButtondelete.clicked.connect(self.DeleteDatabase)
        self.pushButtonSearchName.clicked.connect(lambda: self.SearchDatabase(1))
        self.pushButtonSearchID.clicked.connect(lambda: self.SearchDatabase(2))

        # 连接数据库
        self.conn = sqlite3.connect('database.db')
        self.conn.row_factory = sqlite3.Row  # 设置返回结果为字典形式
        # 创建一个游标对象
        self.cursor = self.conn.cursor()
        # 创建表
        sql_text = '''CREATE TABLE IF NOT EXISTS database
                   (Name TEXT,
                    ID NUMBER,
                    Gender TEXT,
                    Grade NUMBER,
                    Phone NUMBER,
                    Major TEXT,
                    Address TEXT
                    );'''
        # 执行sql语句
        self.cursor.execute(sql_text)
        # 刷新Table UI
        self.refresh_table()
        # 连接鼠标点击事件
        self.clickflag = False
        self.current_row = -1
        self.current_row_sq = -1
        self.tableWidget.cellClicked.connect(self.handle_cell_clicked)
        self.tableWidget.itemChanged.connect(self.ChangeDatabase)
        self.tableWidget.doubleClicked.connect(self.flagset)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        """
        重写QWidget类的closeEvent方法，在窗口被关闭的时候自动触发
        """
        reply = QtWidgets.QMessageBox.question(self, '提示', "确认退出吗？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            super().closeEvent(event)  # 先添加父类的方法，以免导致覆盖父类方法（这是重点！！！）
            # 关闭游标
            self.cursor.close()
            # 关闭连接
            self.conn.close()
            event.accept()
        else:
            event.ignore()

    def flagset(self):
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.AllEditTriggers)
        self.clickflag = True

    def handle_cell_clicked(self, row, column):
        self.current_row = self.tableWidget.currentRow()
        item = self.tableWidget.item(self.current_row, 1)  # 取唯一标识符ID
        # 查询选中的ROWID
        self.cursor.execute("SELECT ROWID, * FROM database WHERE ID = ?", (int(item.text()),))
        results = self.cursor.fetchall()
        for result in results:
            self.current_row_sq = result['ROWID']

    def openDialog(self):
        insert_window = insert_dialog(self)
        insert_window.exec_()

    def AddDatabase(self, StudentInfo):
        data = [(StudentInfo.Name, int(StudentInfo.ID), StudentInfo.Gender, int(StudentInfo.Grade), int(StudentInfo.Phone), StudentInfo.Major, StudentInfo.Addr )]
        self.cursor.executemany('INSERT INTO database VALUES (?,?,?,?,?,?,?)', data)
        self.conn.commit()
        self.refresh_table()

    def ClearDatabase(self):
        self.cursor.execute("DELETE FROM database")
        self.conn.commit()
        self.refresh_table()

    def DeleteDatabase(self):
        self.cursor.execute("DELETE FROM database WHERE ROWID = ?", (self.current_row_sq, ))
        # 执行 VACUUM 命令
        self.conn.commit()
        self.cursor.execute("VACUUM")
        self.conn.commit()
        self.tableWidget.removeRow(self.current_row)
        # self.refresh_table()

    def SearchDatabase(self, value):
        if value == 1:  # 按Name查询
            if self.plainTextEditName.toPlainText() is not '':
                self.cursor.execute("SELECT ROWID, * FROM database WHERE Name = ?", (self.plainTextEditName.toPlainText(),))
            else:
                self.refresh_table()
                return
        else:
            if self.plainTextEditID.toPlainText() is not '':
                self.cursor.execute("SELECT ROWID, * FROM database WHERE ID = ?", (int(self.plainTextEditID.toPlainText()), ))
            else:
                self.refresh_table()
                return
        results = self.cursor.fetchall()
        if results is None:
            QMessageBox.warning(self, '警告', '查询为空！')
            return None
        search_list = []   # 存放搜寻所有行号的列表
        # 检查查询结果
        for result in results:
            rowid = result[0]
            search_list.append(rowid - 1)
        # 找到暂时删除的其他行
        all_list = range(self.tableWidget.rowCount())
        set1 = set(all_list)
        set2 = set(search_list)
        complement = set1 - set2  # 获取 list1 相对于 list2 的补集
        complement_list = list(complement)  # 将补集转换为列表
        for i in sorted(complement_list, reverse=True):
            self.tableWidget.removeRow(i)

    def ChangeDatabase(self, item):
        if self.clickflag == True:
            self.clickflag = False  # 重置标志位
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)

            column = item.column()
            value = item.text()
            self.cursor.execute('SELECT * FROM database')
            col_name_list = [tuple[0] for tuple in self.cursor.description]
            if col_name_list[column] in ['ID', 'Grade', 'Phone']:
                value = int(value)
            # 执行 UPDATE 命令来修改数据
            query = "UPDATE database SET " + col_name_list[column] + "= ? WHERE ROWID = ?"
            data = (value, self.current_row_sq)
            self.cursor.execute(query, data)
            # 提交事务并关闭连接
            self.conn.commit()
            self.tableWidget.resizeColumnsToContents()


    def refresh_table(self):
        self.cursor.execute("SELECT * FROM database")
        data = self.cursor.fetchall()
        # 创建一个副本或拷贝的数据列表
        self.tableWidget.setRowCount(len(data))
        for row, record in enumerate(data):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
        self.tableWidget.resizeColumnsToContents()

class insert_dialog(QDialog, Ui_Dialog):
    """ 插入数据条目的子界面类
    继承parent:main_window
    Methods:
        send_data:读取textEdit中数据并通过parent的AddDatabase函数返回参数
    """
    def __init__(self, parent=None):
        super(insert_dialog, self).__init__(parent)
        self.setupUi(self)  # 创建窗体对象
        self.pushButtonOk.clicked.connect(self.send_data)
        self.pushButtonCancel.clicked.connect(self.reject)

    def send_data(self):
        student_info = StudentInfo(self.textEditName_2.toPlainText(), self.textEditID.toPlainText(), self.textEditGender.toPlainText(),
                                   self.textEditGrade_2.toPlainText(), self.textEditPhone_2.toPlainText(), self.textEditMajor_2.toPlainText(), self.textEditAddr.toPlainText())
        self.accept()
        self.parent().AddDatabase(student_info)


class StudentInfo:
    """ 学生基本信息类，方便界面之间统一传参、
        Name:  姓名 str
        ID:    学号 int
        Gender:性别 str
        Phone: 电话 int
        Addr:  地址 str
        Major: 专业 str
        Grade: 年级 int
    """
    def __init__(self, Name, ID, Gender, Grade, Phone, Major, Addr):
        self.Name = Name
        self.ID = ID
        self.Gender = Gender
        self.Phone = Phone
        self.Addr = Addr
        self.Major = Major
        self.Grade = Grade

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 自适应分辨率
    app = QtWidgets.QApplication(sys.argv)
    window = login_window()
    window.show()
    sys.exit(app.exec_())
