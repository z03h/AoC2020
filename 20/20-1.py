with open('input.txt', 'r') as f:
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


#@lru_cache(maxsize=None)
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
    if {o, o[::-1]} & {p,p[::-1]}:
        return True
    return False

def get_match(t1, s1):
    m = []
    for t2 in tiles:
        if t1==t2:
            continue
        for j in range(4):
            if compare_sides(t1,s1, t2,j):
                m.append((t2,j))
    return m

tile2side = []
def printsides(i):
    for ii in range(4):
        print(get_match(i,ii))


#printsides(1951)

for t1 in tiles:
    count = 0
    for i in range(4):
        _ = get_match(t1, i)
        count += len(_)
    if count == 2:
        tile2side.append(t1)
print(tile2side)


