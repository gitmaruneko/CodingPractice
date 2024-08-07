#!/bin/python3


# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.


if __name__ == '__main__':
    s = input()
    hasAN = False
    hasAB = False
    hasD = False
    hasU = False
    hasL = False

    for char in s:
        asc_value = ord(char)
        if asc_value > 64 and asc_value < 91:
            hasAN = True
            hasAB = True
            hasU = True
        if asc_value > 96 and asc_value < 123:
            hasAN = True
            hasAB = True
            hasL = True
        if  asc_value > 47 and asc_value < 58:
            hasAN = True
            hasD = True

    print("%s\n%s\n%s\n%s\n%s\n"%(hasAN, hasAB, hasD, hasL, hasU))


#opt
    # print(any(char.isalnum() for char in s))
    # print(any(char.isalpha() for char in s))
    # print(any(char.isdigit() for char in s))
    # print(any(char.islower() for char in s))
    # print(any(char.isupper() for char in s))