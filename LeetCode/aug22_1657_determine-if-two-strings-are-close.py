#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

# Intuition: 
# To determine if two strings are “close,” 
# we need to ensure that they can be transformed into each other 
# using specific operations. The key insight is that two strings are close if they have the same set of characters and the same frequency distribution of these characters.

# Approach:

# Character Set Comparison: First, check if both strings contain the same set of unique characters. 
# If they don’t, they can’t be transformed into each other.
# Frequency Distribution Comparison: Next, 
# count the frequency of each character in both strings. 
# Sort these frequency counts and compare them. 
# If the sorted frequency distributions match, the strings are close

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


# 解題思路
# 要判斷兩個字串是否「接近」，需要滿足以下條件：

# - 兩個字串必須包含相同的字符集合。
# - 兩個字串中每個字符的頻率必須相同（順序可以不同）。

class Solution(object):
    def close_strings(word1, word2):
        if set(word1) != set(word2):
            return False
        return sorted(Counter(word1).values()) == sorted(Counter(word2).values())


s1 = Solution()
print(s1.closeStrings( "abc", "bca"))