# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 

1-2-3 
      l1
2-3-4-5
    l2

d-1-2-2-3
        
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        # condition, both list 1 and list 2 are None empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        # append longer ones
        if list2:
            tail.next = list2
        if list1:
            tail.next = list1
        
        return dummy.next
