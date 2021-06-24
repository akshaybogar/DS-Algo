def spiral_traversal(a, r, c):
    for i in range(r):
        if i % 2 == 0:
            for j in range(c):
                print(a[i][j], end=' ')
            print()
        else:
            for j in range(c-1, -1, -1):
                print(a[i][j], end=' ')
            print()

arr = [[1,2,3,4], [5,6,7,8]]
spiral_traversal(arr, 2, 4)