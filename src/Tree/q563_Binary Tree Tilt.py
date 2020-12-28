# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.num = 0
        def tilt(root: TreeNode) -> int:
            if not root:
                return 0
            l, r  = tilt(root.left), tilt(root.right)
            self.num += abs(l-r)
            return root.val + l + r
        tilt(root)
        return self.num
