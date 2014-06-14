#!/usr/bin/env python3

'''
PLAIN  #1.00 (!0.84)

A positive integer is called a palindrome if its representation in the decimal system is the same when read from left to right and from right to left. For a given positive integer K of not more than 1000000 digits, write the value of the smallest palindrome larger than K to output. Numbers are always displayed without leading zeros.

Input
The first line contains integer t, the number of test cases. Integers K are given in the next t lines.

Output
For each K, output the smallest palindrome larger than K.

Example

Input:
2
808
2133

Output:
818
2222
'''

'''
corner case test collection
['0','9','15641','808','2133','841357','199','1999','319887788993','333321','111','1111','999','9999','99999']
'''

'''
#1.00 
http://codereview.stackexchange.com/questions/9790/how-to-reduce-total-execution-time-in-python-for-this-program
>regex, string operation (avoid list)
'''

import re

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

# isPalindrome
# all(f == b for f,b in zip(s[:half], reversed(s[half:])))

if __name__ == '__main__':
    
    # Test
    # testsuite = ['0','9','15641','808','2133','841357','199','1999','319887788993','333321','111','1111','999','9999','99999']
    # for test in testsuite:
    #     print(palindrome2(test))

    T = int(input())
    for _t in range(T):
        print(palindrome(input()))

