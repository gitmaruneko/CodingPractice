#!/usr/bin/python
# -*- coding: UTF-8 -*-

# REF
# https://medium.com/@amber.fragments/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-6-hash-table-%E9%9B%9C%E6%B9%8A%E8%A1%A8-eb33280859ab

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        cnt = 0
        print(len(s))
        while cnt <= len(s)-1:
            char = s[cnt]
            if cnt == len(s)-1:
                total += roman_dict[char]
                break
            else :
                char_next = s[cnt+1]
                val_cur = roman_dict[char]
                val_next = roman_dict[char_next]
                if val_cur >= val_next:
                    total += val_cur
                    cnt += 1
                else:
                    total += val_next - val_cur
                    cnt += 2
            print(total)
            
        return total
                
# opt
        # roman = {'I': 1, 'V': 5, 'X': 10,
        #          'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        # prev, total = 0, 0
        # for c in s:
        #     curr = roman[c]
        #     total += curr
        #     # need to subtract
        #     if curr > prev:
        #         total -= 2 * prev
        #     prev = curr
        # return total

s1 = Solution()
print(s1.romanToInt("III"))
print(s1.romanToInt("LVIII"))
print(s1.romanToInt("MCMXCIV"))
print(s1.romanToInt("MDCXCV"))




