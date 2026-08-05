# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        que = deque([root])
        seen = {}
        seen[root] = None
        while p not in seen or q not in seen:
            node = que.popleft()
            if node.left:
                seen[node.left] = node
                que.append(node.left)
            if node.right:
                seen[node.right] = node
                que.append(node.right)
        p_anc = set()
        current = p
        while current:
            p_anc.add(current)
            current = seen[current]
        current = q
        while current:
            if current in p_anc:
                return current
            current = seen[current]
