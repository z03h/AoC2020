with open('tt.txt', 'r') as f:
    x = f.read()


snap = x.split('\n\n')
tiles = {}
for s in snap:
    name, _, rest = s.partition('\n')
    _lmao, _lmoa, name = name.strip(':').partition(' ')
    name=int(name)
    #print(name, '\n', rest)
    tiles[name] = rest.splitlines()

from functools import lru_cache

def get_side(tile, side):
    #0 top
    #1 right
    #2 bottom
    #3 left
    if side==0:
        return tiles[tile][0]
    elif side==1:
        return ''.join(t[-1] for t in tiles[tile])
    elif side==2:
        return tiles[tile][-1]
    elif side==3:
        return ''.join(t[0] for t in tiles[tile])

def compare_sides(t1,s1, t2,s2):
    o = get_side(t1,s1)
    p = get_side(t2,s2)
    if o ==p:
        return 1
    elif o == p[::-1]:
        return -1
    return False
def get_match(t1, s1):
    for t2 in tiles:
        if t1==t2:
            continue
        for j in range(4):
            orientation = compare_sides(t1,s1, t2,j)
            if orientation:
                return t2, j, orientation
    return 0,0,False


def printsides(i):
    for ii in range(4):
        print(get_match(i,ii))

def hreverse(frame):
    tiles[frame] = [line[::-1] for line in tiles[frame]]
def vflip(frame):
    tiles[frame].reverse()
def rrotate(frame):
    temp = []
    for i in range(len(tiles[frame][0])):
        temp.append(''.join(tiles[frame][j][i] for j in range(len(tiles[frame])-1, -1, -1)))
    tiles[frame] = temp
def lrotate(frame):
    temp = []
    for i in range(len(tiles[frame][0])-1, -1, -1):
        temp.append(''.join(tiles[frame][j][i] for j in range(len(tiles[frame]))))
    tiles[frame] = temp

def rotate_index(frame, side, endside, reverse):
    if frame == 1307:
        print(frame, side, endside, reverse)
    if endside==side:
        if side %2 == 1:
            hreverse(frame)
        elif side%2==0:
            vflip(frame)
            pass
    elif endside==(side+1)%4:
        #match endside to side before
        if endside in (2, 0):
            rrotate(frame)
        else:
            lrotate(frame)
            if endside == 1:
                vflip(frame)
    elif endside==(side+2)%4:
        #opposite
        pass
    elif endside==(side+3)%4:
        #side after
        if endside in (2, 0):
            rrotate(frame)
            if endside==2:
                hreverse(frame)
        else:
            lrotate(frame)

    if reverse==-1:
        if side %2 == 0:
            hreverse(frame)
        elif side%2==1:
            vflip(frame)
            pass
"""
print('\n'.join(tiles[1427]))
lrotate(1427)
hreverse(1427)
print()
print('\n'.join(tiles[1427]))
exit()
"""

for t1 in tiles:
    count = 0
    adjacent = {}
    for i in range(4):
        _ = get_match(t1, i)
        if _[2]:
            count += 1
            adjacent[i] = _
    if count == 2:
        corner = t1
        break


alltiles = {}
grid = {}
visited = []
def explore_tiles(t1, x=0, y=0):
    if t1 in visited:
        return
    visited.append(t1)
    sides = {}
    for side in range(4):

        t2, s2, orientation = get_match(t1, side)
        #print(side,':',t2, s2, orientation)
        if orientation:
            rotate_index(t2, side, s2, orientation)
            sides[side] = t2
    alltiles[t1] = sides
    for oside, t2 in alltiles[t1].items():
        if oside in valid_directions:
            d = {0:(0,1),
                 1:(1,0),
                 2:(0,-1),
                 3:(-1,0)
                 }
            grid[(x+d[oside][0], y+d[oside][1])] = t2
            explore_tiles(t2, x+d[oside][0], y+d[oside][1])


def explore_direction(t1, x=0, y=0, *, d=0):
    if t1 in visited:
        return

    grid[x,y] = t1
    visited.append(t1)
    sides = {}
    for side in range(4):

        t2, s2, orientation = get_match(t1, side)
        if t2 in alltiles:
            continue
        #print(side,':',t2, s2, orientation)
        if orientation:
            rotate_index(t2, side, s2, orientation)
            sides[side] = t2
    alltiles[t1] = sides
    if t1==1307:
        print(sides)
    for oside, t2 in alltiles[t1].items():
        if oside == d:
            ds = {0:(0,1),
                 1:(1,0),
                 2:(0,-1),
                 3:(-1,0)
                 }
            grid[(x+ds[oside][0], y+ds[oside][1])] = t2
            explore_direction(t2, x+ds[oside][0], y+ds[oside][1], d=d)


