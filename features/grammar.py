#!/usr/bin/python3
# -*- coding: utf-8 -*-
tree_list = []
def isSymble(str, node):
    dic_tmp = node.get_dic()
    if str not in dic_tmp:
        return False
    else:
        if dic_tmp[str] >= 18:
            return True
def errorProcess(word_list, should_be):
    print('wrong: ' + should_be + ' but ' + word_list[0])
    print(word_list)
    return
class Node:
    def __init__(self, name, father_id = 0):
        self.__name = name
        self.__id = len(tree_list)
        self.__father_id = father_id
        child_list = []
        child_list.clear()
        self.__child_list = child_list
        self.___dic = {}
        tree_list.append(self)

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_child(self):
        return self.__child_list
    def get_father(self):
        return self.__father_id
    def get_dic(self):
        return self.__dic

    def set_dic(self, dic):
        self.__dic = dic
    def set_father(self, father_id):
        self.__father_id = father_id

    def addChild(self, child_node):
        self.__child_list.append(child_node.get_id())
        child_node.set_father(self.__id)
        child_node.set_dic(self.__dic)
    def showTree(self):
        tree_result = ''
        tree_result = self.__name
        if len(self.__child_list) == 0:
            return tree_result + '\n'
        for child_node in self.__child_list:
            tree_result = tree_result + ' - ' + tree_list[child_node].showTree()
        return tree_result

def p(node, word_list):
    if len(word_list) == 0:
        return
    if word_list[0] == 'int' or word_list[0] == 'void':
        child_node_1 = Node('声明串')
        node.addChild(child_node_1)
        e1(child_node_1, word_list)
    else:
        errorProcess(word_list, 'int void')
        return
def e1(node, word_list):
    if word_list[0] == 'int' or word_list[0] == 'void':
        child_node_1 = Node('声明')
        node.addChild(child_node_1)
        e2(child_node_1, word_list)
        child_node_2 = Node('[声明]')
        node.addChild(child_node_2)
        ee2(child_node_2, word_list)
    else:
        errorProcess(word_list, 'int void')
        return
