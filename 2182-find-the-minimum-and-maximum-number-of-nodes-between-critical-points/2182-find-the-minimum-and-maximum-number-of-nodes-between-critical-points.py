# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        first = head
        second = head.next
        if not second.next:
            return [-1,-1]
        third = second.next
        found = False
        firstIndex = -1
        prevIndex = -1
        index = 1
        minDistance = float("inf")
        maxDistance = 0
        while third:
            if (second.val < first.val and second.val < third.val) or (second.val > first.val and second.val > third.val):
                if not found:
                    firstIndex = index
                    prevIndex = index
                    found = True
                else:
                    minDistance = min(minDistance, index - prevIndex)
                    maxDistance = index - firstIndex
                    prevIndex = index
            index += 1
            first = first.next
            second = second.next
            third = third.next
        if not found or prevIndex == firstIndex:
            return [-1,-1]
        return [minDistance,maxDistance]
                
                



        