print(corner)
print(adjacent)

valid_directions = list(adjacent.keys())
grid[0,0] = corner
#explore_tiles(corner)
explore_direction(corner, d= 2 if 2 in valid_directions else 0)
"""
print('\n'.join(tiles[1307]))
print()
print('\n'.join(tiles[3259]))
"""
explore_direction(2203, -1, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(3697, -2, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1249, -3, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1031, -4, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1867, -5, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1303, -6, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1723, -7, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(2411, -8, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(1871, -9, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(3727, -10, 0, d= 2 if 2 in valid_directions else 0)
explore_direction(3823, -11, 0, d= 2 if 2 in valid_directions else 0)
print('-----')

#print('\n'.join(str(x) for x in alltiles.items()))
#print('\n'.join(str(x) for x in grid.items()))




minx = min(grid, key=lambda k: k[0])[0]
maxx = max(grid, key=lambda k: k[0])[0]
miny = min(grid, key=lambda k: k[1])[1]
maxy = max(grid, key=lambda k: k[1])[1]
#print(minx, maxx, miny, maxy)
"""
for i in range(minx, maxx+1):
    for j in range(maxy, miny-1, -1):
        try:
            print(grid[i,j], end=' ', sep=' ')
        except KeyError:
            print('????', end=' ', sep=' ')
    print()
"""

grid = '''2719 3271 1609 3881 2381 1087 1949 1889 2939 3169 3607 3823
3529 1409 1787 1553 2791 3919 2887 1823 1697 3947 1657 3727
3593 1811 2729 1801 2437 1153 2549 2591 1279 3373 1447 1871
1699 1459 1913 1783 3917 2789 3041 1283 3821 3709 1979 2411
2273 1607 3557 1523 1901 3191 2699 3659 2347 2539 1019 1723
2011 3251 3049 2459 1109 2819 2237 2399 2749 3499 1163 1303
3637 3449 1423 2803 1861 3307 1301 2473 3119 3889 2089 1867
3769 3467 1549 2129 1559 1531 1583 1907 1427 3461 2797 1031
2609 2879 1061 1973 3797 3079 1831 1051 2777 2081 3793 1249
2663 2671 3833 3371 2711 3533 1187 3203 1933 2909 2281 3697
2287 2003 1481 3347 2269 2063 1667 1747 1847 1367 1093 2203
1759 1069 2917 1721 1063 3259 1307 3037 2713 1471 1319 2801'''
grid = [x.split(' ') for x in grid.splitlines()]

def gridrrotate(LL):
    temp = []
    for i in range(len(LL[0])):
        temp.append(' '.join(LL[j][i] for j in range(len(LL)-1, -1, -1)).split())
    return temp
def gridhreverse(LL):
    for l in LL:
        l.reverse()

grid = gridrrotate(grid)
gridhreverse(grid)
for i in grid:
    for j in i:
        print(j, end=' ', sep=' ')
    print()
def combine_row(LL):
    end = []
    for i in range(1, 9):
        line = ''
        for j in range(12):
            line += tiles[int(LL[j])][i][1:-1]
        end.append(line)
    return end
formatted = []
for L in grid:
    formatted.extend(combine_row(L))
lake = '\n'.join(''.join(formatted))
import re
monster = '''                  #.
#    ##    ##    ###
 #  #  #  #  #  #   '''
def rotate_once(x):
    return list("".join(x) for x in zip(*x[::-1]))

monster = monster.replace(' ', '.')
compiled = re.compile(monster)
def gridstrreverse(LL):
    for i, thing in enumerate(LL):
        LL[i] = thing[::-1]
    return LL
orientations = []
for i in range(4):
    formatted = rotate_once(formatted)
    orientations.append(formatted)
    orientations.append(formatted[::-1])

for i in orientations:
    formatted = i
    monster_count = 0
    for starty in range(144):
        for startx in range(125):
            try:
                maybe = '\n'.join((formatted[starty][startx:startx+20],
                           formatted[starty+1][startx:startx+20],
                           formatted[starty+2][startx:startx+20]))
                #print(maybe, '\n')
                if compiled.fullmatch(maybe):
                    monster_count+=1
                    print(monster_count)
            except IndexError:
                pass
    print(monster_count or 'nope')
print(''.join(formatted).count('#') - (35*monster.count('#')))
