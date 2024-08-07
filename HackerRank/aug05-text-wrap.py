#!/bin/python3
import textwrap

def wrap(string, max_width):
    string_list = list(string)
    result = ''
    s_grp = ''
    result_grp = []
    s_len = len(string)
    cnt = 1
    for char in string_list:
        s_grp += char 
        if (cnt % max_width == 0) or (cnt == s_len):
            result_grp.append(s_grp)
            s_grp = ''
        cnt += 1
    
    for s_unit in result_grp:
        if s_unit != result_grp[-1]:
            result += s_unit + '\n'
        else:
            result += s_unit

    return result

# opt 1
    # return textwrap.fill(string, max_width)
# opt 2
    # for i in range(0, len(string), max_width):
    #     print(string[i : i + max_width])




if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result, end = '')