# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        slowPt = head
        fastPt = head.next
        temp = head.val
        while fastPt:
            if temp != fastPt.val:
                slowPt.next = fastPt
                slowPt = slowPt.next
                temp = slowPt.val
            fastPt = fastPt.next
        slowPt.next = None
        return head
            



        