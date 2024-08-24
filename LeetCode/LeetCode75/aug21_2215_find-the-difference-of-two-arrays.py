#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition 
# Given two lists num1, num2, which contains interger, and return 1 list contain two sub list, 
# index 0 contains elements not in num2, index 1 contains elements not in num 1.

# Approach
# create new list and append num1 and num2
# traverse num1 and compare elements to num2, if exist in num2 then remove and vice versa
# return new list 
#
# Complexity 
# - Time complexity: O(N)
# - Space complexity: O(N)


from typing import List


class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # n1 = set()
        # n2 = set()
        # for _ in nums1:
        #     if _ not in nums2:
        #         n1.add(_)
        # for _ in nums2:
        #     if _ not in nums1:
        #         n2.add(_)
        
        # return([list(n1),list(n2)])
    

# solution 2
        s1, s2 = set(nums1), set(nums2)
        return [list(s1 - s2), list(s2 - s1)]
        

                    



s1 = Solution()
# print(s1.canPlaceFlowers([1,0,0,0,1], 1))
# print(s1.findDifference([1,2,3], [2,4,6]))
print(s1.findDifference([1,2,3,3], [1,1,2,2]))