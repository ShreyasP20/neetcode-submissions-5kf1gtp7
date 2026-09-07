class ListNode:
    def __init__(self, key,val, nxt, prev):
        self.val = val
        self.key = key
        self.next = nxt
        self.prev = prev
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = ListNode(0,0, None, None)
        self.right = ListNode(0,0, None, self.left)
        self.left.next = self.right
        self.LRUMap = {}

    def get(self, key: int) -> int:
        if key not in self.LRUMap:
            return -1
        
        node = self.LRUMap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.LRUMap:
            tempNode = self.LRUMap[key]
            tempNode.val = value
            tempNode.next.prev = tempNode.prev
            tempNode.prev.next = tempNode.next
            tempNode.next = self.right
            tempNode.prev = self.right.prev
            self.right.prev.next = tempNode
            self.right.prev = tempNode
            return None 
        
        tempNode = ListNode(key, value, self.right, self.right.prev)
        self.right.prev.next = tempNode
        self.right.prev = tempNode
        self.LRUMap[key] = tempNode
        if len(self.LRUMap) > self.capacity:
            del self.LRUMap[self.left.next.key]
            self.left.next = self.left.next.next
            self.left.next.prev = self.left  

        
