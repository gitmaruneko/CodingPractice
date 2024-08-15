#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional

# REF
# https://ithelp.ithome.com.tw/articles/10213265

# Intuition
# Gradually compare and merge the nodes of the two lists to ensure the new list is sorted.

# Approach
# Use iteration to compare and merge nodes, handling remaining nodes.

# Complexity
# Time complexity:
# Each iteration processes one node, so there will be (O(n + m)) iterations in total, where (n) and (m) are the lengths of the two lists.
# Therefore, the time complexity is (O(n + m)).

# Space complexity:
# Since we are using iteration, there is no additional recursive call stack space.
# Only a constant amount of extra space is used (e.g., pointers dum and mov).
# Therefore, the space complexity is (O(1)).

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(None)
        mov = dum
        while l1 and l2:
            if l1.val <= l2.val:
                mov.next = l1
                l1 = l1.next
            else:
                mov.next = l2
                l2 = l2.next
            mov = mov.next
        if l1 == None:
            mov.next = l2
        elif l2 == None:
            mov.next = l1
        
        return dum.next

# Throughout the entire process, 
# dum remains at the starting point of the linked list, while mov is responsible for constructing the new linked list. 
# Once the merging is complete, dum.next will be the first valid node of the merged linked list.

# solution 2 - recursion
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1
        
        # if list1.val <= list2.val:
        #     list1.next = self.mergeTwoLists(list1.next, list2)
        #     return list1
        # else:
        #     list2.next = self.mergeTwoLists(list1, list2.next)
        #     return list2

# solution 3 - list
        # res = []
        # i, j = 0, 0
        # while i < len(list1) and j < len(list2):
        #     if list1[i] < list2[j]:
        #         res.append(list1[i])
        #         i += 1
        #     else:
        #         res.append(list2[j])
        #         j += 1
        # res.extend(list1[i:])
        # res.extend(list2[j:])
        # return res


if __name__ == "__main__":
    s1 = Solution()
    print(s1.mergeTwoLists([1,2,4],[1,3,4]))





