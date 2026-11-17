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
        q = deque([(root, 1)])
        res = 0    
        while q:
            root, depth = q.popleft()
            if root:
                res = max(res, depth)
                q.append((root.left, depth+1))
                q.append((root.right, depth+1))
        return res



        