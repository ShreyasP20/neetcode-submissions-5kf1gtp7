# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        min_node_val = float("-inf")
        max_node_val = float("inf")

        stack = [(root, min_node_val, max_node_val)]

        while stack:
            node, min_node_val, max_node_val = stack.pop()

            if node.val <= min_node_val or node.val >= max_node_val:
                return False

            if node.left:
                stack.append(
                    (node.left, min_node_val, node.val)
                )

            if node.right:
                stack.append(
                    (node.right, node.val, max_node_val)
                )

        return True