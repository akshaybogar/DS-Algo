from queue import LifoQueue

def next_greater_element(arr):
    stack = LifoQueue()
    for val in arr:
        if stack.empty():
            stack.put(val)
        else:
            while not stack.empty():
                pop_ele = stack.get()
                if val > pop_ele:
                    print('{} -> {}'.format(pop_ele, val))
                else:
                    stack.put(pop_ele)
                    break
            stack.put(val)
    while not stack.empty():
        pop_ele = stack.get()
        print('{} -> -1'.format(pop_ele))


arr = [1,2,3,4,5]
next_greater_element(arr)