#!/usr/bin/python3
# -*- coding: utf-8 -*-

# register_id start form 0
register_id = 0
# instruction_address start from 100
instruction_address = 100
# this list is used to build a tree.
# Every node in the tree is saved here.
# The index of the node is used as address, like pointers in c++.
tree_list = []
# a result str
inter_re = ''

# judge if the str is a Symble(标识符)
def isSymble(str, node):
    dic_tmp = node.get_dic()
    if str not in dic_tmp:
        return False
    else:
        if dic_tmp[str] >= 18:
            return True
# print error
def errorProcess(word_list, should_be):
    # # # print('wrong: ' + should_be + ' but ' + word_list[0])
    # # print(word_list)
    global inter_re
    inter_re = inter_re + ('wrong: ' + should_be + ' but ' + word_list[0] + '\n')
    return
#  define the node in a tree
class Node:
    def __init__(self, name, father_id = 0):
        self.__name = name
        # the index in tree_list
        self.__id = len(tree_list)
        # the father's index in list
        self.__father_id = father_id
        child_list = []
        child_list.clear()
        self.__child_list = child_list
        # the dic storage all the word in source code
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
    # three steps to addChild:
    #   1. add child node to child list
    #   2. set child node's father
    #   3. pass dictionary to child node
    def addChild(self, child_node):
        self.__child_list.append(child_node.get_id())
        child_node.set_father(self.__id)
        child_node.set_dic(self.__dic)
    # ugly tree
    def showTree(self):
        tree_result = ''
        tree_result = self.__name
        if len(self.__child_list) == 0:
            return tree_result + '\n'
        for child_node in self.__child_list:
            tree_result = tree_result + ' - ' + tree_list[child_node].showTree()
        return tree_result
# the begin node
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
        global instruction_address
        true_add = instruction_address
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
        false_add = instruction_address
        return true_add, false_add
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
        return
    else:
        errorProcess(word_list, 'if while return 标识符')
        return
def e13(node, word_list):
    if word_list[0] == 'int':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        if isSymble(word_list[0], node) == False:
            errorProcess(word_list, '标识符')
            return
        child_node_1 = Node('标识符')
        node.addChild(child_node_1)
        processSymble(child_node_1, word_list)
        if word_list[0] != ';':
            errorProcess(word_list, ';')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
        return
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
        return
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
        return
    elif word_list[0] == 'while':
        child_node_0 = Node('while语句')
        node.addChild(child_node_0)
        e16(child_node_0, word_list)
        return
    elif word_list[0] == 'return':
        child_node_0 = Node('return语句')
        node.addChild(child_node_0)
        e17(child_node_0, word_list)
        return
    elif isSymble(word_list[0], node):
        child_node_0 = Node('赋值语句')
        node.addChild(child_node_0)
        e18(child_node_0, word_list)
        return
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
        return
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
        global instruction_address
        # # print(str(instruction_address), ':', '(', 'j', ',', ',', 'false出口', ')')
        global inter_re
        inter_re = inter_re + (str(instruction_address) + ' ' + ':'+ ' ' + '('+ ' ' + 'j'+ ' ' + ','+ ' ' + ','+ ' ' + 'false出口' + ' ' +  ')'+ ' ' + '\n')
        instruction_address = instruction_address + 1
        child_node_4 = Node('语句块')
        node.addChild(child_node_4)
        true_add, false_add = e8(child_node_4, word_list)
        child_node_5 = Node('else语句')
        node.addChild(child_node_5)
        s2_re = s2(child_node_5, word_list)
        if s2_re == '':
            # print('以上true出口,false出口地址分别为:', true_add, false_add)
            inter_re = inter_re + ('以上true出口,false出口地址分别为:' + ' ' + str(true_add) + ' ' + str(false_add) +'\n')
        else:
            false_add = str(int(false_add) + 1)
            # print('以上true出口,false出口地址分别为:', true_add, false_add)
            inter_re = inter_re + ('以上true出口,false出口地址分别为:' + ' ' +  str(true_add) + ' ' +  str(false_add) + '\n')
        return
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
        global instruction_address
        global inter_re
        # print(str(instruction_address), ':', '(', 'j', ',', ',', 'false出口', ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'j' + ' ' +  ',' + ' ' +  ',' + ' ' +  'false出口' + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
        child_node_4 = Node('语句块')
        node.addChild(child_node_4)
        true_add, false_add = e8(child_node_4, word_list)
        # print('以上true出口,false出口地址分别为:', true_add, false_add)
        inter_re = inter_re + ('以上true出口,false出口地址分别为:' + ' ' +  str(true_add) + ' ' +  str(false_add) + '\n')
        return
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
        ss1 = s1(child_node_1, word_list)
        if word_list[0] != ';':
            errorProcess(word_list, ';')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
        global instruction_address
        global register_id
        global inter_re
        # print(str(instruction_address), ':', '(', 'RET', ',', ss1, ',', ',', ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'RET' + ' ' +  ',' + ' ' +  ss1 + ' ' +  ',' + ' ' +  ',' + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
    else:
        errorProcess(word_list, 'return')
        return
