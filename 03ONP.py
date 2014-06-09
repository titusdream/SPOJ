#!/usr/bin/env python

'''
ONP | Shunting-yard algorithm

Transform the algebraic expression with brackets into RPN form 
(Reverse Polish Notation). 
Two-argument operators: +, -, *, /, ^ (priority from the lowest to the highest),
brackets ( ). 
Operands: only letters: a,b,...,z. Assume that there is only one RPN form 
(no expressions like a*b*c).

Input
t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
(Text grouped in [ ] does not appear in the input file.)

Output
The expressions in RPN form, one per line.

Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
'''

'''
http://andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm
'''

# Associativity constants for operators
LEFT_ASSOC = 0
RIGHT_ASSOC = 1

# Supported operators
OPERATORS = {
    '+' : (0, LEFT_ASSOC),
    '-' : (0, LEFT_ASSOC),
    '*' : (5, LEFT_ASSOC),
    '/' : (5, LEFT_ASSOC),
    '%' : (5, LEFT_ASSOC),
    '^' : (10, RIGHT_ASSOC)
}

#Test if a certain token is operator
def isOperator(token):
    return token in OPERATORS.keys()

#Test the associativity type of a certain token
def isAssociative(token, assoc):
    if not isOperator(token):
        raise ValueError('Invalid token: %s' % token)
    return OPERATORS[token][1] == assoc

#Compare the precedence of two tokens
def cmpPrecedence(token1, token2):
    if not isOperator(token1) or not isOperator(token2):
        raise ValueError('Invalid tokens: %s %s' % (token1, token2))
    return OPERATORS[token1][0] - OPERATORS[token2][0]

#Transforms an infix expression to RPN
def infixToRPN(tokens):
    out = []
    stack = []
    #For all the input tokens [S1] read the next token [S2]
    for token in tokens:
        if isOperator(token):
            # If token is an operator (x) [S3]
            while len(stack) != 0 and isOperator(stack[-1]):
                # [S4]
                if (isAssociative(token, LEFT_ASSOC) and cmpPrecedence(token, stack[-1]) <= 0) or (isAssociative(token, RIGHT_ASSOC) and cmpPrecedence(token, stack[-1]) < 0):
                    # [S5] [S6]
                    out.append(stack.pop())
                    continue
                break
            # [S7]
            stack.append(token)
        elif token == '(':
            stack.append(token) # [S8]
        elif token == ')':
            # [S9]
            while len(stack) != 0 and stack[-1] != '(':
                out.append(stack.pop()) # [S10]
            stack.pop() # [S11]
        else:
            out.append(token) # [S12]
    while len(stack) != 0:
        # [S13]
        out.append(stack.pop())
    return out

if __name__ == '__main__':
    # Test:
    # input = "( 1 + 2 ) * ( 3 / 4 ) ^ ( 5 + 6 )".split(" ")
    # output = "".join(infixToRPN(input))
    # print output

    T = int(input())
    for _t in range(T): # idiom for an unused variable is a single underscore _
        print("".join(infixToRPN(list(input()))))


# though not specified in description, but all test inputs are fully parenthesized
# so in this case, a simplified version is available:
# operators = '+-*/^'
# operatorList = []
# for line in sys.stdin:
#     output =''
#     for c in line:
#         if c.isalpha():
#             output += c
#         elif c in operators :
#             operatorList.append(c)
#         elif c == ')':
#             output += operatorList.pop()
#     print(output)