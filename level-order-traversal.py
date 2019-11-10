""" Problem reference -> Leetcode 
    Solution reference -> Leetcode
"""

#  Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ## Check if the root is empty
        if not root:
            return []

        ## Instantiate the return stack
        master_stack = []

        ## Set current root for traversal
        current_stack = [root]

        while True:
            ## Create a new temp stack holding the level nodes
            temp_stack = []

            ## Create a new temp stack holding the level values
            temp_val_stack = []

            ### Loop through each of the level nodes to push the child 
            ### nodes into the temp stack for next level iteration
            for item in current_stack:
                if item.left:
                    temp_stack.append(item.left)
                if item.right:
                    temp_stack.append(item.right)
                    
                temp_val_stack.append(item.val)
                
            ## Push the level values to master list for return
            master_stack.append(temp_val_stack)

            ## Reset the next level of iteration to child in temp stack
            current_stack = temp_stack 

            ## If the next level for iteration is empty, stop the loop
            if not current_stack:
                break
        
        return master_stack        