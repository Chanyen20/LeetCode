"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        convert_mapping = {None: None} #{old_node : new_node}
        dummy_node_new = Node(0)
        curr_new = dummy_node_new
        
        curr_old = head
        while curr_old:
            curr_new.next = Node(curr_old.val)
            convert_mapping[curr_old] = curr_new.next

            curr_new = curr_new.next
            curr_old = curr_old.next
        
        curr_new = dummy_node_new
        curr_old = head
        while curr_old:
            random_node = curr_old.random
            curr_new.next.random = convert_mapping[random_node]

            curr_new = curr_new.next
            curr_old = curr_old.next
        
        return dummy_node_new.next






        