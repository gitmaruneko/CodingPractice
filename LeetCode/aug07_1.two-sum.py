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
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# solution 3 dictionary



s1 = Solution()
print(s1.twoSum([3,3], 6))



