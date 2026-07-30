# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 
My own solution: use three pointers to reverse 1 by 1.

1->2->3


"""


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next
            
        return prev
