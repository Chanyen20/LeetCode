# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        node = head
        while node is not None:
            vals.append(node.val)
            node = node.next

        node = head
        for val in reversed(vals):
            node.val = val
            node = node.next
        
        return head
        

