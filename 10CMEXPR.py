#!/usr/bin/env python3

'''
CMEXPR

> Infix - Suffix exchange using stack or expression tree
> NOT possible for python to run within time requirement
> deque (fast removal of multiple items in a list)
'''

# ---------- 1.38 (local) ---------- a faster (simple, without right associative operator ^) suffix->infix(RPN) convertor (ref. 03ONP problem)
# http://hi.baidu.com/masterray/item/5fe4dee74a0e2e0d570f1d61

isp = {'$':0, '+':3, '-':3, '*':5, '/':5, '(':1}
icp = {'$':0, '+':2, '-':2, '*':4, '/':4, '(':6, ')':1}

def infix_to_suffix(infix):
    # use '$' to avoid stack length check every loop
    infix.append('$')
    stack = ['$']
    suffix = []

    for c in infix:
        # if c is a variable:
        if c.isalpha():
            suffix.append(c)
            continue

        # if c is an operator:
        # append all content between ()
        while icp[c] < isp[stack[-1]]:
            suffix.append(stack.pop())

        if icp[c] == isp[stack[-1]]:
            stack.pop()     # pop () or $$ (end of infix)
        else:
            stack.append(c)

    return suffix

def suffix_to_infix(suffix):
    stack = []

    for c in suffix:
        # if c is a variable:
        if c.isalpha():
            stack.append((c, 255))
            continue

        # if c is an operator:

        # right, priority_right, left, priority_left
        b, pb = stack.pop()
        a, pa = stack.pop()

        # compare to decide if brackets are needed for left/right 
        if isp[c] > pa:
            a = '(' + a + ')'
        if isp[c] > pb or isp[c] == pb and (c in '-/'):
            b = '(' + b + ')'

        stack.append((a + c + b, isp[c]))
    
    return stack[0][0]

# ---------- 1.42 (local) ---------- infix-suffix w/ stack (see above), suffix-infix w/ tree, "print" adapted from official c code

operator_priority = {'+' : (2, 2), '-' : (2, 1), '*' : (1, 1), '/' : (1, 0)}
 
class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
 
class ExressionTree(object):
    def __init__(self, root = None):
        self.__root = root

    def inorder(self, prior):
        return self.__inorder_helper(self.__root, prior)
         
    def __inorder_helper(self, node, prior):
        if node == None: return ""
        if node.value not in operator_priority.keys():
            return str(node)

        lpri, rpri = operator_priority[node.value]

        if lpri > prior: 
            return '('+self.__inorder_helper(node.left, lpri)+str(node)+self.__inorder_helper(node.right, rpri)+')'
        return self.__inorder_helper(node.left, lpri)+str(node)+self.__inorder_helper(node.right, rpri)
 
def create_expression_tree(infix):

    postfix = infix_to_suffix(infix)

    stack = []
 
    for char in postfix:
        if char not in operator_priority.keys():
            node = Node(char)  
            stack.append(node)
        else:
            right = stack.pop()
            left = stack.pop()
            node = Node(char, left, right)
            stack.append(node)
     
    return ExressionTree(stack.pop())

# ---------- 5.89 (local) ---------- original version

def necessary(before, inside, after):
    '''
    function to decide if the pair of brackets are necessary
    '''
    if (before in '-*' and inside == 'PM') or \
        (before == '/' and inside != 'NA') or \
        (inside == 'PM' and after in '*/'):
            return True

    return False

def simplify(string):
    from collections import deque

    left_bracket = deque()
    remove_bracket = deque()

    for i, l in enumerate(string):
        if l == '(':
            left_bracket.append(i)
        elif l == ')':
            lbpos = left_bracket.pop()  # corresponding left_bracket bracket position
            
            before = string[lbpos-1] if lbpos > 0 else '('
            after = string[i+1] if i+1 < len(string) else ')'

            pm = False
            md = False

            internal = 0
            for j in [p for p in range(lbpos+1,i) if p not in remove_bracket]:
                if string[j] in '+-' and internal == 0:
                    pm = True
                elif string[j] in '*/' and internal == 0:
                    md = True
                elif string[j] == '(':
                    internal += 1
                elif string[j] == ')':
                    internal -= 1

            if pm:
                inside = 'PM'
            elif md:
                inside = 'MD'
            else:
                inside = 'NA'

            if not necessary(before, inside, after):
                remove_bracket.extend([lbpos, i])

    deque((list.pop(string, i) for i in sorted(remove_bracket, reverse=True)), maxlen=0)

    return "".join(string)


if __name__ == '__main__':

    import sys
    for _t in range(int(sys.stdin.readline())):
        # original version:
        # print(simplify(list(sys.stdin.readline())[:-1]))

        # suffix -> infix using expression tree
        # print(create_expression_tree(list(sys.stdin.readline())[:-1]).inorder(4))

        # infix <-> suffix using stack
        print(suffix_to_infix(infix_to_suffix(list(sys.stdin.readline())[:-1])))
        