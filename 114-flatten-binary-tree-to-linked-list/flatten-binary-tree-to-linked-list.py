# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.seen = []
        self.dfs(root)
        self.flatNode()

    def dfs(self, node):
        if not node:
            return

        self.seen.append(node)

        self.dfs(node.left)
        self.dfs(node.right)
    
    def flatNode(self):
        for i in range(len(self.seen)):
            self.seen[i].left = None
            if i == len(self.seen) - 1:
                self.seen[i].right = None
            else:
                self.seen[i].right = self.seen[i + 1]


            
