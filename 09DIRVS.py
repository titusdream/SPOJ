#!/usr/bin/env python3

'''
DIRVS

> Bresenham's line algorithm (modified + 3D), BFS (possiblely A* search)
> NOT possible for python to run within time requirement
> deque, 2-dimension array initialization
'''

# ---------- adapted from official c code ----------

def point(p, h):
	return (p[0], p[1], h[p[0]-1][p[1]-1])

def visible(p1, p2, h):
	x1, y1, z1 = point(p1, h)
	x2, y2, z2 = point(p2, h)

	if x1 > x2:
		x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

	dx, dy, dz = x2 - x1, y2 - y1, z2 - z1

	z = (2 * z1 + 1) * dx + dz		# the height at the first intersection times 2dx
	y = 2 * dx * y1 + dy 			# the y coordinate at the first intersection times 2dx

	for t in range(x1, x2):
		ry = (y + dx - (dy > 0)) // (2 * dx) 		# rounded y
		ry2 = (y + dx - (1 - (dy > 0))) // (2 * dx)	# rounded y
		
		if z < point((t, ry), h)[2] * 2 * dx or z < point((t + 1, ry2), h)[2] * 2 * dx:
			return False
		
		z += 2 * dz
		y += 2 * dy

	if y1 > y2:
		x1, y1, z1, x2, y2, z2 = x2, y2, z2, x1, y1, z1

	dx, dy, dz = x2 - x1, y2 - y1, z2 - z1

	z = (2 * z1 + 1) * dy + dz 		# the height at the first intersection times 2dx
	x = 2 * dy * x1 + dx 			# the x coordinate at the first intersection times 2dx
	
	for t in range(y1, y2):
		rx = (x + dy - (dx > 0)) // (2 * dy) 		# rounded x
		rx2= (x + dy - (1 - (dx > 0))) // (2 * dy) 	# rounded x
		
		if z < point((rx, t), h)[2] * 2 * dy or z < point((rx2, t + 1), h)[2] * 2 * dy:
			return False

		z += 2 * dz
		x += 2 * dx
		
	return True

def movable(p1, p2, h):
	return -3 <= point(p2,h)[2] - point(p1,h)[2] <= 1

def path(p1, p2, h, p, q):

	import collections

	# possible steps
	dx = (0,0,1,-1)
	dy = (1,-1,0,0) 

	# steps notation matrix
	steps = [[-1 for i in range(q)] for j in range(p)]		# [-1]*q will cause them same too
	
	# deque to store unexplored points
	plist = collections.deque()
	
	# here we are at the end
	if p1 == p2:
		return 0

	# from_point
	(x1, y1) = p1
	
	# mark the first point
	steps[x1-1][y1-1] = 0 

	# BFS 
	while 1: 
		# try possible steps
		for k in range(4):
			# candidate to_point is (x_n, y_n) 
			(x2, y2) = (x1 + dx[k], y1 + dy[k])
			
			if not (1 <= x2 <= p and 1 <= y2 <= q):
				continue 	# outside
			if steps[x2-1][y2-1] > -1:
				continue 	# we have been here already
			if not movable((x1, y1), (x2, y2), h):
				continue 	# cannot move
			if not visible((x2, y2), p1, h) and not visible((x2, y2), p2, h):
				continue	# cannot see

			# possible move
			steps[x2-1][y2-1] = steps[x1-1][y1-1] + 1 	# assign distance
			
			# reach the end
			if (x2, y2) == p2:
				return steps[x2-1][y2-1]
			# add to the list for further explore
			plist.append((x2, y2))

		# take out the point from the list
		try:
			(x1, y1) = plist.popleft()
		except IndexError:
			return -1

# ---------- modified Bresenham algorithm for 2D ---------- http://lifc.univ-fcomte.fr/~dedu/projects/bresenham/index.html

def intersect(p1, p2):

	x, y = p1	# the line points
	dx = p2[0] - p1[0]
	dy = p2[1] - p1[1]

	rtn = [p1]	# first point

	# NB the last point can't be here, because of its previous point (which has to be verified)
	# the step on y and x axis
	ystep = 1 if dy > 0 else -1	
	xstep = 1 if dx > 0 else -1
	dx, dy = dx*xstep, dy*ystep

	# work with double values for full precision
	# compulsory variables: the double values of dy and dx
	ddx = 2 * dx
	ddy = 2 * dy  
	
	if ddx >= ddy:  # first octant (0 <= slope <= 1)
	# compulsory initialization (even for errorprev, needed when dx==dy)
		# error: the error accumulated during the increment
		# errorprev: vision the previous value of the error variable
		errorprev = error = dx  # start in the middle of the square
		for _i in range(dx):  # do not use the first point (already done)
			x += xstep
			error += ddy
			if error > ddx:   # increment y if AFTER the middle ( > )
				y += ystep
				error -= ddx
				# three cases (octant == right->right-top for directions below)
				if error + errorprev < ddx:  # bottom square also
					rtn.append((x, y - ystep))
				elif error + errorprev > ddx:  # left square also
					rtn.append((x - xstep, y))
				else:  # corner: bottom and left squares also
					pass
					# rtn.append((x, y - ystep))
					# rtn.append((x - xstep, y))	  
			rtn.append((x, y))
			errorprev = error
	else:  # the same as above
		errorprev = error = dy;
		for _i in range(dy):
			y += ystep
			error += ddx
			if error > ddy:
				x += xstep
				error -= ddy
				if error + errorprev < ddy:
					rtn.append((x - xstep, y))
				elif error + errorprev > ddy:
					rtn.append((x, y - ystep))
				else:
					rtn.append((x - xstep, y))
					rtn.append((x, y - ystep))
				
			rtn.append((x, y))
			errorprev = error

	# the last point (y2,x2) has to be the same with the last point of the algorithm
	# assert y == p2[1] and x == p2[0]
	# print(rtn)
	return rtn

# ---------- BUGGY extension for 3D ----------

def interzect(height, ps, p1, p2):

	for i in range(1, len(ps)):
		if ps[i][1] == ps[i-1][1]:
			x = abs(ps[i][0] - p1[0]) - 0.5
			ratio =  x / abs(p2[0] - p1[0])
		else:	# ps[i][0] == ps[i-1][0] or ps[i][0/1] != ps[i-1][0/1]
			y = abs(ps[i][1] - p1[1]) - 0.5
			ratio =  y / abs(p2[1] - p1[1])

		z1 = height[p1[0]][p1[1]]
		z2 = height[p2[0]][p2[1]]
		if abs(z2 - z1) * ratio + min(z1, z2) + 0.5 < height[ps[i][0]][ps[i][1]]:
			return True
	return False

if __name__ == '__main__':

	import sys
	T = int(sys.stdin.readline())
	for _t in range(T):
		p, q = map(int, sys.stdin.readline().split())
		h = []
		for _p in range(p):
			h.append(tuple(map(int, sys.stdin.readline().split())))	
			# tuple instead of list to speed up
		x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
		steps = path((x1, y1), (x2, y2), h, p, q)
		if steps < 0:
			print("Mission impossible!")
		else:
			print("The shortest path is " + str(steps) + " steps long.")
