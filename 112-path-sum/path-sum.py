# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.seenSum = set()
        if not root:
            return False
        
        self.helper(root, 0)

        return targetSum in self.seenSum
           

    def helper(self, node, preSum):
        if not node:
            return
        
        nowSum = preSum + node.val

        if not node.left and not node.right:
            self.seenSum.add(nowSum)
            return

        self.helper(node.left, nowSum)
        self.helper(node.right, nowSum)

        


        