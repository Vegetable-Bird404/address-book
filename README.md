# 学生通讯录管理系统 基于PYQT5和Sqlite3 

## 实现基本功能

- 添加学生地址 手机号 性别等信息

- 管理信息包括增加 删除 修改 按不同信息查找

- 导出信息到PDF文件



```
insert_window = InsertDialog(self)

class InsertDialog(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(insert_dialog, self).__init__(parent)
```

```
super(main_window, self).__init__()
```





ROWID累积 绝对索引 

刷新self.cursor.execute("VACUUM")

获得相对索引

 
