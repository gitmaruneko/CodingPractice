#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    richs = accounts
    richs_sum = []
    richest = 0
    for index in range(len(richs)):
        count = richs[index]
        wealth_sum = 0
        for wealth in count:
            wealth_sum += wealth
        if wealth_sum > richest:
            richest = wealth_sum
    print(richest)
    return richest


accounts = [[1,2,3],[4,5,6]]
maximumWealth(accounts)
