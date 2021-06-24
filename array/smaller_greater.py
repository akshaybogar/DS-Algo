def smaller_greater(arr):
    n = len(arr)
    leftmax = [None] * n
    leftmax[0] = float('-inf')

    for i in range(1, n):
        leftmax[i] = max(leftmax[i-1], arr[i-1])
    print(leftmax)

    rightmin = float('inf')

    for i in range(n-1, -1, -1):
        if leftmax[i] < arr[i] and rightmin > arr[i]:
            return i
        rightmin = min(rightmin, arr[i])

    return -1

arr = [5, 1, 4, 3, 6, 8, 10, 7, 9]
print(smaller_greater(arr))
