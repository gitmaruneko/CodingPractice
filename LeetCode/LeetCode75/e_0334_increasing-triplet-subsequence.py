#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# We need to find an increasing triplet subsequence. To achieve this, we can maintain two variables: mi (the smallest number encountered so far) and mid (a middle number that is greater than mi but smaller than any potential third number). We iterate through the array, updating these two variables as needed to better find a third number that fits the condition.

# Approach
# 1. Initialize mi and mid to positive infinity.
# 2. Iterate through the nums array.
# 3. For each num in nums, perform the following checks:
# 4. If num is less than or equal to mi, update mi to num.
# 5. If num is greater than mi but less than mid, update mid to num.
# 6. If num is greater than mid, we have found a valid triplet, so return True.
# 7. If no valid triplet is found after the loop, return False.

# Complexity

# - Time Complexity
# The solution iterates through the entire nums array once, which takes O(n) time, where n is the length of the array.

# - Space Complexity
# The solution uses only two extra variables (mi and mid), so the space complexity is O(1)..


# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)



class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # left, right = 0, 1 
        # length = len(nums) - 1
        # cnt = 0
        # while left <= length - 2:
        #     print(nums[left],nums[right])
        #     if nums[right] > nums[left] and nums[right+1]>nums[right]:
        #         return True
        #     else:
        #         left = right
        #         right += 1

        # return (cnt >= 2)

# solution 2 - greedy
        mi = float('inf')  
        mid = float('inf')  

        for num in nums:
            if num <= mi:
                mi = num
            elif num <= mid:
                mid = num
            else:
                return True

        return False

        

s1 = Solution()
# print(s1.increasingTriplet([1,2,3,4,5]))
# print(s1.increasingTriplet([5,4,3,2,1]))
# print(s1.increasingTriplet([2,1,5,0,4,6]))
# print(s1.increasingTriplet([0,4,2,1,0,-1,-3]))
print(s1.increasingTriplet([20,100,10,12,5,13]))

