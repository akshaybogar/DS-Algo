def find_min_element(arr, low, high):
    if(high < low):
        return arr[0]
    if(high==low):
        return arr[low]
    mid = int((low + high)/2)
    if(mid < high and arr[mid] > arr[mid+1]):
        return arr[mid+1]
    if(low < mid and arr[mid] < arr[mid-1]):
        return arr[mid]
    if(arr[high] > arr[mid]):
        return find_min_element(arr, low, mid-1)
    return find_min_element(arr, mid+1, high)

if(__name__ == '__main__'):
    arr = [4,5,1,2,3]
    print(find_min_element(arr, 0, len(arr)-1))
