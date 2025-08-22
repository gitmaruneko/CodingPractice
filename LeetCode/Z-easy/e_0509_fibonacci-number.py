#!/usr/bin/python
# -*- coding: UTF-8 -*-

# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

# REF
https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-dynamic-programming-%E5%8B%95%E6%85%8B%E8%A6%8F%E5%8A%83-de980ca4a2d3

class Solution(object):
    def fib(self, n):
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
print(s1.fib(6))






