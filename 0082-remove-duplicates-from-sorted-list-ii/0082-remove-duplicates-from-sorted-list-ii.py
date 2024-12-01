# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linkedListDict = {}
        curr = head
        while curr:
            if curr.val in linkedListDict:
                linkedListDict[curr.val] += 1
            else:
                linkedListDict[curr.val] = 1
            curr = curr.next
        dummy = ListNode()
        curr = dummy
        while head:
            currVal = head.val
            if linkedListDict[currVal] == 1:
                curr.next = head
                curr = curr.next
            head = head.next
        curr.next = None
        return dummy.next
        