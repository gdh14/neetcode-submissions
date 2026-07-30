# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p0, head = ListNode(), ListNode()
        p1, p2 = list1, list2

        # initialze head of the new list
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        # merge two list when they are all not None
        if p1.val <= p2.val:
            head = p1
        else:
            head = p2

        while p1 and p2:
            if p1.val <= p2.val:
                p0.next = p1
                p1 = p1.next
            else:
                p0.next = p2
                p2 = p2.next
            
            p0 = p0.next
        
        if p1:
            p0.next = p1
        if p2:
            p0.next = p2

        return head

""" 
1-2-4
      p1

1-1-3-5
      p2

n-1-1-1-2-3-4
            p0

"""

