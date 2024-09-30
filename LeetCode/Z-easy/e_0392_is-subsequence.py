#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition: 

# Approach:

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)


s1 = Solution()
# print(s1.isSubsequence("abc", "ahbgdc"))
# print(s1.isSubsequence("axc", "ahbgdc"))
# print(s1.isSubsequence("b", "c"))
print(s1.isSubsequence("acb", "ahbgdc"))
