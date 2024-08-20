#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition 
# The problem is to determine if we can plant n new flowers in a flowerbed without violating the rule that no two flowers can be adjacent. 
# The key is to check each position in the flowerbed and see if it can be used to plant a flower by ensuring its adjacent positions are empty.
#
# Approach
# 1. Initialize Counters: Start with a counter count to keep track of the number of flowers planted.
# 2. Iterate Through Flowerbed: Loop through each position in the flowerbed.
# 3. Check Conditions: For each position, check if it is empty (0). If it is, check if the previous and next positions are also empty (or if it’s at the boundary of the array).
# 4. Plant Flower: If both adjacent positions are empty, plant a flower at the current position and increment the counter.
# 5. Early Exit: If at any point the counter reaches n, return True.
# 6. Final Check: After the loop, if the counter is less than n, return False.

# Complexity 
# - Time complexity: O(N)
#- Space complexity: O(1)


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            if flowerbed[i] == 0:
                prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
                next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if prev_empty and next_empty:
                    flowerbed[i] = 1
                    count += 1
                    
            if count >= n:
                return True
        
        return count >= n




s1 = Solution()
# print(s1.canPlaceFlowers([1,0,0,0,1], 1))
print(s1.canPlaceFlowers([1,0,0,0,0,0,1], 2))