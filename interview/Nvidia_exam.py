#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def array_sort():
    array_a = [2, 16, 19, 28]
    array_b = [1, 8 ,14, 17, 30]
    for el in array_b:
        inserted = False
        for i in range(len(array_a)):
                if el < array_a[i]:
                    array_a.insert(i,el)
                    inserted = True
                    break
        if not inserted:
                array_a.append(el)
    
    print(array_a)
                                   

array_sort()