# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total_sum = 0

        if not root:
            return self.total_sum
        
        self.dfs(root, [])
        
        return self.total_sum

    def dfs(self, node, path_list):
        if not node:
            return

        path_list.append(node.val) 
        if not node.left and not node.right:

            digit = 0
            for i in range(len(path_list) - 1, -1, -1):
                self.total_sum += path_list[i] * (10 ** digit)
                digit += 1
        
        

        self.dfs(node.left, path_list)
        self.dfs(node.right, path_list)
        path_list.pop()

            
                
        
        