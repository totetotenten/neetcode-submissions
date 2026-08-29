# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(root, floor, ceil):
            if not root:
                return True
            if floor is not None and root.val <= floor:
                return False
            if ceil is not None and root.val >= ceil:
                return False
            return validate(root.left, floor, root.val) and validate(root.right, root.val, ceil)
        return validate(root, None, None)