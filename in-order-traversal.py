""" Problem reference -> Leetcode 
    Solution reference -> GeeksforGeeks
    https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ## The inorder traversal will be left, root, right
        
        ## Create an empty list
        current = root
        return_list = []
        stack = []
        
        while True:
            ## Check if the left is not empty
            if current:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                return_list.append(current.val)
                current = current.right
            else:
                break

        
        return return_list