#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        # result = []
        # temp = []

        # for item in nums:
        #     if item < target:
        #         temp.append(item)
        
        # while temp:
        #     fst_val = temp.pop()
        #     snd_val = target - fst_val
        #     if snd_val in temp:
        #         result.append(nums.index(snd_val))
        #         result.append(nums.index(fst_val))
        #     break
            

        # return(result)

# solution 2
        seen = {}  # num -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# solution 3 dictionary



s1 = Solution()
print(s1.twoSum([3,3], 6))






