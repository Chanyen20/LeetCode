# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return None

        total_node = 0

        node = head
        while node is not None:
            total_node += 1
            node = node.next
        
        prev = head   
        for _ in range(total_node // 2 - 1):
            prev = prev.next
            
        prev.next = prev.next.next

        return head
# Time: O(n)
# Space: O(1)