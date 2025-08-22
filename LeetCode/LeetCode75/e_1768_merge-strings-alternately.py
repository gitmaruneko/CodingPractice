#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional

# Intuition 
# Merge two strings one character at a time, alternating between str1 and str2.
#
# Approach
# Use a for loop to iterate through str1, adding characters from str1 first. Then compare the lengths of str1 and str2.
# If str1 is shorter than str2 and the current character is the last one in str1, add the remaining characters from str2, and vice versa.
# 
# Complexity 
# -  Time complexity : O(N)
# - Space complexity : O(N)
#
# Runtime 27ms

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ''
        for i in range(len(word1)):
            merged += word1[i]
            if len(word1) > len(word2) and i == len(word2):
                merged += word1[i+1:]
                break
            elif len(word1) < len(word2) and i == len(word1)-1:
                merged += word2[i:]
                break
            else:
                merged += word2[i]
        return merged
    
# solution 2 - runtime 31ms, 
        # i=0
        # j=0
        # res=""
        # while i<len(word1) and j<len(word2):
        #     res+= word1[i] + word2[j]
        #     i+=1
        #     j+=1
        
        # while i <len(word1):
        #     res+=word1[i]
        #     i+=1

        # while j <len(word2):
        #     res+=word2[j]
        #     j+=1

        # return res

if __name__ == "__main__":
    s1 = Solution()
    print(s1.mergeAlternately("ab", "pqrs")) #apbqrs
    print(s1.mergeAlternately("abcd", "pq")) #apbqcd





