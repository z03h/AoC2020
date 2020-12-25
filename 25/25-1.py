pk1 = 8458505
pk2 = 16050997

s1 = 7
s2 = 7

#pk1 = 5764801
#pk2 = 17807724


loop_div = 20201227
def brute(subject, pk):
    loop = 1
    temp_pk = 1
    while True:
        temp_pk = (temp_pk*subject) % loop_div
        if temp_pk== pk:
            break
        loop+=1
    return loop
L1 = brute(s1, pk1)
L2 = brute(s2, pk2)
print(L1, L2)
def unbrute(s, loop):
    temp = 1
    for _ in range(loop):
        temp = (temp * s) % loop_div
    return temp
k1 = unbrute(pk1, L2)
k2 = unbrute(pk2, L1)
print(k1, k2)
