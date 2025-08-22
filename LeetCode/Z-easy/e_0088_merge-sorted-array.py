#!/usr/bin/python
# -*- coding: UTF-8 -*-
from collections import Counter

# Intuition: 
# The goal is to merge two sorted arrays, nums1 and nums2, into one sorted array. 
# nums1 has enough space at the end to hold all elements of nums2. 
# We need to ensure that the merged array remains sorted.

# Approach:
# 1. Initialize Pointers:
#    i points to the last valid element in nums1.
#    j points to the last element in nums2.
#    k points to the last position in nums1 where the merged element will be placed.
# 2. Merge from the End:
#    Compare elements from the end of nums1 and nums2.
#    Place the larger element at the end of nums1 and move the corresponding pointer (i or j) and k backward.
#    Repeat until all elements from nums2 are merged into nums1.
# 3. Edge Cases:
#    If nums2 is exhausted (j < 0), the remaining elements in nums1 are already in place.
#    If nums1 is exhausted (i < 0), continue placing elements from nums2 into nums1.
# Complexity
# - Time complexity: O(m + n)
#   We traverse both arrays once, where m is the number of valid elements in nums1 and n is the number of elements in nums2.
# - Space complexity: O(1): We are merging the arrays in place without using any extra space.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1  # nums1 的有效元素的最後一個索引
        j = n - 1  # nums2 的最後一個索引
        k = m + n - 1  # nums1 的最後一個位置

        while j >= 0:
            if i >= 0 and nums2[j] > nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1           

        print(nums1)

# solution 2
        p1, p2 = m - 1, n - 1
        pos = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[pos] = nums1[p1]
                p1 -= 1
            else:
                nums1[pos] = nums2[p2]
                p2 -= 1
            pos -= 1
        while p2 >= 0:
            nums1[pos] = nums2[p2]
            p2 -= 1
            pos -= 1


s1 = Solution()
print(s1.merge([1,2,3,0,0,0],3,[2,5,6],3))