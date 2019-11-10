# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        ## The preorder traversal will be root, left, right
        
        ## Check the tree is not empty
        if not root:
            return []
        
        ## Create an empty list
        return_list = []
        stack = [root]
        
        while len(stack) != 0:
            current = stack.pop()
            return_list.append(current.val)
            
            if current.right:
                stack.append(current.right)
            
            if current.left:
                stack.append(current.left)
        
        return return_list