# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        node_list1 = list1
        node_list2 = list2
        while node_list1 is not None and node_list2 is not None:
            if node_list1.val <= node_list2.val:
                current.next = node_list1
                current = current.next
                node_list1 = node_list1.next
            else:
                current.next = node_list2
                current = current.next
                node_list2 = node_list2.next
        if node_list1:
            current.next = node_list1
        elif node_list2:
            current.next = node_list2

        return dummy.next
        