# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 
1. Use fast slow pointer to find the mid node
2. revert the links
3. if we need to break existing link, remember to store the next point in temp
"""

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the mid point (s)
        f, s = head
        while f.next:
            f = f.next.next
            s = s.next

        # revert list from mid
        p = None
        while s:
            n = s.next
            s.next = p
            p = s
            s = n

        # merge list (head and p)
        tail = p
        while head and tail and head != tail: 
            h_next = head.next
            t_next = tail.next
            head.next = tail
            tail.next = h_next
            head = h_next
            tail = t_next







