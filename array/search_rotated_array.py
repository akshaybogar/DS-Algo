def search_element(arr, n, key):
    pivot = find_pivot(arr, 0, n-1)
    if(pivot == -1):
        return binary_search(arr, 0, n-1, key)
    if(arr[pivot] == key):
        return pivot
    if(key >= arr[0]):
        return binary_search(arr, 0, pivot-1, key)
    return binary_search(arr, pivot+1, n-1, key)

def find_pivot(arr, low, high):
    if(high < low):
        return -1
    if(high == low):
        return low
    mid = int((low+high)/2)
    if(mid < high and arr[mid]>arr[mid+1]):
        return mid
    if(low < mid and arr[mid]<arr[mid-1]):
        return mid-1
    if(arr[low] >= mid):
        find_pivot(arr, 0, mid-1)
    find_pivot(arr, mid+1, high)

def binary_search(arr, low, high, key):
    if(high < low):
        return -1
    mid = int((low+high)/2)
    if(arr[mid] == key):
        return mid
    elif(arr[mid] < key):
        return binary_search(arr, mid+1, high, key)
    else:
        return binary_search(arr, low, mid-1, key)

if(__name__ == '__main__'):
    idx = search_element([3,4,5,1,2], 5, 3)
    print('Element found at index {}'.format(idx))
