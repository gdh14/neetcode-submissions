# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

""" 

list1. 

1-2-4
  p1


list2. 
1-1-3-5
  p2


p0-1-1


p0 = None 
head = None


if p1.val <= p2.val: 
    p0.next = p1
    p0 = p0.next
else:
    p0.next = p2
    p0 = p0.next

"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list, head = None, None

        # initialze head of the new list


        # 
        while 1:
            if list1.val <= list2.val:
                new_list.next = list1






        