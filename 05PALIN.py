#!/usr/bin/env python3

'''
PLAIN  

> 1.00 [0.84]
> regex, string operation (avoid list)
'''

import re

# ---------- 1.00 ---------- http://codereview.stackexchange.com/questions/9790/how-to-reduce-total-execution-time-in-python-for-this-program

def make_palindrome(text, odd):
    return text + text[- odd - 1::-1]

def upped(match):
    content = match.group(0)
    return chr(ord(content[0]) + 1 ) + '0' * (len(content) - 1)

def palindrome(inputString, extract = re.compile(r'[^9]9*$')):
    """ Code for finding out temporary palindrome. used by nextPalindrome function"""

    # handle the case that increases the input length as a special case
    if all(letter == '9' for letter in inputString):
        return '1' + '0' * (len(inputString) - 1) + '1'

    length = len(inputString)
    odd = length % 2
    number = inputString[:length//2 + odd]

    current = make_palindrome(number, odd)
    if current > inputString:
        return current
    else:
        number = extract.sub(upped, number) 
        return make_palindrome(number, odd)

# ---------- 1.56 ---------- 
def palindrome2(N):

    L = len(N)
 
    left = N[:L//2]
    center = L % 2 and N[L//2] or ''
    right = left[::-1]
    P = left + center + right
 
    # if reversing the left part to the right makes a greater integer :
    if P > N:
        return P
 
    # if it doesn't, but the center is not a '9', it's not a big deal :
    if center and center != '9':
        center = str(int(center) + 1)
        P = left + center + right
        return P
     
    # if it is a '9' or if there is no one, we have to increment left :
    if center: center = '0'
     
    # handle the special case where every number on the left is a '9' :
    if left == '9' * (L // 2):
        P = '1' + '0' * (L - 1) + '1'
        return P
 
    # increment left :
    digits = list(left)
    pos = L // 2 - 1
    while digits[pos] == '9':
        digits[pos] = '0'
        pos -= 1
    digits[pos] = str(int(digits[pos]) + 1)
    left = ''.join(digits)
    right = left[::-1]
    P = left + center + right
    return P

# ---------- 7.04 ---------- original version
def plus(string, pos):  # add 1 to number 9 at pos, do the same for previous if needed
    while string[-pos] == '9':
        string[-pos] = '0'
        pos += 1
    string[-pos] = str(int(string[-pos]) + 1)
    return pos

def resize(string):     # recalculate list length
    string = ['0'] + string
    l = len(string)
    h = l // 2
    return (string, l, h)

def next(string):
    
    # compare the corresponding number at each side, adjust them according to the rules

    s = list(string)
    s, l, h = resize(s)

    all9 = True         # special case "all 9"
    change = False      # special case "already palindrome"
    i = 1
    while i <= h:
        if s[i] > s[-i]:    
            s[-i] = s[i]
            change = True
            i += 1
        elif s[i] < s[-i]:
            s[-i] = s[i]
            change = True
            i2 = l - plus(s, i + 1) # i: new position
            if i2 > i:
                i += 1
            else:
                if i2 == 0:
                    s, l, h = resize(s)
                    i = 1
                else:
                    i = i2
        elif s[i] == s[-i]:
            if not change and i == h:   # input is already a palindrome
                if s[i] < '9':
                    s[i] = str(int(s[i]) + 1)
                    if l % 2 == 1:
                        s[-i] = str(int(s[-i]) + 1)
                    i += 1
                else:
                    if all9:
                        return ['1'] + ['0'] * (l - 2) + ['1']
                    i2 = l - plus(s, i)
                    if i2 > i:
                        i += 1
                    else:
                        if i2 == 0:
                            s, l, h = resize(s)
                            i = 1
                        else:
                            i = i2
                change = True
            else:
                if s[i] < '9':
                    all9 = False
                i += 1

    if s[0] == '0':
        return s[1:]
    return s

# ---------- EXTRA ----------
def isPalindrome(s):
    '''
    function to test if a string is a palindrome
    '''
    return all(f == b for f,b in zip(s[:half], reversed(s[half:])))

if __name__ == '__main__':

    T = int(input())
    for _t in range(T):
        print(palindrome(input()))