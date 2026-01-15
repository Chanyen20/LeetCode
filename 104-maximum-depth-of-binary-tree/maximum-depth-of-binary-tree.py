# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        self.helper(root, 1)

        return self.max_depth

    
    def helper(self, node, depth):
        if not node:
            return None
        
        if not node.left and not node.right:
            self.max_depth = max(self.max_depth, depth)
        
        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)


        