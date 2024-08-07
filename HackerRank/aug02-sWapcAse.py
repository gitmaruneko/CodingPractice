#!/bin/python3


def swap_case(s):
    s_list = []
    s_convert = ''
    for char in s:
        if char.isupper():
            s_list.append(char.lower())
        elif char.islower():
            s_list.append(char.upper())
        else:
            s_list.append(char)
    
    return s_convert.join(s_list)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#solution 1



# solution opt

