#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# Given a non-empty array of integers, find the element that appears only once.

# Approach
# Sort the array and check if each element is equal to the next one (i.e., `array[i] == array[i+1]`).
# Return the element that appears only once.

# Complexity
# - Time complexity: \(O(N \log N)\) due to the sorting step.
# - Space complexity: \(O(1)\) if the sorting is done in place.

class Solution(object):
    def singleNumber(self, nums):
        # nums.sort()
        # i = 0
        # while i < len(nums)-1:
        #     if nums[i] == nums[i+1]:
        #         i += 2
        #     else:
        #         return nums[i]
        # return nums[-1]
    
# solution 2 Time complexity: O(N)
        result = 0
        for num in nums:
            print(num)
            result ^= num
        return result


s1 = Solution()
print(s1.singleNumber([2,2,1]))
print(s1.singleNumber([4,1,2,1,2]))