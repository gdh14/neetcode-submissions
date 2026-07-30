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
        # find the mid point 
        fast = slow = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # cut the list into two
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # merge two half
        second = prev
        first = head
        while second:
            # store 
            tmp1 = first.next
            tmp2 = second.next

            # link
            first.next = second
            second.next = tmp1

            # move
            first = tmp1
            second = tmp2
        

            






