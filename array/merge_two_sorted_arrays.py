def merge_two_sorted_arrays(arr1, arr2):
    m, n = len(arr1), len(arr2)
    for i in range(n-1, -1, -1):
        last = arr1[m-1]
        j = m-2
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j+1] = arr1[j]
            j = j - 1
        if j != m-2 or last > arr2[i]:
            arr1[j+1] = arr2[i]
            arr2[i] = last

arr1 = [1,5,9,10,150,200]
arr2 = [2,3,8,13]

merge_two_sorted_arrays(arr1, arr2)
print(arr1)
print(arr2)