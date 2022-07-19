#!/usr/bin/python3

ROMAN = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
         "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
         "D": 500, "CM": 900, "M": 1000}


def roman_to_int(roman_string):
    result = 0
    if not isinstance(roman_string, str):
<<<<<<< HEAD
        return 0
    if not roman_string.isupper():
        return 0 

    # Dictionary for roman numerals
  
    r_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    result = 0
    temp = list(roman_string)
    
    # Concat 4 and 9s
    
    if len(temp) > 1:
        idx = 0
        for i in temp:
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'V':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            try:
                if temp[idx] == 'I' and temp[idx + 1] == 'X':
                    temp[idx:idx + 2] = [''.join(temp[idx:idx + 2])]
            except IndexError:
                pass
            idx += 1
    # Search in dict for correct numbers and add
    for k, v in r_dict.items():
        for index in temp:
            if index == k:
                result += v
=======
        return result

    r_numeral = ROMAN.keys()
    n = len(roman_string)
    i = 0
    while i < n:
        check1 = roman_string[i:i+2]
        check2 = roman_string[i]
        if check1 in r_numeral:
            result += ROMAN.get(check1)
            i += 2
        elif check2 in r_numeral:
            result += ROMAN.get(check2)
            i += 1

>>>>>>> 40b844185fb1401a52c76f76bfb8298f005ea6b7
    return result
