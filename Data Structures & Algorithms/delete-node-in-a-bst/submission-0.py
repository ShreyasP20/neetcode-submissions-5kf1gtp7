# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == key:
                if curr.left is None and curr.right is None: 
                    if curr == root:
                        return None
                    elif parent.left == curr:
                        parent.left = None
                    else:
                        parent.right = None
                
                elif (curr.left is not None and curr.right is None) or (curr.right is not None and curr.left is None):
                    child = curr.left if curr.left else curr.right

                    if curr == root:
                        return curr.left if curr.left else curr.right
                    
                    elif parent.left == curr:
                        parent.left = child
                    else:
                        parent.right = child


                else:
                    successor_parent = curr
                    successor = curr.right
                    while successor.left:
                        successor_parent = successor
                        successor = successor.left
                    
                    curr.val = successor.val
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

            
            parent = curr

            if curr.val > key:
                curr = curr.left
            else:
                curr = curr.right
        
        return root