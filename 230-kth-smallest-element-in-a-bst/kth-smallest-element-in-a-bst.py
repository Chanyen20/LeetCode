# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.target_left = k
        self.ans = None
        self.inorder(root)

        return self.ans
    
    def inorder(self, node):
        if not node or self.ans is not None:
            return
        
        self.inorder(node.left)
        

        self.target_left -= 1
        if self.target_left == 0:
            self.ans = node.val
            return

        self.inorder(node.right)

        

        