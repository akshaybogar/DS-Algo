def get_leaders_array(arr):
    larr = [arr[-1]]
    prev_max = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > prev_max:
            larr.append(arr[i])
            prev_max = arr[i]
    return larr

arr = [1,6,17,4,3,5,2]
print(get_leaders_array(arr))