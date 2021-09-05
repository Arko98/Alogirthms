# Problem URL: https://leetcode.com/problems/rotate-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head ==  None:
            return None
        if head is not None and head.next == None:
            return head
        else:
            temp_ = head
            length = 0
            while (temp_.next != None):
                length += 1
                temp_ = temp_.next
            k = k % (length+1)
            for i in range(k):
                temp = head
                while (temp.next.next != None):
                    temp = temp.next
                first = head
                temp.next.next = head
                head = temp.next
                temp.next = None
            return head
        