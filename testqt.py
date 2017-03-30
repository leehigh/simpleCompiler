#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import ( QApplication, QWidget, QPushButton, QTextEdit, QGridLayout, QFileDialog)

class demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 按钮
        openfile = QPushButton( '打开文件', self)
        openfile.resize(openfile.sizeHint())
        cifa = QPushButton( '词法分析', self)
        cifa.resize(cifa.sizeHint())
        yufa = QPushButton( '语法分析', self)
        yufa.resize(yufa.sizeHint())
        yuyi = QPushButton('语义分析', self)
        yuyi.resize(yuyi.sizeHint())
        zhongjian = QPushButton('中间代码', self)
        zhongjian.resize(zhongjian.sizeHint())
        final = QPushButton('最终结果', self)
        final.resize(final.sizeHint())
        self.codeEdit = QTextEdit(self)

        grid = QGridLayout()
        grid.setSpacing(20)
        grid.addWidget(self.codeEdit, 0, 0, 6, 3)
        grid.addWidget(openfile, 0, 4)
        grid.addWidget(cifa, 1, 4)
        grid.addWidget(yufa, 2, 4)
        grid.addWidget(yuyi, 3, 4)
        grid.addWidget(zhongjian, 4, 4)
        grid.addWidget(final, 5, 4)
        openfile.clicked.connect(self.buttonClicked)
        cifa.clicked.connect(self.buttonClicked)
        yufa.clicked.connect(self.buttonClicked)
        yuyi.clicked.connect(self.buttonClicked)
        zhongjian.clicked.connect(self.buttonClicked)
        final.clicked.connect(self.buttonClicked)
        self.resize( 485.4, 300)
        self.setLayout(grid)
        self.show()
        self.setWindowTitle('厉害的编译器')

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == '打开文件':
            fname = QFileDialog.getOpenFileName(self, 'open file', '.')
            if fname[0]:
                f = open(fname[0], 'r')
                with f:
                    data = f.read()
                    self.codeEdit.setText(data)
        elif sender.text() == '词法分析':
            print(sender.text())
        elif sender.text() == '语义分析':
            pass
        elif sender.text() == '语义分析':
            pass
        elif sender.text() == '中间代码':
            pass
        elif sender.text() == '最终结果':
            pass
        # if sender.text() == openfile:
        # a = open('a.txt')
        # data = a.read()
        # self.codeEdit.setText(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = demo()
    sys.exit(app.exec_())
