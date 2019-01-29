# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        pre = head
        cur = head.next
        while pre != None or cur != None:
            next = cur.next
            cur.next = pre
            if next == None:
                pre.next = None
                break
            else:
                pre.next = next.next
            pre = next
            cur = next.next
        return head

if __name__ == '__main__':
    sol = Solution()