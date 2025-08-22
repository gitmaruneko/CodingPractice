#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition

# Approach
# 
# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)

class Solution(object):
    def findComplement(self, num: int) -> int:
        # # Find binary representation of the number without the '0b' prefix
        # binary_rep = bin(num)[2:]
        # # Find the complement by flipping each bit
        # complement = ''.join('1' if bit == '0' else '0' for bit in binary_rep)
        # # Convert the complement back to decimal
        # return int(complement, 2)
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
        return num ^ mask


s1 = Solution()
print(s1.findComplement(5))