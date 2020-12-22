with open('input', 'r') as f:
    lines = f.read()
p1, p2 = lines.split('\n\n')

from collections import deque
p1 = deque(int(i) for i in p1.splitlines())
p2 = deque(int(i) for i in p2.splitlines())

while p1 and p2:
    c1 = p1.popleft()
    c2 = p2.popleft()
    table_cards = [c1,c2]
    winner = 0
    if c2 > c1:
        table_cards.reverse()
        winner = p2
    else:
        winner = p1
    winner.extend(table_cards)
print('1=', ' '.join(str(x) for x in p1))
print('2=', ' '.join(str(x) for x in p2))

winner = p1 or p2

score = sum(i*num for i, num in enumerate(reversed(winner), 1))
print(score)


