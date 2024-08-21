#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import List

# Intuition 
# Given ( m ) sorted arrays, find the maximum distance among the arrays. The minimum value and maximum value cannot be in the same list.
#
# Approach
# As the arrays are sorted, assign the minimum and maximum values to the first array at positions ([0]) and ([-1]).
# Retrieve other arrays ([1:]) and calculate the distances ( a ) and ( b ).
# Get the maximum value from ( a ), ( b ), and the current answer.
# Recheck the minimum and maximum values.

# Complexity 
# - Time complexity: O(N)
# - Space complexity: O(1)


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        ans = 0
        mi, mx = arrays[0][0], arrays[0][-1]
        for arr in arrays[1:]:
            a, b = abs(arr[0] - mx), abs(arr[-1] - mi)
            ans = max(ans, a, b)
            mi = min(mi, arr[0])
            mx = max(mx, arr[-1])
        return ans
      






if __name__ == "__main__":
    s1 = Solution()
    print(s1.maxDistance([[1,2,3],[4,5],[1,2,3]]))
    print(s1.maxDistance([[1,4],[0,5]]))
    print(s1.maxDistance([[1],[1]]))