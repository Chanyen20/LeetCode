# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        max_sum_level = 0
        curr_level = 0

        if not root:
            return curr_level
        
        queue = deque()
        queue.append(root)

        while queue:
            curr_level += 1         
            level_sum = 0
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            
            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = curr_level
            
            

        
        return max_sum_level

        