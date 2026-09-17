# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = [(root, False)]
        height = {}
        diameter = 0

        while stack:
            node, visited = stack.pop()

            if not node:
                continue

            if not visited:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
            
            else:
                left_height = height.get(node.left, 0)
                right_height = height.get(node.right, 0)
                height[node] = 1 + max(left_height, right_height)
                diameter = max(diameter, left_height+ right_height)
        
        return diameter 


