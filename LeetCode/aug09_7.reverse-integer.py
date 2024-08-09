#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution(object):
    def reverse(self, x):

        # if x > 2**31 -1:
        #     return 0
        
        # reverse = ''
        # str_x = str(x)
        # list_s = list(str_x)
        
        # if str_x[0] == '-':
        #     reverse = '-'
        #     list_s.remove('-')
        
        # if str_x[0] == '0':
        #     list_s.remove('0')
        
        
        # cnt = len(list_s)
        # while cnt :
        #     reverse += list_s.pop()
        #     cnt -= 1
        
        # return int(reverse) 
        

                
# opt

        x = str(x)
        if x[0] == '-':
            a = int('-' + x[-1:0:-1])
            if a >= -2147483648 and a<= 2147483647:
                return a
            else:
                return 0
        else:
            a = int(x[::-1])
            
        if a >= -2147483648 and a<= 2147483647:
           return a
        else:
           return 0


s1 = Solution()
print(s1.reverse(1534236469))
print(s1.reverse(-123))





