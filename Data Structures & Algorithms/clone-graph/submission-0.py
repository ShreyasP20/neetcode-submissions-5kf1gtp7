"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        graph_map = {}

        def clone_dfs(node):
            if node is None:
                return None
            
            if node in graph_map:
                return graph_map[node]

            cloned_node = Node(node.val)
            graph_map[node] = cloned_node
            for nxt in node.neighbors:
                cloned_node.neighbors.append(clone_dfs(nxt))
            
            return cloned_node


        return clone_dfs(node)
