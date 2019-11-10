"""
Find Maximum Depth of binary tree

Reference: Leetcode

Problem Statement: 

        Given a binary tree, find its maximum depth.

        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

        Note: A leaf is a node with no children.

        Example:

        Given binary tree

            3
        / \
        9  20
            /  \
        15   7

        return its depth = 3.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.answer = 0
        
    def maxDepth(self, root: TreeNode, depth=1) -> int:
        
        ### Check if tree is not empty
        if not root:
            return self.answer
        
        ### Check if the maximum between current depth and 
        ### stored depth. 
        if root.left is None and root.right is None:
            self.answer = max(self.answer, depth)
        
        ## Recursively call the maxDepth to find the maximum depth of left child
        self.maxDepth(root.left, depth + 1)
        ## Recursively call the maxDepth to find the maximum depth of right child
        self.maxDepth(root.right, depth + 1)
        
        ## Return the answer
        return self.answer