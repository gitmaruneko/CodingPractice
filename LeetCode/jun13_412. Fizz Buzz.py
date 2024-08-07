#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_total = []
        result = ""
        for i in range(1, n+1):
            curr_str = ""

            if i % 3 == 0:
                curr_str = "Fizz" 
            if i % 5 == 0 :
                curr_str += "Buzz" 

            if not curr_str:
                curr_str += str(i)

            result = curr_str
            result_total.append(result)

        return result_total

p1 = Solution()
print(p1.fizzBuzz(15))


