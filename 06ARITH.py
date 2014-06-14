#!/usr/bin/env python3

'''
ARITH  #0.93 (!0.66)

One part of the new WAP portal is also a calculator computing expressions with very long numbers. To make the output look better, the result is formated the same way as is it usually used with manual calculations.

Your task is to write the core part of this calculator. Given two numbers and the requested operation, you are to compute the result and print it in the form specified below. With addition and subtraction, the numbers are written below each other. Multiplication is a little bit more complex: first of all, we make a partial result for every digit of one of the numbers, and then sum the results together.

Input
There is a single positive integer T on the first line of input (equal to about 1000). It stands for the number of expressions to follow. Each expression consists of a single line containing a positive integer number, an operator (one of +, - and *) and the second positive integer number. Every number has at most 500 digits. There are no spaces on the line. If the operation is subtraction, the second number is always lower than the first one. No number will begin with zero.

Output
For each expression, print two lines with two given numbers, the second number below the first one, last digits (representing unities) must be aligned in the same column. Put the operator right in front of the first digit of the second number. After the second number, there must be a horizontal line made of dashes (-).

For each addition or subtraction, put the result right below the horizontal line, with last digit aligned to the last digit of both operands.

For each multiplication, multiply the first number by each digit of the second number. Put the partial results one below the other, starting with the product of the last digit of the second number. Each partial result should be aligned with the corresponding digit. That means the last digit of the partial product must be in the same column as the digit of the second number. No product may begin with any additional zeros. If a particular digit is zero, the product has exactly one digit -- zero. If the second number has more than one digit, print another horizontal line under the partial results, and then print the sum of them.

There must be minimal number of spaces on the beginning of lines, with respect to other constraints. The horizontal line is always as long as necessary to reach the left and right end of both numbers (and operators) directly below and above it. That means it begins in the same column where the leftmost digit or operator of that two lines (one below and one above) is. It ends in the column where is the rightmost digit of that two numbers. The line can be neither longer nor shorter than specified.

Print one blank line after each test case, including the last one.

Example

Sample Input:

4
12345+67890
324-111
325*4405
1234*4

Sample Output:

 12345
+67890
------
 80235

 324
-111
----
 213

    325
  *4405
  -----
   1625
     0
 1300
1300
-------
1431625

1234
  *4
----
4936

'''

import re

#0.93 with more logic optimization
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

#str.rjust(width) | 1.02 is faster than {0:>{1}}.format(str, width) | 1.27
#1.02 change rtn from list to str

#1.23 eliminate "eval" (both danger and inefficient)
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

#3.11 original version
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

def calc_file_list_eval(expr):
    res = eval(expr)
    rtn = []
    op1, op, op2 = list(filter(None, re.split('(\w+)',expr)))
    
    width = max(len(op1), len(op2)+1, len(str(res)))

    if op == '+' or op == '-':
        dash = '-' * max(len(op2)+1, len(str(res)))
        rtn = [op1.rjust(width,'.'), (op+op2).rjust(width,'.'), dash.rjust(width,'.'), str(res).rjust(width,'.')]
    else: # op == '*'
        dash = '-' * max(len(op2)+1, len(str(eval(op1+op+op2[-1]))))
        rtn = [op1.rjust(width,'.'), (op+op2).rjust(width,'.'), dash.rjust(width,'.')]
        
        for index, digit in enumerate(op2[::-1]):
            rtn.append(str(eval(op1+op+digit)).rjust(width - index,'.') + ' ' * index)
        
        if len(op2) > 1:
            dashM = '-' * max(len(str(res)), len(str(eval(op1+op+op2[0]))))
            rtn.append(dashM.rjust(width,'.'))
            rtn.append(str(res).rjust(width,'.'))
    
    return rtn


if __name__ == '__main__':
    
    # Test
    # testsuite = ["12345+67890","324-111","325*4405","1234*4","999*101"]
    # for test in testsuite:
    #     print(calc(test))

    # Test with rtn as list
    # for test in testsuite:
    #     for line in calc(test):
    #         print(line)
    #     print("")

    # Test with file
    # fi = open("input", 'r')
    # fo = open("output", 'w')
    # for test in fi.readlines():
    #     for line in calc2(test.rstrip('\n')):
    #         fo.write(line+'\n')
    #     fo.write("\n")
    # fi.close()
    # fo.close()

    T = int(input())
    for _t in range(T):
        print(calc(input()))

'''
file test input

2*444444444
111+22
1000-1
444-444
555+555
33555+555
4+999
1+10000000
2*22222
112*16
12*116
11876411*226
99+1
101010*10101
9999+9
1+1
5+6
8-3
11-2
100000000-1
100000000+1
9+9999999999
1000+999999999999999999999993
1*1
2*2
1*10000001111
8888888*999999
10000-1
100001-1
10000-9999
451*1
1*451
6*2011
9999+9999
9999-9998 
'''