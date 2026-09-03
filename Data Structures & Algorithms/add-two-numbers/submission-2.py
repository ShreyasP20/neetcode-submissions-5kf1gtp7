# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        sum_list = ListNode()
        curr_sum_list = sum_list
        carry = 0
        while curr_l1 and curr_l2:
            temp_Node = ListNode()
            if curr_l1.val + curr_l2.val >= 10:
                temp_Node.val = ((curr_l1.val + curr_l2.val)%10)+carry
                carry = 1
            else:
                temp_Node.val = ((curr_l1.val + curr_l2.val)%10)+ carry
                carry = 0

            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
            curr_sum_list.next = temp_Node
            curr_sum_list = curr_sum_list.next
        
        while curr_l1:
            temp_Node = ListNode()
            if curr_l1.val + carry >= 10:
                temp_Node.val = ((curr_l1.val + carry)%10)
                carry = 1
            else:
                temp_Node.val = curr_l1.val + carry
                carry = 0
            curr_sum_list.next = temp_Node
            curr_sum_list = curr_sum_list.next
            curr_l1 = curr_l1.next

        while curr_l2:
            temp_Node = ListNode()
            if curr_l2.val + carry >= 10:
                temp_Node.val = ((curr_l2.val + carry)%10)
                carry = 1
            else:
                temp_Node.val = curr_l2.val + carry
                carry = 0
            curr_sum_list.next = temp_Node
            curr_sum_list = curr_sum_list.next
            curr_l2 = curr_l2.next

        if carry:
            temp_Node = ListNode()
            temp_Node.val = carry 
            curr_sum_list.next = temp_Node


        return sum_list.next

            