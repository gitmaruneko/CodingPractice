#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    
    num_sum = nums
    for index in range(len(nums)):
        if index == 0:        
            num_sum[index] = nums[index]
        else:
            num_sum[index] = nums[index] + nums[index-1]
    return num_sum


nums = [1,2,3,4]
runningSum(nums)
