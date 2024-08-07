#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        while num != 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            
            cnt += 1
        
        return cnt


p1 = Solution()
print(p1.numberOfSteps(15))



