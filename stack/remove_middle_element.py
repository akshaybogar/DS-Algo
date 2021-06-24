from collections import deque

def remove_mid_ele_from_stack(stack, cur, n):
    if not stack or cur == n:
        return
    pop_ele = stack.pop()
    remove_mid_ele_from_stack(stack, cur+1, n)
    if cur != n//2:
        stack.append(pop_ele)

stack = deque()
for i in range(7):
    stack.append(i)
print('Before deleting mid element', stack)
remove_mid_ele_from_stack(stack, 0, len(stack))
print('After deleting mid element', stack)
stack.reverse()
print(stack)