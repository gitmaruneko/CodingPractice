#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    name = s.split(' ')
    result = ''
    new_name = []
    for item in name:
        if len(item) != 0 and item[0].isalpha():
            new_name.append(re.sub(r"\w", item[0].upper(), item, count=1))
        else:
            new_name.append(item)

    result = " ".join(new_name)
    print(result)
# opt
    # for word in s.split():
    #     s = s.replace(word, word.capitalize())
    # return s

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()