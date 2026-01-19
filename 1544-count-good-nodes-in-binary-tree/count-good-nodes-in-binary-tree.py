# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.seen = []
        self.cnt = 0

        if not root:
            return self.cnt
        self.seen.append(root.val)

        self.dfs(root, self.seen)
        return self.cnt

    def dfs(self, node, seen):
        if not node:
            return
        
        if node.val >= max(seen):
            self.cnt += 1
        seen.append(node.val)

        self.dfs(node.left, self.seen)
        self.dfs(node.right, self.seen)

        seen.pop()



        
        

        