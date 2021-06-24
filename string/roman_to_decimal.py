def roman_to_decimal(rno):
    roman_decimal_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    decimal_number = 0
    for ch in rno:
        decimal_number += roman_decimal_map[ch]
    return decimal_number

rno = 'MVIII'
print('Decimal equivalent of {} is {}'.format(rno, roman_to_decimal(rno)))