def e2(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('int')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('<ID>')
        node.addChild(child_node_1)
        e3(child_node_1, word_list)
        child_node_2 = Node('声明类型')
        node.addChild(child_node_2)
        e4(child_node_2, word_list)
    elif word_list[0] == 'void':
        child_node_0 = Node('void')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('<ID>')
        node.addChild(child_node_1)
        e3(child_node_1, word_list)
        child_node_2 = Node('函数声明')
        node.addChild(child_node_2)
        e5(child_node_2, word_list)
    else:
        errorProcess(word_list, 'int void')
        return
def ee2(node, word_list):
    if word_list[0] == 'int' or word_list[0] == 'void':
        child_node_1 = Node('声明')
        node.addChild(child_node_1)
        e2(child_node_1, word_list)
        child_node_2 = Node('[声明]')
        node.addChild(child_node_2)
        ee2(child_node_2, word_list)
    elif word_list[0] == '#':
        return
    else:
        errorProcess(word_list, 'int void')
        return
def e3(node, word_list):
    if isSymble(word_list[0], node) == False:
        errorProcess(word_list, '标识符')
        return
    child_node = Node(word_list[0])
    node.addChild(child_node)
    del word_list[0]
    return
def e4(node, word_list):
    if word_list[0] == ';':
        child_node_1 = Node('变量声明')
        node.addChild(child_node_1)
        e6(child_node_1, word_list)
    elif word_list[0] == '(':
        child_node_1 = Node('函数声明')
        node.addChild(child_node_1)
        e5(child_node_1, word_list)
    else:
        errorProcess(word_list, '; (')
        return
def e5(node, word_list):
    if word_list[0] == '(':
        child_node_0 = Node('(')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('形参')
        node.addChild(child_node_1)
        e7(child_node_1, word_list)
        child_node_2 = Node(')')
        node.addChild(child_node_2)
        del word_list[0]
        child_node_3 = Node('语句块')
        node.addChild(child_node_3)
        e8(child_node_3, word_list)
    else:
        errorProcess(word_list, '(')
        return
def e6(node, word_list):
    if word_list[0] == ';':
        child_node_0 = Node(';')
        node.addChild(child_node_0)
        del word_list[0]
    else:
        errorProcess(word_list, ';')
        return
def e7(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('参数列表')
        node.addChild(child_node_0)
        e9(child_node_0, word_list)
    elif word_list[0] == 'void':
        child_node_0 = Node('void')
        node.addChild(child_node_0)
        del word_list[0]
    else:
        errorProcess(word_list, 'int void')
        return
def e8(node, word_list):
    if word_list[0] == '{':
        child_node_0 = Node('{')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('内部声明')
        node.addChild(child_node_1)
        e11(child_node_1, word_list)
        child_node_2 = Node('语句串')
        node.addChild(child_node_2)
        e12(child_node_2, word_list)
        if word_list[0] != '}':
            errorProcess(word_list, '}')
            return
        child_node_3 = Node(word_list[0])
        node.addChild(child_node_3)
        del word_list[0]
    else:
        errorProcess(word_list, '{')
        return
def e9(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('参数')
        node.addChild(child_node_0)
        e10(child_node_0, word_list)
        child_node_1 = Node('[参数]')
        node.addChild(child_node_1)
        ee10(child_node_1, word_list)
    else:
        errorProcess(word_list, 'int')
        return
def e10(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('int')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('标识符')
        node.addChild(child_node_1)
        processSymble(child_node_1, word_list)
    else:
        errorProcess(word_list, 'int')
        return
def ee10(node, word_list):
    if word_list[0] == ',':
        child_node_0 = Node(',')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('参数')
        node.addChild(child_node_1)
        e10(child_node_1, word_list)
        child_node_2 = Node('[参数]')
        node.addChild(child_node_2)
        ee10(child_node_2, word_list)
    elif word_list[0] == ')':
        return
    else:
        errorProcess(word_list, ', )')
        return
def e11(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('内部变量声明')
        node.addChild(child_node_0)
        e13(child_node_0, word_list)
        child_node_1 = Node('[内部变量声明]')
        node.addChild(child_node_1)
        ee13(child_node_1, word_list)
    elif word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] == 'return' or isSymble(word_list[0], node):
        return
    else:
        errorProcess(word_list, 'int if whild return')
        return
def e12(node, word_list):
    if word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] =='return' or isSymble(word_list[0], node):
        child_node_0 = Node('语句')
        node.addChild(child_node_0)
        e14(child_node_0, word_list)
        child_node_1 = Node('[语句]')
        node.addChild(child_node_1)
        ee14(child_node_1, word_list)
    else:
        errorProcess(word_list, 'if while return 标识符')
        return
def e13(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('标识符')
        node.addChild(child_node_1)
        processSymble(child_node_1, word_list)
        if isSymble(word_list[0], node) == False:
            errorProcess(word_list, '标识符')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
    else:
        errorProcess(word_list, 'int')
        return
def ee13(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node('内部变量声明')
        node.addChild(child_node_0)
        e13(child_node_0, word_list)
        child_node_1 = Node('[内部变量声明]')
        node.addChild(child_node_1)
        ee13(child_node_1, word_list)
    elif word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] == 'return' or isSymble(word_list[0], node):
        return
    else:
        errorProcess(word_list, 'int if while return')
        return
def e14(node, word_list):
    if word_list[0] == 'if':
        child_node_0 = Node('if语句')
        node.addChild(child_node_0)
        e15(child_node_0, word_list)
    elif word_list[0] == 'while':
        child_node_0 = Node('while语句')
        node.addChild(child_node_0)
        e16(child_node_0, word_list)
    elif word_list[0] == 'return':
        child_node_0 = Node('return语句')
        node.addChild(child_node_0)
        e17(child_node_0, word_list)
    elif isSymble(word_list[0], node):
        child_node_0 = Node('赋值语句')
        node.addChild(child_node_0)
        e18(child_node_0, word_list)
    else:
        errorProcess(word_list, 'if while return b')
        return
def ee14(node, word_list):
    if word_list[0] == '}':
        return
    elif word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] == 'return' or isSymble(word_list[0], node):
        child_node_0 = Node('语句')
        node.addChild(child_node_0)
        e14(child_node_0, word_list)
        child_node_1 = Node('[语句]')
        node.addChild(child_node_1)
        ee14(child_node_1, word_list)
    else:
        errorProcess(word_list, '} if while return b')
        return
def e15(node, word_list):
    if word_list[0] == 'if':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        if word_list[0] != '(':
            errorProcess(word_list, 'if')
            return
        child_node_1 = Node(word_list[0])
        node.addChild(child_node_1)
        del word_list[0]
        child_node_2 = Node('表达式')
        node.addChild(child_node_2)
        e19(child_node_2, word_list)
        if word_list[0] != ')':
            errorProcess(word_list, ')')
            return
        child_node_3 = Node(word_list[0])
        node.addChild(child_node_3)
        del word_list[0]
        child_node_4 = Node('语句块')
        node.addChild(child_node_4)
        e8(child_node_4, word_list)
        child_node_5 = Node('else语句')
        node.addChild(child_node_5)
        s2(child_node_5, word_list)
    else:
        errorProcess(word_list, 'if')
        return
def e16(node, word_list):
    if word_list[0] == 'while':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        if word_list[0] != '(':
            errorProcess(word_list, 'while')
            return
        child_node_1 = Node(word_list[0])
        node.addChild(child_node_1)
        del word_list[0]
        child_node_2 = Node('表达式')
        node.addChild(child_node_2)
        e19(child_node_2, word_list)
        if word_list[0] != ')':
            errorProcess(word_list, ')')
            return
        child_node_3 = Node(word_list[0])
        node.addChild(child_node_3)
        del word_list[0]
        child_node_4 = Node('语句块')
        node.addChild(child_node_4)
        e8(child_node_4, word_list)
    else:
        errorProcess(word_list, 'while')
        return
def e17(node, word_list):
    if word_list[0] == 'return':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('表达式')
        node.addChild(child_node_1)
        s1(child_node_1, word_list)
        if word_list[0] != ';':
            errorProcess(word_list, ';')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
    else:
        errorProcess(word_list, 'return')
        return
def e18(node, word_list):
    if isSymble(word_list[0], node):
        child_node_0 = Node('标识符')
        node.addChild(child_node_0)
        processSymble(child_node_0, word_list)
        if word_list[0] != '=':
            errorProcess(word_list, '=')
            return
        child_node_1 = Node(word_list[0])
        node.addChild(child_node_1)
        del word_list[0]
        child_node_2 = Node('表达式')
        node.addChild(child_node_2)
        e19(child_node_2, word_list)
        if word_list[0] != ';':
            errorProcess(word_list, ';')
            return
        child_node_3 = Node(word_list[0])
        node.addChild(child_node_3)
        del word_list[0]
    else:
        errorProcess(word_list, 'b')
        return
def e19(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('加法表达式')
        node.addChild(child_node_0)
        e20(child_node_0, word_list)
        child_node_1 = Node('[加法表达式]')
        node.addChild(child_node_1)
        ee20(child_node_1, word_list)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee19(node, word_list):
    if word_list[0] == ',':
        child_node_0 = Node(',')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('表达式')
        node.addChild(child_node_1)
        e19(child_node_1, word_list)
        child_node_2 = Node('[表达式]')
        node.addChild(child_node_2)
        ee19(child_node_2, word_list)
    elif word_list[0] == ')':
        return
    else:
        errorProcess(word_list, ', ) e19')
        return
def e20(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('项')
        node.addChild(child_node_0)
        e21(child_node_0, word_list)
        child_node_1 = Node('[项]')
        node.addChild(child_node_1)
        ee21(child_node_1, word_list)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee20(node, word_list):
    if word_list[0] == ';' or word_list[0] == ')' or word_list[0] == ',':
        return
    elif word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('加法表达式')
        node.addChild(child_node_1)
        e20(child_node_1, word_list)
        child_node_2 = Node('[加法表达式]')
        node.addChild(child_node_2)
        ee20(child_node_2, word_list)
    else:
        errorProcess(word_list, '; ) 算符')
        return
def e21(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('因子')
        node.addChild(child_node_0)
        e22(child_node_0, word_list)
        child_node_1 = Node('[因子]')
        node.addChild(child_node_1)
        ee22(child_node_1, word_list)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee21(node, word_list):
    if word_list[0] == ')' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==' or word_list[0] == ';' or word_list[0] == ',':
        return
    elif word_list[0] == '+' or word_list[0] == '-':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('项')
        node.addChild(child_node_1)
        e21(child_node_1, word_list)
        child_node_2 = Node('[项]')
        node.addChild(child_node_2)
        ee21(child_node_2, word_list)
    else:
        errorProcess(word_list, ') 算符 + -')
        return
def e22(node, word_list):
    if word_list[0] == '(':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('表达式')
        node.addChild(child_node_1)
        e19(child_node_1, word_list)
        if word_list[0] != ')':
            errorProcess(word_list, ')')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
    elif word_list[0].isdigit():
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
    elif isSymble(word_list[0], node):
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node(word_list[1])
        node.addChild(child_node_1)
        e23(child_node_1, word_list)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee22(node, word_list):
    if word_list[0] == ')' or word_list[0] == '+' or word_list[0] == '-' or word_list[0] == ';' or word_list[0] == ',' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        return
    elif word_list[0] == '*' or word_list[0] == '/':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('因子')
        node.addChild(child_node_1)
        e22(child_node_1, word_list)
        child_node_2 = Node('[因子]')
        node.addChild(child_node_2)
        ee22(child_node_2, word_list)
    else:
        errorProcess(word_list, ') + - * /')
        return
def e23(node, word_list):
    if word_list[0] == ')' or word_list[0] == '+' or word_list[0] == '-' or word_list[0] == '*' or word_list[0] == '/' or word_list[0] == ';' or word_list[0] == ',' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        return
    elif word_list[0] == '(':
        child_node_0 = Node('call')
        node.addChild(child_node_0)
        e24(child_node_0, word_list)
    else:
        errorProcess(word_list, '( ) + - * /')
        return
def e24(node, word_list):
    if word_list[0] == '(':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('实参')
        node.addChild(child_node_1)
        e27(child_node_1, word_list)
        if word_list[0] != ')':
            errorProcess(word_list, ')')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
    else:
        errorProcess(word_list, '(')
        return
def e25(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('表达式')
        node.addChild(child_node_0)
        e19(child_node_0, word_list)
        child_node_1 = Node('[表达式]')
        node.addChild(child_node_1)
        ee19(child_node_1, word_list)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def e27(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('实参列表')
        node.addChild(child_node_0)
        e25(child_node_0, word_list)
    elif word_list[0] == ')':
        return
    else:
        errorProcess(word_list, '( 数字 b')
        return
def s1(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('表达式')
        node.addChild(child_node_0)
        e19(child_node_0, word_list)
    elif word_list[0] == ';':
        return
    else:
        errorProcess(word_list, '( 数字 b')
        return
def s2(node, word_list):
    if word_list[0] == '{' or word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] == 'return' or isSymble(word_list[0], node):
        return
    elif word_list[0] == 'else':
        child_node_0 = Node('else')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('语句块')
        node.addChild(child_node_1)
        e8(child_node_1, word_list)
    else:
        errorProcess(word_list, '{ if while return b')
        return
def processSymble(node, word_list):
    if isSymble(word_list[0], node):
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
def grammar(word_list, dic):
    tree_list.clear()
    begin_node = Node('programm')
    begin_node.set_dic(dic)
    p(begin_node, word_list)
    result_tree = begin_node.showTree()
    output_result = ''
    for node in tree_list:
        # print(node.get_name(), node.get_id(), node.get_child())
        output_result = output_result + node.get_name() + ' ' + str(node.get_id()) + ' ['
        for i in node.get_child():
            output_result = output_result + str(i) + ', '
        output_result = output_result + '] \n'
    f = open('grammar_tree', 'w')
    f.write(result_tree)
    f.close()
    return output_result
