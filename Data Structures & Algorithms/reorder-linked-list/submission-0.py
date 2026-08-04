# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = {}
        current = head
        i = 0
        while current is not None:
            seen[i] = current
            current = current.next
            i += 1
        n = i
        current = head
        for j in range(n//2):
            current.next = seen[n-j-1]
            current = current.next
            if j != n-j-2:
                current.next = seen[j+1]
                current = current.next
            if j == n//2 - 1:
                current.next = None


