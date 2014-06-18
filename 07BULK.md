BULK
====================
[ACM Central European Programming Contest, Prague 2000](http://contest.felk.cvut.cz/00cerc/solved/)

ACM uses a new special technology of building its transceiver stations. This technology is called Modular Cuboid Architecture (MCA) and is covered by a patent of Lego company. All parts of the transceiver are shipped in unit blocks that have the form of cubes of exactly the same size. The cubes can be then connected to each other. The MCA is modular architecture, that means we can select preferred transceiver configuration and buy only those components we need .

The cubes must be always connected "face-to-face", i.e. the whole side of one cube is connected to the whole side of another cube. One cube can be thus connected to at most six other units. The resulting equipment, consisting of unit cubes is called The Bulk in the communication technology slang.

Sometimes, an old and unneeded bulk is condemned, put into a storage place, and replaced with a new one. It was recently found that ACM has many of such old bulks that just occupy space and are no longer needed. The director has decided that all such bulks must be disassembled to single pieces to save some space. Unfortunately, there is no documentation for the old bulks and nobody knows the exact number of pieces that form them. You are to write a computer program that takes the bulk description and computes the number of unit cubes.

Each bulk is described by its faces (sides). A special X-ray based machine was constructed that is able to localise all faces of the bulk in the space, even the inner faces, because the bulk can be partially hollow (it can contain empty spaces inside). But any bulk must be connected (i.e. it cannot drop into two pieces) and composed of whole unit cubes.

 
**Input**

There is a single positive integer T on the first line of input (equal to about 1000). It stands for the number of bulks to follow. Each bulk description begins with a line containing single positive integer F, 6 <= F <= 250, stating the number of faces. Then there are F lines, each containing one face description. All faces of the bulk are always listed, in any order. Any face may be divided into several distinct parts and described like if it was more faces. Faces do not overlap. Every face has one inner side and one outer side. No side can be "partially inner and partially outer".

Each face is described on a single line. The line begins with an integer number P stating the number of points that determine the face, 4 <= P <= 200. Then there are 3 x P numbers, coordinates of the points. Each point is described by three coordinates X,Y,Z (0 <= X,Y,Z <= 1000) separated by spaces. The points are separated from each other and from the number P by two space characters. These additional spaces were added to make the input more human readable. The face can be constructed by connecting the points in the specified order, plus connecting the last point with the first one.

The face is always composed of "unit squares", that means every edge runs either in X, Y or Z-axis direction. If we take any two neighbouring points X1,Y1,Z1 and X2,Y2,Z2, then the points will always differ in exactly one of the three coordinates. I.e. it is either X1 <> X2, or Y1 <> Y2, or Z1 <> Z2, other two coordinates are the same. Every face lies in an orthogonal plane, i.e. exactly one coordinate is always the same for all points of the face. The face outline will never touch nor cross itself.

 
**Output**

Your program must print a single line for every test case. The line must contain the sentence The bulk is composed of V units., where V is the volume of the bulk.

**Example**

Sample Input:

	2
	12
	4  10 10 10  10 10 20  10 20 20  10 20 10
	4  20 10 10  20 10 20  20 20 20  20 20 10
	4  10 10 10  10 10 20  20 10 20  20 10 10
	4  10 20 10  10 20 20  20 20 20  20 20 10
	4  10 10 10  10 20 10  20 20 10  20 10 10
	5  10 10 20  10 20 20  20 20 20  20 15 20  20 10 20
	4  14 14 14  14 14 16  14 16 16  14 16 14
	4  16 14 14  16 14 16  16 16 16  16 16 14
	4  14 14 14  14 14 16  16 14 16  16 14 14
	4  14 16 14  14 16 16  16 16 16  16 16 14
	4  14 14 14  14 16 14  16 16 14  16 14 14
	4  14 14 16  14 16 16  16 16 16  16 14 16
	12
	4  20 20 30  20 30 30  30 30 30  30 20 30
	4  10 10 10  10 40 10  40 40 10  40 10 10
	6  10 10 20  20 10 20  20 30 20  30 30 20  30 40 20  10 40 20
	6  20 10 20  20 20 20  30 20 20  30 40 20  40 40 20  40 10 20
	4  10 10 10  40 10 10  40 10 20  10 10 20
	4  10 40 10  40 40 10  40 40 20  10 40 20
	4  20 20 20  30 20 20  30 20 30  20 20 30
	4  20 30 20  30 30 20  30 30 30  20 30 30
	4  10 10 10  10 40 10  10 40 20  10 10 20
	4  40 10 10  40 40 10  40 40 20  40 10 20
	4  20 20 20  20 30 20  20 30 30  20 20 30
	4  30 20 20  30 30 20  30 30 30  30 20 30

Sample Output:

	The bulk is composed of 992 units.
	The bulk is composed of 10000 units.


[Point in Polygon Strategies](http://erich.realtimerendering.com/ptinpoly/)
====================

General Algorithms, Random Polygons:

	                       number of edges per polygon
	                         3       4      10      100    1000
	MacMartin               2.9     3.2     5.9     50.6    485
	Crossings               3.1     3.4     6.8     60.0    624
	Triangle Fan+edge sort  1.1     1.8     6.5     77.6    787
	Triangle Fan            1.2     2.1     7.3     85.4    865
	Barycentric             2.1     3.8    13.8    160.7   1665
	Angle Summation        56.2    70.4   153.6   1403.8  14693

	Grid (100x100)          1.5     1.5     1.6      2.1      9.8
	Grid (20x20)            1.7     1.7     1.9      5.7     42.2
	Bins (100)              1.8     1.9     2.7     15.1    117
	Bins (20)               2.1     2.2     3.7     26.3    278

General Algorithms, Regular Polygons:

	                       number of edges per polygon
	                         3       4      10      100    1000
	MacMartin               2.7     2.8     4.0     23.7    225
	Crossings               2.8     3.1     5.3     42.3    444
	Triangle Fan+edge sort  1.3     1.9     5.2     53.1    546
	Triangle Fan            1.3     2.2     7.5     86.7    894
	Barycentric             2.1     3.9    13.0    143.5   1482
	Angle Summation        52.9    68.1   158.8   1489.3  15762

	Grid (100x100)          1.5     1.5     1.5      1.5      1.5
	Grid (20x20)            1.6     1.6     1.6      1.7      2.5
	Bins (100)              2.1     2.2     2.6      4.6      3.8
	Bins (20)               2.4     2.5     3.4      9.3     55.0

Convex Algorithms, Regular Polygons:

	                       number of edges per polygon
	                         3       4      10      100    1000
	Inclusion               4.82    5.01    6.21     7.12     8.3

	Sorted Triangle Fan     1.11    1.41    3.75    29.36   289.6
	Unsorted Triangle Fan   1.25    2.04    6.30    69.18   734.7

	Unsorted Barycentric*   1.79    2.80    6.94    65.62   668.7

	Random Exterior Edges   1.11    1.61    3.82    33.44   333.6
	Ordered Exterior Edges  1.28    1.70    4.15    41.07   408.9

	Convex MacMartin        2.44    2.48    3.18    17.31   159.8
