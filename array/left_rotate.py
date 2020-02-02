def left_rotate(arr, d, n):
    d = d % n
    gcd = find_gcd(d, n)
    for i in range(gcd):
        temp = arr[i]
        j = i
        while True:
            k = j + d
            if(k>=n):
                k = k - n
            if(k==i):
                break
            arr[j] = arr[k]
            j = k
        arr[j] = temp

def find_gcd(a, b):
    if(b==0):
        return a
    return find_gcd(b, a%b)

if(__name__ == '__main__'):
    arr = [1,2,3,4,5]   #Feel free to change array elements
    left_rotate(arr, 3, len(arr))
    print(arr)
