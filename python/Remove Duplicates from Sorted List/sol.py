# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        node = ListNode(-101)
        node.next = head 
        prev, curr = node, head
        
        while curr:
            if curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next 
        
        return node.next