# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = ListNode(None)
        node = prev
        while l1 or l2:
            if l1 and l2:
                node_sum = l1.val + l2.val + carry
                tmp = node_sum % 10 
                carry = node_sum//10
                l1, l2 = l1.next, l2.next
            elif l1:
                node_sum = l1.val + carry
                tmp = node_sum % 10
                carry = node_sum//10
                l1 = l1.next
            else:
                node_sum = l2.val + carry
                tmp = node_sum % 10
                carry = node_sum//10
                l2 =l2.next            
            node.next = ListNode(tmp)
            node = node.next
        if carry:
            node.next = ListNode(carry)
        return prev.next


        