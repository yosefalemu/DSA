# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        currSum = 0
        start = head.next
        while start:
            if start.val == 0:
                curr.next = ListNode(currSum)
                curr = curr.next
                currSum = 0
            else:
                currSum += start.val
            start = start.next
        return dummy.next

        