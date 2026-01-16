# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.tempt = []
        self.cnt = 0

        self.dfs(root)

        return self.cnt

    def dfs(self, node):
        if not node:
            return self.cnt
        
        self.tempt.append(node.val)
        
        if node.val >= max(self.tempt):
           self.cnt += 1 

        self.dfs(node.left)
        self.dfs(node.right)
        
        self.tempt.pop()

        