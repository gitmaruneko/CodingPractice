#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# The goal is to calculate and return the highest altitude reached during the journey.

# Approach
# Initialize a variable to keep track of the current altitude.
# Iterate through the gain array, updating the current altitude and storing it in a result array.
# Return the maximum value from the result array.

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        max_altitude = 0
        
        for g in gain:
            current += g
            if current > max_altitude:
                max_altitude = current
        
        return max_altitude



        

s1 = Solution()
print(s1.largestAltitude([-5,1,5,0,-7]))
print(s1.largestAltitude([-4,-3,-2,-1,4,3,2]))