from collections import OrderedDict

od = OrderedDict()
arr = [7,0,25,6,16,17,0]
k = 3
for val in arr:
    if val in od:
        od[val] += 1
    else:
        od[val] = 1

print(od)
cnt = 0
for k in od:
    cnt += od[k]
    if cnt > k:
        print(od[k])
 