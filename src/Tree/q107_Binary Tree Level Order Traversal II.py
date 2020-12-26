# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        levelOrder = []
        if root is None:
            return levelOrder
        q = collections.deque([root])
        while q:
            sizes = len(q)
            level = []
            for _ in range(sizes):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                level.append(node.val)
            levelOrder.append(level)
        return levelOrder[::-1]
