def reverse_array_in_given_size(arr, k):
    i, n = 0, len(arr)
    while i < n:
        left = i
        right = min(i+k-1, n-1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i += k
        

arr = [1,2,3,4,5]
k = 3
reverse_array_in_given_size(arr, k)
print(arr)