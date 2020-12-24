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

print(sum(not x for x in tiles.values()))
