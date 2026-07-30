# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 

1-2-3-4

"""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head

        while s and f and s.next and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False