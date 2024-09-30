#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intuition

# Approach



# Complexity
# - Time complexity: O(N)
# - Space complexity: O(1)


from collections import Counter

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # arr_set = set(arr)
        # result = {item: 0 for item in arr_set}
        # value = set()

        # for item in arr:
        #     result[item] += 1

        # for item in result:
        #     value.add(result.get(item))
        
        # return len(value) == len(arr_set)

# solution 2
        # 使用 Counter 計算每個元素的出現次數
        count = Counter(arr)
        
        # 使用 set 存儲出現次數
        occurrences = set(count.values())
        
        # 檢查出現次數是否唯一
        return len(occurrences) == len(count)

                


        

s1 = Solution()
print(s1.uniqueOccurrences([1,2,2,1,1,3]))
print(s1.uniqueOccurrences([1,2]))
print(s1.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))