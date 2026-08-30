# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            return 1+max(height(root.left),height(root.right))
        def diametere(root):
            if root is None:
                return 0
            lheight=height(root.left)
            rheight=height(root.right)
            ldiametere=diametere(root.left)
            rdiametere=diametere(root.right)
            return max(lheight+rheight,ldiametere+rdiametere)
        return diametere(root)
        