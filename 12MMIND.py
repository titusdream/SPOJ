#!/usr/bin/env python3

'''
MMIND

> DFS + Pruning
> NOT possible for python to run within time requirement
> local variable lookup, itertools.product, filter, all, 2-dim list init, collections.Counter, taskset
'''

# ---------- 0.0097 (local.ex) 160.4 (local) ---------- http://blog.csdn.net/keshuai19940722/article/details/23155575       game.cpp 5.05 (SPOJ C++ 4.0.0.8)

import sys, collections
from operator import add

class Mind():
   def __init__(self, pins, colors, trys):
      self.p = pins              # number of pins
      self.ans = [0] * self.p    # final answer

      self.c = colors            # number of all colors
      
      self.m = trys              # number of guesses
      self.black = []            # all guess's black number
      self.white = []            # all guess's white number
      self.guesses = []          # all m guesses
      self.pcnt = [0] * self.m   # count of position (also color) correct
      self.ccnt = [0] * self.m   # count of color (maybe position or not) correct
      
      # equivalent to x = [[foo for i in range(10)] for j in range(10)]
      self.colors = [x[:] for x in [[0] * (self.c+1)] * self.m] # number of appearance of each color in each guess
      self.ctable = [x[:] for x in [[0] * (self.c+1)] * self.m] # number of appearance of each color in current search
      # each col.0 is unused, color number from 1 - c

   def judge(self, c, d):
      '''
      test if color 'c' in position 'd' is possible based on previous position in current answer, return True only if it's possible for every guess
      it is not a judge for final answer, but for illiminate impossible answer in d position (Pruning)
      '''
      for i in range(self.m):
         # not possible if current color&position match, but position match number already used up
         if c == self.guesses[i][d]:
            if self.pcnt[i] == self.black[i]:
               return False
         # not possible if current color can increase the color match, but this match will cause the color match exceeds allowed position + color match (see setting() for reason why here we use the total)
         elif self.ctable[i][c] < self.colors[i][c]: 
            if self.ccnt[i] >= self.black[i] + self.white[i]:
               return False

      return True

   def setting(self, c, d, flag):
      '''
      helper function to set associated lists
      '''

      if flag: # set
         for i in range(self.m):
            if c == self.guesses[i][d]:
               self.pcnt[i] += 1                      # position correct +1
            if self.ctable[i][c] < self.colors[i][c]: # if color 'c' appearence in current answer is less than that in guess, one more color = one more color match (could also be position match if previous "if" is true, too)
               self.ccnt[i] += 1                      # color correct +1
            self.ctable[i][c] += 1                    # color appearance +1
      else: # unset
         for i in range(self.m):
            if c == self.guesses[i][d]:
               self.pcnt[i] -= 1
            self.ctable[i][c] -= 1
            if self.ctable[i][c] < self.colors[i][c]:
               self.ccnt[i] -= 1

   def dfs(self, d):
      '''
      Depth-First Search (try each color 'i' at position 'd') with Pruning (judge())
      '''

      # evaluate a complete answer
      if d == self.p:
         if self.pcnt != self.black or self.ccnt != list(map(add, self.black, self.white)): # if != current answer has all black, white tuple feedback valid agaisnt every guesses, answer is wrong
               return False
         return True

      # for position 'd', try each color 'd'
      for i in range(1, self.c + 1):

         # Pruning
         if not self.judge(i, d):
            continue

         # if possible, set help lists and answer (up to position 'd')
         self.setting(i, d, True)
         self.ans[d] = i

         # if current answer is correct
         if self.dfs(d + 1):
            return True

         # if color 'i' in position 'd' doesn't yield valid answer, unset help lists and try next color
         self.setting(i, d, False)

      # every color in position 'd' (and its successors) cannot yield valid answer
      return False


# ---------- 46.52 (local.ex) ---------- improved version

import itertools

# optimized by replacing global lookups with local variables defined as default values
def evaluation(g1, g2, sum=sum, zip=zip, set=set, min=min):
    # number of correct colors at the right position
    black = sum(1 for c1, c2 in zip(g1, g2) if c1 == c2)
    
    # number of correct colors at the wrong position
    white = -black
    for c in set(g1):
        white += min(g1.count(c), g2.count(c))

    return (black, white)

def match(guess, solution):
    return solution != guess[0] and evaluation(guess[0], solution) == guess[1]

def makeguess(guesses, p, c, m):

    solutionSet = itertools.product(range(1, c+1), repeat=p)
    # cannot apply filter to filter
    # list/set conversion is a tragedy... freeze the machine
    # "taskset 01 python test.py < test.in" to force run on 1 cpu

    # strategy 2: illiminate all solutions against each guess
    for guess in guesses:
        # special case illimination
        if guess[1] == (0, 0):
            solutionSet = set(solution for solution in solutionSet if set(guess[0]).isdisjoint(set(solution)))   
        solutionSet = set(filter(lambda solution: solution != guess[0] and evaluation(guess[0], solution) == guess[1], solutionSet))
        if not solutionSet:
            return "You are cheating"

    return " ".join(map(str, sorted(solutionSet)[0]))


# ---------- 397.28 (local.ex) ---------- original version

def makeguess1(guesses, p, c, m):

    solutionSet = itertools.product(range(1, c+1), repeat=p)

    # strategy 1: test each possible solution against each guess
    for solution in solutionSet:
        # 9.76 if tuple(map(match, guesses, [solution] * m)).count(True) == m:
        # 9.12 if len(tuple(guess for guess in guesses if match(guess, solution))) == m: 
        # 8.80 if sum(1 for _ in (guess for guess in guesses if match(guess, solution))) == m:
        # 4.97
        if all(map(match, guesses, [solution] * m)):
            # sum(1 for _ in generator) is a hack of len(tuple(generator))
            return " ".join(map(str, solution))

    return "You are cheating!"


# ---------- TIMEIT ----------
def timeit(filename):
    '''
    python3 -m timeit "import test; test.timeit()"
    '''
    fin = open(filename, 'r')
    
    main(fin, printout=False, timing=False)

    fin.close()

def main(source, printout=True, timing=False):

    if timing:
        import time
        start_time = time.time()
    
    # for _t in range(int(source.readline())):
    #     P, C, M = map(int, source.readline().split())
    #     guesses = []
    #     for _m in range(M):
    #         guesses.append( ( tuple(map(int, source.readline().split())), tuple(map(int, source.readline().split())) ) )
    #     result = makeguess(guesses, P, C, M)
    #     if printout: print(result)

    for _t in range(int(sys.stdin.readline())):
        p, c, m = map(int, sys.stdin.readline().split())
        mind = Mind(p, c, m)
       
        for i in range(m):
            guess = list(map(int, sys.stdin.readline().split()))
            mind.guesses.append(guess)

            # collections.Counter is a 'multiset'
            cset = collections.Counter(guess)
            for color in cset.keys():
             mind.colors[i][color] = cset[color]

            b, w = map(int, sys.stdin.readline().split())
            mind.black.append(b)
            mind.white.append(w)

        result = mind.dfs(0)
        if printout:
            if result:
                print(" ".join(map(str,mind.ans)))
            else:
                print("You are cheating!")

    if timing:
        print("Running time: ", time.time() - start_time)

if __name__ == '__main__':
    
    import sys
    main(sys.stdin, timing=True)
