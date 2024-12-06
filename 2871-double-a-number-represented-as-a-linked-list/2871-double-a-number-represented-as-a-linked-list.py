# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        remainder = 0
        headRev = prev
        dummy = ListNode()
        curr = dummy
        count = 1
        while headRev or remainder:
            currDouble = (headRev.val*2) + remainder  if headRev else remainder 
            curr.next = ListNode(currDouble % 10)
            remainder = currDouble // 10
            curr = curr.next
            if headRev:
                headRev = headRev.next
            count += 1
        curr = dummy.next
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


        