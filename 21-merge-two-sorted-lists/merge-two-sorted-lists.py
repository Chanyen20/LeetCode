# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        curr = dummy_node
        l1_pointer = list1
        l2_pointer = list2
    
        while l1_pointer or l2_pointer:
            if not l1_pointer:
                curr.next = l2_pointer
                break
            
            if not l2_pointer:
                curr.next = l1_pointer
                break
            
            if l1_pointer.val <= l2_pointer.val:
                curr.next = l1_pointer
                
                l1_pointer = l1_pointer.next
                curr = curr.next
            elif l1_pointer.val > l2_pointer.val:
                curr.next = l2_pointer
                
                l2_pointer = l2_pointer.next
                curr = curr.next

        
        return dummy_node.next


            
