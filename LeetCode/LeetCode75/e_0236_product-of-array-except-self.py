#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# The goal is to return an array where each element is the product of all elements in the given array except itself.

# Approach
# create an array and calculate prefix products first
# use another loop to calculate the product of prefix and suffix products.
# 

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)



class Solution(object):
    def productExceptSelf(self, nums):
        # n = len(nums)
        # answer = [1] * n
        
        # prefix = 1
        # for i in range(n):
        #     answer[i] = prefix
        #     prefix *= nums[i]
        
        # print(answer)
        
        # suffix = 1
        # for i in range(n - 1, -1, -1):
        #     answer[i] *= suffix
        #     suffix *= nums[i]
        
        # return answer
    
# solution 2
        n = len(nums)
        answer = [1] * n
        
        # 同時計算前綴和後綴乘積
        prefix = 1
        suffix = 1
        for i in range(n):
            answer[i] *= prefix
            prefix *= nums[i]
            answer[n - 1 - i] *= suffix
            suffix *= nums[n - 1 - i]
        
        return answer


        

s1 = Solution()
print(s1.productExceptSelf([1,2,3,4]))