from collections import deque

def insert_at_bottom(stack, ele):
    if not stack:
        stack.append(ele)
    else:
        pop_ele = stack.pop()
        insert_at_bottom(stack, ele)
        stack.append(pop_ele)

def reverse_stack(stack):
    if stack:
        pop_ele = stack.pop()
        reverse_stack(stack)
        insert_at_bottom(stack, pop_ele)


stack = deque()
stack.extend([1,2,3,4,5])
print('Original stack', stack)
reverse_stack(stack)
print('After reversing the stack', stack)