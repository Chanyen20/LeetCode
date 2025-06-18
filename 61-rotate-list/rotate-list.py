# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # handle the edge case
        if head is None or head.next is None or k == 0:
            return head
        
        # find the Linked List length
        tail_node = head
        length = 1
        while tail_node.next is not None:
            length += 1
            tail_node = tail_node.next
        
        if k % length == 0:
            return head

        # find the new head and tail
        step = length - k % length - 1       
        tail_node.next = head
        while step > 0:
            head = head.next
            step -= 1
        
        new_head = head.next
        head.next = None

        return new_head

            