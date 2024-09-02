#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def toHex(self, num):
        # Handle zero case
        if num == 0:
            return "0"
        
        # Define the hexadecimal characters
        hex_chars = "0123456789abcdef"
        
        # Handle negative numbers using two's complement
        if num < 0:
            num += 2 ** 32
        
        # Convert to hexadecimal
        hex_str = ""
        while num > 0:
            hex_str = hex_chars[num % 16] + hex_str
            num //= 16
        
        return hex_str



s1 = Solution()
print(s1.toHex(26))
print(s1.toHex(-1))



