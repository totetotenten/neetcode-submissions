# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, late = head, head
        while fast:
            fast = fast.next
            late = late.next
            if fast:
                fast = fast.next
                if fast == late:
                    return True
        return False