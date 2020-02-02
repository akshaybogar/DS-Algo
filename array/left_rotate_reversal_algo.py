def reverse_array(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1

def left_rotate(arr, d, n):
    if(d==0):
        return
    reverse_array(arr, 0, d-1)
    reverse_array(arr, d, n-1)
    reverse_array(arr, 0, n-1)

if(__name__ == '__main__'):
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    d = 0
    d = d % n
    left_rotate(arr, d, n)
    print(arr)
