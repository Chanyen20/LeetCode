# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        curr = dummy_node
        temp = 0

        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + temp
                curr.next = ListNode(value % 10)
                curr = curr.next
                temp = value // 10
                l1 = l1.next
                l2 = l2.next
                continue
            if l1 and not l2:
                value = l1.val + temp
                curr.next = ListNode(value % 10)
                curr = curr.next
                temp = value // 10
                l1 = l1.next
                continue
            if not l1 and l2:
                value = l2.val + temp
                curr.next = ListNode(value % 10)
                curr = curr.next
                temp = value // 10
                l2 = l2.next
                continue
            
        if temp != 0:
            curr.next = ListNode(temp)

        return dummy_node.next

# l1 = [2, 4, 3]
#          |
# l2 = [5, 6, 4, 6]
#          |



            





        