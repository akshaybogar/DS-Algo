def get_max_element(arr, l, h):
    if l == h:
        return arr[l]
    if h == l+1:
        return max(arr[l], arr[h])
    mid = (l+h)//2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    if arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        return get_max_element(arr, mid+1, h)
    else:
        return get_max_element(arr, l, mid-1)

arr = [6,9,15,25,35,50,41,29,23,8]
print('Max element - {}'.format(get_max_element(arr, 0, len(arr)-1)))