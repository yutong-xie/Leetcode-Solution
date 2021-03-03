# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        
        node = ListNode()
        node.next = head
        curr = head 
        prev = node 
        
        while curr: 
            if curr.val == val: 
                prev.next = curr.next 
            else:
                prev = curr 
                
            curr = curr.next
        
        return node.next
                
                