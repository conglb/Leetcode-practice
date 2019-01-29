# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur3 = head
        while n > 0:
            cur3 = cur3.next
            n -= 1
        if cur3 == Node:
            return head.next
        cur1 = head
        while cur3.next != None:
            cur3 = cur3.next
            cur1 = cur1.next
        cur1.next = cur1.next.next
        return head