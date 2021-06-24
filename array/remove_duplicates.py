def remove_duplicates(arr):
    i, s, n = 1, 1, len(arr)
    if not arr:
        return []
    elif n == 1:
        return arr
    elif n == 2:
        if arr[0] == arr[1]:
            return arr[:1]
    else:
        val = arr[0]
        while s < n:
            while arr[s] == val:
                s += 1
                continue
            arr[i] = arr[s]
            val = arr[i]
            i += 1
            s += 1
        return arr[:i]
        

arr = [1,1,2,2,3,3,3,3,3,3,3,4,6,8,8,9]
arr = remove_duplicates(arr)
print(arr)