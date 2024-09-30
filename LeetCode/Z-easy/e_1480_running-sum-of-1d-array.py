#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition: 
# The goal is to compute the running sum of a 1D array in place, meaning we update the original array without using extra space.

# Approach:
# Iterate through the array starting from the second element.
# For each element, add the value of the previous element to it.
# This way, each element at index i will store the sum of all elements from index 0 to i.

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # result = []
        # acc = 0
        # for i in nums:
        #     acc += i
        #     result.append(acc)
        
        # return result

# solution 2
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        
        return nums



s1 = Solution()
print(s1.runningSum([1,2,3,4]))