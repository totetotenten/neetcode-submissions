# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_dict = {}
        for i, val in enumerate(inorder):
            index_dict[val] = i
        self.pre_idx = 0
        return self.build(preorder, inorder, index_dict, 0, len(inorder) - 1)


    def build(self, preorder, inorder, index_dict, left, right):
        if left > right:
            return None

        root_val = preorder[self.pre_idx]
        self.pre_idx += 1

        root_index = index_dict[root_val]

        root = TreeNode(root_val)
        root.left = self.build(preorder, inorder, index_dict, left, root_index - 1)
        root.right = self.build(preorder, inorder, index_dict, root_index + 1, right)

        return root
        