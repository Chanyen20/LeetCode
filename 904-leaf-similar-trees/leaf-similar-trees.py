# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.helper(root1, []) == self.helper(root2, [])
    
    def helper(self, root, leaf):
        if not root:
            return

        if not root.left and not root.right:
            leaf.append(root.val)
            return leaf
        
        self.helper(root.left, leaf)
        self.helper(root.right, leaf)
        return leaf


        