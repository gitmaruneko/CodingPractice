#!/usr/bin/python
# -*- coding: UTF-8 -*-

# # Intuition 
# The array shows the number of candies each child owns. 
# By giving the extra candies to each child, we can compare if they have the greatest number of candies among all the kids.

# # Approach
# 1. Create a new boolean list.
# 2. Use a for loop to iterate through the candies array and add the extra candies to each child's count.
# 3. Check if the new count is the greatest number among the list.
# 4. If yes, append `True` to the boolean list; otherwise, append `False`.

# # Complexity 
# - Time complexity: O(N)
# - Space complexity: O(N)


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        # result = [False for _ in range(len(candies))]
        # for index, item in enumerate(candies):
        #     initial = list(candies)
        #     initial[index] = item + extraCandies
        #     if initial[index] == max(initial):
        #         result[index] =  True
        #     if index == len(initial) - 1:
        #         break
        
        # return result

# solution 2 
        result = []
        max_candies = max(candies)
        for num in candies:
            result.append(num + extraCandies >= max_candies)
            # if num + extraCandies >= max_candies:
            #     result.append(True)
            # else:
            #     result.append(False)
        return result      



s1 = Solution()
print(s1.kidsWithCandies([2,3,5,1,3], 3))
print(s1.kidsWithCandies([12,1,12], 10))