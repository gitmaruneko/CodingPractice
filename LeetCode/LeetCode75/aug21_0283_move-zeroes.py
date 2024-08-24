#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition 
#

# Approach
# 
#
# Complexity 
# - Time complexity: O()
# - Space complexity: O()


from typing import List


class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for right in range(len(nums)):
                if nums[right] != 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        left += 1
        
        # print(nums)


s1 = Solution()

# print(s1.moveZeroes([0,1,0,3,12]))
# print(s1.moveZeroes([0]))
print(s1.moveZeroes([0,0,1]))