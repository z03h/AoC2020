num = '6,4,12,1,20,0,16'
numm = '0,3,6'


num = [int(i) for i in num.split(',')]
nums = num.copy()
lastindex = {v:[i] for i,v in enumerate(nums)}
count = 0



while 1:
    count += 1
    length = len(nums)
    lastnum = nums[length-1]
    #print(nums)
    countof  =  nums.count(lastnum)

    if countof > 1:
        #print(f'{length-1}-{lastindex[lastnum][-2]}', lastindex)
        newnum = length -1- lastindex[lastnum][-2]
        nums.append(newnum)
        #print('\tnewnum', newnum)
        lastindex.setdefault(newnum, []).append(length)
    elif countof == 1:
        nums.append(0)
        lastindex[0].append(length)
        #print('\tzero')

    if len(nums) == 2020:
        break
print(nums[2019])
