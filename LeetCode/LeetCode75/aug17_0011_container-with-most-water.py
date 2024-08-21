#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

# Intuition 
# Given an integer array representing the heights of vertical lines, find two values that, together, form a container that can hold the maximum amount of water.

# Approach
# Use two pointers, 'left' and 'right'. The width is the distance between the two pointers on the x-axis. Move the pointer pointing to the shorter line inward to potentially find a larger container.

# Complexity 
# - Time complexity: O(N)
# - Space complexity: O(1)


class Solution:
    def maxArea(self, height: List[List[int]]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            h = min(height[left], height[right])
            area = h*(right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
            
        return max_area
     






if __name__ == "__main__":
    s1 = Solution()
    print(s1.maxArea([1,8,6,2,5,4,8,3,7]))
