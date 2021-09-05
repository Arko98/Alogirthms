# Problem URL: https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_list = ListNode(val = 0, next = None)
        out_list = return_list
        carry = 0
        while (l1 != None and l2 != None):
            sum_val = carry + l1.val + l2.val
            if sum_val < 10:
                out_list.val = sum_val
                carry = 0
            elif sum_val >= 10:
                out_list.val = sum_val % 10
                carry = 1
            l1 = l1.next
            l2 = l2.next
            if (l1 != None or l2 != None or carry == 1):
                out_list.next = ListNode(val = carry, next = None)
                out_list = out_list.next
        if (l1 == None and l2 != None):
            while (l2 != None):
                sum_val = carry + l2.val
                if sum_val < 10:
                    out_list.val = sum_val
                    carry = 0
                elif sum_val >= 10:
                    out_list.val = sum_val % 10
                    carry = 1
                l2 = l2.next
                if (l2 != None or carry == 1):
                    out_list.next = ListNode(val = carry, next = None)
                    out_list = out_list.next
        elif (l2 == None and l1 != None):
            while (l1 != None):
                sum_val = carry + l1.val
                if sum_val < 10:
                    out_list.val = sum_val
                    carry = 0
                elif sum_val >= 10:
                    out_list.val = sum_val % 10
                    carry = 1
                l1 = l1.next
                if (l1 != None or carry == 1):
                    out_list.next = ListNode(val = carry, next = None)
                    out_list = out_list.next
        return return_list