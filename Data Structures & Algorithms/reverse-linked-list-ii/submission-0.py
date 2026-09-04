# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        DummyNode = ListNode(0, head)
        
        LeftPrevious = DummyNode
        curr = head
        for i in range(left - 1):
            LeftPrevious = curr
            curr = curr.next 
        
        prev = None 
        for i in range(right - left + 1):
            tempNext = curr.next
            curr.next = prev
            prev = curr
            curr = tempNext

        LeftPrevious.next.next = curr
        LeftPrevious.next = prev

        return DummyNode.next
        