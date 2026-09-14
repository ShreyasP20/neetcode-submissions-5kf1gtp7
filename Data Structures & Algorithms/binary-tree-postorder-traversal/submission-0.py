# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        last_visited = None
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            node = stack[-1]
            if node.right is None or node.right == last_visited:
                result.append(node.val)
                last_visited = node
                stack.pop()
            else:
                current = node.right

        return result