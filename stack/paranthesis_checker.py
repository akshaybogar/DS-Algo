from queue import LifoQueue

def match(ch1, ch2):
    if ch1 == '[' and ch2 == ']':
        return True
    elif ch1 == '{' and ch2 == '}':
        return True
    elif ch1 == '(' and ch2 == ')':
        return True
    return False

def paranthesis_checker(s):
    stack = LifoQueue()
    for ch in s:
        if ch in ['[', '{', '(']:
            stack.put(ch)
        else:
            if stack.empty():
                return False
            pop_ele = stack.get()
            if not match(pop_ele, ch):
                return False
    if stack.empty():
        return True
    else:
        return False

s = '((((((((())))))'
print(paranthesis_checker(s))
