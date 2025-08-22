#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# The goal is to to count characters requence and return an array with characters and apear times 

# Approach
# 1. create new array
# 2. use two poiinter left and right to count characters


# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


from typing import List


class Solution(object):
    def compress(self, chars: List[str]) -> int:
        result = []
        l, r = 0, 1
        cnt = 1
        length = len(chars) -1
        if len(chars) == 1:
            return chars
        while l <= r and r <= length:
            if chars[l] == chars[r]:
                cnt += 1
                r += 1
            else: 
                result.append(chars[l])
                result.append(str(cnt))

                l = r
                r = r+1
                cnt = 1

        result.append(chars[l])
        result.append(str(cnt))

        
        return len(result)

                


        

s1 = Solution()
print(s1.compress(["a","a","b","b","c","c","c"])) #[a,2,b,2,c,3]
print(s1.compress(["a"])) #["a"]