#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def convertToBase7(self, number):
    #     if number < 0:
    #         return '-' + self.convertToBase7(-number)
    #     elif number < 7:
    #         return str(number)
    #     else:
    #         return self.convertToBase7(number // 7) + str(number % 7)

# solution 2

        if num == 0:
            return "0"
        
        negative = num < 0
        num = abs(num)
        digits = []
        
        while num:
            digits.append(str(num % 7))
            num //= 7
        
        if negative:
            return '-' + ''.join(digits[::-1])
        else:
            return ''.join(digits[::-1])



s1 = Solution()
print(s1.convertToBase7(100))



