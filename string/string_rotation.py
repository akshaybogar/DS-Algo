def check_string_rotation(s1, s2):
    temp_string = s2[2:] + s2[:2]
    if s1 == temp_string:
        return True
    temp_string = s2[-2:] + s2[:-2]
    if temp_string == s1:
        return True
    return False

s1 = 'amazon'
s2 = 'azonam'
print(check_string_rotation(s1, s2))