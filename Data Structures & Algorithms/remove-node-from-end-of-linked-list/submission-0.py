# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr= head
        N = 0
        while curr:
            curr= curr.next
            N += 1
        


        node_delete = (N - n)
        if node_delete ==0:
            return head.next
        
        curr_1 = head
        prev = None
        while node_delete >= 0:
            if node_delete == 0:
                prev.next = curr_1.next
                curr_1.next = None
            else:
                prev = curr_1
                curr_1 = curr_1.next
                
            node_delete -= 1

        return head