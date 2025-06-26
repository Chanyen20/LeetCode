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
        self.helper(root, cnt = 0)
        return self.res
        
    def helper(self, node, cnt):
        if not node:
            return
        cnt += 1
        self.res = max(self.res, cnt)
        self.helper(node.left, cnt)
        self.helper(node.right, cnt)

        
        