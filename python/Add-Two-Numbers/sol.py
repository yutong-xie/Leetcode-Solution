# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        carry = 0
        head = ListNode(0)
        curr = head
        while l1 or l2: 
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = carry + v1 + v2
            carry = s // 10 
            res = s % 10
            curr.next = ListNode(res)
            curr = curr.next 
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry: 
            curr.next = ListNode(1)
        
        return head.next
            