def e18(node, word_list):
    if isSymble(word_list[0], node):
        child_node_0 = Node('标识符')
        node.addChild(child_node_0)
        s1 = processSymble(child_node_0, word_list)
        if word_list[0] != '=':
            errorProcess(word_list, '=')
            return
        child_node_1 = Node(word_list[0])
        node.addChild(child_node_1)
        del word_list[0]
        child_node_2 = Node('表达式')
        node.addChild(child_node_2)
        s2 = e19(child_node_2, word_list)
        if word_list[0] != ';':
            errorProcess(word_list, ';')
            return
        child_node_3 = Node(word_list[0])
        node.addChild(child_node_3)
        del word_list[0]
        global instruction_address
        global register_id
        global inter_re
        # print(str(instruction_address), ':', '(', '=', ',', s2, ',', ',', s1, ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  '=' + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  ',' + ' ' +  s1 + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
    else:
        errorProcess(word_list, 'b')
        return
def e19(node, word_list):
    global instruction_address
    global inter_re
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('加法表达式')
        node.addChild(child_node_0)
        s1 = e20(child_node_0, word_list)
        child_node_1 = Node('[加法表达式]')
        node.addChild(child_node_1)
        sym, s2 = ee20(child_node_1, word_list)
        if sym == '':
            # # print(s1)
            return s1
        elif sym[0] == 'j':
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'true出口', ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'true出口' + ' ' +  ')' + '\n')
            instruction_address = instruction_address + 1
        else:
            global register_id
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return 'T' + str(register_id - 1)
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
        s1 = e19(child_node_1, word_list)
        child_node_2 = Node('[表达式]')
        node.addChild(child_node_2)
        ee19(child_node_2, word_list)
        global instruction_address
        global register_id
        global inter_re
        # print(str(instruction_address), ':', '(', 'push', ',', s1, ',', ',', 'stack', ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'push' + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  ',' + ' ' +  'stack' + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
        return s1
    elif word_list[0] == ')':
        return ''
    else:
        errorProcess(word_list, ', ) e19')
        return
def e20(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('项')
        node.addChild(child_node_0)
        s1 = e21(child_node_0, word_list)
        child_node_1 = Node('[项]')
        node.addChild(child_node_1)
        sym, s2 = ee21(child_node_1, word_list)
        if sym == '':
            return s1
        else:
            global instruction_address
            global register_id
            global inter_re
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')' +'\n')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return 'T' + str(register_id - 1)
        return
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee20(node, word_list):
    if word_list[0] == ';' or word_list[0] == ')' or word_list[0] == ',':
        return '', ''
    elif word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('加法表达式')
        node.addChild(child_node_1)
        s1 = e20(child_node_1, word_list)
        child_node_2 = Node('[加法表达式]')
        node.addChild(child_node_2)
        sym, s2 = ee20(child_node_2, word_list)
        if sym == '':
            return 'j' + child_node_0.get_name(), s1
        else:
            global instruction_address
            global inter_re
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'True', ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'True' + ' ' +  ')' +'\n')
            instruction_address = instruction_address + 1
            return 'j' + child_node_0.get_name(), 'zhenchukou'
        return
    else:
        errorProcess(word_list, '; ) 算符')
        return
def e21(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('因子')
        node.addChild(child_node_0)
        s1 = e22(child_node_0, word_list)
        child_node_1 = Node('[因子]')
        node.addChild(child_node_1)
        sym, s2 = ee22(child_node_1, word_list)
        if s2 == '':
            return s1
        else:
            global instruction_address
            global register_id
            global inter_re
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')' +'\n')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return 'T' + str(register_id - 1)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee21(node, word_list):
    if word_list[0] == ')' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==' or word_list[0] == ';' or word_list[0] == ',':
        return '', ''
    elif word_list[0] == '+' or word_list[0] == '-':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('项')
        node.addChild(child_node_1)
        s1 = e21(child_node_1, word_list)
        child_node_2 = Node('[项]')
        node.addChild(child_node_2)
        sym, s2 = ee21(child_node_2, word_list)
        if sym == '':
            return child_node_0.get_name(), s1
        else:
            global instruction_address
            global register_id
            global inter_re
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')' +'\n')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return child_node_0.get_name(), 'T' + str(register_id - 1)
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
        s1 = e19(child_node_1, word_list)
        if word_list[0] != ')':
            errorProcess(word_list, ')')
            return
        child_node_2 = Node(word_list[0])
        node.addChild(child_node_2)
        del word_list[0]
        return s1
    elif word_list[0].isdigit():
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        return child_node_0.get_name()
    elif isSymble(word_list[0], node):
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('FTYPE')
        node.addChild(child_node_1)
        s = e23(child_node_1, word_list)
        if s == '':
            return child_node_0.get_name()
        else:
            global instruction_address
            global register_id
            global inter_re
            # print(str(instruction_address), ':', '(', 'call', ',', child_node_0.get_name(), ',', ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'call' + ' ' +  ',' + ' ' +  child_node_0.get_name() + ' ' +  ',' + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')' +'\n')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return 'T' + str(register_id - 1)
    else:
        errorProcess(word_list, '( 数字 b')
        return
