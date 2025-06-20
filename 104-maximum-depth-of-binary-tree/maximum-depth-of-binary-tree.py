# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        height = 0
        self.res = 0
        self.helper(root, height)
        return self.res


    def helper(self, node, height):
        if not node:
            return
        height += 1
        self.res = max(self.res, height)
        self.helper(node.left, height)
        self.helper(node.right, height)


        