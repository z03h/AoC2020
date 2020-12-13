x = '''13,x,x,41,x,x,x,x,x,x,x,x,x,641,x,x,x,x,x,x,x,x,x,x,x,19,x,x,x,x,17,x,x,x,x,x,x,x,x,x,x,x,29,x,661,x,x,x,x,x,37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,23'''
# chinese remainder theorum something something
x='7,13,x,x,59,x,31,19'
busses =  x.split(',')
mapping = {}
total = 1

for index, value in enumerate(busses):
    try:
        mapping[index] = int(value)
        total *= int(value)
    except ValueError:
        continue

print("total:",total)


def find_mod(mult, bus, index):
    current = 1
    while 1:
        x = (mult/bus) *current + index
        if (x%bus) ==  0:
            #print(' in',  x, x % bus, current)
            return current
        current += 1


running = 0
for index, bus in mapping.items():
#for index, bus in mapping:
    #print('={}, {}'.format(index, bus))
    m = (find_mod(total, bus, index))
    running += total/bus *m
    print('==found' , m, total/bus*m, running,'\n')
print(running % (total))



