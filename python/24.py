#24. Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        rs = ListNode(0, head)
        prev = rs
        curr = head
        if curr is None or curr.next is None:
            return rs.next
        while curr and curr.next:
            nxt = curr.next
            after = nxt.next

            nxt.next = curr
            curr.next = after
            prev.next = nxt

            prev = curr
            curr = after
            
        return rs.next