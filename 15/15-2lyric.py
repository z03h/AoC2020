#lyricly solution, for reference and test comparison

num = '6,4,12,1,20,0,16'
numm = '0,3,6'

data =  list(map(int, numm.split(',')))

import time
start = time.time()
from collections import defaultdict
base = 0
been_since = defaultdict(int)
for t in data:
    base += 1
    been_since[t] = base
last_bean = base


for _ in (range(20-len(data))):
    a = base-last_bean
    print('a', a, 'base', base)
    base += 1
    last_bean = been_since[a]
    print('last_bean', last_bean)
    if last_bean == 0:
        last_bean = base
    been_since[a] = base

print(a)
print(time.time()-start)
