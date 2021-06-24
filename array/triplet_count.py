def triplet_count(arr):
    freq = [0] * 100
    for i in range(len(arr)):
        freq[arr[i]] = 1
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if freq[arr[i]+arr[j]]:
                count += 1
    return count

arr = [2,3,7]
print(triplet_count(arr))