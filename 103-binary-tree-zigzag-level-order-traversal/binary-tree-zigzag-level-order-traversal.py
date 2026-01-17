# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0

        if not root:
            return res
        
        queue = deque()
        queue.append(root)

        while queue:
            level_res = []
            level_lengrh = len(queue)
            level += 1

            for i in range(level_lengrh):
                node = queue.popleft()
                level_res.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 0:
                res.append(level_res[::-1])
            else:
                res.append(level_res)
        return res


            

        