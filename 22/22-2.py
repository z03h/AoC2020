with open('input', 'r') as f:
    lines = f.read()
p1, p2 = lines.split('\n\n')

from collections import deque
pp1 = [int(i) for i in p1.splitlines()]
pp2 = [int(i) for i in p2.splitlines()]
def play_decks(p1, p2, count):
    played_combos = set()
    print('start game', count)
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        table_cards = [c1,c2]
        winner = 0
        if c1 <= len(p1) and c2 <= len(p2):
            #sub game
            sub_winner, _ = play_decks(p1[:c1], p2[:c2], count+1)
            if sub_winner:
                table_cards.reverse()
            winner = (p1,p2)[sub_winner]
        elif (tuple(p1),tuple(p2)) in played_combos:
            #already played combo
            print('recruse')
            return 0,(p1,p2)
        else:
            #normal check
            if c2 > c1:
                table_cards.reverse()
                winner = p2
            else:
                winner = p1
        played_combos.add((tuple(p1), tuple(p2)))
        winner.extend(table_cards)
    return (0,(p1,p2)) if p1 else (1,(p1,p2))



final_winner, decks = play_decks(pp1,pp2, 0)
final_winner = decks[final_winner]
print('1=', ' '.join(str(x) for x in decks[0]))
print('2=', ' '.join(str(x) for x in decks[1]))
score = sum(i*num for i, num in enumerate(reversed(final_winner), 1))
print(score)


