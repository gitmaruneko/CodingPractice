#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional
import math

# Intuition 
# reverse input string words and seperate them with space 
#
# Approach
# use string function "split" to split string then store them into list and reversed
# remove space item from list then combine them into string 
#
# Complexity 
# -  Time complexity : O(N)
# - Space complexity : O(1)
#
# Runtime 41ms

class Solution:
    def reverseWords(self, s: str) -> str:
        # rev = list(reversed(s.split(" ")))
        # # cleaned_list = [s for s in rev if s.strip()]
        # cleaned_list = []
        # for s in rev:
        #    stripped_string = s.strip()
        #    if stripped_string:
        #        cleaned_list.append(s)
        # cleaned = " ".join(cleaned_list)

        # return cleaned
    
# solution2  - Space complexity: O(1)
        rev = list(reversed(s.split(" ")))
        write_index = 0
        for i in range(len(rev)):
            # 如果元素不是空白或僅包含空白字符，則將其移動到 write_index 位置
            if rev[i].strip():
                rev[write_index] = rev[i]
                write_index += 1
        # 刪除多餘的元素
        del rev[write_index:]
        cleaned = " ".join(rev)

        return cleaned

        
        




if __name__ == "__main__":
    s1 = Solution()
    print(s1.reverseWords("  hello world  "))





