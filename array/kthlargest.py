def quicksort(a, s, e, k):
    while True:
        if s > e:
            return
        p = s
        l =  s+1
        r = e
        while l <= r:
            print(a, p)
            if a[l] > a[p] and a[r] < a[p]:
                a[l], a[r] = a[r], a[l]
            if a[l] <= a[p]:
                l += 1
            if a[r] >= a[p]:
                r -= 1
        a[r], a[p] = a[p], a[r]
        if r == k:
            return a[r]
        if r > k:
            e = r - 1
        else:
            s = r + 1

def kthlargest(a, k):
    print(quicksort(a, 0, len(a)-1, len(a)-1))

a = [2,1,7,4,3]
kthlargest(a, 2)
    