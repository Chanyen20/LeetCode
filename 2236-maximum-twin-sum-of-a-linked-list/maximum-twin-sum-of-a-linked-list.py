# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        head_list = []
        while head is not None:
            head_list.append(head.val)
            head = head.next
        
        max_num = float('-inf')
        left, right = 0, len(head_list) - 1
        while left < right:
            max_num = max(max_num, head_list[left] + head_list[right])
            left += 1
            right -= 1
        return max_num