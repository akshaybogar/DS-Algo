from collections import OrderedDict

def remove_duplicates(s):
    final_string = ''
    set_chars = set()
    for ch in s:
        if ch not in set_chars:
            set_chars.add(ch)
            final_string += ch
    return final_string

def remove_duplicates_using_ordereddict(s):
    return ''.join(OrderedDict.fromkeys(s))

s = 'geeksforgeeks'
print(remove_duplicates_using_ordereddict(s))