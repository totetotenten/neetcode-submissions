# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        q = deque([(root, None, None)])
        while q:
            node, low, high = q.popleft()
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            if node.left:
                q.append((node.left, low, node.val))
            if node.right:
                q.append((node.right, node.val, high))

        return True

        