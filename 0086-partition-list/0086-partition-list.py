# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smallDummy, largeDummy = ListNode(),ListNode()
        smallCurr, largeCurr = smallDummy,largeDummy
        while head:
            if head.val < x:
                smallCurr.next = head
                smallCurr = smallCurr.next
            else:
                largeCurr.next = head
                largeCurr = largeCurr.next
            head = head.next
        smallCurr.next = largeDummy.next
        largeCurr.next = None
        return smallDummy.next 
        