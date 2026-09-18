# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = [(root, False)]
        height= {}

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
                if abs(left_height - right_height) > 1:
                    return False
                height[node] = 1 + max(left_height, right_height)

        return True
