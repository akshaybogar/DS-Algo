def rearrange_array(arr):
    max_ele = arr[-1] + 1
    min_idx, max_idx = 0, len(arr)-1
    for i in range(len(arr)):
        if i%2 == 0:
            arr[i] += (arr[max_idx] % max_ele) * max_ele
            max_idx -= 1
        else:
            arr[i] += (arr[min_idx] % max_ele) * max_ele
            min_idx += 1
    #print(arr)
    for i in range(len(arr)):
        arr[i] //= max_ele

arr = [10,20,30,42,59]
rearrange_array(arr)
print(arr)