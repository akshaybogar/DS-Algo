def cyclic_rotate(arr, n):
    temp = arr[n-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = temp

if(__name__ == '__main__'):
    arr = [1,2,3,4,5]
    no_rotations = 2
    for i in range(no_rotations):
        cyclic_rotate(arr, len(arr))
    print(arr)
