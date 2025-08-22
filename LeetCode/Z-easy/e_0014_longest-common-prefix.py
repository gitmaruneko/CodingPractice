#!/usr/bin/python
# -*- coding: UTF-8 -*-

# REF
# https://ithelp.ithome.com.tw/articles/10213258


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        
        for i, c in enumerate(s1):
            if c != s2[i]:
                return s1[:i]
        return s1 
        

# opt   



s1 = Solution()
print(s1.longestCommonPrefix(["flower","flow","flight"]))






