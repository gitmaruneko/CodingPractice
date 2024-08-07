#!/bin/python3


if __name__ == '__main__':
    N = int(input())

#solution 1
    data_int = map(int, input().split(' '))
    print(hash(tuple(data_int)))


# solution opt

