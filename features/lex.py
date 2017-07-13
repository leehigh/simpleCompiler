#!/usr/bin/python3
# -*- coding: utf-8 -*-

'词法分析'

__author__ = 'Leehigh'

def lex(code):
    dic = { 'int': 1, 'void': 2, ',': 3, ';': 4, '{': 5, '}': 6, '(': 7, ')': 8, 'if': 9,
            'while': 10, 'return': 11, '=': 12, '==': 12, '>': 12, '<': 12, '>=': 12, '<=': 12,
            '!=': 12, 'else': 13, '+': 14, '-': 15,
            '*': 16, '/': 17, '#': 18}
    dic_num = 18
    result = ''
    buff = ''
    flag = 0
    word_list = []
    word_list.clear()
    for i in range( len(code)):
        if ( code[i] == '#'):
            word_list.append('#')
            break
        if ( len(buff) == 0):
            buff = buff + code[i]
            continue

        # 缓冲区内结束条件:
        #     下一个字符为空格或换行
        #     下一个字符为界符或符号
        #     当前缓冲区为保留符号

        if ( ( code[i] in dic and dic[code[i]] <= 18) or code[i] == ' ' or code[i] == '\n'
            or buff == '(' or buff == '{' or buff == ')' or buff == '}' or buff == '='
            or buff == ',' or buff == ';' or buff == '+' or buff == '-' or buff == '*'
            or buff == '/' or buff == '>' or buff == '<' or buff == '!='
            or buff == '>=' or buff == '<=' or buff == '==' ):

            # 对缓存区中的字符串进行处理
            if ( buff == '>' or buff == '<' or buff == '='):
                if ( code[ i] == '='):
                    buff = buff + code[i]
                    continue
            # 去空格换行

            buff = "".join(buff.split())

            if ( len(buff) == 0):
                buff = buff + code[i]
                continue

            # 不是数字,则为保留字或标识符
            if ( buff.isdigit() == False):
                # 判断缓冲区字符串第一个字符是否为数字 是则出错
                if ( buff[0] >= '0' and buff[0] <= '9'):
                    return buff + ' ' + 'error', [], {}
                # 不是则为保留字或标识符
                else:
                    if ( buff not in dic):
                        dic_num = dic_num + 1
                        dic[ buff] = dic_num
                    result = result + '<  %s  ,  %d  > \n' % ( buff.center( 20 - len(buff), ' '), dic[buff])
                    word_list.append(buff)

            # 是数字
            else:
                result = result + '<  %s  ,  %d  > \n' % ( buff.center( 20 - len(buff), ' '), 0)
                word_list.append(buff)

            buff = ''

        buff = buff + code[i]

    return result, word_list, dic
