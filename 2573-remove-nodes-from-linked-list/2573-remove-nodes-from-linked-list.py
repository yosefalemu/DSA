# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        newHead = prev
        maxVal = newHead.val
        dummy = ListNode()
        curr = dummy
        while newHead:
            maxVal = max(maxVal,newHead.val)
            if newHead.val >= maxVal:
                curr.next = newHead
                curr = curr.next
            newHead = newHead.next
        curr.next = None
        curr = dummy.next
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev




        