def subarray_with_given_sum(arr, given_sum):
    start, i, n = 0, 1, len(arr)
    cur_sum = arr[0]

    while i < n:
        while cur_sum > given_sum and start < i-1:
            cur_sum = cur_sum - arr[start]
            start += 1
        if cur_sum == given_sum:
            print('Sub array found between {} and {}'.format(start, i-1))
            return
        else:
            cur_sum = cur_sum + arr[i]
            i += 1
    print('Subarray with given sum not found')
    return

def subarray_with_given_sum_negative(arr, given_sum):
    cur_sum, Map = 0, {}
    for i in range(len(arr)):
        print(Map)
        cur_sum += arr[i]
        if cur_sum == given_sum:
            print('Array found at indices {} and {}'.format(0, i))
            return
        if cur_sum - given_sum in Map:
            print('Array found at indices {} and {}'.format(Map[cur_sum-given_sum]+1, i))
            return
        Map[cur_sum] = i
    print('Array not found!')
    return


arr = [-2, 3, -5, 6, -1, 3]
given_sum = 5
subarray_with_given_sum_negative(arr, given_sum)