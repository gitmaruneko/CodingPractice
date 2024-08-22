#!/bin/python3


#5
#2 3 6 6 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

#solution 1
    arr_order = list(set(arr))
    arr_order.sort()
    print(arr_order[-2])

# solution opt
#    print(sorted(list(set(arr)))[-2])


    
