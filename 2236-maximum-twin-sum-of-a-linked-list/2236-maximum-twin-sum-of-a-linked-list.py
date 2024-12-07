# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prevSlow = ListNode()
        slow = fast = head
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        prevSlow.next = None
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        first = head
        second = prev
        ans = float("-inf")
        while first and second:
            ans = max(ans,(first.val + second.val))
            first = first.next
            second = second.next
        return ans


        