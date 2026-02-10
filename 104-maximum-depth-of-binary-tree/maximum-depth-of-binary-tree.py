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
        self.max_depth = float('-inf')
        self.dfs(root, 1)
        
        return self.max_depth
    def dfs(self, node, level):      
        if not node:
            return 0
        
        self.dfs(node.left, level + 1)
        if not node.left and not node.left:
            self.max_depth = max(self.max_depth, level)
        self.dfs(node.right, level + 1)
    
        

        

        