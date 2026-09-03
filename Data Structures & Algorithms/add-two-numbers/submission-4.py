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

        while carry or curr_l1 or curr_l2:
            temp_node = ListNode()
            curr_l1_val = curr_l1.val if curr_l1 else 0
            curr_l2_val = curr_l2.val if curr_l2 else 0
            
            curr_sum = carry + curr_l1_val + curr_l2_val
            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            temp_node.val = curr_sum
            curr_sum_list.next = temp_node
            
            curr_sum_list = curr_sum_list.next
            curr_l1 = curr_l1.next if curr_l1 else None
            curr_l2 = curr_l2.next if curr_l2 else None


        return sum_list.next

            