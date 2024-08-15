#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
# solution 2 - recurssion
        # if not head or not head.next:
        #     return head
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p



if __name__ == "__main__":
    s1 = Solution()
    print(s1.reverseList([1,2,3,4,5]))





