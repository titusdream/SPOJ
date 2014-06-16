#!/usr/bin/env python3

'''
BULK

> polygon area, point in polygon test, += & =...+... difference, OrderedDict
> NOT possible for python to run within time requirement
'''

import collections

def area(polygon):
    '''
    function to calculate area of a polygon
    '''

    polygon = polygon + polygon[:2]

    # compute area
    area = 0
    for i in range(1, len(polygon)-1):
        area += polygon[i][0] * (polygon[i+1][1] - polygon[i-1][1])
    area /= 2

    return area

def pnpoly(polygon, point):
    '''
    function to test if a point is inside a polygon
    '''

    polygon = polygon + polygon[:1]
    # polygon[0] is a tuple, polygon[:1] is a list
    # polygon += polygon[:1] will reuse the same reference to the list, even with "polygon = poly", the reference remains the same

    rtn = False
    for i in range(1, len(polygon)):
        # border check (without, the upper & right border is considered False, left & botton True)
        # if (polygon[i][0] == polygon[i-1][0] == point[0] and (polygon[i][1] <= point[1] <= polygon[i-1][1] or polygon[i][1] >= point[1] >= polygon[i-1][1])) \
        # or (polygon[i][1] == polygon[i-1][1] == point[1] and (polygon[i][0] <= point[0] <= polygon[i-1][0] or polygon[i][0] >= point[0] >= polygon[i-1][0])):
        #     return True
        if ((polygon[i][1] > point[1]) is not (polygon[i-1][1] > point[1])) \
            and point[0] < (polygon[i-1][0] - polygon[i][0]) * (point[1] - polygon[i][1]) / (polygon[i-1][1] - polygon[i][1]) + polygon[i][0]:
            rtn = not rtn

    return rtn

def volume(surfaces, bounding):
    '''
    function to calculate the volume of the bulk.
    
    within bouding box, for each point(lego), scan from the highest surface (largest z index) to the bottom,
    if the point is inside some surface, +/- the volume accordingly
    for all the surface containing the same point(x,y), the surface orientation is alternative (+,-,+,-...)
    '''

    volume = 0
    for x, y in [(x,y) for x in range(bounding[0], bounding[1]+1) for y in range(bounding[2], bounding[3]+1)]:
        orientation = 1
        for z, surface_list in surfaces.items():
            for surface in surface_list:
                if pnpoly(surface, (x,y)):
                    volume += orientation * z
                    orientation = -orientation
                    break
    return volume

if __name__ == '__main__':
    
    # Test points in polygon

    # testsuite = [[(10,10),(10,40),(40,40),(40,10)],[(10,10),(20,10),(20,30),(30,30),(30,40),(10,40)]]
    # points = [(5,5),(10,10),(10,15),(10,40),(15,5),(15,35),(25,20),(25,35),(30,30),(30,35),(35,10),(35,40),(40,45)]
    
    # testsuite = [[(10,10),(10,40),(40,40),(40,10)]]
    # points = [(10,10), (10,20), (10,40), (20,10), (20,40), (40,10), (40,40)]
    
    # testsuite = [[(10,10),(20,10),(20,30),(30,30),(30,40),(10,40)]]
    # points = [(10,10),(10,30),(10,40),(15,30),(15,40),(20,10),(20,20),(20,30),(20,40),(25,30),(25,40),(30,30),(30,35),(35,40)]
    
    # for test in testsuite:
    #     print("=================")
    #     for point in points:
    #         print(pnpoly(test, point))

    T = int(input())
    for _t in range(T):
        F = int(input())
        surfaces = {}
        bounding = [1000,0,1000,0]
        for _f in range(F):
            line = input().split()
            z = [line[i] for i in range(3, int(line[0])*3+1, 3)]
            # http://stackoverflow.com/questions/3844801/check-if-all-elements-in-a-list-are-identical
            # checkEqualIvo http://stackoverflow.com/q/3844948/
            # only store horizontal surfaces
            if z.count(z[0]) == len(z):
                x = [int(line[i]) for i in range(1, int(line[0])*3+1, 3)]
                y = [int(line[i]) for i in range(2, int(line[0])*3+1, 3)]
                bounding = [min(min(x),bounding[0]), max(max(x),bounding[1]), min(min(y),bounding[2]), max(max(y),bounding[3])]
                # surface = [tuple(map(int,line[i:i+2])) for i in range(1, int(line[0])*3+1, 3)]
                surface = list(zip(x, y))
                key = int(z[0])
                if key in surfaces:
                    surfaces[key].append(surface)
                else:
                    surfaces[key] = [surface]
        surfaces = collections.OrderedDict(sorted(surfaces.items(), reverse=True))

        print("The bulk is composed of " + str(volume(surfaces, bounding)) + " units.")

