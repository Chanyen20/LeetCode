# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.node_list = []

        self.inorder(root)

        for i in range(len(self.node_list)):
            if i == 0 or self.node_list[i] > self.node_list[i - 1]:
                continue
            return False
        return True

    def inorder(self, node):
        if not node:
            return
        
        self.inorder(node.left)

        self.node_list.append(node.val)

        self.inorder(node.right)