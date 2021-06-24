def longest_palindromic_substring(s):
    low, high = 0, 0
    maxlength = 1
    length = len(s)
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxlength:
                maxlength = high - low + 1
                start = low
            low = low - 1
            high = high + 1
        
        low = i - 1
        high = i + 1
        while low >= 0 and high < length and s[low] == s[high]:
            if high - low + 1 > maxlength:
                maxlength = high - low + 1
                start = low
            low = low - 1
            high = high + 1
    
    return s[start:start+maxlength]

s = 'abradaracdnfj'
print(longest_palindromic_substring(s))
