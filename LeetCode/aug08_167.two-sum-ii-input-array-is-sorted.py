#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def twoSum(self, numbers, target):
        start = 0
        end = len(numbers) - 1
        res = []
        while start < end:
            sum = numbers[start] + numbers[end]
            if target > sum:
                start+=1
            elif target < sum:
                end-=1
            else:
                return [start + 1, end + 1]




s1 = Solution()
print(s1.twoSum([2,7,11,15], 9))
print(s1.twoSum([0,0,3,4], 0))
print(s1.twoSum([-1,0], -1))



