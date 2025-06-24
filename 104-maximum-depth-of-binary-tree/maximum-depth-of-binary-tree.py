# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = 0
        self.helper(root, height = 0)
        return self.res

    def helper(self, node, height):
        if not node:
            return
        else:            
            self.res = max(self.res, height + 1)

        self.helper(node.left, height + 1)
        self.helper(node.right, height + 1)


        
        

        