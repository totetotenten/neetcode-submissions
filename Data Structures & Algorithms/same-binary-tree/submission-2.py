# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_que = deque([p])
        q_que = deque([q])
        while p_que and q_que:
            p_node = p_que.popleft()
            q_node = q_que.popleft()
            if p_node:
                if not q_node:
                    return False
                elif p_node.val != q_node.val:
                    return False

                p_que.append(p_node.left)
                p_que.append(p_node.right)
                q_que.append(q_node.left)
                q_que.append(q_node.right)
            else:
                if q_node:
                    return False

        if p_que or q_que:
            return False
        else:
            return True







        