"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {}

        def searchnode(node):
            if node is None:
                return None
            if node in seen:
                return seen[node]
            seen[node] = Node(node.val)
            return seen[node]

        node = head
        while node:
            copy = searchnode(node)
            copy.next = searchnode(node.next)
            copy.random = searchnode(node.random)
            node = node.next

        return searchnode(head)
      