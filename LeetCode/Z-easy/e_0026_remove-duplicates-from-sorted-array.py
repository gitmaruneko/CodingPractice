#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition:
# The goal is to remove duplicate numbers from a sorted array and return the length of the array with unique elements.

# Approach:
# Use two pointers, i and j. Initialize i to 0 and j to 1.
# Traverse the array with j. If nums[i] is not equal to nums[j], increment i and update nums[i] to nums[j].
# Continue this process until j reaches the end of the array.

# Complexity:
# - Time complexity: (O(N)), where (N) is the length of the array, because we traverse the array once.
# - Space complexity: (O(1)), because we are modifying the array in place and not using any extra space.


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


s1 = Solution()
print(s1.removeDuplicates([1,1,2]))