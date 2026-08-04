# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = deque([root])
        d = {}
        d[root] = 1
        while q:
            node = q.popleft()
            if node.left:
                q.append(node.left)
                d[node.left] = d[node] + 1
            if node.right:
                q.append(node.right)
                d[node.right] = d[node] + 1
        
        return max(d.values())        