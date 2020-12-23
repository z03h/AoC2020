cups = [1,8,6,5,2,4,9,7,3]
#cups = [3,8,9,1,2,5,4,6,7]
mincup = min(cups)
maxcup = max(cups)
for _ in range(100):
    current = cups.pop(0)
    cups.append(current)
    pickup = [cups.pop(0) for i in range(3)]
    dest = current -1
    while dest not in cups:
        dest -= 1
        if dest < mincup:
            dest = maxcup
    index = cups.index(dest)+1
    newcups = cups[:index]
    newcups.extend(pickup)
    newcups.extend(cups[index:])
    cups = newcups
print(cups)
index_one = cups.index(1)
end_cups = cups[index_one+1:]
end_cups.extend(cups[:index_one])
print(''.join(str(x) for x in end_cups))
