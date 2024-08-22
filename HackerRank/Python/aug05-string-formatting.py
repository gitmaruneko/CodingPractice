#!/bin/python3

def print_formatted(number):
    width = len(bin(number)[2:])
    for num in range(1, number + 1):
        n_dec = str(num)
        n_oct = oct(num)[2:]
        n_hex = hex(num)[2:].upper()
        n_bin = bin(num)[2:]
        print('%s %s %s %s'%(n_dec.rjust(width), n_oct.rjust(width), n_hex.rjust(width).upper(), n_bin.rjust(width)))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)