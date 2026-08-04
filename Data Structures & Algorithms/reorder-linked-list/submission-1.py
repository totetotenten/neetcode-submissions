# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, current = None, slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        first, second = head, prev
        while second.next:
            first_next = first.next
            first.next = second
            first = first_next
            second_next = second.next
            second.next = first
            second = second_next
            
        
        