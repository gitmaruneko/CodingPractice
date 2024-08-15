#!/usr/bin/python
# -*- coding: UTF-8 -*-

# REF

class Solution(object):
    def threeSum(self, nums):
        result = []
        nums_sort = sorted(nums)
        total = 0
        for fix in range(len(nums)-2):
            if fix > 0 and nums_sort[fix] == nums_sort[fix - 1]:
                continue
            fix_v = nums_sort[fix]
            left = fix + 1
            right = len(nums) -1

            while left < right:
                left_v = nums_sort[left]
                right_v = nums_sort[right]
                total = fix_v + left_v + right_v
                if total == 0:
                    result.append([nums_sort[fix], left_v, right_v])
                    while left < right and nums_sort[left] == nums_sort[left + 1]:
                        left += 1
                    while left < right and nums_sort[right] == nums_sort[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return result
                        
# opt


s1 = Solution()
print(s1.threeSum([-1,0,1,2,-1,-4])) # [[-1,-1,2],[-1,0,1]]
print(s1.threeSum([0,1,1])) #[]
print(s1.threeSum([0,0,0])) #[[0,0,0]]
print(s1.threeSum([0,0,0,0])) #[[0,0,0]]





