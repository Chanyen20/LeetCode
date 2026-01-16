# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0

        self.dfs(root.left, True)
        self.dfs(root.right, False)

        return self.sum


    def dfs(self, node, is_left):
        if not node:
            return
        
        if not node.left and not node.right and is_left:
            self.sum += node.val
        
        self.dfs(node.left, True)
        self.dfs(node.right, False)


        