#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
# Definition for singly-linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

class Solution(object):
    def middleNode(self, head):
        # Initialize length and temp pointer
        length = 0
        temp = head
        
        # Traverse the linked list and count the number of nodes
        while temp:
            length += 1
            temp = temp.next
            
        # Calculate the index of the middle node(s)
        middle = length // 2
        
        # Traverse the linked list again to find the middle node(s)
        i = 0
        while i < middle:
            head = head.next
            i += 1
        
        # Return the middle node(s)
        return head


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(4)
ll.append(5)
ll.display()

p1 = Solution(ll)






