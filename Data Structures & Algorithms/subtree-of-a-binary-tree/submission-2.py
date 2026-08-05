# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                is_match = True
                p = deque([(node, subRoot)])

                while p:
                    main, sub = p.popleft()
                    if not main and not sub:
                        continue
                    if not main or not sub:
                        is_match = False
                        break
                    if main.val != sub.val:
                        is_match = False
                        break
            
                    p.append((main.left, sub.left))
                    p.append((main.right, sub.right))

                if is_match:
                    return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False

        

            


        