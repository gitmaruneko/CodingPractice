#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional
import math

# Intuition 
# Given two strings str1 and str2, return the largest string x that x divides both str1 and str2 
#
# Approach
# find shorter str and see if long str strat with short one to find gcd
# 
#
# Complexity 
# -  Time complexity : O(N)
# - Space complexity : O(1)
#
# Runtime 37ms

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1 + str2 != str2 + str1:
            return ""
        
        # Find the GCD of the lengths of str1 and str2
        gcd_length = math.gcd(len(str1), len(str2))
        
        # Return the substring of str1 up to the GCD length
        return str1[:gcd_length]

# solution 3 - recurssion
        # if len(str1) < len(str2):
        #     return self.gcdOfStrings(str2, str1)
        # # 如果 str1 不以 str2 开头，返回空字符串
        # if not str1.startswith(str2):
        #     return ""
        # # 如果 str2 为空，返回 str1
        # if not str2:       
        #     return str1
        # # 递归调用，减去 str2 的部分
        # return self.gcdOfStrings(str1[len(str2):], str2)

     

    


if __name__ == "__main__":
    s1 = Solution()
    # print(s1.gcdOfStrings("ABCABC", "ABC"))
    # # print(s1.gcdOfStrings("ABABAB", "ABAB")) 
    # print(s1.gcdOfStrings("LEET", "CODE"))
    print(s1.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
    # s1.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX")







   

    


if __name__ == "__main__":
    s1 = Solution()
    print(s1.kidsWithCandies([4,2,1,1,2]))






