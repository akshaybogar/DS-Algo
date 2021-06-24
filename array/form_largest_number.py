from itertools import permutations

def form_largest_number(arr):
    nums = []
    for num in permutations(arr, len(arr)):
        nums.append(''.join(map(str, num)))
    return max(nums)

arr = [54, 546, 548, 60]
print(form_largest_number(arr))