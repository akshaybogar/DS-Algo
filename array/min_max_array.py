def find_min_max(arr, low, high):
    arr_min, arr_max = arr[low], arr[low]
    #If the divided array contains only one element both arr_min and arr_max will be the first element
    if low == high:
        arr_min, arr_max = arr[low], arr[low]
        return (arr_min, arr_max)
    #If the divided array contains two elements then make 2 comparisons for finding arr_min and arr_max
    elif low+1 == high:
        if arr[low] > arr[high]:
            arr_min, arr_max = arr[high], arr[low]
        else:
            arr_min, arr_max = arr[low], arr[high]
        return (arr_min, arr_max)
    #If the array has more than 2 elements then divide the array recursively until they have either 1 or 2 elements
    else:
        mid = int((low+high)/2)
        arr_min1, arr_max1 = find_min_max(arr, low, mid)
        arr_min2, arr_max2 = find_min_max(arr, mid+1, high)
    #Compare the minimum and maximum of divided arrays and return minimum and maximum elements of the array
    return (min(arr_min1, arr_min2), max(arr_max1, arr_max2))


arr = [100, 11, 445, -1, 330, 3000]
if not arr:
    print('Given array is empty!')
else:
    min_max = find_min_max(arr, 0, len(arr)-1)
    print('Min element: {} and Max element: {}'.format(min_max[0], min_max[1]))
