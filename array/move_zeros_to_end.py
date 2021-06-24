def move_zeros_to_end(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[cnt] = arr[i]
            cnt += 1
    while cnt < len(arr):
        arr[cnt] = 0
        cnt += 1

arr = [1,0,5,0,9,4,0,5,6]
move_zeros_to_end(arr)
print(arr)