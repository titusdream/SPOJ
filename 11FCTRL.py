#!/usr/bin/env python3

'''
FCTRL  

> 2.94 [1.27]
> functools.reduce, one-time readin
'''

# ---------- py3: 3.16, 2.94 ---------- w/ bruteforce + one-time readin

def factorial_zero3(n):
    count = n//5 + n//25 + n//125 + n//625 + n//3125 + n//15625 + n//78125 + n//390625 + n//1953125 + n//9765625 + n//48828125 + n//244140625 
    return count

# for n in list(map(int, sys.stdin.read().split()))[1:]:
#     print(z(n))

# ---------- py2: 3.05 py3: 3.54 ---------- second version

def factorial_zero2(n):
    zeros = new = n // 5
    while new >= 5:
        add = new // 5  # one more line to reduce redundent calculation
        zeros, new = zeros + add, add
    return zeros

# ---------- py2: 4.91 py3: TLE > 6 ---------- original version

def factorial_zero(n):
    return reduce(lambda x, y: x + n // y, five(n), 0)

def five(n):
    factor = 5
    while factor <= n:
        yield factor
        factor *= 5

# ---------- EXTRA ---------- output factorial
from operator import mul
from functools import reduce
 
def factorial(n):
    return reduce(mul, range(1,n+1), 1)


# ---------- TIMEIT ----------
def timeit():
    '''
    python -m timeit "import test; test.timeit()"
    '''
    fin = open('factor.in', 'r')
    
    for _t in range(int(fin.readline())):
        factorial_zero2(int(fin.readline()))

    fin.close()

if __name__ == '__main__':
    
    import sys

    # Normal read
    # for _t in range(int(sys.stdin.readline())):
    #     print(factorial_zero2(int(sys.stdin.readline())))

    # One-time read
    for n in list(map(int, sys.stdin.read().split()))[1:]:
        print(factorial_zero3(n))