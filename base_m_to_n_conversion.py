baseArray = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
    'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

def all_chars_in_list(s, char_list):
    return all(char in char_list for char in s)

def base_n_to_base_10(baseString, base_n):
    value = 0
    if not all_chars_in_list(baseString, baseArray):
        return 0

    for i, char in enumerate(reversed(baseString)):
        digit = baseArray.index(char)
        value += digit * (base_n ** i)
    return value

def base_10_to_base_m(number, base_m):
    if number == 0:
        return baseArray[0]

    value = ""
    while number > 0:
        mod = number % base_m
        number //= base_m
        value += baseArray[mod]
    
    return value[::-1] 

def base_n_to_base_m(string, base_n, base_m):
    final_value = 0
    value_base_10 = base_n_to_base_10(string, base_n)
    value_base_8 = base_10_to_base_m(value_base_10, base_m)
    final_value = value_base_8
    return final_value

print(base_n_to_base_m("1A3", 11, 8))