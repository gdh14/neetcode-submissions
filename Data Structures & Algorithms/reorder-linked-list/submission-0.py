# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # get the length of the list
        list_len = 0
        cur = head
        while cur:
            cur = cur.next
            list_len += 1

        # get the middle node
        mid_idx = list_len // 2

        # reverse link after middle node
        idx_cnt = 0
        mid = head
        while idx_cnt < mid_idx:
            mid = mid.next
            idx_cnt += 1

        prev = None
        while mid:
            nxt = mid.next
            mid.next = prev        
            prev = mid
            mid = nxt

        # merge list one by one
        dummy = ListNode()
        cur = dummy
        while prev and head:
            cur.next = head
            # prev and head are the same, only assign one
            if prev == head:
                break
            cur = cur.next
            cur.next = prev
            cur = cur.next
            head = head.next
            prev = prev.next

        return dummy.next


