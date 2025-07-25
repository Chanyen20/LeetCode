# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = self.reverse_and_str(l1)
        s2 = self.reverse_and_str(l2)
        res_num = int(s1) +  int(s2) 
        res = self.turnToListNode(res_num)
        return res 

    def reverse_and_str(self, listNode):
        curr = listNode
        s = ''
        while curr:
            s += str(curr.val)
            curr = curr.next
        return s[::-1]
    
    def turnToListNode(self, res_num):
        dummy = ListNode()
        curr = dummy
        for ch in str(res_num)[::-1]:
            curr.next = ListNode(int(ch))
            curr = curr.next
        return dummy.next






        