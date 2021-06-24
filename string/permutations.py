def print_string(l):
    print(''.join(l))

def permute(a, l, r):
    if l == r:
        print_string(a)
    else:
        for i in range(l, r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

s = 'ABCD'
permute(list(s), 0, len(s))