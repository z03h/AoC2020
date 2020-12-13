x = '''1006697
13,x,x,41,x,x,x,x,x,x,x,x,x,641,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,661,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'''

xx = '''939
7,13,x,x,59,x,31,19'''
ts, busses = x.split('\n')
ts=int(ts)
busses = [int(b) for b in busses.split(',') if b!='x']
def min_take(num):
    q, r = divmod(ts, num)
    pp = (q+1)*num
    print(pp)
    return pp, 0, (pp-ts)*num
print(min_take(min(busses, key=min_take)))
