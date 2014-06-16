#!/usr/bin/env python3

'''
PRIME1 

> Sieve of Eratosthenes
> 1.74 [0.24]
> generator, set
'''

# ---------- 1.74 ---------- http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188

# Prime Generator
# steps through each odd number from 3 to 32000 
# (the sqrt of the given upper bound) by 2s
# if an individual number is prime, adds it to the list "primes"

# primes = [2]
# for i in range(3, 32000, 2):
#     isprime = True

#     cap = i**0.5 + 1

#     for j in primes:
#         if (j >= cap):
#             break
#         if (i % j == 0):
#             isprime = False
#             break

#     if (isprime):
#         primes.append(i)

def rwh_primes1(n):
    """ Returns a list of primes < n """
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def gen(m, n):
    primes = rwh_primes1(32000)

    cap = n**0.5 + 1

    # if the lower bound is not at least 2, make it 2
    if (m < 2):
        m = 2

    # a list of n+1-m (problem description says <= 100001) "True"s
    isprime = [True] * (n+1-m)

    # for all the irrelevant values in "primes", sets the corresponding 
    # True/False value in "isprime" to False
    # faster than looping through all the values of isprime 
    # and setting them to False individually
    for i in primes:

        if (i >= m):
            start = i * 2
            # a speed up (which doesn't seem effective)
            # if start > n:
                # break
        else:
            start = m + ((i - m % i) % i)

        falseblock = [False] * len(isprime[start-m : n+1-m : i]);
        isprime[start-m : n+1-m : i] = falseblock

    # output
    for i in range(m, n+1):
        if (isprime[i-m] == True):
            # print(i)      # only change print to yield makes 2.05 -> 1.74
            yield i


# ---------- 1.98 ---------- # http://www.codechef.com/viewsolution/1287533
def gen2(m,n):
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

if __name__ == '__main__':
    
    T = int(input())
    for _t in range(T):
        m, n = map(int, input().split())
        primes = gen(m, n)
        for prime in primes:
            print(prime)