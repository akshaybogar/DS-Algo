def pair_sorted_rotated(arr, val):
    n = len(arr)
    for i in range(n-1):
        if(arr[i] > arr[i+1]):
            break
    l, r = (i+1)%n, i
    while(l!=r):
        if(arr[l] + arr[r] == val):
            return True
        if(arr[l] + arr[r] < val):
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    return False

if(__name__ == '__main__'):
    li = [3,4,5,1,2]
    if(pair_sorted_rotated(li, 5)):
        print('Pair found')
    else:
        print('No pair found')
