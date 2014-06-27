MMIND
====================
[ACM Central European Programming Contest, Prague 2000](http://contest.felk.cvut.cz/00cerc/solved/)

If you want to buy a new cellular phone, there are many various types to choose from. To decide which one is the best for you, you have to consider several important things: its size and weight, battery capacity, WAP support, colour, price. One of the most important things is also the list of games the phone provides. Nokia is one of the most successful phone makers because of its famous Snake and Snake II. ACM wants to make and sell its own phone and they need to program several games for it. One of them is Master-Mind, the famous board logical game.

The game is played between two players. One of them chooses a secret code consisting of P ordered pins, each of them having one of the predefined set of C colours. The goal of the second player is to guess that secret sequence of colours. Some colours may not appear in the code, some colours may appear more than once.

The player makes guesses, which are formed in the same way as the secret code. After each guess, he/she is provided with an information on how successful the guess was. This feedback is called a hint. Each hint consists of B black points and W white points. The black point stands for every pin that was guessed right, i.e. the right colour was put on the right position. The white point means right colour but on the wrong position. For example, if the secret code is "white, yellow, red, blue, white" and the guess was "white, red, white, white, blue", the hint would consist of one black point (for the white on the first position) and three white points (for the other white, red and blue colours). The goal is to guess the sequence with the minimal number of hints.

The new ACM phone should have the possibility to play both roles. It can make the secret code and give hints, but it can also make its own guesses. Your goal is to write a program for the latter case, that means a program that makes Master-Mind guesses.

**Input**

There is a single positive integer T on the first line of input. It stands for the number of test cases to follow. Each test case describes one game situation and you are to make a guess. On the first line of each test case, there are three integer numbers, P, C and M. P ( 1 <= P <= 10) is the number of pins, C (1 <= C <= 100) is the number of colours, and M (1 <= M <= 100) is the number of already played guesses.

Then there are 2 x M lines, two lines for every guess. At the first line of each guess, there are P integer numbers representing colours of the guess. Each colour is represented by a number Gi, 1 <= Gi <= C. The second line contains two integer numbers, B and W, stating for the number of black and white points given by the corresponding hint.

Let's have a secret code S1, S2, ... SP and the guess G1, G2, ... GP. Then we can make a set H containing pairs of numbers (I,J) such that SI = GJ, and that any number can appear at most once on the first position and at most once on the second position. That means for every two different pairs from that set, (I1,J1) and (I2,J2), we have I1 <> I2 and J1 <> J2. Then we denote B(H) the number of pairs in the set, that meet the condition I = J, and W(H) the number of pairs with I <> J.

We define an ordering of every two possible sets H1 and H2. Let's say H1 <= H2 if and only if one of the following holds:

  B(H1) < B(H2), or
  B(H1) = B(H2) and W(H1) <= W(H2)

Then we can find a maximal set Hmax according to this ordering. The numbers B(Hmax) and W(Hmax) are the black and white points for that hint.

**Output**

For every test case, print the line containing P numbers representing P colours of the next guess. Your guess must be valid according to all previous guesses and hints. The guess is valid if the sequence could be a secret code, i.e. the sequence was not eliminated by previous guesses and hints.

If there is no valid guess possible, output the sentence You are cheating!. If there are more valid guesses, output the one that is lexicographically smallest. I.e. find such guess G that for every other valid guess V there exists such a number I that:

  GJ = VJ for every J<I, and
  GI<VI. 

**Example**

Sample Input:

	3
	4 3 2
	1 2 3 2
	1 1
	2 1 3 2
	1 1
	4 6 2
	3 3 3 3
	3 0
	4 4 4 4
	2 0
	8 9 3
	1 2 3 4 5 6 7 8
	0 0
	2 3 4 5 6 7 8 9
	1 0
	3 4 5 6 7 8 9 9
	2 0

Sample Output

	1 1 1 3
	You are cheating!
	9 9 9 9 9 9 9 9


Scoring function is SYMMETRIC
====================
if score(guess, secret) == (a, b), then a valid new guess must satisfy score(newguess, guess) == (a, b), use this rule to eliminate possibilities

[UVA1548 - The Game of Master-Mind](http://blog.csdn.net/keshuai19940722/article/details/23155575)
====================
解题思路：DFS，复杂度为100^10。当时因为题目中给的限定条件特别多，所以如果在过程中对黑点白点的情况进行判断，时间上是没有问题的。

在判断黑点和白点的时候要注意，统计时要统计黑点个数和点数总和，因为如果将黑点和白点分开计算的话会比较麻烦，因为会有说guess1：2 1，黑1，白0，这样的话ans为1 1是满足的，但是在dfs0层时，ans中的第一个1就变成了白点，如果剪枝为白点个数为0返回就错了。处理方法就是可以先向黑点预支，但如果超过现存黑点的个数也是不行的。


[Analyzing guess (aka. Mastermind)](http://www.mschoebel.info/2012/03/15/analyzing-guess-aka-mastermind.html)
====================
Algorithm by [Donald E. Knuth](http://colorcode.laebisch.com/links/Donald.E.Knuth.pdf)  
GitHub: https://github.com/mschoebel/guess
