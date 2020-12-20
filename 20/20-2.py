with open('input.txt', 'r') as f:
    x = f.read()
y=(x.count('#'))
print(y)
for i in range(33,40):
    print(y-i*15)
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
    m = []
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
    for i in range(len(tiles[frame][0])-1):
        temp.append(''.join(tiles[frame][j][i] for j in range(len(tiles[frame])-1, -1, -1)))
    tiles[frame] = temp
def lrotate(frame):
    temp = []
    for i in range(len(tiles[frame][0])-1, -1, -1):
        temp.append(''.join(tiles[frame][j][i] for j in range(len(tiles[frame]))))
    tiles[frame] = temp

def rotate_index(frame, side, endside, reverse):
    if endside==side:
        vflip(frame)
    elif endside==(side+1)%4:
        rrotate(frame)
    elif endside==(side+2)%4:
        pass
    elif endside==(side+3)%4:
        lrotate(frame)
    """
    if side == 0:
        if endside==0:
            vflip(frame)
        elif endside==1:
            rrotate(frame)
        elif endside==2:
            pass
        elif endside==3:
            lrotate(frame)
    elif side ==1:
        if endside==1:
            vflip(frame)
        elif endside==2:
            rrotate(frame)
        elif endside==3:
            pass
        elif endside==0:
            lrotate(frame)
    elif side ==2:
    elif side==3:
            """
    if reverse==-1:
        if side %2 == 0:
            hreverse(frame)
        elif side%2==1:
            vflip(frame)

"""
print('\n'.join(tiles[1427]))
lrotate(1427)
print()
print('\n'.join(tiles[1427]))
"""



alltiles = {}
grid = {}
visited = []
def explore_tiles(t1):
    if t1 in visited:
        return
    visited.append(t1)
    sides = {}
    for side in range(4):
        t2, s2, orientation = get_match(t1, side)
        #print(side,':',t2, s2, orientation)
        if orientation:
            rotate_index(t2, side, s2, orientation)
            explore_tiles(t2)
            sides[side] = t2
    alltiles[t1] = sides



explore_tiles(3557)
print('\n'.join(str(x) for x in alltiles.items()))







@lru_cache(maxsize=None)
def translate(direction, orientation, reverse):
    x = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    return x[(direction+orientation)%4]

@lru_cache(maxsize=None)
def translate_side(direction, orientation):
    return (direction+orientation+2)%4 if direction% 2==0 else (direction+orientation)%4
visited=[]
def create_grid(x,y, tile):
    point = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
    if tile in visited:
        #print(tile,'visited')
        return
    if tile not in grid:
        grid[tile] = (x,y)
    visited.append(tile)

    for side, frame in alltiles[tile].items():
        if frame not in grid:
            print(frame,x,y, x+point[side][0],y+point[side][1])
            grid[frame] = x+point[side][0],y+point[side][1]
    for side, frame in alltiles[tile].items():
        create_grid(x+point[side][0],y+point[side][1],frame)

for i in alltiles:
    create_grid(0,0, i)
    break

#create_grid(0,0, 3079)
print(grid)

