# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        prev = None
        curr = head 
        
        while curr != None:
            tmp = curr.next 
            curr.next = prev 
            prev = curr
            curr = tmp 
             
        return prev
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        carry = 0 
        head = ListNode(0)
        ans = head
        
        while l1 != None or l2 != None:
            x = l1.val if l1 != None else 0
            y = l2.val if l2 != None else 0 
            total = x + y + carry
            num = total % 10
            carry = total // 10
            ans.next = ListNode(num)
            ans = ans.next
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            
        if carry > 0:
            ans.next = ListNode(carry)
            
        return self.reverseList(head.next)
        