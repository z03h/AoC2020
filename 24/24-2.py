with open('d', 'r') as f:
    directions = f.read().splitlines()

from collections import defaultdict

tiles = defaultdict(lambda: True)
#directions = ['esewnw', 'nwwswee']
def parse_d(ds):
    directions=defaultdict(lambda: 0)
    i = iter(ds)
    current = ''
    while 1:
        try:
            current = next(i)
            if current in ('e','w'):
                directions[current] += 2
            else:
                current += next(i)
                if current in ('nw','ne', 'sw','se'):
                    for letter in current:
                        directions[letter] += 1
                else:
                    print(current, 'WRONG')
            current = ''
        except StopIteration:
            if current:
                if current in ('e','w'):
                    directions[current] += 2
                elif current in ('nw','ne', 'sw','se'):
                    for letter in current:
                        directions[letter] += 1
                else:
                    print(current, 'WRONG')
            break
    return directions

for d in directions:
    dd = parse_d(d)
    ns, ew = dd['n']-dd['s'], dd['e']-dd['w']
    tiles[(ns,ew)] = not tiles[(ns,ew)]

def get_adjacent(coord):
    y,x = coord
    return [(y+yy,x+xx) for yy,xx in ((0,2), (0,-2), (1,1), (-1,1), (1,-1), (-1,-1))]
def new_tile_color(itiles, coord):
    adj = get_adjacent(coord)
    blacktiles = sum(not itiles[c] for c in adj)

    if itiles[coord]:
        #white
        return False if blacktiles == 2 else True
    else:
        #black
        return True if (blacktiles ==0 or blacktiles > 2) else False


def flip_all(itiles):
    newtiles = defaultdict(lambda: True)
    for coord, color in [(c,cc) for c, cc in itiles.items()]:
        if color:
            continue
        newcolor = new_tile_color(itiles, coord)
        if not newcolor:
            newtiles[coord] = False
        for adjcoord in get_adjacent(coord):
            newcolor = new_tile_color(itiles, adjcoord)
            if not newcolor:
                newtiles[adjcoord] = False
    return newtiles

for _ in range(100):
    tiles = flip_all(tiles)
print(sum(not x for x in tiles.values()))

