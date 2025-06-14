# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # fast 每次走 2 步
        # slow 每次走 1 步
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        prev = None  # 記錄 slow 的前一個節點

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # 此時 slow 指向中間節點，prev 是它的前一個
        prev.next = slow.next  # 刪除中間節點

        return head




# Time: O(n)
# Space: O(1)