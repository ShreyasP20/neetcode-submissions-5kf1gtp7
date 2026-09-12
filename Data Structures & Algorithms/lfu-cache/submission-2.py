class ListNode:
    def __init__(self, val, key, nxt, prev):
        self.val = val
        self.key = key
        self.cnt = 1
        self.next = nxt
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.left = ListNode(0,0, None, None)
        self.right = ListNode(0,0,None, self.left)
        self.left.next = self.right
        self.size = 0
    
    def addNode(self, node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
        self.size += 1
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLRU(self):
        node = self.left.next
        self.removeNode(node)
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.keyMap ={}
        self.freqMap = {}
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        oldfreq = node.cnt
        self.freqMap[oldfreq].removeNode(node)

        if oldfreq == self.minFreq and self.freqMap[oldfreq].size ==0:
            self.minFreq += 1
        
        node.cnt += 1

        if node.cnt not in self.freqMap:
            self.freqMap[node.cnt] = DoublyLinkedList()
        
        self.freqMap[node.cnt].addNode(node)

        return node.val



    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.keyMap:
            node = self.keyMap[key]
            node.val = value
            self.get(key)
            return
        
        if len(self.keyMap) >= self.capacity:
            minFreqList = self.freqMap[self.minFreq]
            removedNode = minFreqList.removeLRU()
            del self.keyMap[removedNode.key]
        
        newNode = ListNode(value, key, None, None)
        if 1 not in self.freqMap:

            self.freqMap[1] = DoublyLinkedList()

        self.freqMap[1].addNode(newNode)
        self.keyMap[key] = newNode
        self.minFreq = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)