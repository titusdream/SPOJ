#!/usr/bin/env python

'''
PRIME1 | Sieve of Eratosthenes

Peter wants to generate some prime numbers for his cryptosystem. Help him! 
Your task is to generate all prime numbers between two given numbers!

Input
The input begins with the number t of test cases in a single line (t<=10). 
In each of the next t lines there are two numbers m and n 
(1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output
For every test case print all prime numbers p such that m <= p <= n, 
one number per line, test cases separated by an empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
'''

'''
http://www.codechef.com/viewsolution/1287533
> generator
> set
'''

def gen(m,n):
    if m == 1:
        m += 1
    if m <= 2 <= n:
        yield 2
    if m % 2 == 0:
        m += 1
    isp = set(range(m, n + 1, 2));  # all odd interger in range (possible primes)
    sq = int(n**0.5) + 1
    for i in range(3, sq, 2):       # test between 3 and sqrt of n
        if i == 3 or (i % 3) != 0:
            if i in isp:
                yield i
            isp.difference_update(range((m // i) * i, n+1, i)) # Update the set, removing elements found in others.
    for i in sorted(isp):
        yield i
 
T = int(input())
 
for _t in range(T):
    m, n = map(int, input().split())
    primes = gen(m, n)
    for prime in primes:
        print(prime)