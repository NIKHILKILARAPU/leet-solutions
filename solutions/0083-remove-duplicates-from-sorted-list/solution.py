# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        h1 = head
        h2 = h1.next
        while h2 is not None:
            if h1.val != h2.val:
                h1.next = h2
                h1=h2
            h2=h2.next
        h1.next=None    
        return head        

        
