#!/usr/bin/env python3

'''
CMPLS

> Method of Finite Differences (polynomial)
> 4.72 [4.72] python3
> 3.83 [1.28] python2
> sys.stdin vs. input()
'''

# http://en.wikipedia.org/wiki/Difference_engine#Method_of_differences

def genseq(s, c, matrix):
    # build finite differences table
    for i in range(s-1):
        matrix.append([matrix[i][j+1]-matrix[i][j] for j in range(s-1-i)])
        # early termination (~3x faster)
        if matrix[-1].count(matrix[-1][0]) == len(matrix[-1]):
            s = i + 2
            break

    for _c in range(c):
        # matrix[s-1].append(matrix[s-1][-1])
        # matrix[s-1] has all items identical, no need to build to the 'correct' form
        for i in range(s-2,-1,-1):
            matrix[i].append(matrix[i][-1] + matrix[i+1][-1])

    return matrix[0][-c:]


if __name__ == '__main__':
    
    import time
    start_time = time.time()

    # ---------- TLE ----------
    # T = int(input())
    # for _t in range(T):
        # s, c = map(int, input().split())
        # matrix = [list(map(int, input().split()))]
        # print(" ".join(map(str, genseq(s, c, matrix))))
    
    # ---------- 4.72 ----------
    # python3: sys.stdin.read/readline() is 3x faster than input()
    
    import sys 
    stdin = sys.stdin.read()
    stdin = stdin.split("\n")[::-1]
    T = int(stdin.pop())
    for _t in range(T):
        s, c = map(int, stdin.pop().split())
        matrix = [list(map(int, stdin.pop().split()))]
        print(" ".join(map(str, genseq(s, c, matrix))))
        # sys.stdout.write(" ".join(map(str, genseq(s, c, matrix))) + '\n')
        # one-time output, using sys.stdout.write doesn't gain anything

    # ---------- 3.83 ----------
    # python2: equivalent performance using raw_input() (+xrange)

    end_time = time.time()
    print("Elapsed time was %g seconds" % (end_time - start_time))