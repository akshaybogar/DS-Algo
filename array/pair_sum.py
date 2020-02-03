def pair_sum_sorted(arr, val):
    l, r = 0, len(arr)-1
    while(l < r):
        if(arr[l] + arr[r] == val):
            return True
        elif(arr[l] + arr[r] < val):
            l+=1
        else:
            r+=1
    return False

if(__name__ == '__main__'):
    li = [1,2,3,4,5]
    if(pair_sum_sorted(li, 10)):
        print('Pair found')
    else:
        print('No pair found')
