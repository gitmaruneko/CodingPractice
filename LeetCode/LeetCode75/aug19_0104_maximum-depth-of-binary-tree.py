#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Intution
# The given code is for searching a value in a Binary Search Tree (BST). 
# The intuition is to leverage the properties of BST, 
# where the left subtree contains values less than the root, 
# and the right subtree contains values greater than the root. 
# By comparing the target value with the current node’s value, 
# we can decide whether to move left or right, effectively narrowing down the search space.

# Approach
# Start at the Root: Begin the search at the root node.
# Compare Values:
# If the current node’s value equals the target value (val), return the current node.
# If the current node’s value is greater than the target value, move to the left child (root = root.left).
# If the current node’s value is less than the target value, move to the right child (root = root.right).
# Repeat: Continue this process until the target value is found or the tree is fully traversed (i.e., root becomes None).
# Return Result: If the target value is found, return the corresponding node; otherwise, return None.

# Complexity 
# - Time complexity: O(H)
# - Space complexity: O(1)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # 每個節點的深度是通過遞迴調用來累加計算的，
        # 最終返回整棵樹的最大深度。每個節點本身的深度是 1，
        # 但我們需要計算從根節點到這個節點的路徑長度，
        # 這就是為什麼我們在每次遞迴調用中加 1。
        if root is None:
            return 0
        ld = self.maxDepth(root.left)
        rd = self.maxDepth(root.right)
        print('ld: %s, rd: %s' %(ld,rd))
        return 1 + max(ld, rd)






if __name__ == "__main__":
    s1 = Solution()
    print(s1.maxDepth([3,9,20,'null','null',15,7]))
