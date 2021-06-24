def search(arr, l, r, k):
    if l > r:
        return False
    mid = (l+r)//2
    if arr[mid] == k:
        return True
    if arr[mid] > arr[l]:
        if k >= arr[l] and k <= arr[mid]:
            return search(arr, l, mid-1, k)
        else:
            return search(arr, mid+1, r, k)
    else:
        if k >= arr[mid] and k <= arr[r]:
            return search(arr, mid+1, r, k)
        else:
            return search(arr, l, mid-1, k)


arr = [3,4,5,6,7,8,9,10,1,2]
k = 1
print(search(arr, 0, len(arr)-1, 2))