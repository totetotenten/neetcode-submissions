# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        seen = {}
        que = deque([root])
        seen[root] = [root]
        while p not in seen or q not in seen:
            node = que.popleft()
            if node.left:
                seen[node.left] = seen[node] + [node.left]
                que.append(node.left)
            if node.right:
                seen[node.right] = seen[node] + [node.right]
                que.append(node.right)
        p_anc = set(seen[p])
        q_anc_list = seen[q]
        n = len(seen[q])
        
        for i in range(n):
            if q_anc_list[n-i-1] in p_anc:
                return q_anc_list[n-i-1]