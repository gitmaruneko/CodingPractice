#!/usr/bin/python
# -*- coding: UTF-8 -*-

# intution
# find the pairs that sum equal 100

# apporach
# 
#

def find_pairs(X):
    pairs = []
    seen = set()

    for i, v in enumerate(X):
        target = 100 - v
        if target in seen:
            pair_index = len(pairs)
            pair_string = f"Pair {pair_index}: [X. index:{target}, value:{target}], [index:{i}, value:{v}]"
            pairs.append(pair_string)
            seen.remove(target)
        else:
            seen.add(v)
    return pairs

X = [58,62,58,48,38,62,42,58] 
result = find_pairs(X)
for pair in result:
    print(pair)  