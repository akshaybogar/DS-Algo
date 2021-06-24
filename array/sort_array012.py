def sortarray(arr):
    l, m, h = 0, 0, len(arr)-1
    while m <= h:
        if arr[m] == 1:
            m += 1
        elif arr[m] == 2:
            arr[m], arr[h] = arr[h], arr[m]
            h -= 1
        else:
            arr[m], arr[l] = arr[l], arr[m]
            m += 1
            l += 1
    return

arr = [2,1,2,2,1,0,0]
sortarray(arr)
print(arr)