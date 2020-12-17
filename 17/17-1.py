cells = '''##.#...#
#..##...
....#..#
....####
#.#....#
###.#.#.
.#.#.#..
.#.....#'''

cellsz = '''.#.
..#
###'''

cells = cells.splitlines()

minx, maxx = -1, len(cells[0])+1
miny, maxy = -1, len(cells)+1
minz, maxz = -1, 2
from itertools import product

active = set()
for i,line in enumerate(cells):
    for j,char in enumerate(line):
        if char == '#':
            active.add((i,j,0))
def getpoints(x,y,z):
    for i in (x-1, x, x+1):
        for j in (y-1, y, y+1):
            for k in (z-1, z, z+1):
                if not(i==x and j==y and k==z):
                    yield (i,j,k)

def check(x,y,z):
    return sum((i,j,k) in active for i,j,k in getpoints(x,y,z))

"""for z in range(minz,maxz):
    for x in range(minx,maxx):
        for y in range(miny,maxy):
            print('#' if (x,y,z) in active else '.', end=' ')
        print()
    print('z=',z)

print(len(active),'====______________________==')"""

for _ in range(6):
    to_add = set()
    to_remove = set()
    for point in product(range(minx,maxx), range(miny,maxy), range(minz,maxz)):
        around = check(*point)
        if around == 3:
            to_add.add(point)
        elif around == 2 and point in active:
            to_add.add(point)
        else:
            to_remove.add(point)

    active |= to_add
    active -= to_remove


    """for z in range(minz,maxz):
        for x in range(minx,maxx):
            for y in range(miny,maxy):
                print('#' if (x,y,z) in active else '.', end=' ')
            print()
        print('z=',z)"""
    minx-=1
    maxx+=1
    miny-=1
    maxy+=1
    minz-=1
    maxz+=1


    print(len(active),'======================================')



