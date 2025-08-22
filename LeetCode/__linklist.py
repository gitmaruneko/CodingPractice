#!/usr/bin/python
# -*- coding: UTF-8 -*-
from typing import Optional

# Definition for singly-linked list.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next= next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # def delete_node(self, key):
    #     temp = self.head
    #     if temp and temp.data == key:
    #         self.head = temp.next
    #         temp = None
    #         return
    #     prev = None
    #     while temp and temp.data != key:
    #         prev = temp
    #         temp = temp.next
    #     if temp is None:
    #         return
    #     prev.next = temp.next
    #     temp = None

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.val, end=" -> ")
            current_node = current_node.next
        print("None")


if __name__ == "__main__":
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_end(2)
    llist.insert_at_end(3)
    llist.insert_at_beginning(0)
    llist.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
    # llist.delete_node(2)
    # llist.print_list()  # Output: 0 -> 1 -> 3 -> None







