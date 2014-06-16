#!/usr/bin/env python3

'''
ONP

> Shunting-yard algorithm  
> 0.26 [0.08]
'''

# ---------- 0.26 ---------- http://andreinc.net/2010/10/05/converting-infix-to-rpn-shunting-yard-algorithm

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

# Test if a certain token is operator
def isOperator(token):
    return token in OPERATORS.keys()

# Test the associativity type of a certain token
def isAssociative(token, assoc):
    return OPERATORS[token][1] == assoc

# Compare the precedence of two tokens
def cmpPrecedence(token1, token2):
    return OPERATORS[token1][0] - OPERATORS[token2][0]

# Transforms an infix expression to RPN
def infixToRPN(tokens):
    out = ""    # string operation is faster than list
    stack = []
    # For all the input tokens [S1] read the next token [S2]
    for token in tokens:
        if isOperator(token):
            # If token is an operator (x) [S3]
            while len(stack) != 0 and isOperator(stack[-1]):
                # [S4]
                if (isAssociative(token, LEFT_ASSOC) and cmpPrecedence(token, stack[-1]) <= 0) or (isAssociative(token, RIGHT_ASSOC) and cmpPrecedence(token, stack[-1]) < 0):
                    # [S5] [S6]
                    out += stack.pop()
                    continue
                break
            # [S7]
            stack.append(token)
        elif token == '(':
            stack.append(token) # [S8]
        elif token == ')':
            # [S9]
            while len(stack) != 0 and stack[-1] != '(':
                out += stack.pop() # [S10]
            stack.pop() # [S11]
        else:
            out += token # [S12]
    while len(stack) != 0:
        # [S13]
        out += stack.pop()
    return out

# ---------- 0.19 ---------- 
# though not specified in description, but all test inputs are fully parenthesized
# so in this case, a simplified version is available
def infixToRPN2(tokens):
    operators = '+-*/^'
    operatorList = []
    output =''
    for token in tokens:
        if token.isalpha():
            output += token
        elif token in operators:
            operatorList.append(token)
        elif token == ')':
            output += operatorList.pop()
    return output


if __name__ == '__main__':

    T = int(input())
    for _t in range(T): # idiom for an unused variable is a single underscore _
        print(infixToRPN(input()))
