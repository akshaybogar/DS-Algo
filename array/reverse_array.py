def reverse_array(arr):
    start, end = 0, len(arr)-1
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverse_array_recursive(arr, start, end):
    if start > end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array_recursive(arr, start+1, end-1)


arr = [1,2,3,4,5,6,7]
#print(reverse_array(arr))
reverse_array_recursive(arr, 0, len(arr)-1)
print(arr)
