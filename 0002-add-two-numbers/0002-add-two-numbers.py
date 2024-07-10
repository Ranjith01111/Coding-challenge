# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        s = ListNode()
        cur = s
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tot = val1 + val2 + carry
            carry = tot//10
            cur.next = ListNode(tot%10)
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return s.next

        