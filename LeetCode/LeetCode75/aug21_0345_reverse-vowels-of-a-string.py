#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition 
# Given a string s, reverse only all the vowels in the string and return it.

# Approach
# use two pointer left and right, move left and right to vowels, switch position
#
# Complexity 
# - Time complexity: O()
# - Space complexity: O()


from typing import List


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # length = len(s)
        # left = 0
        # right = length - 1
        # vowels = "aeiouAEIOU"
        # move = list(s)
        

        # while left <= right:
        #     if move[left] in vowels and move[right] in vowels:
        #         tmp = move[left]
        #         move[left] = move[right]
        #         move[right] = tmp
        #         right -= 1
        #     elif move[left] in vowels and move[right] not in vowels:
        #         right -= 1
        #     else:      
        #         left += 1
        
        # return "".join(move)

# soultion 2
        vowels = "aeiouAEIOU"
        i, j = 0, len(s) - 1
        cs = list(s)
        while i < j:
            while i < j and cs[i] not in vowels:
                i += 1
            while i < j and cs[j] not in vowels:
                j -= 1
            if i < j:
                cs[i], cs[j] = cs[j], cs[i]
                i, j = i + 1, j - 1
        return "".join(cs)
            

            
        

                    



s1 = Solution()
# print(s1.reverseVowels([1,0,0,0,1], 1))
# print(s1.reverseVowels([1,2,3], [2,4,6]))
# print(s1.reverseVowels("hello"))
# print(s1.reverseVowels("leetcode"))
print(s1.reverseVowels("aA"))