#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Solution(object):
    def maxProfit(self, prices):
        # profit = 0
        # max_profit = 0
        # for i in range(len(prices)):
        #     p1 = prices[i]
        #     for j in range(i+1, len(prices)):
        #         p2 = prices[j]
        #         if p2 - p1 > 0:
        #             profit = p2 -p1
                
        #         max_profit = max(max_profit, profit)

        # return max_profit

# solution 2
        min_price = float('inf')  # Start with a very high value for the minimum price
        max_profit = 0  # Start with zero profit

        for price in prices:
            if price < min_price:
                min_price = price  # Update the minimum price
                print('min_price %s'%min_price)
            elif price - min_price > max_profit:
                max_profit = price - min_price  # Update the maximum profit

        return max_profit



p1 = Solution()
print(p1.maxProfit([7,1,5,3,6,4]))
print(p1.maxProfit([7,6,4,3,1]))
print(p1.maxProfit([1,2]))
print(p1.maxProfit([2,4,1]))
print(p1.maxProfit([2,1,2,0,1]))
print(p1.maxProfit([3,2,6,5,0,3]))




