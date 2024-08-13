#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        # """
        # :type s: str
        # :rtype: int
        # """
        # s_comb = []
        # max_len = 0
        # if len(s) == 1:
        #     return 1
        # for i, c in enumerate(s):
            
        #     if c not in s_comb:
        #         s_comb.append(c)
        #         if len(s_comb) >= 2:
        #             s_comb.append(s_comb[-2] + s[i])
        #     else:
        #         s_comb = []
        #         s_comb.append(c)
        #     len_substr = len(max(s_comb, key=len))
        #     if len_substr > max_len:
        #         max_len = len_substr
        # return max_len
      

# opt   
# use sliding window and set for non repeat characters
#  
        ss = set()
        ans = i = 0
        for j, c in enumerate(s):
            while c in ss:
                ss.remove(s[i])
                i += 1
            ss.add(c)
            ans = max(ans, j - i + 1)
            print(ss)
        return ans



s1 = Solution()
# print(s1.lengthOfLongestSubstring("abcabcbb"))
# print(s1.lengthOfLongestSubstring("bbbbb"))
print(s1.lengthOfLongestSubstring("pwwkew"))
# print(s1.lengthOfLongestSubstring(" "))
# print(s1.lengthOfLongestSubstring("au"))
# print(s1.lengthOfLongestSubstring("aab"))






