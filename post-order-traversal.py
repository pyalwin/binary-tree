""" Problem reference -> Leetcode 
    Solution reference -> GeeksforGeeks
    https://www.geeksforgeeks.org/iterative-postorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        ## The postorder traversal will be left, right, root

        if root is None:
            return []
        
        ## Create an stacks for root
        root_stack = []
        return_list = []
        current = root
        while True:
            while current:
                if current.right:
                    root_stack.append(current.right)

                root_stack.append(current)

                current = current.left
            
            current = root_stack.pop()

            if current.right and self.peek(root_stack) == current.right:
                root_stack.pop()
                root_stack.append(current)
                current = current.right
            else:
                return_list.append(current.val)
                current = None
            
            if not root_stack:
                break;
            
    def peek(self, stack):
        if len(stack) > 0:
            return stack[-1]
        return None

