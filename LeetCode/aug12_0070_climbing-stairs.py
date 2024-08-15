#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# REF

class Solution(object):
    def climbStairs(self, n):
        # if n==0 or n==1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n-2)
        
# opt   
        dp = [0,1]
        for i in range(2, n+1):
            dp.insert(n,(dp[i-1] + dp[i-2]))
        
        return dp[-1]



s1 = Solution()
print(s1.climbStairs(6))






