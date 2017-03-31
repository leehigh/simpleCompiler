#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import ( QLabel, QApplication, QWidget, QPushButton, QTextEdit, QGridLayout, QFileDialog)
from features import ( lex, grammar, semantic, intermediate, final)
# The script engine has some components, include symbol table, lexical analyzer, parser, semantic checker, intermediate code generator, optimizer, code generator, virtual machine

class demo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # 按钮
        sourcecode = QLabel('<h2 style="color:orange;">待分析源码:</font></h2>')
        resultshow = QLabel('<h2 style="color:grey;">分析结果:</font></h2>')

        openfile = QPushButton( '打开文件', self)
        openfile.resize(openfile.sizeHint())

        lexical = QPushButton( '词法分析', self)
        lexical.resize(lexical.sizeHint())

        grammar = QPushButton( '语法分析', self)
        grammar.resize(grammar.sizeHint())

        semantic = QPushButton('语义分析', self)
        semantic.resize(semantic.sizeHint())

        intermediate = QPushButton('中间代码', self)
        intermediate.resize(intermediate.sizeHint())

        final = QPushButton('最终结果', self)
        final.resize(final.sizeHint())

        self.codeEdit = QTextEdit(self)
        self.resultEdit = QTextEdit(self)
        self.resultEdit.setReadOnly(True)
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(sourcecode, 0, 0)
        grid.addWidget(resultshow, 0, 3)
        grid.addWidget(self.codeEdit, 1, 0, 1, 3)
        grid.addWidget(self.resultEdit, 1, 3, 1, 3)
        grid.addWidget(openfile, 2, 0)
        grid.addWidget(lexical, 2, 1)
        grid.addWidget(grammar, 2, 2)
        grid.addWidget(semantic, 2, 3)
        grid.addWidget(intermediate, 2, 4)
        grid.addWidget(final, 2, 5)
        openfile.clicked.connect(self.buttonClicked)
        lexical.clicked.connect(self.buttonClicked)
        grammar.clicked.connect(self.buttonClicked)
        semantic.clicked.connect(self.buttonClicked)
        intermediate.clicked.connect(self.buttonClicked)
        final.clicked.connect(self.buttonClicked)
        self.resize( 809, 500)
        self.setLayout(grid)
        self.show()
        self.setWindowTitle('厉害的编译器')

    def buttonClicked(self):
        sender = self.sender()
        a = self.codeEdit.toPlainText()

        lexText = lex.lex(a)
        grammarText = grammar.grammar(a)
        semanticText = semantic.semantic(a)
        intermediateText = intermediate.intermediate(a)
        finalText = final.final(a)

        if sender.text() == '打开文件':
            fname = QFileDialog.getOpenFileName(self, 'open file', '.')
            if fname[0]:
                f = open(fname[0], 'r')
                with f:
                    data = f.read()
                    self.codeEdit.setText(data)
        elif sender.text() == '词法分析':
            self.resultEdit.setText(lexText)
        elif sender.text() == '语法分析':
            self.resultEdit.setText(grammarText)
        elif sender.text() == '语义分析':
            self.resultEdit.setText(semanticText)
        elif sender.text() == '中间代码':
            self.resultEdit.setText(intermediateText)
        elif sender.text() == '最终结果':
            self.resultEdit.setText(finalText)

# if __name__ == '__main__':
app = QApplication(sys.argv)
demo = demo()
sys.exit(app.exec_())
