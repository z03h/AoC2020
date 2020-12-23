cups = [1,8,6,5,2,4,9,7,3] + list(range(10, 1000001))
#cups = [3,8,9,1,2,5,4,6,7]
mincup = min(cups)
maxcup = max(cups)
class Node:
    def __init__(self, baselist, value, left, right):
        self.baselist = baselist
        self.value = value
        self.left = left
        self.right = right
    def node(self):
        return self.baselist[self.value]
    def left_node(self):
        return self.baselist[self.left]
    def right_node(self):
        return self.baselist[self.right]
    def __repr__(self):
        return f'<{self.left}|{self.value}|{self.right}>'


current = None
dcups = {}
for index, num in enumerate(cups):
    left = cups[index-1] if index>0 else None
    try:
        right = cups[index+1]
    except:
        right = current.value
    dcups[num] = Node(dcups, num, left, right)
    if left is None:
        current = dcups[num]
dcups[cups[0]].left = maxcup
count = 0
for _ in range(10_000_000):
    count+=1
    if count % 1_000_000 == 0:
        print(count, flush=True)
    l1 = current.right_node()
    l2 = l1.right_node()
    l3 = l2.right_node()
    rcurrent = l3.right_node()
    current.right = rcurrent.value
    rcurrent.left = current.value
    moveto = current.value - 1
    if moveto < mincup:
            moveto = maxcup
    while moveto in (l1.value, l2.value, l3.value):
        moveto -= 1
        if moveto < mincup:
            moveto = maxcup
    moveL = dcups[moveto]
    moveR = moveL.right_node()
    moveL.right = l1.value
    l1.left = moveL.value
    moveR.left = l3.value
    l3.right = moveR.value
    current = rcurrent
oner = dcups[1].right_node()
onerr = oner.right_node()
print(oner, onerr, oner.value*onerr.value)
