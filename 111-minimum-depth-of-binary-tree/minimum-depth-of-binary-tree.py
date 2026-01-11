# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        self.res = float('inf')

        if not root:
            return 0
        
        self.helper(root, 1)
        return self.res

    
    def helper(self, node, height):
        if not node:
            return

        if not node.right and not node.left:
            self.res = min(self.res, height)
            return
        
        if not node:
            return
        
        self.helper(node.left, height + 1)
        self.helper(node.right, height + 1)



        


        