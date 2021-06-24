def get_equilibrium_point(arr):
    tsum = sum(arr)
    lsum = 0
    for i, val in enumerate(arr):
        tsum -= val
        if tsum == lsum:
            return i
        lsum += val
    return None

arr = [1,3,5,2,2]
idx = get_equilibrium_point(arr)
if not idx:
    print('No equilibrium point')
else:
    print('Equilibrium point at index %s' % idx)