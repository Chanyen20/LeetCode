# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []

        queue = deque()
        queue.append(root)
        
        while len(queue) > 0:
            total = 0
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(total / size)
            total = 0
        
        return res
                

        