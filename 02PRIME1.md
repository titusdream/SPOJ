PRIME1
====================

Peter wants to generate some prime numbers for his cryptosystem. Help him! 
Your task is to generate all prime numbers between two given numbers!

**Input**

The input begins with the number t of test cases in a single line (t<=10). 
In each of the next t lines there are two numbers m and n 
(1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

**Output**

For every test case print all prime numbers p such that m <= p <= n, 
one number per line, test cases separated by an empty line.

**Example**

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


[Fastest Way to List all Primes below N in Python](http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python)
====================

plain Python methods, with psyco, for n=1000000

	+---------------------+-------+
	| Method              | ms    |
	+---------------------+-------+
	| rwh_primes1         | 43.0  |
	| sieveOfAtkin        | 46.4  |
	| rwh_primes          | 57.4  |
	| sieve_wheel_30      | 63.0  |
	| rwh_primes2         | 67.8  |    
	| sieveOfEratosthenes | 147.0 |
	| ambi_sieve_plain    | 152.0 |
	| sundaram3           | 194.0 |
	+---------------------+-------+

plain Python methods, without psyco, for n=1000000

	+---------------------+-------+
	| Method              | ms    |
	+---------------------+-------+
	| rwh_primes2         | 68.1  |
	| rwh_primes1         | 93.7  |
	| rwh_primes          | 94.6  |
	| sieve_wheel_30      | 97.4  |
	| sieveOfEratosthenes | 178.0 |
	| ambi_sieve_plain    | 286.0 |
	| sieveOfAtkin        | 314.0 |
	| sundaram3           | 416.0 |
	+---------------------+-------+

all methods, allowing numpy, for n=1000000

	+---------------------+-------+
	| Method              | ms    |
	+---------------------+-------+
	| primesfrom2to       | 15.9  |
	| primesfrom3to       | 18.4  |
	| ambi_sieve          | 29.3  |
	+---------------------+-------+

Timings were measured using the command:
python -mtimeit -s"import primes" "primes.{method}(10000000)"
with {method} replaced by each of the method names.
