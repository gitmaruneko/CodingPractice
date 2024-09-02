#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# The goal is to count the number of 1s in the binary representation of a given integer n. By using bitwise operations, we can efficiently check each bit of the integer.

# Approach
# Initialize a counter: Start with a counter set to zero.
# Bitwise AND operation: Use the bitwise AND operation (&) with 1 to check if the least significant bit (LSB) of n is 1.
# Shift right: Use the right shift operation (>>) to discard the LSB and move to the next bit.
# Repeat: Continue the process until n becomes zero.
# Return the count: The counter will hold the number of 1s in the binary representation of n.

# Complexity
# Time complexity: O(log N), where N is the given integer. This is because the number of bits in the binary representation of N is proportional to log N.
# Space complexity: O(1), as we are using a constant amount of extra space regardless of the input size.

class Solution(object):
    def hammingWeight(self, n):
        digits = []
        while n:
            digits.append(n%2)
            n = n // 2
        return digits.count(1)

# solution 2
        # count = 0
        # while n:
        #     count += n & 1
        #     n >>= 1
        # return count


s1 = Solution()
print(s1.hammingWeight(11))