def ee22(node, word_list):
    if word_list[0] == ')' or word_list[0] == '+' or word_list[0] == '-' or word_list[0] == ';' or word_list[0] == ',' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        return '', ''
    elif word_list[0] == '*' or word_list[0] == '/':
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('因子')
        node.addChild(child_node_1)
        s1 = e22(child_node_1, word_list)
        child_node_2 = Node('[因子]')
        node.addChild(child_node_2)
        sym, s2 = ee22(child_node_2, word_list)
        if s2 == '':
            return child_node_0.get_name(), s1
        else:
            global instruction_address
            global register_id
            global inter_re
            # print(str(instruction_address), ':', '(', sym, ',', s1, ',', s2, ',', 'T' + str(register_id), ')')
            inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  sym + ' ' + ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  s2 + ' ' +  ',' + ' ' +  'T' + str(register_id) + ' ' +  ')' +'\n')
            register_id = register_id + 1
            instruction_address = instruction_address + 1
            return child_node_0.get_name(), 'T' + str(register_id - 1)
    else:
        errorProcess(word_list, ') + - * /')
        return
def e23(node, word_list):
    if word_list[0] == ')' or word_list[0] == '+' or word_list[0] == '-' or word_list[0] == '*' or word_list[0] == '/' or word_list[0] == ';' or word_list[0] == ',' or word_list[0] == '>' or word_list[0] == '>=' or word_list[0] == '<' or word_list[0] == '<=' or word_list[0] == '!=' or word_list[0] == '==':
        return ''
    elif word_list[0] == '(':
        child_node_0 = Node('call')
        node.addChild(child_node_0)
        s1 = e24(child_node_0, word_list)
        return 'call'
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
        s1 = e19(child_node_0, word_list)
        child_node_1 = Node('[表达式]')
        node.addChild(child_node_1)
        ee19(child_node_1, word_list)
        global instruction_address
        global register_id
        global inter_re
        # print(str(instruction_address), ':', '(', 'push', ',', s1, ',', ',', 'stack', ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'push' + ' ' +  ',' + ' ' +  s1 + ' ' +  ',' + ' ' +  ',' + ' ' +  'stack' + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
    else:
        errorProcess(word_list, '( 数字 b')
        return
def e27(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('实参列表')
        node.addChild(child_node_0)
        e25(child_node_0, word_list)
    elif word_list[0] == ')':
        return ''
    else:
        errorProcess(word_list, '( 数字 b')
        return
def s1(node, word_list):
    if word_list[0] == '(' or word_list[0].isdigit() or isSymble(word_list[0], node):
        child_node_0 = Node('表达式')
        node.addChild(child_node_0)
        s1 = e19(child_node_0, word_list)
        return s1
    elif word_list[0] == ';':
        return ''
    else:
        errorProcess(word_list, '( 数字 b')
        return
def s2(node, word_list):
    if word_list[0] == '{' or word_list[0] == 'if' or word_list[0] == 'while' or word_list[0] == 'return' or isSymble(word_list[0], node):
        return ''
    elif word_list[0] == 'else':
        global instruction_address
        global inter_re
        # print(str(instruction_address), ':', '(', 'j', ',', ',', '跳出else地址', ')')
        inter_re = inter_re + (str(instruction_address) + ' ' +  ':' + ' ' +  '(' + ' ' +  'j' + ' ' +  ',' + ' ' +  ',' + ' ' +  '跳出else地址' + ' ' +  ')' + '\n')
        instruction_address = instruction_address + 1
        child_node_0 = Node('else')
        node.addChild(child_node_0)
        del word_list[0]
        child_node_1 = Node('语句块')
        node.addChild(child_node_1)
        e8(child_node_1, word_list)
        # print('以上跳出else地址为:' + str(instruction_address))
        inter_re = inter_re + ('以上跳出else地址为:' + str(instruction_address) +'\n')
        return 'else'
    else:
        errorProcess(word_list, '{ if while return b')
        return
def processSymble(node, word_list):
    if isSymble(word_list[0], node):
        child_node_0 = Node(word_list[0])
        node.addChild(child_node_0)
        del word_list[0]
        return child_node_0.get_name()
def grammar(word_list, dic):
    tree_list.clear()
    begin_node = Node('programm')
    begin_node.set_dic(dic)
    p(begin_node, word_list)
    result_tree = begin_node.showTree()
    output_result = ''
    for node in tree_list:
        # # print(node.get_name(), node.get_id(), node.get_child())
        output_result = output_result + node.get_name() + ' ' + str(node.get_id()) + ' ['
        for i in node.get_child():
            output_result = output_result + str(i) + ', '
        output_result = output_result + '] \n'
    f = open('grammar_tree', 'w')
    f.write(result_tree)
    f.close()
    global inter_re
    fi = open('inter', 'w')
    fi.write(inter_re)
    fi.close()
    return output_result, inter_re
