# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        if current is None:
            return False
        while current.next and current not in seen:
            seen.add(current)
            current = current.next

        if current.next is None:
            return False
        else:
            return True
        