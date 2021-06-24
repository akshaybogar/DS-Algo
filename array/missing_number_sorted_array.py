def missing_number_from_sorted_array(arr):
    freq = [0] * (arr[-1] + 1)
    for i in arr:
        freq[i] = 1
    for i in range(arr[0], arr[-1]):
        if not freq[i]:
            print(i, end=' ')
    print()
    return


arr = [0,2,4,5,19]
missing_number_from_sorted_array(arr)