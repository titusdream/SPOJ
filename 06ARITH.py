#!/usr/bin/env python3

'''
ARITH  

> 0.93 [0.66]
> eval elimination
'''

import re

# ---------- 0.93 ---------- with more logic optimization
def calc(expr):
    
    rtn = ""
    op1, op, op2 = list(filter(None, re.split('(\w+)',expr)))
    op1i = int(op1)
    op2i = int(op2)

    if op == '+':
        res = op1i + op2i
    elif op == '-':
        res = op1i - op2i
    else: # op == '*'
        res = op1i * op2i

    width = max(len(op2)+1, len(str(res)))

    if op == '*':
        dash = '-' * max(len(op2)+1, len(str(op1i * int(op2[-1]))))
        rtn =  op1.rjust(width) + "\n" + (op+op2).rjust(width) + "\n" + dash.rjust(width) + "\n"
        
        for index, digit in enumerate(op2[::-1]):
            rtn += str(op1i * int(digit)).rjust(width - index) + "\n"
        
        if len(op2) > 1:
            dashM = '-' * max(len(str(res)), len(str(op1i * int(op2[0]))))
            rtn += dashM.rjust(width) + "\n"
            rtn += str(res).rjust(width) + "\n"
    else: # op == '+' or op == '-'
        dash = '-' * width
        rtn = op1.rjust(width) + "\n" + (op+op2).rjust(width) + "\n" + dash.rjust(width) + "\n" + str(res).rjust(width) + "\n"
    
    return rtn

# str.rjust(width) is faster than {0:>{1}}.format(str, width) (1.27)
# ---------- 1.02 ---------- change rtn from list to str

# ---------- 1.23 ---------- eliminate "eval" (both danger and inefficient)
def calc_list(expr):
    rtn = []
    op1, op, op2 = list(filter(None, re.split('(\w+)',expr)))
    op1i = int(op1)
    op2i = int(op2)

    if op == '+' or op == '-':
        if op == '+':
            res = op1i + op2i
        else:
            res = op1i - op2i
        width = max(len(op1), len(op2)+1, len(str(res)))
        dash = '-' * max(len(op2)+1, len(str(res)))
        rtn = [op1.rjust(width), (op+op2).rjust(width), dash.rjust(width), str(res).rjust(width)]
    else: # op == '*'
        res = op1i * op2i
        width = max(len(op1), len(op2)+1, len(str(res)))
        dash = '-' * max(len(op2)+1, len(str(op1i * int(op2[-1]))))
        rtn = [op1.rjust(width), (op+op2).rjust(width), dash.rjust(width)]
        
        for index, digit in enumerate(op2[::-1]):
            rtn.append(str(op1i * int(digit)).rjust(width - index) + ' ' * index)
        
        if len(op2) > 1:
            dashM = '-' * max(len(str(res)), len(str(op1i * int(op2[0]))))
            rtn.append(dashM.rjust(width))
            rtn.append(str(res).rjust(width))

    return rtn

# ---------- 3.11 ---------- original version
def calc_list_eval(expr):
    res = eval(expr)
    rtn = []
    op1, op, op2 = list(filter(None, re.split('(\w+)',expr)))
    
    width = max(len(op1), len(op2)+1, len(str(res)))

    if op == '+' or op == '-':
        dash = '-' * max(len(op2)+1, len(str(res)))
        rtn = [op1.rjust(width), (op+op2).rjust(width), dash.rjust(width), str(res).rjust(width)]
    else: # op == '*'
        dash = '-' * max(len(op2)+1, len(str(eval(op1+op+op2[-1]))))
        rtn = [op1.rjust(width), (op+op2).rjust(width), dash.rjust(width)]
        
        for index, digit in enumerate(op2[::-1]):
            rtn.append(str(eval(op1+op+digit)).rjust(width - index) + ' ' * index)
        
        if len(op2) > 1:
            dashM = '-' * max(len(str(res)), len(str(eval(op1+op+op2[0]))))
            rtn.append(dashM.rjust(width))
            rtn.append(str(res).rjust(width))
    
    return rtn

if __name__ == '__main__':

    T = int(input())
    for _t in range(T):
        print(calc(input()))
