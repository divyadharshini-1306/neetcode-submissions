# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next   # save the next node before we overwrite curr.next
            curr.next = prev        # reverse the pointer
            prev = curr             # move prev forward
            curr = next_temp        # move curr forward
        
        return prev   # prev is now the new head