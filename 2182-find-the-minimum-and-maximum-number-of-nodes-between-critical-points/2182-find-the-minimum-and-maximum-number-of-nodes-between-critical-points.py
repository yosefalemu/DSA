# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]  # Less than 3 nodes, no critical points possible

        # Initialize variables
        first = head
        second = head.next
        third = second.next
        firstIndex = -1
        prevIndex = -1
        minDistance = float('inf')
        index = 1  # Start at the second node since we need to compare neighbors
        foundFirst = False
        maxDistance = 0

        while third:
            # Check if the second node is a critical point
            if (second.val < first.val and second.val < third.val) or (second.val > first.val and second.val > third.val):
                if not foundFirst:
                    # First critical point
                    firstIndex = index
                    prevIndex = index
                    foundFirst = True
                else:
                    # Subsequent critical points
                    minDistance = min(minDistance, index - prevIndex)
                    maxDistance = index - firstIndex
                    prevIndex = index

            # Move to the next set of nodes
            first = second
            second = third
            third = third.next
            index += 1

        if not foundFirst or prevIndex == firstIndex:
            return [-1, -1]  # No critical points or only one critical point

        return [minDistance, maxDistance]
