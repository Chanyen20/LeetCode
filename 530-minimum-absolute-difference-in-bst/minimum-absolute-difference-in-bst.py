# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.min_diff = float('inf')

        self.inorderDFS(root)
        return self.min_diff

    
    def inorderDFS(self, node):
        if not node:
            return 
        
        self.inorderDFS(node.left)
        
        if self.prev:
            self.min_diff = min(self.min_diff, abs(self.prev.val - node.val))
        self.prev = node
        
        self.inorderDFS(node.right)

        