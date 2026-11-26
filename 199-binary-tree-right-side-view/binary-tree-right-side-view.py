# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        result = []

        if root is None:
            return result

        q = [root]

        while q:
            size = len(q)
            current_level = []

            for i in range(size):
                node = q.pop(0)
                current_level.append(node.val)

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            result.append(current_level[-1])

        return result
