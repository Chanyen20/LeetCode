# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.cnt = 0

        self.dfs(root, [])
        return self.cnt

    def dfs(self, node, seen):
        if not node:
            return
        
        if not seen or node.val >= max(seen):
            self.cnt += 1
        seen.append(node.val)

        self.dfs(node.left, seen)
        self.dfs(node.right, seen)

        seen.pop()



        
        

        