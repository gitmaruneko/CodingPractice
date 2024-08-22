#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition
# The goal is to find the maximum average of any subarray of length k in the given list nums. Instead of recalculating the sum for each subarray from scratch, we can use a sliding window approach to efficiently update the sum as we move the window across the array.

# Approach
# Initialization:
# Calculate the sum of the first k elements and store it in s.
# Initialize ans with this sum, as it represents the maximum sum found so far.
# Sliding Window:
# Iterate through the array starting from the k-th element to the end.
# For each element at index i, update the sum s by adding the current element nums[i] and subtracting the element that is k positions behind (nums[i - k]).
# Update ans to be the maximum of ans and the current sum s.
# Result:
# After the loop, divide ans by k to get the maximum average and return it.

# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)

class Solution(object):
    def findMaxAverage(self, nums, k):
        # max_avg = float('-inf')
        # length = len(nums) - k + 1
        # i = 0
        # while i < length:
        #     total = sum(nums[i:i+k])
        #     temp_avg = total/k
        #     max_avg = max(max_avg, temp_avg)
        #     i += 1
        # return max_avg

# solution 2
        ans = s = sum(nums[:k])
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            ans = max(ans, s)
        return ans / k
        

s1 = Solution()
# print(s1.findMaxAverage([1,12,-5,-6,50,3], 4))
# print(s1.findMaxAverage([5], 1))
print(s1.findMaxAverage([-1], 1))