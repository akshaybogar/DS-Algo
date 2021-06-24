def min_jumps(arr):
    if not arr:
        return -1
    a, b, jumps = arr[0], arr[0], 1
    for i in range(1, len(arr)):
        a = a - 1
        b = b - 1
        b = max(b, arr[i])
        if a == 0:
            jumps += 1
            a = b
    return jumps
        
arr = [1,3,5,8,9,2,6,7,6,8,9]
print('Min jumps - {}'.format(min_jumps(arr)))
