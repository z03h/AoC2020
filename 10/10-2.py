x = '''145
3
157
75
84
141
40
20
60
48
15
4
2
21
129
113
54
28
69
42
34
1
155
63
151
8
139
135
33
81
70
132
150
112
102
59
154
53
144
149
116
13
41
156
85
22
165
51
14
125
52
64
16
134
110
71
107
124
164
160
10
25
66
74
161
111
122
166
140
87
126
123
146
35
91
106
133
26
77
19
86
105
39
99
76
58
31
96
78
88
168
119
27
45
9
92
138
38
97
32
7
98
167
95
55
65'''
import functools

x = x.split('\n')

x =[0] +[int(i) for i in x]
x.sort()
x += [max(x)+3]
end = max(x)+3
diff = {1:0, 3:0}

total = 0
"""
@functools.lru_cache
def validstart(index, num):
    global total
    if num+3 == end or index == len(x)-1:
        print('ENDED')
        time.sleep(3)
        return True, 1
    else:
        viable = [(x.index(v),v) for v in x[index+1:index+4] if 1<= v-num <=3]
        found = False
        inner_sum = 0
        for i in viable:
            good, num = validstart(*i)
            if good:
                total += num
                inner_sum+=num
        if inner_sum:
            print(index, num, 'SUMMED', inner_sum)
            return True, inner_sum
        else:
            return False, inner_sum
"""
ci = 100
#print(validstart(0, x[0]))
#print(total)

#index : count
valid_jumps = {}
# uh get valid indexes that can jump to this index?
#create dict of index: indexes that can jump to here?
for i in range(len(x)-1, -1, -1):
    valid_jumps[i] = [x.index(num) for num in x if 1<=(x[i]-num)<=3]
print(valid_jumps)
#start from end?
cache = {0:0}
@functools.lru_cache
def valid(index):
    if index == 0:
        return 1
    else:
        """
        #not original solution, but alt to @lru cache
        try:
            return cache[index]
        except KeyError:
            pass
        """
        s = 0
        for i in valid_jumps[index]:
            s += valid(i)
        cache[index] = s
        return s

print(valid(len(x)-1))
