#!/usr/bin/python
# -*- coding: UTF-8 -*-

#
# Nvidia_stock = [
# [day1, 203.7],
# [day2, 210.9],
# [day3, 212.8]]
# 
#  

# intution
# find the best price

# apporach
# 
#

def find_best_benefit(nvidia_stock):
    min_price = float('inf')
    max_profit = 0
    buyD = 0
    sellD = 0
    min_priceD = 0

    for i in range(len(nvidia_stock)):
        if nvidia_stock[i] < min_price:
            min_price = nvidia_stock[i]
            min_priceD = i + 1
        elif nvidia_stock[i] - min_price > max_profit:
            max_profit = nvidia_stock[i] - min_price
            buyD = min_priceD
            sellD = i + 1
    return buyD, sellD, max_profit
        

nvidia_stock = [203.7, 210.9, 212.8, 312.5]
buyD, sellD, profit = find_best_benefit(nvidia_stock)
print('Suggest buy-in date: %s'%buyD)
print('Suggest sell-out date: %s'%sellD)
print('The profit: %s'%profit)