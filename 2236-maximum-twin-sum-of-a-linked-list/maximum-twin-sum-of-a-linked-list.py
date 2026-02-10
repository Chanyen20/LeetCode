# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_val = []

        while head:
            node_val.append(head.val)
            head = head.next
        
        left, right = 0, len(node_val) - 1
        max_sum = float('-inf')

        while left < right:
            total = node_val[left] + node_val[right]
            max_sum = max(max_sum, total)
            left += 1
            right -= 1
        
        return max_sum
        