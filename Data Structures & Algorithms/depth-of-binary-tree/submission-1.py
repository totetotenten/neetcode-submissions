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
        q = deque([[root, 1]])
        result = 0
        while q:
            node = q.popleft()
            result = max(result, node[1])
            if node[0].left:
                q.append([node[0].left, node[1]+1])
            if node[0].right:
                q.append([node[0].right, node[1]+1])
        
        return result
        