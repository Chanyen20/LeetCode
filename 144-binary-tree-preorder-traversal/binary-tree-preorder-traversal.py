# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.res = []
        self.helper(root)
        return self.res

    def helper(self, node):
        if not node:
            return
        else:
            self.res.append(node.val)
        self.helper(node.left)
        self.helper(node.right)
