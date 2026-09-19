# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                sameTree_stack = [(node, subRoot)]
                is_same = True
                while sameTree_stack:
                    node_root, node_subRoot = sameTree_stack.pop()

                    if node_root is None and node_subRoot is None:
                        continue
                    if node_root is None and node_subRoot is not None:
                        is_same = False
                        break
                    if node_subRoot is None and node_root is not None:
                        is_same = False
                        break
                    if node_root.val != node_subRoot.val:
                        is_same = False
                        break
                    sameTree_stack.append((node_root.left, node_subRoot.left))
                    sameTree_stack.append((node_root.right, node_subRoot.right))
                if is_same:
                    return is_same
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return False