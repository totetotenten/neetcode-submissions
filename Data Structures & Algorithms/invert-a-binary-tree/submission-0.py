# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        seen = set()
        if current:
            seen.add(current)
        while seen:
            add_node = []
            del_node = []
            for node in seen:
                left = node.left
                node.left = node.right
                node.right = left
                if node.left:
                    add_node.append(node.left)
                if node.right:
                    add_node.append(node.right)
                del_node.append(node)
            for node in del_node:
                seen.discard(node)
            for node in add_node:
                seen.add(node)
        return root
            
            