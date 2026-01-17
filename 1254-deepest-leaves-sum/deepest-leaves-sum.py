# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root :
            return total_sum

        queue = deque()
        queue.append(root)

        while queue:
            total_sum = 0
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                total_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if not queue:
                return total_sum




        