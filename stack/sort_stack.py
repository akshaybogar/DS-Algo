def sorted_insert(stack, ele):
    if not stack or stack[-1] < ele:
        stack.append(ele)
    else:
        pop_ele = stack.pop()
        sorted_insert(stack, ele)
        stack.append(pop_ele)

def sort_stack(stack):
    if stack:
        pop_ele = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, pop_ele)

stack = []
stack.extend([3,5,1,6,7,-3,0])
print('Original stack', stack)
sort_stack(stack)
print('Sorted stack', stack)