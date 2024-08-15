#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        currentNode = head
        while currentNode and currentNode.next:
            if currentNode.val == currentNode.next.val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
        return head




if __name__ == "__main__":
    s1 = Solution()
    print(s1.deleteDuplicates([1,1,2]))





